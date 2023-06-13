from django.forms import ModelForm
from .models import Member

class MembersForm(ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'phone', 'joined_date']