# Generated by Django 4.1.2 on 2022-11-16 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(max_length=50)),
                ('especialista', models.CharField(default='Desconoce', max_length=50)),
                ('fecha', models.DateField()),
                ('lugar', models.CharField(max_length=50)),
                ('hora', models.TimeField()),
                ('observaciones', models.CharField(max_length=100)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ejemplo.cliente')),
            ],
        ),
    ]
