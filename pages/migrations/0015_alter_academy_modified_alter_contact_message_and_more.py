# Generated by Django 4.1 on 2022-08-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0014_rename_maritalstatus_wishlist_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academy",
            name="modified",
            field=models.DecimalField(decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name="contact", name="message", field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="wishlist",
            name="firstwish",
            field=models.BooleanField(default=True, null=True),
        ),
    ]
