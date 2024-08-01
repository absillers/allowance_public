from django import forms
from .models import Allowance_app, Allowance_input_app

category_choices = [
("Groceries","Groceries"),
("Coffee", "Coffee"),
("Dining out", "Dining out"),
("Clothing", "Clothing"),
("Make-up", "Make-up"),
("Home", "Home"),
("Toiletries", "Toiletries"),
("Coffee", "Coffee"),
("Travel", "Travel"),
("Gas", "Gas"),
("Alcohol", "Alcohol"),
("Public transportation", "Public transportation"),
("Books and magazines", "Books and magazines"),
("Entertainment", "Entertainment"),
("Hobbies", "Hobbies")]
    
class SpendingForm(forms.ModelForm):
      class Meta:
            model = Allowance_app
            fields = [
                'category',
                'description',
                'price',
                'date',
                'allowance_no_debt_spending',
                'credit'
            ]
      category = forms.CharField(label="Category:", 
                                   widget=forms.Select(
                                         choices=category_choices,
                                               attrs={"class":"form-control"}))
      price = forms.DecimalField(required=False, 
                                widget = forms.NumberInput(
                                      attrs={'placeholder':0.00,
                                            "id":"my-id-for-decimal",
                                            "rows":1,
                                            "cols": 10,
                                            "class":'form-control'}))
      description= forms.CharField(
              required=False,
              widget=forms.Textarea(
                    attrs={
                          'placeholder':'Notes (optional)',
                          "id":"my-id-for-textarea",
                          "rows":1,
                          "cols":20,
                          "class":'form-control'
                    }
              ))    
      date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date', 'class':'form-control'}))
      credit = forms.BooleanField(required=False)



class AllowanceForm(forms.ModelForm):
      class Meta: 
            model = Allowance_input_app
            fields = [
                'allowance_no_debt']
      allowance_no_debt = forms.IntegerField(required=True, 
                                widget = forms.NumberInput(
                                      attrs={'placeholder':25,
                                            "id":"my-id-for-decimal",
                                            "rows":1,
                                            "cols": 10,
                                            "class":'form-control'}))
