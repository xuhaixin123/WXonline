# Generated by Django 2.2.18 on 2021-02-23 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
        ('course', '0005_video_learn_times'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.Teacher', verbose_name='讲师'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_tell',
            field=models.CharField(default='', max_length=300, verbose_name='老师告诉你'),
        ),
        migrations.AddField(
            model_name='course',
            name='youneed_know',
            field=models.CharField(default='', max_length=300, verbose_name='课程须知'),
        ),
    ]
