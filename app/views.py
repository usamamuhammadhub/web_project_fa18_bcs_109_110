
from os import name, times
from re import L, T
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import html
from django.views import View


from app.models import About_us, Services,Customer,OrderPlaced,contact_us


from PIL import Image
from django import forms
from django.contrib.auth.models import Group,User
from django.db.models.query_utils import Q
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.utils.translation import to_language
from django.views import View
from .models import Cart, Customer,  OrderPlaced
from .forms import CustomerRegistrationForm
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CustomerForm,Orderfrom,Servicesform,contact_usform
from django.core.mail import send_mass_mail


from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.template.loader import render_to_string
from django.utils.html import strip_tags



class ServiceView(View):
 def get(self ,request):
  as_perr = Services.objects.filter(as_per='Day')

  # bottomwers = Services.objects.filter(as_per='BW')
  # mobiles =Services.objects.filter(category='M')
  fott =Services.objects.filter(as_per='Square Fit')
  return render(request, 'app/home.html', {'as_perr': as_perr, 'fott': fott})


# sevice show
def sevice(request):
    
    sevices = Services.objects.all()

    # elif data=='toyota' or data=='dk':
    #      mobiles=Product.objects.filter(category='M').filter(Brand=data)

    return render(request, 'app/services.html', {'sevices': sevices})


# About us
def about(request):
    ab = About_us.objects.all()

    return render(request, 'app/about.html', {'ab': ab})






 # About us
def abouts(request):
    ab = About_us.objects.all()

    return render(request, 'app/abouts.html', {'ab': ab})   


# customerrigtation

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.info(request, 'Congratulations You are Register')
            user=form.save()
            print(form)
            groups=Group.objects.get(name='CUSTOMER')
            user.groups.add(groups)
            

        return render(request, 'app/customerregistration.html', {'form': form})
       

# login funtion
# def login1(request):
#   return render(request, 'app/login.html')


# after login redirct
@login_required
def dash(request):
    
    
    return render(request, "app/dashbase.html")


# view services in customer dash board
@login_required
def viewserviescustomerdash(request, data=None):
    if data == None:
        services = Services.objects.all()
    elif data == 'Billboard' or data == 'Creatives' or data == 'Streamers':
        services = Services.objects.filter(title=data)

    return render(request, 'app/dashservices.html', {'services': services})


# def viewserviescustomerdash(request,data=None):
# if data== None:
# services=Services.objects.all()


# return render(request,'app/dashservices.html',{'services': services})

# class viewserviescustomerdash(View):
# def get(self,request,pk):
#  services=Services.objects.get(pk=pk )
# item_already_in_cart=False
# item_already_in_cart =Cart.objects.filter(Q(service=service.id)& Q(user=request.user)).exists()

# return render(request,'app/servicedetail.html',{'services':services})


def index(request):
    return render(request, "app/index.html")


def inner_page(request):
    #  params= {'name':'usama','place':'okara'}
    return render(request, "app/inner-page.html")


def portfolio_details(request):
    return render(request, "app/portfolio-details.html")


# def home(request):

# return render(request,"app/home.html")


# def bas(request):

#   return render(request,"app/base1.html")
# @method_decorator(login_required,name='dispatch')
@method_decorator(login_required,name='dispatch')
class service_detail(View):
    def get(self, request, pk):
        service = Services.objects.get(pk=pk)
        item_already_in_cart=False
        item_already_in_cart =Cart.objects.filter(Q(service=service.id)& Q(user=request.user)).exists()

        #return render(request, 'app/servicedetail.html', {'servic': servic})
        return render(request,'app/servicedetail.html',{'service':service,'item_already_in_cart':item_already_in_cart})


# add to card
@login_required
def add_to_cart(request):
    user = request.user
    service_id = request.GET.get('ser_id')
    service = Services.objects.get(id=service_id)
    Cart(user=user, service=service).save()
    return redirect('showcart')

@login_required
def showcart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 0.0
        total_amount = 0.0
        cart_service = [p for p in Cart.objects.all() if p.user == user]
        if cart_service:
            for p in cart_service:
                tempamount = (p.quantity * p.service.discounted_price)
                amount += tempamount
                totalamount = amount + shipping_amount

            return render(request, 'app/addtocart.html', {'carts': cart, 'totalamount': totalamount, 'amount': amount})
        else:
            return render(request, 'app/emptycart.html')


