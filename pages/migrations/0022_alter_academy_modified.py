# Generated by Django 4.1 on 2022-08-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0021_alter_academy_modified_alter_contact_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="academy",
            name="modified",
            field=models.CharField(max_length=50, null=True),
        ),
    ]