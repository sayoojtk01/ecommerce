from django.db import models

# Create your models here.


class u_reg(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=200)
	password=models.CharField(max_length=100)
	phone=models.CharField(max_length=100)
	



class ad_product(models.Model):
	name=models.CharField(max_length=100)
	price=models.CharField(max_length=100)
	desc=models.CharField(max_length=100)
	qty=models.IntegerField(max_length=10)
	image=models.ImageField(upload_to='product/')
	category=models.CharField(max_length=100)


class ad_cart(models.Model):
	num=models.ForeignKey(u_reg, on_delete=models.CASCADE)
	pid=models.ForeignKey(ad_product, on_delete=models.CASCADE)
	total=models.CharField(max_length=100)
	status=models.CharField(max_length=100)
	quantity=models.IntegerField(max_length=255,default=1)


	def __str__(self):
		return f'{self.pid.qty} - {self.quantity}'