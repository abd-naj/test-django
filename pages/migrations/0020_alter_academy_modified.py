# Generated by Django 4.1 on 2022-08-15 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0019_alter_academy_modified"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academy",
            name="modified",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
