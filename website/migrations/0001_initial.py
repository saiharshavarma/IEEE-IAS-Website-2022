# Generated by Django 4.0.1 on 2022-01-24 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hyperlink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_google_form', models.TextField()),
                ('group_invite_link', models.TextField()),
            ],
        ),
    ]
