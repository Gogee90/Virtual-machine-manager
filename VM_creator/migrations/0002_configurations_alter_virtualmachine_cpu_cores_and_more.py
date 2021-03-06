# Generated by Django 4.0 on 2021-12-27 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VM_creator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configurations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Plans')),
                ('number_of_cores', models.IntegerField(blank=True, default=1, null=True, verbose_name='Number of cores')),
                ('os_disk_space', models.IntegerField(blank=True, default=1, null=True, verbose_name='OS disk space')),
                ('resource_disk_size_in_mb', models.IntegerField(blank=True, default=1, null=True, verbose_name='Resource disk size')),
                ('memory_in_mb', models.IntegerField(blank=True, default=1, null=True, verbose_name='Memory')),
                ('max_data_disk_count', models.IntegerField(blank=True, default=1, null=True, verbose_name='MAX data disk count')),
            ],
        ),
        migrations.AlterField(
            model_name='virtualmachine',
            name='cpu_cores',
            field=models.IntegerField(default=1, verbose_name='Количество Ядер vCPU'),
        ),
        migrations.AlterField(
            model_name='virtualmachine',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='division', to='VM_creator.division', verbose_name='Подразделение'),
        ),
        migrations.AlterField(
            model_name='virtualmachine',
            name='hdd_capacity',
            field=models.IntegerField(default=10, verbose_name='Объём HDD, Гб'),
        ),
        migrations.AlterField(
            model_name='virtualmachine',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название ВМ'),
        ),
        migrations.AlterField(
            model_name='virtualmachine',
            name='pool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pool', to='VM_creator.pool', verbose_name='Пул'),
        ),
        migrations.AlterField(
            model_name='virtualmachine',
            name='ram_capacity',
            field=models.IntegerField(default=1, verbose_name='Объём RAM, Гб'),
        ),
    ]
