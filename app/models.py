
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


from django.core.validators import MinValueValidator ,MinLengthValidator

# Create your models here.
state_choice =(('National' ,'National') ,('International' ,'International'))

class Customer(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mobile = models.IntegerField()
    whatsapp_no =models.IntegerField()
    phone_no = models.IntegerField()
    Address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    state = models.CharField(choices=state_choice, max_length=200)
    email = models.EmailField(max_length=200)
    customer_image1 = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


category_choices = (('Day', 'Day'), ('Second', 'Second'), ('Minute', 'Minute'),
                    ('Square Fit', 'Square Fit'), ('Week', 'Week'), ('Year', 'Year'), ('Hour', 'Hour'),
                    ('Inch', 'Inch'), ('Centimeter', 'Centimeter'))


class Services(models.Model):
    title = models.CharField(max_length=100)
    Actual_price = models.FloatField()
    discounted_price = models.FloatField()
    expenditure_price = models.FloatField(default=0.0)
    as_per = models.CharField(choices=category_choices, max_length=15)
    description = models.TextField()
    Service_image1 = models.ImageField(upload_to='productimg')
    Service_image2 = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


    @property
    def total_cost(self):
       return self.quantity * self.service.discounted_price


status_choice = (('Accepted', 'Accepted'), ('Call Me', 'Call Me'), ('Service is Start', 'Service is Start'),
                 ('Wait For Our Message', 'Wait For Our Message'), ('Service is Complete', 'Service is Complete'),
                 ('Cancel', 'Cancel'), ('Service is near to end', 'Service is near to end'),
                 ('This time is not Available', 'This time is not Available'),)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=status_choice, default='Pending')
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    message = models.TextField(null=True, default='none')
    document = models.FileField(upload_to='productimg', default=None)

    def __str__(self):
        return str(self.id)


    
    @property
    def total_price(self):
       return self.quantity * self.service.discounted_price    




class expence(models.Model):
    
    title = models.CharField(max_length=100)
    excost = models.FloatField(default=0.0)
    description = models.TextField()

    def __str__(self):
        return str(self.id)


class profit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    expencess = models.ForeignKey(expence, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_costs = models.FloatField()
    total_pad = models.FloatField(default=0.0)
    remaing_amount = models.FloatField(default=0.0)
    total_profit = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.id)


class About_us(models.Model):
    title = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)
    description = models.TextField()
    about_image1 = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)
status_choice= (('read', 'read'), ('later', 'later'))

class contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    Subject = models.CharField(max_length=200)
    phone = models.IntegerField()
    description = models.TextField()
    status=models.CharField(max_length=100, choices=status_choice, default='unread')
    msg_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


rate_choices = (('30', '30'), ('50', '50'), ('40', '40'),
                ('50', '50'), ('60', '60'), ('70', '70'), ('90', '90'),
                ('99', '99'), ('100', '100'))


class feed_back(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    name_of_serves = models.CharField(max_length=100)
    description = models.TextField()
    rate_us = models.CharField(choices=rate_choices, max_length=4)

    def __str__(self):
        return str(self.id)


class blogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subject = models.EmailField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return str(self.id)



   