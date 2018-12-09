# Generated by Django 2.0.9 on 2018-12-06 18:20

import django.utils.timezone
import django_extensions.db.fields
import wagtailmarkdown.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('wagtailimages', '0020_add-verbose-name'),
        ('taggit', '0002_auto_20150616_2121'),
        ('home', '0029_auto_20181021_2044'),
        ('wagtailcore', '0040_page_draft_title'),
        ('crm', '0026_remove_project_recruiter'),
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created',
                 django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified',
                 django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('earliest_available', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('full_name',
                 models.CharField(help_text='Name to use in the title of the file, default is current user',
                                  max_length=200)),
                ('title', models.CharField(help_text='Title to be placed under the name', max_length=200)),
                ('experience_overview', wagtailmarkdown.fields.MarkdownField(help_text='Notice on your experience')),
                ('education_overview', wagtailmarkdown.fields.MarkdownField(help_text='Notice on your education')),
                ('contact_details', wagtailmarkdown.fields.MarkdownField()),
                ('languages_overview', wagtailmarkdown.fields.MarkdownField()),
                ('rate_overview', wagtailmarkdown.fields.MarkdownField()),
                ('picture',
                 models.ForeignKey(blank=True, help_text='Picture to use, default is current user pic', null=True,
                                   on_delete=django.db.models.deletion.SET_NULL, related_name='+',
                                   to='wagtailimages.Image')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Project')),
                ('project_pages', models.ManyToManyField(help_text='Project pages to include in the application',
                                                         related_name='applications_included', to='home.ProjectPage')),
                ('relevant_project_pages', models.ManyToManyField(
                    help_text='Project pages to be placed on the first page, eye catcher for this project',
                    related_name='applications_highlighted', to='home.ProjectPage')),
                ('skills', models.ManyToManyField(
                    help_text='Technology tags to be included, will be automatically formed to look relevant',
                    to='taggit.Tag')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CVGenerationSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_title', models.CharField(help_text='Default title to use', max_length=255)),
                ('default_experience_overview',
                 wagtailmarkdown.fields.MarkdownField(default='Python developer experience: 7 years',
                                                      help_text='Notice on your experience')),
                ('default_education_overview',
                 wagtailmarkdown.fields.MarkdownField(default='Novosibirsk State Technical University',
                                                      help_text='Notice on your education')),
                ('default_contact_details', wagtailmarkdown.fields.MarkdownField(default='sergey@cheparev.com')),
                ('default_languages_overview', wagtailmarkdown.fields.MarkdownField(default='English: fluent')),
                ('default_rate_overview',
                 wagtailmarkdown.fields.MarkdownField(default='<<change default in settings>>')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE,
                                              to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
