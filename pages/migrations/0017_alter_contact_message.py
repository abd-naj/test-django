# Generated by Django 4.1 on 2022-08-15 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0016_alter_wishlist_firstwish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="message",
            field=models.TextField(max_length=50, null=True),
        ),
    ]
