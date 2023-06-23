from django import forms
from .models import Blog, Tags


class Blog_Form(forms.ModelForm):
    cover_photo = forms.FileField(widget=forms.FileInput(attrs={'class': 'border-btn input-btn'}))
    tags = forms.ModelMultipleChoiceField(
        queryset=Tags.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Blog
        fields = [ 'cover_photo', 'title','blog', 'tags']
        

    def __init__(self, *args, **kwargs):
        super(Blog_Form, self).__init__(*args, **kwargs)
        for field in self.fields:
            if not field == 'cover_photo':
                self.fields[field].widget.attrs['class'] = 'form-control'
