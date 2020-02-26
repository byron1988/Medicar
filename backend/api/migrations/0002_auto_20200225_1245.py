# Generated by Django 2.2 on 2020-02-25 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Medico', verbose_name='Medico'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='especialidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Especialidade', verbose_name='Especialidade'),
        ),
    ]
