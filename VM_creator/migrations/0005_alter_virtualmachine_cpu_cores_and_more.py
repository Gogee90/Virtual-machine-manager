# Generated by Django 4.0 on 2021-12-27 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VM_creator', '0004_alter_configurations_max_data_disk_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtualmachine',
            name='cpu_cores',
            field=models.FloatField(default=1, verbose_name='Количество Ядер vCPU'),
        ),
        migrations.AlterField(
            model_name='virtualmachine',
            name='hdd_capacity',
            field=models.FloatField(default=10, verbose_name='Объём HDD, Гб'),
        ),
        migrations.AlterField(
            model_name='virtualmachine',
            name='ram_capacity',
            field=models.FloatField(default=1, verbose_name='Объём RAM, Гб'),
        ),
    ]
