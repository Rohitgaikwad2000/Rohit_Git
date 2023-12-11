from django import forms  
from .models import FileUpload

class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name", max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 100)



class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['name', 'uploaded_file']        


