# Generated by Django 3.1.7 on 2021-06-02 22:26

from django.db import migrations, models
import summa.models


class Migration(migrations.Migration):

    dependencies = [
        ('summa', '0013_campus_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='campus',
            name='logo',
            field=models.FileField(default='39841c45-a3f7-4f2f-b211-130fdbbd2cab.png', upload_to=summa.models.get_file_path, verbose_name='Logo Instituição'),
            preserve_default=False,
        ),
    ]
