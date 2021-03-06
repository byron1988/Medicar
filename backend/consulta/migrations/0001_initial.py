# Generated by Django 2.2 on 2020-03-09 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medico', '0001_initial'),
        ('especialidade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dia', models.DateField()),
                ('horario', models.TimeField()),
                ('especialidade', models.ForeignKey(help_text='Selecione a especialidade para consulta', on_delete=django.db.models.deletion.PROTECT, to='especialidade.Especialidade')),
                ('medico', models.ForeignKey(help_text='Selecione um médico para a consulta', on_delete=django.db.models.deletion.PROTECT, to='medico.Medico', verbose_name='Médico')),
            ],
            options={
                'verbose_name': 'consulta',
                'verbose_name_plural': 'consultas',
            },
        ),
    ]
