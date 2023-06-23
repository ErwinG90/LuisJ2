# Generated by Django 4.2.2 on 2023-06-22 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concierto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(max_length=100)),
                ('personas_total', models.IntegerField()),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_entrada', models.CharField(max_length=200)),
                ('stock', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('conciert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.concierto')),
            ],
        ),
        migrations.AlterField(
            model_name='ingreso',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('Concierto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.concierto')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ingreso')),
                ('entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.entrada')),
            ],
        ),
    ]
