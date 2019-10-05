from django import forms
from .models import Restaurant

class RestaurantForm (forms.ModelForm):
	class Meta:
		model = Restaurant
		# fields =['name','description','opening_time','closing_time']  #look into this later
		fields = "__all__"