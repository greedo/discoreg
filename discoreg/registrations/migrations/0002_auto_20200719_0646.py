# Generated by Django 3.0.8 on 2020-07-19 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registrations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="discordrole",
            name="name",
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name="discordserver",
            name="name",
            field=models.CharField(blank=True, max_length=32),
        ),
    ]