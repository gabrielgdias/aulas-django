# Generated by Django 2.2.10 on 2020-02-29 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula5', '0006_auto_20200229_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_nascimento',
            field=models.DateField(verbose_name=False),
        ),
    ]