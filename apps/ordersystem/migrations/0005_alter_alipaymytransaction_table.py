# Generated by Django 4.1.4 on 2022-12-23 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ordersystem", "0004_alter_alipaymytransaction_amount_and_more"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="alipaymytransaction",
            table="ordersystem",
        ),
    ]