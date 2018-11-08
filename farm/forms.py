from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    location = forms.ChoiceField()
    message = forms.CharField(
        max_length=750,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    