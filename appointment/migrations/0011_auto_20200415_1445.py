# Generated by Django 3.0.2 on 2020-04-15 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0010_auto_20200415_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='topic',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
