# Generated by Django 3.0.7 on 2020-06-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200620_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='description',
            field=models.CharField(blank=True, db_index=True, max_length=150),
        ),
    ]