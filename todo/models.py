from django.db import models

# Create your models here.


class Item(models.Model):
    """
    When Django sees that we've created a new item class it will automatically 
    create an items table when we make and run the database migrations.
    There's a key thing you need to understand here though. And that's that by 
    itself this class won't do anything We need to use something called class 
    inheritance to give it some functionality.
    """
    # this is why we put models.Model into the class it inherits the base 
    # model class.
    # CharField means will have charachters and text in it.
    name = models.CharField(max_length=50, null=False, blank=False)   
    done = models.BooleanField(null=False, blank=False, default=False)


    def __str__(self):
        return self.name
