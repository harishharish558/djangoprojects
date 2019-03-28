from  django import forms

class createform(forms.Form):
    studentnumber=forms.IntegerField(
        label='enter your rollno',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'please enter your rollno'
            }
        )
    )
    firstname=forms.CharField(
        label='enter your first name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'please enter your first name'
            }
        )
    )
    lastname = forms.CharField(
        label='enter your last name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'please enter your last name'
            }
        )
    )
    mobile=forms.IntegerField(
        label='Enter your mobile number:',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'please enter your mobile number'
            }
        )
    )
    email=forms.EmailField(
        label='Enter your mailid:',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter your email'
            }
        )
    )

class updateform(forms.Form):
    studentnumber = forms.IntegerField(
        label='enter your rollno',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'please enter your rollno'
            }
        )
    )
    firstname = forms.CharField(
        label='enter your first name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'please enter your first name'
            }
        )
    )
    lastname = forms.CharField(
        label='enter your last name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'please enter your last name'
            }
        )
    )

class deleteform(forms.Form):
    studentnumber = forms.IntegerField(
        label='enter your rollno',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'please enter your rollno'
            }
        )
    )