# Generated by Django 4.0.1 on 2022-01-15 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='categoria',
            field=models.CharField(choices=[('acao', 'Ação'), ('comedia', 'Comédia'), ('terror', 'Terror'), ('ficcao', 'Ficção Científica')], max_length=15),
        ),
        migrations.CreateModel(
            name='Episodio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('video', models.URLField()),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodios', to='filme.filme')),
            ],
        ),
    ]
