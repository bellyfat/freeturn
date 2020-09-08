# Generated by Django 2.2.12 on 2020-09-08 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_auto_20200518_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='project_listing_title',
            field=models.CharField(default='Recent projects', help_text="The title of your project listing, something like 'my projects' or 'recent projects'", max_length=200),
        ),
    ]