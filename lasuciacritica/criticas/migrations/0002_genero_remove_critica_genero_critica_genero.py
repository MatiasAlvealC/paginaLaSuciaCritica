# Generated by Django 4.1 on 2024-11-06 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criticas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='critica',
            name='genero',
        ),
        migrations.AddField(
            model_name='critica',
            name='genero',
            field=models.ManyToManyField(related_name='criticas', to='criticas.genero'),
        ),
    ]
