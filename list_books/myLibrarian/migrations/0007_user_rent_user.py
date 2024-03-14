# Generated by Django 5.0.1 on 2024-03-14 18:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myLibrarian', '0006_remove_rent_user_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=20)),
                ('cellPhoneNumber', models.CharField(max_length=12)),
            ],
        ),
        migrations.AddField(
            model_name='rent',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='myLibrarian.user'),
            preserve_default=False,
        ),
    ]
