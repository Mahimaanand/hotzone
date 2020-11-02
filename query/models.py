from django.db import models

# Create your models here.
class Location (models.Model):
    '''Residence = 'R'
    Workplace = 'W'
    Visit = 'V'
    Category_Options = [(Residence, 'Residence'), (Workplace,'Workplace'),(Visit, 'Visit')]'''
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    x_coordinates = models.FloatField()
    y_coordinates = models.FloatField()
    # from_date = models.DateField()
    # till_date = models.DateField()
    # location_category  = models.CharField(
    #     max_length=1,
    #     choices=Category_Options,
    #     default=Residence
    # )