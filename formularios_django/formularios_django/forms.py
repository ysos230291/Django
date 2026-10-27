from django import forms

class CommenntForm(forms.Form):
    name=forms.CharField(label="Escribe tu nombre", max_length=100, help_text="100 caracteres maximo")
    url=forms.URLField(label="Tu sitio web", required=False, initial="http://")
    comment=forms.CharField()

class ContactForm(forms.Form):
    name=forms.CharField(label="Nombre: ", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField(label="Email: ", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    message=forms.CharField(label="Mensaje: ", widget=forms.Textarea(attrs={"class":"form-control"}))

    def clean_name(self):         # esto es para las validaciones clean
        name = self.cleaned_data.get("name")                # ----> esto es para trabajar con el name despues de pasar la validacion anterior
        if name != "Open":
            raise forms.ValidationError("Tan solo el valor Open esta permitido para este campo")
        else:
            return name
