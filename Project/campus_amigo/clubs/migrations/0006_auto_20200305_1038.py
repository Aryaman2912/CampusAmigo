# Generated by Django 3.0.3 on 2020-03-05 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0005_auto_20200305_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='email',
            field=models.EmailField(help_text='Club email id', max_length=1000, unique=True, verbose_name='Email Id'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(help_text='Club email id', max_length=1000, unique=True, verbose_name='Email Id'),
        ),
    ]
