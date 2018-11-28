# Generated by Django 2.1.2 on 2018-11-26 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMascota', models.CharField(max_length=20)),
                ('razaMascota', models.CharField(max_length=20)),
                ('descripcionMascota', models.CharField(max_length=50)),
                ('estadoMascota', models.CharField(choices=[('disponible', 'Disponible'), ('adoptado', 'Adoptado'), ('rescatado', 'Rescatado')], default='', max_length=15, verbose_name='estadoMascota')),
                ('fotoMascota', models.ImageField(upload_to='Sistema/static/images/')),
            ],
        ),
    ]
