# Generated by Django 2.0.9 on 2019-01-15 16:12

from django.db import migrations


def copy_connections(apps, schema_editor):
    CV = apps.get_model('crm', 'CV')
    TechnologyInfo = apps.get_model('home', 'TechnologyInfo')

    for cv in CV.objects.all():
        skills = list(TechnologyInfo.objects.filter(id__in=cv.relevant_skills.values_list('info')))
        cv.relevant_skills_temp.set(skills)


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0044_auto_20190115_1559'),
        ('crm', '0033_cv_relevant_skills_temp'),
    ]

    operations = [
        migrations.RunPython(copy_connections),
    ]