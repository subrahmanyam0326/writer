# Generated by Django 2.2.14 on 2021-01-27 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewerLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=65)),
                ('password', models.CharField(max_length=65)),
            ],
        ),
        migrations.CreateModel(
            name='ViewerReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=65)),
                ('l_name', models.CharField(max_length=65)),
                ('username', models.CharField(max_length=65)),
                ('password', models.CharField(max_length=65)),
            ],
        ),
    ]
