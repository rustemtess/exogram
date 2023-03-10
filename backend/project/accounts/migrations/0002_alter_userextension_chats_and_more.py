# Generated by Django 4.1.4 on 2022-12-25 20:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_alter_message_sender'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextension',
            name='chats',
            field=models.ManyToManyField(blank=True, null=True, to='chat.chat'),
        ),
        migrations.AlterField(
            model_name='userextension',
            name='contacts',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
