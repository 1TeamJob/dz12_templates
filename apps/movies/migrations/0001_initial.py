# Generated by Django 3.2.8 on 2021-10-22 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('birth_date', models.DateField(verbose_name='Birth date')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('release_date', models.DateField(verbose_name='Release date')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.director')),
            ],
        ),
    ]