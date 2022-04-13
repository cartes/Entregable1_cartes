from django import forms

class FormularioSeller(forms.Form):

    user_id = forms.IntegerField(widget=forms.HiddenInput(), required=False, initial=1)
    titulo = forms.CharField()
    descripcion = forms.Field()
    precio = forms.IntegerField()
    fecha_publicacion = forms.DateField()