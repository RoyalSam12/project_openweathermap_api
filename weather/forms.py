from django import forms


class CityForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        self.fields['city'].label = 'Введите название города'
        self.fields['city'].widget.attrs.update({'class': 'form-control-lg d-flex justify-content-center'})

    city = forms.CharField(max_length=100)
