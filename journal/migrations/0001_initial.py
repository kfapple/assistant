# Generated by Django 2.1.3 on 2019-06-05 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='內容')),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
