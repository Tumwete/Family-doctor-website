# Generated by Django 4.0.4 on 2022-05-13 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='sent_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
