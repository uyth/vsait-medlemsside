from datetime import datetime
from enum import Enum

from django import forms

#TODO: move out enum
class UserType(Enum):
	STUDENT = 1
	NON_STUDENT = 2

current_year = datetime.today().year
year_range = tuple([i for i in range(current_year, current_year - 70, -1)])
student_choices = [(UserType.STUDENT, 'Ja'), (UserType.NON_STUDENT, 'Nei')]
allergens = ['Melk', 'Nøtter','Egg', 'Hvete', 'Fisk', 'Skalldyr', 'Soya']
allergens_choices = [(allergens.index(item), item) for item in allergens]

class RegistrationForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput)

    name = forms.CharField(max_length=100)
    #TODO: change widget for date
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=year_range))

    user_type = forms.ChoiceField(choices=student_choices, widget=forms.RadioSelect)
    # TODO: if student, add start_year and expected_end_year
    start_year = forms.DateField(widget=forms.SelectDateWidget(years=year_range))
    expected_end_year = forms.DateField(widget=forms.SelectDateWidget(years=year_range))

    food_needs = forms.MultipleChoiceField(choices=allergens_choices, widget=forms.CheckboxSelectMultiple(), required=False)
    #TODO: fix [checkbox] andre: [inputField]
    food_needs_other = forms.CharField()

    has_vietnamese_background = forms.ChoiceField(choices=[(True, 'Ja'), (False, 'Nei')], widget=forms.RadioSelect())

