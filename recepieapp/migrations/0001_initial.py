# Generated by Django 4.2.4 on 2023-12-08 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recepie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recepie_name', models.CharField(max_length=200)),
                ('recepie_description', models.TextField()),
                ('recepie_image', models.ImageField(upload_to='media')),
            ],
        ),
    ]
