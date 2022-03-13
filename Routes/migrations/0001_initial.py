# Generated by Django 4.0 on 2022-03-12 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('project_name', models.CharField(max_length=100)),
                ('project_number', models.IntegerField(primary_key=True, serialize=False)),
                ('client', models.CharField(max_length=100)),
                ('project_manager', models.CharField(max_length=100)),
                ('last_review', models.DateField()),
                ('scope_of_work', models.TextField()),
            ],
        ),
    ]
