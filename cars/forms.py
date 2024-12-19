from django import forms
from cars.models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 20000:
            self.add_error('price', 'O valor mínimo do carro não pode ser menor que R$ 20.000')
        return price