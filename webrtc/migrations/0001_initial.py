# Generated by Django 2.1.3 on 2019-01-08 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=1000, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
