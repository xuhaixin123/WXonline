# Generated by Django 2.2.18 on 2021-02-24 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_course_is_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.CharField(default='', max_length=250, verbose_name='访问地址'),
        ),
    ]
