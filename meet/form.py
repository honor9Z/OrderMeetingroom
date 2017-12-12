from django.forms import Form
from django.forms import fields
from django.forms import widgets

class LoginForm(Form):
    name = fields.CharField(
        required=True,
        error_messages={'required': '用户名不能为空'},
        widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '用户名', 'id': 'name'})
    )
    password = fields.CharField(
        required=True,
        error_messages={'required': '密码不能为空'},
        widget=widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码', 'id': 'password'})
    )
    rmb = fields.BooleanField(required=False, widget=widgets.CheckboxInput(attrs={'value': 1}))


