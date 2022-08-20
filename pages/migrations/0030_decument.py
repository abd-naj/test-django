# Generated by Django 4.1 on 2022-08-18 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0029_alter_academy_certificatedate"),
    ]

    operations = [
        migrations.CreateModel(
            name="Decument",
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
                ("imgper", models.ImageField(upload_to="personalPhoto/%y/%m/%d")),
                ("imgid", models.ImageField(upload_to="idPhotos/%y/%m/%d")),
                ("imgcer", models.ImageField(upload_to="certificatePhotos/%y/%m/%d")),
            ],
        ),
    ]
