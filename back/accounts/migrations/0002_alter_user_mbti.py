# Generated by Django 4.2.7 on 2023-11-16 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mbti',
            field=models.CharField(blank=True, choices=[('ISFP', 'ISFP'), ('ISFJ', 'ISFJ'), ('ISTP', 'ISTP'), ('ISTJ', 'ISTJ'), ('INFP', 'INFP'), ('INFJ', 'INFJ'), ('INTP', 'INTP'), ('INTJ', 'INTJ'), ('ESFP', 'ESFP'), ('ESFJ', 'ESFJ'), ('ESTP', 'ESTP'), ('ESTJ', 'ESTJ'), ('ENFP', 'ENFP'), ('ENFJ', 'ENFJ'), ('ENTP', 'ENTP'), ('ENTJ', 'ENTJ')], max_length=10, null=True),
        ),
    ]
