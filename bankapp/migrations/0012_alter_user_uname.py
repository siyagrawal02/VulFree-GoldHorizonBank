# Generated by Django 4.1b1 on 2023-10-01 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0011_remove_user_firstname_remove_user_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uname',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
