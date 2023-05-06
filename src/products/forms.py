from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    title       = forms.CharField( label= "name", widget=forms.TextInput(attrs={ "placeholder":"your title"}) )
    description = forms.CharField( required=True, widget=forms.Textarea(
        attrs={
            'placeholder' : "your description",
            'class': 'new-class-name two',
            'id'   : 'myid',
            'rows' : 20,
            'cols' : 100
        }
    ) )
    price       = forms.DecimalField( initial= 100.0 )  