from django import forms
from . import models

class CreateArticle(forms.ModelForm):
	class Meta:
		model = models.Article
		fields = ['title', 'body', 'slug', 'thumb',]

	def __init__(self,*args,**kwargs):
		super(CreateArticle,self).__init__(*args,**kwargs)
		self.fields['title'].widget.attrs['class']='form-control'
		self.fields['body'].widget.attrs['class']='form-control'
		self.fields['slug'].widget.attrs['class']='form-control'	  
		self.fields['thumb'].widget.attrs['class']='form-control'
		