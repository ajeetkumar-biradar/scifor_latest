# Generated by Django 5.0.6 on 2024-06-20 10:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carrer", "0016_alter_casestudy_short_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="casestudy",
            name="short_desc",
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
