from django.urls import path
from . import views
from django.contrib import admin
from django.conf import Settings, settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm

urlpatterns = [
    path('', views.home, name='home'),
    path('allproduct/', views.allproduct, name='allproduct'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:val>', views.CategoryView.as_view(), name = 'category'),
    path('category.title/<val>', views.CategoryTitle.as_view(), name = 'category.title'),
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    path('address/', views.address, name = 'address'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('customer/<str:pk>', views.customer, name = 'customer'),
    path('product.detail/<int:pk>', views.ProductDetail.as_view(), name = 'productdetail'),
    path('updateAddress/<int:pk>', views.UpdateAddress.as_view(), name = 'updateAddress'),

    path('add-to-cart/', views.add_to_cart, name = 'add-to-cart'),
    path('cart/', views.show_cart, name = 'showcart'),
    path('checkout/', views.checkout.as_view(), name = 'checkout'),
    path('paymentdone/', views.payment_done, name = 'paymentdone'),

    path('search/', views.search, name = 'search'),
    path('comingsoon/', views.comingsoon, name = 'comingsoon'),

    
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),

#login Authentication
    path('registration', views.CustomerRegistrationView.as_view(), name = 'customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name = 'app/login.html', 
    authentication_form=LoginForm), name = 'login'),
    
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyPasswordChangeForm,
    success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),

    path('payapp/', views.PayApp, name='payapp'),
    path('order/', views.order, name='order'),
    path('paymentsuccessful/', views.paymentsuccessful, name='paymentsuccessful'),

#lpassword Authentication
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Winners Exclusive World"
admin.site.site_title = "Winners Exclusive World"
admin.site.site_index_title = "Welcome to Winners Exclusive World"