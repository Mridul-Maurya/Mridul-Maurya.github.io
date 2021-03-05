from django import forms
from .models import Snippet

class ContactForm(forms.Form):
	name = forms.CharField(max_length=100)
	Email = forms.EmailField()
	subject = forms.CharField( required=False)
	message = forms.CharField(widget=forms.Textarea)


class SnippetForm(forms.ModelForm):

	class Meta:
		model = Snippet
		fields = ('name','body')
		