
from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'  # Уберем поле 'fio' из exclude, чтобы оно было включено в форму

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if self.instance and hasattr(self.instance, field_name):
                field.widget.attrs['value'] = getattr(self.instance, field_name)


class InnForm(forms.Form):
    inn = forms.CharField(label='ИНН', max_length=20)
