from django.db import models


class Category(models.Model):
    id = models.IntegerField(max_length=11, primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Brand(models.Model):
    id = models.IntegerField(max_length=11, primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Image(models.Model):
    id = models.IntegerField(max_length=11, primary_key=True)
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.IntegerField(max_length=11, primary_key=True)
    category = models.ManyToManyField(Category)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=11  , decimal_places=2)
    description = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Size(models.Model):
    id = models.IntegerField(max_length=11, primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name




class Color(models.Model):
    id = models.IntegerField(max_length=11, primary_key=True)
    name = models.CharField(max_length=255)
    hexecode = models.CharField(max_length=255)
    def __str__(self):
        return self.name



class Customer(models.Model):
    id = models.IntegerField(max_length=11, primary_key=True)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=100)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    id = models.IntegerField(max_length=11, primary_key=True)
    date = models.DateTimeField
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Cart(models.Model):
    id = models.IntegerField(max_length=11, primary_key=True)
    created = models.DateField(max_length=255)



class Wishlist(models.Model):
    id = models.IntegerField(max_length=11, primary_key=True)
    created = models.DateField()


class Variant(models.Model):
    id = models.IntegerField(max_length=11, primary_key=True)
    stock = models.IntegerField(max_length=11)
    isDefault = models.BooleanField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LineItem(models.Model):
    id = models.IntegerField(max_length=11, primary_key=True)
    quantity = models.IntegerField(max_length=255)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)


class Imagedetail(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    id = models.IntegerField(max_length=11, primary_key=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
