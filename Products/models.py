from django.db import models

# Create your models here.
class FoodProducts(models.Model):

    ITEM_TYPE = [
        ('Tiffin', 'Tiffin'),
        ("Chuteys", 'Chutneys'),
        ('Meals', 'Meals'),
        ('Biriyanis', 'Biriyanis'),
        ('Curries', 'Curries'),
    ]

    MADE_OF_CATEGORY = [ 
        ('Normal', 'Normal'),
        ('Ghee', 'Ghee')
    ]

    MATERIAL_USED = [
        ('Normal', 'Normal'),
        ('Ragi', 'Ragi'),
        ('Jonna','Jonna')

    ]

    item_name        = models.CharField(max_length=70,null=True,blank=True)
    item_type        = models.CharField(max_length=30 ,choices=ITEM_TYPE, default=None)
    made_of_category = models.CharField(max_length=30, choices= MADE_OF_CATEGORY, default =None)
    material_used    = models.CharField(max_length=30, choices= MATERIAL_USED, default =None)
    item_added_date  = models.DateTimeField(auto_now_add=True)
    item_price       = models.PositiveIntegerField(null=True,blank=True)
    item_available   = models.BooleanField(default=True)
    item_count       = models.PositiveIntegerField(null = True, blank = True)
    item_id          = models.CharField(max_length=25,null=True,blank=True)

    def __str__(self):
        return self.item_name
