# Generated by Django 4.1.2 on 2022-10-28 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_enrollment'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='ssn',
            field=models.CharField(default='', max_length=11),
        ),
    ]