# Generated by Django 4.1 on 2022-08-15 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0009_contact_alter_personal_dataofbirth_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Academy",
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
                ("elementaryschool", models.CharField(max_length=50, null=True)),
                ("certificatedate", models.CharField(max_length=50, null=True)),
                ("preparatoryschool", models.CharField(max_length=50, null=True)),
                ("modified", models.CharField(max_length=50, null=True)),
                ("highschool", models.CharField(max_length=50, null=True)),
                ("certificatesource", models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
