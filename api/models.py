from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError 
import uuid



class Receipt(models.Model):
    id = models.CharField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
        max_length=255
    )    
    retailer = models.CharField(max_length=255)
    purchaseDate = models.CharField(max_length=255)  
    purchaseTime = models.CharField(max_length=255)
    items = models.JSONField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    totalPoints = models.IntegerField(null=True, blank=True, default=None) 

    

    def clean(self):
        super().clean()

        # Validate purchaseDate
        try:
            datetime.strptime(self.purchaseDate, "%Y-%m-%d")
        except ValueError:
            raise ValidationError({"purchaseDate": "Date must be in the format YYYY-MM-DD."})

        # Validate purchaseTime
        try:
            datetime.strptime(self.purchaseTime, "%H:%M")
        except ValueError:
            raise ValidationError({"purchaseTime": "Time must be in the format HH:MM."})

