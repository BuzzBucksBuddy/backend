# Generated by Django 4.2.7 on 2023-11-16 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_mbti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mbti',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
