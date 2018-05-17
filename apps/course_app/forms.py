from django.forms import ModelForm, Textarea
from .models import Course, Comment

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = [ 'name', 'description']
        widgets = {
            'description' : Textarea(attrs = { 'rows': 5 })
        }

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'       
            
            
            
class CommentForm(ModelForm):
     class Meta:
         model = Comment
         fields = [ 'comment']
         widgets = {
             'comment' : Textarea(attrs = { 'rows': 5 })
         }
 
     def __init__(self, *args, **kwargs):
         super(CommentForm, self).__init__(*args, **kwargs)
         for visible in self.visible_fields():
             visible.field.widget.attrs['class'] = 'form-control'
             
