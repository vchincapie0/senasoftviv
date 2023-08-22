from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

GEEKS_CHOICES =(
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
)

class Cliente(User):
    class Meta:
        proxy = True

    def get_products(self):
        return[] #todos los productos que el cliente obtenga, devolverlos en la lista 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)#La relacion quiere decir que si el usuario de elimina, tambien se elimina el profile
    type_user = models.SmallIntegerField(choices=GEEKS_CHOICES,default=0,null=True,blank=True) # aprovechando la relacion onetoone, un usuario es un tipo de cliente
