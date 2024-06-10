from django import forms

from .models import User

class UserForm(forms.ModelForm):
    # Modleform comes from django
    # Feilds are from  account,models.py
    #Creating custom fields Ch 34
    password = forms.CharField(widget=forms.PasswordInput()) # CH 34
    confirm_password=forms.CharField(widget=forms.PasswordInput()) # CH 34

    class Meta:
        model= User
        fields =['first_name','last_name','username','email','password']
    #CH 36
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )

        