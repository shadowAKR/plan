# Generated by Django 4.2.13 on 2024-09-30 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.TextField(blank=True, null=True),
        ),
    ]
