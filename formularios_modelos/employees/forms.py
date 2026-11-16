from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):           # debe coincidir con el nombre del modelo
    class Meta:
        model = Employee
        fields = ["name", "last_name", "email"]              # los campos que quiero que pregunte 
        # fields = "__all__"                                 ----> esto solo cuando quiero preguntar todos los campos
        # extra_fields =  ["salary"]                         ----> agregara este campo al formulario aunque no este en el modelo
        # exclude = ("email",)                               ----> esto hace una exclusion de ese campo