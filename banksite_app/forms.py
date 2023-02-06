from django import forms

from .models import Person, Branch


class PersonCreationForm(forms.ModelForm):
    CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    MATERIALS = [
        ('Debit Card', 'Debit Card'),
        ('Credit Card', 'Credit Card'),
        ('Cheque Book', 'Cheque Book'),
        ('Passbook', 'Passbook'),
    ]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    materials = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=MATERIALS)
    dob = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'dd/mm/yyyy'}))
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')
