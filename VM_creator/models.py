from django.db import models

# Create your models here.
class ModelTemplate(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Pool(ModelTemplate):
    pass

    verbose_name = "Пул"
    verbose_name_plural = "Пулы"


class Division(ModelTemplate):
    pass

    verbose_name = "Подразделение"
    verbose_name_plural = "Подразделения"


class Configurations(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name", null=True, blank=True)
    number_of_cores = models.IntegerField(
        verbose_name="Number of cores", default=1, null=True, blank=True
    )
    os_disk_space = models.FloatField(
        verbose_name="OS disk space", default=1, null=True, blank=True
    )
    resource_disk_size_in_mb = models.FloatField(
        verbose_name="Resource disk size", default=1, null=True, blank=True
    )
    memory_in_mb = models.FloatField(
        verbose_name="Memory", default=1, null=True, blank=True
    )
    max_data_disk_count = models.FloatField(
        verbose_name="MAX data disk count", default=1, null=True, blank=True
    )

    def __str__(self):
        return self.name

    verbose_name = "Configuration"
    verbose_name_plural = "Configurations"


class VirtualMachine(models.Model):
    configuration = models.ForeignKey(
        Configurations,
        related_name="configuration",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    pool = models.ForeignKey(
        Pool,
        verbose_name="Пул",
        related_name="pool",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    division = models.ForeignKey(
        Division,
        verbose_name="Подразделение",
        related_name="division",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=200, verbose_name="Название ВМ")
    ram_capacity = models.FloatField(verbose_name="Объём RAM, Гб", default=1)
    cpu_cores = models.IntegerField(verbose_name="Количество Ядер vCPU", default=1)
    hdd_capacity = models.FloatField(verbose_name="Объём HDD, Гб", default=10)

    def __str__(self):
        return self.name

    verbose_name = "Виртуальная машина"
    verbose_name_plural = "Виртуальные машины"
