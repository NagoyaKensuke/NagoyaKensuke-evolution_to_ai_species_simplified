# Generated by Django 4.2.5 on 2023-09-04 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_delete_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]