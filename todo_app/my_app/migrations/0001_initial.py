# Generated by Django 4.0.4 on 2022-04-27 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('descripton', models.CharField(max_length=50)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
