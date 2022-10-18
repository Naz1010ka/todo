# Generated by Django 4.1.2 on 2022-10-18 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0003_alter_goal_for_month_month_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('done_for_today', models.TextField(default='')),
                ('important', models.TextField(default='')),
                ('comment', models.TextField(default='')),
            ],
        ),
    ]