from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cliente
from .models import Mascota

REGION_CHOICES=[
    ('XV de Arica y Parinacota ', 'XV de Arica y Parinacota '),
    ('I de Tarapacá ','I de Tarapacá '),
    ('II de Antofagasta','II de Antofagasta'),
    ('III de Atacama', 'III de Atacama'),
    ('IV de Coquimbo','IV de Coquimbo'),
    ('V de Valparaíso','V de Valparaíso'),
    ('VI del Libertador General Bernardo OHiggins', 'VI del Libertador General Bernardo OHiggins'),
    ('VII del Maule','VII del Maule'),
    ('VIII del Biobío','VIII del Biobío'),
     ('IX de la Araucanía', 'IX de la Araucanía'),
    ('XIV de los Ríos','XIV de los Ríos'),
    ('X de los Lagos','X de los Lagos'),
    ('XI Aysén del General Carlos Ibáñez del Campo','XI Aysén del General Carlos Ibáñez del Campo'),
    ('XII de Magallanes y Antártica Chilena','XII de Magallanes y Antártica Chilena'),
    ]


CIUDAD_CHOICES=[
    ('Providencia', 'Providencia'),
    ('Puente Alto','Puente Alto'),
    ('Santiago','Santiago'),
    ('Quinta Normal', 'Quinta Normal'),

    ('Arica','Arica'),
    ('Camarones','Camarones'),
    ('Putre', 'Putre'),

    ('Iquique','Iquique'),
    ('Alto Hospicio','Alto Hospicio'),
    ('Pozo Almonte', 'Pozo Almonte'),

    ('Antofagasta','Antofagasta'),
    ('Calama','Calama'),
    ('Tocopilla', 'Tocopilla'),

    ('Copiapó','Copiapó'),
    ('Chañaral','Chañaral'),
     ('Vallenar', 'Vallenar'),


    ('La Serena','La Serena'),
    ('Coquimbo','Coquimbo'),
     ('Los Vilos', 'Los Vilos'),


    ('Valparaíso','Valparaíso'),
    ('Viña del Mar','Viña del Mar'),
     ('San Antonio', 'San Antonio'),

    ('Rancagua','Rancagua'),
    ('Pichilemu','Pichilemu'),
    ('San Fernando', 'San Fernando'),

    ('Talca','Talca'),
    ('Cauquenes','Cauquenes'),
     ('Curicó', 'Curicó'),

    ('Concepción','Concepción'),
    ('Arauco','Arauco'),
     ('Los Angeles', 'Los Angeles'),


    ('Temuco','Temuco'),
    ('Angol','Angol'),
    ('Villarrica', 'Villarrica'),

    ('Valdivia','Valdivia'),
    ('Panguipulli','Panguipulli'),
    ('Lago Ranco', 'Lago Ranco'),

    ('Puerto Montt','Puerto Montt'),
    ('Castro','Castro'),
    ('Osorno', 'Osorno'),

    ('Coyhaique','Coyhaique'),
    ('Aysén','Aysén'),
    ('Cochrane', 'Cochrane'),

    ('Punta Arenas','Punta Arenas'),
    ('Porvenir','Porvenir'),
    ('Antártica', 'Antártica'),

    ]

TP_VIV_CHOICES=[
    ('Casa con patio grande', 'Casa con patio grande'),
    ('Casa con patio pequeño','Casa con patio pequeño'),
    ('Casa sin patio','Casa sin patio'),
    ('Departamento','Departamento'),
    ]    


class AgregarCliente(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    first_name=forms.CharField(widget=forms.TextInput(),label="Primer Nombre")
    last_name=forms.CharField(widget=forms.TextInput(),label="Apellido")
    correo=forms.EmailField(widget=forms.EmailInput(),label="Correo")
    telefono=forms.CharField(widget=forms.TextInput(),label="Telefono")
    fec_nac=forms.CharField(widget=forms.TextInput(),label="Fecha Nacimiento")
    region = forms.ChoiceField(label='Region',choices=REGION_CHOICES) 
    ciudad = forms.ChoiceField(label='Ciudad',choices=CIUDAD_CHOICES)
    tipo_vivienda = forms.ChoiceField(label='Tipo de vivienda',choices=TP_VIV_CHOICES)

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre de Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")


class AgregarMascota(forms.ModelForm):
    class Meta:
        model = Mascota

        fields = [
            'nombreMascota',
            'razaMascota',
            'descripcionMascota',
            'estadoMascota',
            'fotoMascota',
        ]
        labels = {
            'nombreMascota': 'Nombre de mascota',
            'razaMascota' : 'Raza de mascota',
            'descripcionMascota' : 'Descripción',
            'estadoMascota' : 'Estado de mascota',
            'fotoMascota' : 'Imagen de mascota',
        }
        widgets = {
            'nombreMascota' : forms.TextInput(attrs={'class':'form'}),
            'razaMascota' : forms.TextInput(attrs={'class':'form'}),
            'descripcionMascota': forms.TextInput(attrs={'class':'form'}),
            'estadoMascota' : forms.Select(attrs={'class':'form'}),
        }