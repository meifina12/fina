# Generated by Django 4.2.7 on 2023-11-11 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hewan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hewan', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jenis_Hewan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jenis_Hewan', models.CharField(max_length=100)),
                ('Makanan_Hewan', models.TextField()),
                ('Hewan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vina.hewan')),
            ],
        ),
    ]
