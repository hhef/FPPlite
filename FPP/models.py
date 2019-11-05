from django.db import models

ORDERTYPE = (
    (1, "Dostawa"),
    (2, "Sprzedaż")
)

CONTRACTORTYPE = (
    (1, "Klient"),
    (2, "Dostawca")
)


class Category(models.Model):
    category = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category


class Product(models.Model):
    code = models.CharField(max_length=12)
    name = models.CharField(max_length=256)
    quantity = models.PositiveIntegerField()
    price_for_sale = models.ManyToManyField('ProductHistory')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    @property
    def last_price(self):
        return self.price_for_sale.last()

    def __str__(self):
        return f"Kod: {self.code}, Produkt: {self.name}"


class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    amount = models.FloatField()


class Order(models.Model):
    type = models.FloatField(choices=ORDERTYPE)
    date = models.DateField()
    contractor = models.ManyToManyField('Contractor')
    details = models.ForeignKey(OrderDetail, on_delete=models.DO_NOTHING)


class Contractor(models.Model):
    type = models.FloatField(choices=CONTRACTORTYPE)
    name = models.CharField(max_length=256)
    contact = models.TextField()
    debt = models.FloatField(default=0)

    def __str__(self):
        return self.name


class ProductHistory(models.Model):
    price_for_sale = models.FloatField()
    purchase_price = models.FloatField()

# Można zrobić cenę w produkcie stałą, i z historii ceny foreign key do ceny aktualnej. Jeżeli cena aktualnie jest różna
# się updateuje, a jeżeli nie to zostaje. Przy dostawie cena zostanie wrzucona do historii cen
