# Generated by Django 3.0.7 on 2020-06-22 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_link_man'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]
