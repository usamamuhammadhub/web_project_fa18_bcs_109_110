from django.urls import path
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# logout,
from os import name
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.utils import html
from django.utils.translation import templatize
from app.forms import CustomerForm 
#CustomerForm
from app.forms import CustomerRegistrationForm
from app.forms import Servicesform
from app.models import Customer
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .forms import LoginForm, MypasswordChangeform, MypasswordChangeform, Mypasswordrestform,Mysetpasswordform
from django.contrib.auth.views import LoginView, PasswordChangeView
#from app import views
from django.contrib.auth.views import LogoutView
# from .forms import  Loginform
#
from django.conf.urls import url
from . import views
from django.conf import settings
#from django.urls.exceptions 



urlpatterns = [

                  path('', views.index, name='index'),
             
               path('contant', views.contant, name='contant'),
                  path('inner', views.inner_page, name='inner_page'),
                  # path('pd', views.portfolio_details, name='portfolio_details'),

                  # path('home', views.home,name="home"),
                  # trending services
                  path('ServiceView/', views.ServiceView.as_view(), name="ServiceView"),

                  # service
                  path('services/', views.sevice, name="services"),

                  # about us
                  path('about/', views.about, name='about'),
                  path('abouts/', views.abouts, name='abouts'),

                  # login
                  path('accounts/login/',
                       auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm),
                       name='login'),
                  # registarioncustomer
                  path('registration/', views.CustomerRegistrationView.as_view(),name="customerregistration"),
# path('registration/', views.CustomerRegistrationView.as_view(), success_url=reverse_lazy('CustomerFormview') , name="customerregistration"),

                  # dashbord cu
                  # dashbord customerservics
                  path('viewserviescustomerdash/', views.viewserviescustomerdash, name='viewserviescustomerdash'),
                  path('viewserviescustomerdash/<slug:data>', views.viewserviescustomerdash,
                       name='viewserviescustomerdashf'),
                  # service detail
                  path('service-detail/<int:pk>', views.service_detail.as_view(), name='service-detail'),

                  # dashbord
                  path('dash/', views.dash, name='dash'),

                  # add to card
                  path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
                   # add to order
              


                  path('cart/', views.showcart, name='showcart'),
                      
                  path('pluscart/', views.plus_cart, name='plus_cart'),

                  path('minuscart/', views.minus_cart, name='minus_cart'),

                  path('removecart/', views.remove_cart, name='remove_cart'),
                 # url(r'^changepassword/', 'django.contrib.auth.views.password_change',
                          # {'post_change_redirect' : '/changepassword/'}),
#url(r'^changepassword/', 'django.contrib.auth.views.passwordchangedone'),

  # path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html'), redirect_field_name='passwordchangedone',
  #       name='changepassword'),

path('changepassword/',auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html',form_class=MypasswordChangeform,success_url='/passwordchangedone/'),name='changepassword'),
    

    #success url
path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),

#path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
#path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # reset password urls








path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',
                                                                               form_class=Mypasswordrestform),
                       name='password_reset'),

                  path('password-reset/done/',
                       auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),
                       name='password_reset_done'),
                  path('password-reset-confirm/<uidb64>/<token>/',
                       auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',
                                                                   form_class=Mysetpasswordform),
                       name='password_reset_confirm'),

                  path('password-reset-complete/',
                       auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_complete.html'),
                       name='password_reset_complete'),

                  url(r'^logout$', LogoutView.as_view(), name='logout'),

                  # path('product-detail/', views.product_detail, name='product-detail'),
                 
               path('checkout/', views.checkout, name='checkout'),
                path('pymentdone/', views.pymentdone, name='pymentdone'),
                path('orders/', views.orders, name='orders'),
                
            
                path('orderadmin/', views.orderadmin, name='orderadmin'),
                #updateservice
                  # path('registration/', views.customerregistration, name='customerregistration'),





                path('updateservice/<int:id>', views.updateservice, name="updateservice"),

                 path('delservice/<int:id>', views.delservice, name="delservice"),
                  
                  path('CustomerFormview/', views.CustomerFormview, name="CustomerFormview"),
                  path('viewcustomeredit/', views.viewcustomeredit, name="viewcustomeredit"),
                  #adminviewcutomer adminviewcutomer
                  path('adminviewcutomer/', views.adminviewcutomer, name="adminviewcutomer"),
                    path('delcustomeredit/<int:id>', views.delcustomeredit, name="delcustomeredit"),
                    
                    path('updatecustomeredit/<int:id>', views.updatecustomeredit, name="updatecustomeredit"),
                    #updatecustomerbyadmin
                    path('updatecustomerbyadmin/<int:id>', views.updatecustomerbyadmin, name="updatecustomerbyadmin"),
  
                    path('delorder/<int:id>', views.delorder, name="delorder"),
                    path('updateorder/<int:id>', views.updateorder, name="updateorder"),
                     #add services
                     
                     path('addservices/', views.addservices, name="addservices"),
                     path('viewserviescustomerdash/<slug:data>', views.viewserviescustomerdash,
                       name='viewserviescustomerdashf'),

                       #indexviewcustomer
                    
                 #view cutomer on index
                     path('indexviewcustomer/', views.indexviewcustomer, name="indexviewcustomer"),
                  # path('base1/', views.bas, name='bas'),
 path('count/', views.countcustomer, name="count"),
 
                   path('read/<int:id>', views.raedmsg, name="read"),
                   #path('contant/', views.countcustomer, name="count"
                   


                  
#pdf
####

  
path('pie_chart/', views.pie_chart, name='pie_chart'),


                  


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
