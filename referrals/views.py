from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CreateReferralLinkForm
from .models import ReferralLink, ReferralClick
import uuid

@login_required
def create_referral_link(request):
    if request.method == 'POST':
        form = CreateReferralLinkForm(request.POST)
        if form.is_valid():
            referral_link = form.save(commit=False)
            referral_link.user = request.user
            referral_link.referral_code = str(uuid.uuid4())
            referral_link.save()
            referral_url = request.build_absolute_uri(f'/referrals/r/{referral_link.referral_code}/')
            return render(request, 'referrals/referral_link_list.html', {'referral_url': referral_url})
    else:
        form = CreateReferralLinkForm()
    return render(request, 'referrals/create_referral_link.html', {'form': form})

def redirect_referral_link(request, referral_code):
    referral_link = get_object_or_404(ReferralLink, referral_code=referral_code)
    user = request.user if request.user.is_authenticated else None
    ip_address = request.META.get('REMOTE_ADDR') if not user else None

    ReferralClick.objects.create(
        referral_link=referral_link,
        user=user,
        ip_address=ip_address
    )

    return redirect(referral_link.original_url)

@login_required
def referral_link_list(request):
    referral_links = ReferralLink.objects.filter(user=request.user)
    referral_link_data = []
    base_url = request.build_absolute_uri('/referrals/r/')

    for link in referral_links:
        clicks = ReferralClick.objects.filter(referral_link=link)
        click_count = clicks.count()
        
        # Отримуємо підреферальні посилання, які не є самим цим посиланням
        sub_links = ReferralLink.objects.filter(original_url=link.original_url).exclude(id=link.id)
        
        referral_link_data.append({
            'link': link,
            'clicks': clicks,
            'click_count': click_count,
            'sub_links': [{'referral_code': sub_link.referral_code, 'url': f"{base_url}{sub_link.referral_code}/"} for sub_link in sub_links]
        })

    return render(request, 'referrals/referral_link_list.html', {'referral_link_data': referral_link_data})
