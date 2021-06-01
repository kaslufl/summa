# Generated by Django 3.1.7 on 2021-06-01 00:39

from django.db import migrations, models
import travel.models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to=travel.models.get_file_path, verbose_name='Foto'),
        ),
    ]
