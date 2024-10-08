# Generated by Django 5.1 on 2024-08-22 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_work_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Ingrese el título del servicio', max_length=100, verbose_name='Título')),
                ('icon', models.CharField(help_text='Ingrese el ícono del servicio', max_length=50, verbose_name='Ícono')),
                ('description', models.TextField(help_text='Ingrese la descripción del servicio', verbose_name='Descripción')),
                ('modal_image', models.ImageField(help_text='Seleccione la imagen para el modal', upload_to='services/', verbose_name='Imagen Modal')),
                ('modal_subtitle', models.CharField(default='SERVICIOS', help_text='Ingrese el subtítulo para el modal', max_length=100, verbose_name='Subtítulo Modal')),
                ('modal_title', models.CharField(help_text='Ingrese el título para el modal', max_length=100, verbose_name='Título Modal')),
                ('modal_content', models.TextField(help_text='Ingrese el contenido para el modal', verbose_name='Contenido Modal')),
                ('process_title', models.CharField(help_text='Ingrese el título para el proceso', max_length=100, verbose_name='Título del Proceso')),
                ('process_description', models.TextField(help_text='Ingrese la descripción para el proceso', verbose_name='Descripción del Proceso')),
                ('process_steps', models.TextField(help_text='Ingrese los pasos para el proceso', verbose_name='Pasos del Proceso')),
                ('additional_info', models.TextField(blank=True, help_text='Ingrese información adicional (opcional)', null=True, verbose_name='Información Adicional')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='work',
            name='categories',
            field=models.ManyToManyField(help_text='Las categorías del trabajo.', related_name='works', to='main.category', verbose_name='Categorías'),
        ),
    ]
