# Generated by Django 4.1.2 on 2022-10-06 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToMeet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persone', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField(default=True)),
                ('date_of_meeting', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(default='')),
                ('is_closed', models.BooleanField(default=False)),
                ('is_favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
