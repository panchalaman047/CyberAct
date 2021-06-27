from django import forms

class SignUpOrganization(forms.Form):
    name = forms.CharField(label="Name of Organization",max_length=200)
    Categories = (('HUMANITIES','HUMANITIES'),('EDUCATION','EDUCATION'),('ENVIRONMENT','ENVIORNMENT'),('HEALTH','HEALTH'),('CHARITY','CHARITY'),('RELIGION','RELIGION'),('SERVICES','SERVICES'),('OTHER','OTHER'))
    Category = forms.ChoiceField(choices=Categories,label='Category')
    description=forms.CharField(label="Description",widget=forms.Textarea())