from django import forms 
from .models import *

class create_document(forms.ModelForm):
	class Meta():
		model = Document
		fields = (
			'first_name',
			'last_name',
			'pass_id',
			'phone_number',
		)

