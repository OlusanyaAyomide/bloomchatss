from django import forms
from .models import Topic,Room,Message,Reply,Topic
from django.forms import ModelForm
choisess=[]
for i in Topic.objects.all():
    chois=[(i.name),(i.name)]
    choisess.append(chois)

class loginForm(forms.Form):
    username=forms.CharField(max_length=200)
    password=forms.CharField(widget=forms.PasswordInput())

class CreateRoomForm(forms.Form):
    Topic=forms.ModelChoiceField(required=True,widget=forms.Select,queryset=Topic.objects.all())
    Room_Name=forms.CharField(max_length=100)
    Add_Description=forms.CharField(widget=forms.Textarea,label="Add Room Description")
  
class CreateRoomModelForm(forms.Form):
    class Meta:
        model=Room
        fields=['name','topic','title']
        label={
            'room':'Room Name',
            'title':'Add description'
        }

class UpdateForm(ModelForm):
    class Meta:
        model=Room
        fields=["name","title"]
        label={
            "name":"Room name",
            "title":"Group Description",
        }
class MessageUpdateForm(ModelForm):
    class Meta:
        model=Message
        fields=["body"]
        label={
            "body":"Message Body"
        }
class NewUserForm(forms.Form):
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    username=forms.CharField(max_length=30)
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput())
    password2=forms.CharField(label="confirm Password",widget=forms.PasswordInput())
class UpdateReplyForm(ModelForm):
    class Meta:
        model=Reply
        fields=["body"]

class CreateTopicForm(ModelForm):
    class Meta:
        model=Topic
        fields=["name"]
        labels={
            "name":"Topic name"
        }