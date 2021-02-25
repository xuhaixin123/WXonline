from django import forms
from captcha.fields import CaptchaField
from .models import UserProfile


class LoginForm(forms.Form):
    '''登录验证表单'''

    username = forms.CharField(
        required=True,
        label="用户名",

    )
    password = forms.CharField(
        required=True,
        min_length=6,
        widget=forms.PasswordInput,
        label="密码",
        error_messages={
            'required':'不能为空',
            'min_length':'密码长度最小为六位',
        }
    )
    catagory = forms.ChoiceField(
        required=True,
        label='类别',
        widget=forms.RadioSelect,
        choices=(('1','学生'),('2','教师'),('0','系统管理人员')),
    )


class RegisterForm(forms.Form):
    '''注册验证表单'''
    username = forms.CharField(
        required=True,
        label="用户名",
    )
    catagory = forms.ChoiceField(
        required=True,
        label='类别',
        widget=forms.RadioSelect,
        choices=(('1', '学生'), ('2', '教师')),
    )
    email = forms.EmailField(required=True,label='邮箱')
    password = forms.CharField(required=True, min_length=5, label='密码')
    # 验证码
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ForgetPwdForm(forms.Form):
    '''忘记密码'''
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ModifyPwdForm(forms.Form):
    '''重置密码'''
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)


class UploadImageForm(forms.ModelForm):
    '''用户更改图像'''

    class Meta:
        model = UserProfile
        fields = ['image']


class UserInfoForm(forms.ModelForm):
    '''个人中心信息修改'''

    class Meta:
        model = UserProfile
        fields = ['nick_name', 'gender', 'birthday', 'adress', 'mobile']