def plus_cart(request):
    if request.method == 'GET':
        ser_id = request.GET['ser_id']
        c = Cart.objects.get(Q(service=ser_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 0.0
        cart_service = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_service:
            tempamount = (p.quantity * p.service.discounted_price)
            amount += tempamount
            totalamount = amount + shipping_amount

        data = {'quantity': c.quantity, 'amount': amount, 'totalamount': totalamount}
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        ser_id = request.GET['ser_id']
        c = Cart.objects.get(Q(service=ser_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 0.0
        cart_service = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_service:
            tempamount = (p.quantity * p.service.discounted_price)
            amount += tempamount
            totalamount = amount + shipping_amount

        data = {'quantity': c.quantity, 'amount': amount, 'totalamount': totalamount}
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        ser_id = request.GET['ser_id']
        c = Cart.objects.get(Q(service=ser_id) & Q(user=request.user))

        c.delete()
        amount = 0.0
        shipping_amount = 0.0
        cart_service = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_service:
            tempamount = (p.quantity * p.service.discounted_price)
            amount += tempamount
            totalamount = amount + shipping_amount

        data = {'amount': amount, 'totalamount': totalamount}
        return JsonResponse(data)


"""
def about(request):
    return HttpResponse("about")
     """

# def openbutten(request):
# return HttpResponse('''<a href="https://www.youtube.com/" >open </a>''')
"""
def remove(request):
    page = request.GET.get('text','default')
    print(page)
    #text analzsis



    return HttpResponse("remove punctionation")
    """


def home(request):
    return render(request, 'app/home.html')





#

@login_required
def checkout(request):
   user=request.user
   add=Customer.objects.filter(user=user)
   cart_item = Cart.objects.filter(user=user)
   amount=0.0
   shipping_amount =0.0
   totalamount=0.0
   cart_service= [p for p in Cart.objects.all() if p.user==request.user]
   if cart_service:
      for p in cart_service:
         tempamount=(p.quantity*p.service.discounted_price)
         amount+=tempamount
      totalamount= amount+shipping_amount
      return render(request, 'app/checkout.html',{'add':add,'totalamount':totalamount,'cart_item':cart_item})



@login_required
def pymentdone(request):
    user=request.user
    email=request.user.email
    custid=request.GET.get('custid')
    customer=Customer.objects.get(id=custid)

    if customer:
      cart=Cart.objects.filter(user=user)
      messag='none'
      for c in cart:
        OrderPlaced(user=user,customer=customer,service=c.service,quantity=c.quantity,message=messag).save()
        amount=0.0
        shipping_amount =0.0
        totalamount=0.0
        cart_service= [p for p in Cart.objects.all() if p.user==request.user]
        if cart_service:
           for p in cart_service:
               tempamount=(p.quantity*p.service.discounted_price)
               amount+=tempamount
        totalamount= amount+shipping_amount
        c.delete()
        

        html_content = render_to_string("app/djmail.html",{'user':user,'totalamount':totalamount})
        text_content= strip_tags(html_content)
        email=EmailMultiAlternatives(
            'Thanks to Order',text_content,'usamamahar014@gmail.com',[email]


        )
        email.attach_alternative(html_content,"text/html")
        email.send()
        send_mail(
       'New Order',
    'Check you Account',
    'usamamahar014@gmail.com',
    ['usamamuhammadmahar@gmail.com'],
    fail_silently=False,
)
        
        
        
        #msg1="Thanks to order you totatal bill is "
       # msg12=print("Thanks to order you totatal bill is ",totalamount) 
        
        
       # message1 = ('New order','new order a gaya',  'usamamahar014@gmail.com', ['usamamuhammadmahar@gmail.com'])
       # message2 = ('thanks', des, 'usamamahar014@gmail.com',[email])
       # send_mass_mail((message1, message2), fail_silently=False)
        
        

    
    else:
    
       return redirect('CustomerFormview/')    
    return redirect("orders")

@login_required
def orders(request):
   ordplc=OrderPlaced.objects.filter(user=request.user)
   
   return render(request, 'app/orders.html',{'ordplc':ordplc})

def orderadmin(request):
    orders=OrderPlaced.objects.all()

    return render(request,'app/orderadmin.html',{'orders':orders})








#add to order
"""
def add_to_order(request):
    user = request.user
    service_id = request.GET.get('ser_id')
    service = Services.objects.get(id=service_id)
    if request.method=='POST':
        start_date=request.POST.get('stdate')
        end_date=request.POST.get('enddate')
        messag=request.POST.get('msg')


        OrderPlaced(user=user, service=service,customer=user,start_date=start_date,end_date=end_date,message=messag).save()
        messages.success(request,'date enter')
    return redirect(request,'orders.html')"""



#customerprofile
@login_required
def CustomerFormview(request):
    user=request.user
    name=request.user.username
    email=request.user.email
    if request.method == 'POST':
        fm=CustomerForm(request.POST, request.FILES)
        if fm.is_valid():
            
            #name=fm.cleaned_data['name']
            #email=fm.cleaned_data['email']
            phon=fm.cleaned_data['phone_no']
            whattpp=fm.cleaned_data['whatsapp_no']
            mobile=fm.cleaned_data['mobile']
            state=fm.cleaned_data['state']
            country=fm.cleaned_data['country']
            city=fm.cleaned_data['city']
            Address=fm.cleaned_data['Address']
            image=fm.cleaned_data['customer_image1']
            Customer(user=user,name=name,email=email,whatsapp_no=whattpp,phone_no=phon,mobile=mobile,country=country,state=state,city=city,Address=Address,customer_image1=image).save()
            username = request.user.username
            email=request.user.email
            msg="The New Customer is reigister who name is "
            msg2=" The email of customer is "
            description=msg+username+msg2+email
            email=request.user.email
            message1 = ('New Customer is Registered', description, 'usamamahar014@gmail.com', ['usamamuhammadmahar@gmail.com'])
            message2 = ('wellcome', 'Wellcome to being a part of AWSONS', 'usamamahar014@gmail.com', [email])
            send_mass_mail((message1, message2), fail_silently=False)
            
            
            return redirect('viewcustomeredit')            

    else:
        fm=CustomerForm()
    return render(request,'app/cutomerprofileform.html',{'form':fm})        


#fectch the customer detail
@login_required
def viewcustomeredit(request):
    
    
    customer = Customer.objects.filter(user=request.user)


    return render(request, 'app/customerviewupdate.html', {'form':  customer})





#admin view ther customer
from django.db.models import Count

@login_required
def adminviewcutomer(request):
    
    
    customer = Customer.objects.all()
    
    customers = Customer.objects.count()
    #take_order=OrderPlaced.objects.annotate(Count(customer))
    #take_order=OrderPlaced.objects.filter(customer=customer).count
    take_order=OrderPlaced.objects.annotate(Count('id')).count()

    return render(request, 'app/adminviewcutomer.html', {'form':  customer,'take_order':take_order, 'customers': customers })

#####    

@login_required
def updatecustomerbyadmin(request,id):
    if request.method=='POST':
        pi=Customer.objects.get(pk=id)
        
        fm=CustomerForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('adminviewcutomer')      
        

    else:
          pi=Customer.objects.get(pk=id)
        
          fm=CustomerForm(instance=pi)  
    return render(request,'app/updatebyadmin.html',{'form':fm })





#deting custumen detail

def delcustomeredit(request,id):
    if request.method=='POST':
        pi=Customer.objects.get(pk=id)
       # pii=User.objects.get(pk=id)
       # pii.delete()
        pi.delete()
        return redirect('adminviewcutomer')



#update custumen detail
@login_required
def updatecustomeredit(request,id):
    if request.method=='POST':
        pi=Customer.objects.get(pk=id)
        
        fm=CustomerForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('viewcustomeredit')      
        

    else:
          pi=Customer.objects.get(pk=id)
        
          fm=CustomerForm(instance=pi)  
    return render(request,'app/update.html',{'form':fm })



#order delete

def delorder(request,id):
    if request.method=='POST':
        pi=OrderPlaced.objects.get(pk=id)
        pi.delete()
        return redirect('orderadmin')      




# order update
def updateorder(request,id):

    if request.method=='POST':
        pi=OrderPlaced.objects.get(pk=id)
        
        
        fm=Orderfrom(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
           
            return redirect('orderadmin')      
        

    else:
          pi=OrderPlaced.objects.get(pk=id)
        
          fm=Orderfrom(instance=pi)  
    return render(request,'app/orderupdate.html',{'form':fm })













#add services
def addservices(request):
    user=request.user
    if request.method == 'POST':
        fm=Servicesform(request.POST, request.FILES)
        if fm.is_valid():
            title=fm.cleaned_data['title']
            Actual_price=fm.cleaned_data['Actual_price']
            discounted_price=fm.cleaned_data['discounted_price']
            as_per=fm.cleaned_data['as_per']
            description=fm.cleaned_data['description']
            Service_image1=fm.cleaned_data['Service_image1']
            Service_image2=fm.cleaned_data['Service_image2']
            Services(title=title,Actual_price=Actual_price,discounted_price=discounted_price,as_per=as_per,description=description,Service_image1=Service_image1,Service_image2=Service_image2).save()
            msg1=" is add new service "
           
            Subject="Add New Service"

            description="A new services is adding in to you system"
            

            send_mail(
       Subject,
    description,
    'usamamahar014@gmail.com',
    ['usamamuhammadmahar@gmail.com'],
    fail_silently=False,
)
            return redirect('viewserviescustomerdash')            

    else:
        fm=Servicesform()
    return render(request,'app/seviceadd.html',{'form':fm}) 


# order update
def updateservice(request,id):

    if request.method=='POST':
        pi=Services.objects.get(pk=id)
        
        fm=Servicesform(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('viewserviescustomerdash')      
        

    else:
          pi=Services.objects.get(pk=id)
        
          fm=Servicesform(instance=pi)  
    return render(request,'app/updateservice.html',{'form':fm })


def delservice(request,id):
      if request.method=='POST':
        pi=Services.objects.get(pk=id)
        pi.delete()
        return redirect('viewserviescustomerdash')      


#view coutomer on index

def indexviewcustomer(request):
    
    
    customer = Customer.objects.all()


    return render(request, 'app/home.html', {'customer':  customer})



    # count of dashbase count

def countcustomer(request):
    customer = Customer.objects.count()
    order=OrderPlaced.objects.count()
    orders=OrderPlaced.objects.filter(status='Pending').count()
    orderscom=OrderPlaced.objects.filter(status='Service is Complete').count()
    total_services=Services.objects.count()
    msg= contact_us.objects.filter( status='unread')
    msg_count= contact_us.objects.filter( status='unread').count()
    
    customer_img = Customer.objects.filter(user=request.user)



    labels = []
    data = []

    queryset = OrderPlaced.objects.order_by('-order_date')[:5]
    for rderPlaced in queryset:
        labels.append(rderPlaced.service.title)
        data.append(rderPlaced.quantity)
   

    return render(request, 'app/count.html', {'labels': labels,'data': data,'msg_count':msg_count,'customer':  customer,'customer_img':customer_img ,'msg':msg, 'order':order,'orders':orders ,'orderscom':orderscom ,'total_services':total_services})



#raedmsg




def raedmsg(request,id):

    if request.method=='POST':
        pi=contact_us.objects.get(pk=id)
        
        fm=contact_usform(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('count')      
        

    else:
          pi=contact_us.objects.get(pk=id)
        
          fm=contact_usform(instance=pi)  
    return render(request,'app/contant.html',{'form':fm })    





    #contact us
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.template.loader import render_to_string
from django.utils.html import strip_tags
def contant(request): 
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Subject = request.POST.get('Subject')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
     
        contact_us(name=name,email=email,Subject=Subject,description=description,phone=phone).save()
        messages.info(request, 'Your Messsage are sended to Admin')
        

       # subject, from_email, to = 'hello', 'usamamahar014@gmail.com', 'usamamuhammadmahar@gmail.com'
       # text_content = 'This is an important message.'
        #html_content = '<p>This is an <strong>important {{phone}}</strong> message.</p>'
        #msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        #msg.attach_alternative(html_content, "text/html")
        #msg.send()
        



        html_content = render_to_string("app/htmlmailcustomer.html",{'name':name})
        text_content= strip_tags(html_content)
        email=EmailMultiAlternatives(
            Subject,text_content,'usamamahar014@gmail.com',[email]


        )
        email.attach_alternative(html_content,"text/html")
        email.send()
       
        send_mail(
       Subject,
    description,
    'usamamahar014@gmail.com',
    ['usamamuhammadmahar@gmail.com'],
    fail_silently=False,
)
     

        #message1 = (Subject, description, 'usamamahar014@gmail.com', ['usamamuhammadmahar@gmail.com'])
       # message2 = ('thanks', 'Thanks to contanct us. we will reponce as early as possible', 'usamamahar014@gmail.com', [email])
       # send_mass_mail((message1, message2), fail_silently=False)






        return redirect('index')

    

    else:
        
       return render(request,'index') 
 

















  #send_mail(Subject,description, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
""" send_mail(
       Subject,
    description,
    'usamamahar014@gmail.com',
    ['usamamuhammadmahar@gmail.com'],
    fail_silently=False,
)"""

""""
        send_mail(
       Subject,
    description,
    'usamamahar014@gmail.com',
    ['usamamuhammadmahar@gmail.com',email],
    fail_silently=False,
)"""





    #pdf

















#######

#chart is dashboard
from django.shortcuts import render
from app.models import  Services,Customer,OrderPlaced,contact_us


def pie_chart(request):
    labels = []
    data = []

    queryset = OrderPlaced.objects.order_by('-order_date')[:5]
    for rderPlaced in queryset:
        labels.append(rderPlaced.service.title)
        data.append(rderPlaced.quantity)

    return render(request,'app/count.html', {'data':data,'labels':labels })










