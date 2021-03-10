from django.forms import ModelForm
from django import forms

from reserva.models import Reserva

class DateInput(forms.DateInput):
    input_type = 'date'

class TextArea(forms.Textarea):
    text_area = 'textarea'

class ReservarVeiculoForm(ModelForm):

    class Meta:
        model = Reserva
        fields = ('id_usuario','data_inicio','data_final','id_horario','id_veiculo','observacoes','tipo_reserva')
        date_input = DateInput()
        widgets = {
            'data_inicio' : DateInput(),
            'data_final': DateInput(),
            'observacoes': TextArea(attrs={'cols': 80, 'rows': 5})
        }