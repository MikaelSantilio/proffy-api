# Generated by Django 3.0.9 on 2020-08-10 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('subject', models.CharField(max_length=64, verbose_name='Matéria')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Custo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProffyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('name', models.CharField(max_length=128, verbose_name='Nome')),
                ('avatar', models.CharField(max_length=164, verbose_name='Avatar')),
                ('whatsapp', models.CharField(max_length=20, verbose_name='Whatsapp')),
                ('bio', models.CharField(max_length=256, verbose_name='Bio')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('proffy_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ProffyUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('week_day', models.IntegerField(verbose_name='Dia da Semana')),
                ('start_at', models.IntegerField(verbose_name='De')),
                ('end_at', models.IntegerField(verbose_name='Até')),
                ('klass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Class')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='class',
            name='proffy_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ProffyUser'),
        ),
    ]
