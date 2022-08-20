# Generated by Django 4.1 on 2022-08-14 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0004_personal"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personal",
            name="dataofbirth",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="personal",
            name="gender",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="personal",
            name="mothername",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="personal",
            name="name",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="personal",
            name="namefather",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="personal",
            name="placeofpirth",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="personal",
            name="status",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
