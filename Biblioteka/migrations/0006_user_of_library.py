# Generated by Django 3.2.9 on 2021-12-08 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Biblioteka', '0005_auto_20211208_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_of_Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_start', models.DateField(auto_now=True)),
                ('date_of_end', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
