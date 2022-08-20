# Generated by Django 4.1 on 2022-08-14 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0007_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Personal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, null=True)),
                (
                    "placeofpirth",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("ratio", models.CharField(max_length=50)),
                ("dataofbirth", models.CharField(blank=True, max_length=50, null=True)),
                ("namefather", models.CharField(blank=True, max_length=50, null=True)),
                ("gender", models.CharField(blank=True, max_length=50, null=True)),
                ("mothername", models.CharField(blank=True, max_length=50, null=True)),
                ("status", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
