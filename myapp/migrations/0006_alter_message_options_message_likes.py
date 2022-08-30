# Generated by Django 4.1 on 2022-08-28 14:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0005_alter_unread_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('created',)},
        ),
        migrations.AddField(
            model_name='message',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
