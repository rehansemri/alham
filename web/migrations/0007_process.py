# Generated by Django 5.1.3 on 2024-11-14 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_remove_aboutus_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='images/process')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/process')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/process')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='images/process')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='images/process')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='images/process')),
                ('p1', models.TextField(blank=True, null=True)),
                ('p2', models.TextField(blank=True, null=True)),
                ('p3', models.TextField(blank=True, null=True)),
                ('p4', models.TextField(blank=True, null=True)),
                ('p5', models.TextField(blank=True, null=True)),
                ('p6', models.TextField(blank=True, null=True)),
            ],
        ),
    ]