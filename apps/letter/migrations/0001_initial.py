# Generated by Django 4.2.2 on 2023-08-12 21:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('message', ckeditor.fields.RichTextField(null=True, verbose_name='Mensaje')),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Mensajes',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('activo', models.BooleanField(default=True, verbose_name='Activo')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de suscripción')),
            ],
            options={
                'verbose_name': 'Suscripción',
                'verbose_name_plural': 'Suscripciones',
                'ordering': ['-id'],
            },
        ),
    ]
