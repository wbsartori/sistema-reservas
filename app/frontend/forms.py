from django.forms import ModelForm
from django import forms

from backend.models import Reserva

class DateInput(forms.DateInput):
    input_type = 'date'

class TextArea(forms.Textarea):
    text_area = 'textarea'

class ReservarEquipamentoForm(ModelForm):

    class Meta:
        model = Reserva
        fields = ('id_usuario','data_inicio','data_final','id_horario','id_equipamento','id_sala','id_veiculo','observacoes')
        date_input = DateInput()
        widgets = {
            'data_inicio' : DateInput(),
            'data_final': DateInput(),
            'observacoes': TextArea(attrs={'cols': 80, 'rows': 5})
        }
