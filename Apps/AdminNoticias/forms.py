from django import forms

from Apps.AdminNoticias.models import ArticuloModelo

FAMILIAS_CHOICES = (
    ('', ''),
    ('N', 'Noticia'),
    ('E', 'Evento'),
)

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = ArticuloModelo

        fields = ['titulo', 'fecha', 'resumen', 'detalle', 'familia']

        label= {
            'titulo':'Título:',
            'fecha':'Fecha: ',
            'resumen':'Resumen: ',
            'detalle':'Detalle: ',
            'familia': 'Tipo',
         } 

        widgets= {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control'}),
            'resumen': forms.TextInput(attrs={'class':'form-control'}),
            'detalle': forms.Textarea(attrs={'class':'form-control'}),
            'fono': forms.NumberInput(attrs={'class':'form-control'}),
            'familia': forms.Select(choices=FAMILIAS_CHOICES, attrs={'class':'form-control'})
        }
