# Generated by Django 3.0.5 on 2021-12-18 20:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='SEyear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]