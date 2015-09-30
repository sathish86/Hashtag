from django.db import models

# Create your models here.

class Notes(models.Model):
    description = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):   
        return self.description

class HashTags(models.Model):
    tags = models.CharField(max_length=100)
    notes = models.ManyToManyField(Notes)
    created_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):    
        return self.tags
