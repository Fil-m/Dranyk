# referrals/models.py
from django.db import models
from django.contrib.auth.models import User


class ReferralLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField()
    referral_code = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.referral_code}"

class ReferralClick(models.Model):
    referral_link = models.ForeignKey(ReferralLink, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    clicked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.referral_link} - {self.clicked_at}"
