from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
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
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CEF" in title:
            raise forms.ValidationError("There is no CEF in title")
        if not "news" in title:
            raise forms.ValidationError("There is no news in title")
        return title

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