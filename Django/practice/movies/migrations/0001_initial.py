# Generated by Django 2.1.5 on 2020-06-18 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('title_en', models.TextField()),
                ('audience', models.TextField()),
                ('open_date', models.CharField(max_length=20)),
                ('genre', models.TextField()),
                ('watch_grade', models.TextField()),
                ('score', models.TextField()),
                ('poster_url', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]