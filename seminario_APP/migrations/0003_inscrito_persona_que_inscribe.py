# Generated by Django 5.1 on 2024-12-17 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminario_APP', '0002_inscrito_correo_alter_inscrito_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscrito',
            name='persona_que_inscribe',
            field=models.CharField(default='Administrador', max_length=100),
            preserve_default=False,
        ),
    ]