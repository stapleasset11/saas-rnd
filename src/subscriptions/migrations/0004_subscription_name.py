# Generated by Django 5.0.9 on 2024-10-03 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_subscription_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='name',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
