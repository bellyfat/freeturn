# Generated by Django 2.0.9 on 2018-10-21 20:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_homepage_earliest_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='earliest_available',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]