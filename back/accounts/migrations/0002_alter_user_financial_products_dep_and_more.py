# Generated by Django 4.2.7 on 2023-11-21 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_depositoptions_rsrv_type_and_more'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='financial_products_dep',
            field=models.ManyToManyField(related_name='dep_users', to='products.depositproducts'),
        ),
        migrations.AlterField(
            model_name='user',
            name='financial_products_sav',
            field=models.ManyToManyField(related_name='sav_users', to='products.savingproducts'),
        ),
    ]
