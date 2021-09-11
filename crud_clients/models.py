from django.db import models




class Country(models.Model):
    """Countries model.

    Extends from Django's AbstractUser."""

    class Meta:
        verbose_name_plural = "Countries"

    name = models.CharField(max_length=20, null=False)

    iso_code = models.CharField(max_length=5, unique=True, null=False)

    def __str__(self):

        return self.name

    def get_short_name(self):
 
        return self.iso_code




class City(models.Model):

    class Meta:
        verbose_name_plural = "Cities"

    name = models.CharField(max_length=20, null=False)

    iso_code = models.CharField(max_length=5, unique=True, null=False)

    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    def __str__(self):
        """Return name."""
        return self.name

    def get_short_name(self):
        """Return iso_code."""
        return self.iso_code

class Customer(models.Model):  
    name = models.CharField(max_length=100)  
    email = models.EmailField()  
    contact = models.CharField(max_length=15) 
    date_attention= models.DateField()
    time_attention  =models.TimeField()
    final_attention_time = models.TimeField()
    company = models.CharField(max_length=50) 
    city = models.CharField(max_length=50) 
    affair = models.CharField(max_length=50) 
    response  =models.CharField(max_length=150) 
    date_of_request = models.DateField() 
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    class Meta:  
        db_table = "Customer"


