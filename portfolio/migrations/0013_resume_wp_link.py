# Generated by Django 4.0.10 on 2023-06-23 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_features_languages_web_cat_delete_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='wp_link',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
