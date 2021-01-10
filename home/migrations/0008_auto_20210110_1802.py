# Generated by Django 2.2.10 on 2021-01-10 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_vsaituser_alert_membership_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='vsaituser',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vsaituser',
            name='secret_email_confirmation_url',
            field=models.CharField(default='0c4ab720a3584ea4b910890e4a9bac53', max_length=100),
        ),
        migrations.AddField(
            model_name='vsaituser',
            name='secret_password_change_url',
            field=models.CharField(default='b73fe5555dce44d69a938e45cb996e30', max_length=100),
        ),
    ]
