from django import forms

class SubmitForm(forms.Form):
	email = forms.EmailField(label="Your email", max_length=30)
	content = forms.CharField(label="Your message", max_length=200)

	
