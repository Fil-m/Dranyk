# Generated by Django 4.2.5 on 2024-08-31 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referralclick',
            old_name='created_at',
            new_name='clicked_at',
        ),
        migrations.AlterField(
            model_name='referrallink',
            name='referral_code',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
