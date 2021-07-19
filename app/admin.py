from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import (Customer, Services, Cart, OrderPlaced,expence,profit,About_us,contact_us, feed_back,blogs)

# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'mobile', 'whatsapp_no','phone_no','Address','country','city', 'email', 'state','customer_image1']

@admin.register(Services)
class ServicesModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'Actual_price', 'discounted_price', 'description', 'as_per', 'expenditure_price','Service_image1', 'Service_image2']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','service','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'service', 'quantity', 'order_date', 'status','start_date','end_date','message','document']




@admin.register(expence)
class expenceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'excost', 'description']

@admin.register(profit)
class profitModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'service', 'expencess', 'quantity', 'total_costs', 'total_pad', 'remaing_amount','total_profit']

@admin.register(About_us)
class About_usModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'Subject','description', 'about_image1']

@admin.register(contact_us)
class contact_usModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'Subject', 'phone', 'description','status','msg_time']

@admin.register(feed_back)
class feed_backModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'email', 'name', 'phone', 'name_of_serves', 'description','rate_us']


@admin.register(blogs)
class blogsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'subject', 'description']


