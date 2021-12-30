# Generated by Django 4.0 on 2021-12-27 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VM_creator', '0003_virtualmachine_configuration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configurations',
            name='max_data_disk_count',
            field=models.FloatField(blank=True, default=1, null=True, verbose_name='MAX data disk count'),
        ),
        migrations.AlterField(
            model_name='configurations',
            name='memory_in_mb',
            field=models.FloatField(blank=True, default=1, null=True, verbose_name='Memory'),
        ),
        migrations.AlterField(
            model_name='configurations',
            name='os_disk_space',
            field=models.FloatField(blank=True, default=1, null=True, verbose_name='OS disk space'),
        ),
        migrations.AlterField(
            model_name='configurations',
            name='resource_disk_size_in_mb',
            field=models.FloatField(blank=True, default=1, null=True, verbose_name='Resource disk size'),
        ),
    ]
