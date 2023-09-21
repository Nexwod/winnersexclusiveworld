from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES={
    ('CL',"Clothes"),
    ('BG',"Bags"),
    ('SH',"Shoe"),
    ('BW',"Baby Clothes"),
    ('OT',"Others"),
}

STATE_CHOICES={
    ('AB',"Abia"),
    ('AD',"Adamawa"),
    ('AK',"Akwa-ibom"),
    ('AN',"Anambra"),
    ('BC',"Bauchi"),
    ('BY',"Bayelsa"),
    ('BN',"Benue"),
    ('BR',"Borno"),
    ('CR',"Cross-River"),
    ('DT',"Delta"),
    ('EB',"Ebonyi"),
    ('ED',"Edo"),
    ('EK',"Ekiti"),
    ('EN',"Enugu"),
    ('GB',"Gombe"),
    ('IM',"Imo"),
    ('JG',"Jigawa"),
    ('KD',"Kaduna"),
    ('KN',"Kano"),
    ('KT',"Kastina"),
    ('KO',"Kano"),
    ('KB',"Kebbi"),
    ('KG',"Kogi"),
    ('KW',"Kwara"),
    ('LG',"Lagos"),
    ('NS',"Nassarawa"),
    ('NG',"Niger"),
    ('OG',"Ogun"),('ON',"Ondo"),('OS',"Osun"),('OY',"Oyo"),
    ('PT',"Plateau"),
    ('RV',"Rivers"),
    ('SK',"Sokoto"),
    ('TB',"Taraba"),
    ('YB',"Yobe"),
    ('ZM',"Zamfara"),
    
    
   
    
}

PRODUCER_CHOICES={
    ('GC',"Gucci"),
    ('LV',"Louis Vuitton"),
    ('VS',"Versace"),
    ('DG',"Dolce and Gabanna"),
    ('CK',"Calvin Klein"),
    ('AD',"Addidas"),
    ('FL', "Fila"),
    ('RX',"Rolex"),
    ('GV',"Givenchy"),
    ('HR',"Hermes"),
    ('LC',"Lacosta"),
    ('SP',"Supreme"),
}

STATUS_CHOICES={
    ('Accepted',"Accepted"),
    ('Packed',"Packed"),
    ('On the Way',"On the Way"),
    ('Delivered',"Delivered"),
    ('Canceled',"Canceled"),
    ('Pending',"Pending"),
    
}




class Product(models.Model):
    title = models.CharField(max_length = 100)
    selling_price = models.FloatField()
    added_to_cart = models.BooleanField(default=False)
    discounted_price = models.FloatField()
    producer = models.CharField(choices=PRODUCER_CHOICES, max_length = 2)
    description = models.TextField(default = '')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length = 2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title

class Incart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length=200)
    locality = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    email = models.EmailField(max_length=50)
    mobile = models.IntegerField(default=0)
    state = models.CharField(choices=STATE_CHOICES, max_length = 20)
    def __str__(self):
        return self.name



class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    payment_image = models.ImageField(upload_to='payment')
    amount = models.FloatField()
    paid = models.BooleanField(default=False)

class Payapp(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    contact = models.IntegerField(default=0)
    address = models.CharField(max_length=50 )
    state = models.CharField(max_length = 20)
    receipt = models.ImageField(upload_to='receipt' )
    amount = models.FloatField(default=0)
    payment_time = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)



class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default = 1, null=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices = STATUS_CHOICES, default='Pending', null=True)
    payment = models.ForeignKey(Payapp, on_delete=models.CASCADE, default='', null=True)
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price