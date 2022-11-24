from .models import Resume
from django.forms import ModelForm


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'last_name', 'description', 'email', 'phone1', 'phone2', 'address', 'profession', 'image']
