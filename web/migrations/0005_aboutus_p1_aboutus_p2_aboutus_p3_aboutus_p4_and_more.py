# Generated by Django 5.1.3 on 2024-11-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_aboutus_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='p1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='p2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='p3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='p4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='p5',
            field=models.TextField(blank=True, null=True),
        ),
    ]
