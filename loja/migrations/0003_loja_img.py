# Generated by Django 4.2.7 on 2023-12-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_alter_loja_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='loja',
            name='img',
            field=models.CharField(default='#', max_length=200),
        ),
    ]
