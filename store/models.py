from django.db import models

# Create your models here.

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=50)
    featured_produckt = models.ForeignKey('Produckt', on_delete=models.SET_NULL, null= True , related_name= '+')


class Produckt(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete = models.PROTECT)
    promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, "BRONZE"),
        (MEMBERSHIP_SILVER, "SILVER"),
        (MEMBERSHIP_GOLD, "GOLD")
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1 ,choices= MEMBERSHIP_CHOICES , default= MEMBERSHIP_BRONZE)
    

class Order(models.Model):
    STATUS_PENDING = "P"
    STATUS_COMPLITE = "C"
    STATUS_FAILED  = "F"
    PAYMENT_STATUSES = [
        (STATUS_PENDING, "PENDING"),
        (STATUS_COMPLITE, "COMPLATE"),
        (STATUS_FAILED, "FAILED")
    ]
    payment_status = models.CharField(max_length= 1 , choices= PAYMENT_STATUSES, default= STATUS_PENDING)
    pleased_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete= models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete = models.PROTECT)
    produckt = models.ForeignKey(Produckt , on_delete = models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    stret = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Card(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CardItem(models.Model):
    card = models.ForeignKey(Card , on_delete=models.CASCADE)
    product = models.ForeignKey(Produckt, on_delete= models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    

