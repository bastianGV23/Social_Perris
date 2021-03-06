# Generated by Django 2.1.3 on 2018-11-13 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='perrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePerro', models.CharField(max_length=50)),
                ('razaP', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('imagen', models.FileField(upload_to='media')),
                ('estado', models.OneToOneField(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='rescate.Estado')),
            ],
        ),
    ]
