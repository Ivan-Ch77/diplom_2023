# Generated by Django 4.2.3 on 2023-07-06 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='prog_language',
            field=models.CharField(choices=[('PY', 'Python'), ('JS', 'JavaScript'), ('HTML', 'HTML'), ('SQL', 'SQL'), ('PHP', 'PHP')], default='PY', max_length=4, verbose_name='Programming language'),
        ),
    ]
