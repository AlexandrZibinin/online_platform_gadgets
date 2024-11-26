from django.db import models

from config.settings import NULLABLE

TYPES_AGENT = {
    "Индивидуальный предприниматель": "ip",
    "Розничная сеть": "retail",
    "Завод": "factory",
}


class Agent(models.Model):
    """Модель участника сети"""

    type_agent = models.CharField(choices=TYPES_AGENT, verbose_name="Тип контрагента")
    name = models.CharField(max_length=100, verbose_name="Имя контрагента")
    email = models.EmailField(max_length=100, verbose_name="Электронная почта")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.CharField(max_length=100, verbose_name="Номер дома")
    level = models.IntegerField(verbose_name="Уровень в сети", **NULLABLE)

    def __str__(self):
        return f"Контрагент: {self.type_agent} {self.name}"

    class Meta:
        verbose_name = "Контрагент"
        verbose_name_plural = "Контрагенты"


class Product(models.Model):
    """Модель продукта сети"""

    name = models.CharField(max_length=100, verbose_name="Название продукта")
    model_name = models.CharField(max_length=100, verbose_name="Название модели")
    date_launch_market = models.DateField(
        verbose_name="Дата выхода продукта на рынок", **NULLABLE
    )

    def __str__(self):
        return f"Продукт: {self.name} {self.model_name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Link(models.Model):
    """Модель звена сети(сделка)"""

    supplier = models.ForeignKey(
        Agent,
        on_delete=models.CASCADE,
        verbose_name="Поставщик",
        related_name="supplier_link",
    )
    buyer = models.ForeignKey(
        Agent,
        on_delete=models.CASCADE,
        verbose_name="Покупатель",
        related_name="buyer_link",
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Продукт"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания звена"
    )
    duty = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=20,
        verbose_name="Задолженность",
        **NULLABLE,
    )

    def __str__(self):
        return f"Покупатель: {self.buyer.name} {self.created_at}"

    class Meta:
        verbose_name = "Звено"
        verbose_name_plural = "Звенья"
