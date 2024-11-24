# referrals/forms.py
from django import forms
from .models import ReferralLink

class CreateReferralLinkForm(forms.ModelForm):
    class Meta:
        model = ReferralLink
        fields = ['original_url']
