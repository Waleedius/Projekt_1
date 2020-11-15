from django.db import models

class category(models.Model):
    category_id = models.IntegerField(max_length=11, primary_key= True)
    category_name = models.CharField(max_length=45)

class brand(models.Model):
    brand_id = models.IntegerField(max_length=11 , primary_key= True)
    brand_name = models.CharField(max_length=45)

class product(models.Model):
    bBrand = models.ForeignKey(brand, on_delete=models.CASCADE)
    product_id = models.IntegerField(max_length=11, primary_key= True)
    product_name = models.CharField(max_length=45)
    product_price = models.BooleanField(default=False)
    product_description = models.TextField()
    product_brand_id = models.IntegerField(max_length=11)
# eine category hat viele Product category

class product_category(models.Model):
    cCategory = models.ForeignKey(category, on_delete=models.CASCADE)
    pProduct = models.ForeignKey(product, on_delete=models.CASCADE)
    product_category_product_id = models.IntegerField(max_length=11)
    product_category_category_id = models.IntegerField(max_length=11)

class size(models.Model):
    size_id = models.IntegerField(max_length=11, primary_key= True)
    size_name = models.CharField(max_length=45)

class image(models.Model):
    image_id = models.IntegerField(max_length=11, primary_key= True)
    image_name = models.CharField(max_length=45)
    image_path = models.CharField(max_length=250)




class color(models.Model):
    color_id = models.IntegerField(max_length=11, primary_key= True)
    color_name = models.CharField(max_length=45)
    color_hexecode = models.CharField(max_length=45)

class variant(models.Model):
    pProduct = models.ForeignKey(product,on_delete=models.CASCADE)
    cColor = models.ForeignKey(color,on_delete=models.CASCADE)
    iImage = models.ForeignKey(image,on_delete=models.CASCADE)
    sSize= models.ForeignKey(size,on_delete=models.CASCADE)
    variant_id = models.IntegerField(max_length=11, primary_key= True)
    variant_stock = models.IntegerField(max_length=11)
    variant_product_id = models.IntegerField(max_length=11)
    variant_size_id = models.IntegerField(max_length=11)
    variant_color_id = models.IntegerField(max_length=11)
    variant_color_id = models.IntegerField(max_length=11)
    variant_default = models.IntegerField(max_length=4)


class customer(models.Model):
    customer_id = models.IntegerField(max_length=11, primary_key= True)
    customer_email = models.EmailField(max_length=45)
    customer_password = models.CharField(max_length=100)
    customer_firstname = models.CharField(max_length=45)
    customer_lastname = models.CharField(max_length=45)


class order(models.Model):
    cCustomer = models.ForeignKey(customer,on_delete=models.CASCADE)
    order_id = models.IntegerField(max_length=11, primary_key= True)
    order_date = models.DateTimeField
    order_customer_id = models.IntegerField(max_length=11)


class order_item(models.Model):
    oOrder= models.ForeignKey(order, on_delete=models.CASCADE)
    vVariant = models.ForeignKey(variant)
    order_item_variant_id = models.IntegerField(max_length=11)
    order_item_order_id = models.IntegerField(max_length=11)
    order_item_quantity = models.IntegerField(max_length=11)





class imagedetail(models.Model):
    iImage= models.ForeignKey(image, on_delete=models.CASCADE)
    imagedetail_id = models.IntegerField(max_length=11, primary_key= True)
    imagedetail_name = models.CharField(max_length=45)
    imagedetail_path = models.CharField(max_length=250)
    imagedetail_image_id = models.IntegerField(max_length=11)


class customer(models.Model):
    customer_id = models.IntegerField(max_length=11, primary_key= True)
    customer_email = models.EmailField(max_length=45)
    customer_password = models.CharField(max_length=100)
    customer_firstname = models.CharField(max_length=45)
    customer_lastname = models.CharField(max_length=45)
