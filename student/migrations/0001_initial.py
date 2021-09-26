# Generated by Django 3.2.7 on 2021-09-26 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filier', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=250)),
                ('l_name', models.CharField(max_length=250)),
                ('filiers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.filier')),
            ],
        ),
    ]
