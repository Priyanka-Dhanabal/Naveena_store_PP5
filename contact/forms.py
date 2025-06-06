from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """
    Form for users to submit contact messages.
    Excludes admin-only fields like 'replied' and 'resolved'.
    """

    class Meta:
        model = ContactMessage
        exclude = ["replied", "resolved"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 5}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("This field is required.")
        return email

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message:
            raise forms.ValidationError("Please enter a message.")
        return message
