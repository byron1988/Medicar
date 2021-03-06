# Generated by Django 2.2 on 2020-03-04 21:45

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('especialidade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(help_text='Digite a nome do médico', max_length=100)),
                ('crm', models.CharField(help_text='Digite o CRM do médico', max_length=7, unique=True)),
                ('email', models.EmailField(help_text='Digite o E-mail do médico', max_length=254, verbose_name='E-mail')),
                ('telefone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Digite o telefone do médico', max_length=128, region=None)),
                ('especialidade', models.ForeignKey(help_text='Selecione a especialidade do médico', on_delete=django.db.models.deletion.PROTECT, to='especialidade.Especialidade')),
            ],
            options={
                'verbose_name': 'Médico',
                'verbose_name_plural': 'Médicos',
            },
        ),
    ]
