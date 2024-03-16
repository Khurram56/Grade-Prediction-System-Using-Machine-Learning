from django import forms
from.models import Data

class DataForm(forms.ModelForm):
    G1_percentage = forms.ChoiceField(choices=[(0, '0-25%'), (1, '25-50%'), (2, '50-75%'), (3, '75-90%'), (4, '90-100%')], required=False)
    G2_percentage = forms.ChoiceField(choices=[(0, '0-25%'), (1, '25-50%'), (2, '50-75%'), (3, '75-90%'), (4, '90-100%')], required=False)
    class Meta:
        model=Data
        fields=['name','sex','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob',
        #'reason',
        'guardian','traveltime',
        'studytime','failures','schoolsup','famsup','paid','activities','nursery','higher','internet','romantic',
        'famrel','freetime','goout','Dalc','Walc','health','absences','G1','G2']
        labels = {
            'name': 'Full Name',
            'sex': 'Gender',
            'address': 'Address',
            'famsize': 'Family Size',
            'Pstatus': 'Parental Status',
            'Medu': 'Mother Education',
            'Fedu': 'Father Education',
            'Mjob': 'Mother Job',
            'Fjob': 'Father Job',
            'guardian': 'Guardian',
            'traveltime': 'Travel Time',
            'studytime': 'Weekly Study Time',
            'failures': 'Number of Failures',
            'schoolsup': 'School Support',
            'famsup': 'Family Support',
            'paid': 'Extra Paid Classes',
            'activities': 'Extracurricular Activities',
            'nursery': 'Attended Nursery School',
            'higher': 'Wants to Pursue Higher Education',
            'internet': 'Internet Access at Home',
            'romantic': 'Peer Pressure',
            'famrel': 'Family Relationship Quality',
            'freetime': 'Free Time After School',
            'goout': 'Going Out with Friends',
            'Dalc': 'Workday Drugs Consumption',
            'Walc': 'Weekend Drugs Consumption',
            'health': 'Health Status',
            'absences': 'Number of School Absences',
            'G1': 'Grade 1',
            'G2': 'Grade 2'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['G1_percentage'].initial = self.map_value_to_percentage(instance.G1)
            self.fields['G2_percentage'].initial = self.map_value_to_percentage(instance.G2)

    def clean(self):
        cleaned_data = super().clean()
        g1_percentage = cleaned_data.get('G1_percentage')
        g2_percentage = cleaned_data.get('G2_percentage')

        # Map percentage range to actual integer value and update the cleaned_data
        cleaned_data['G1'] = self.map_percentage_to_value(g1_percentage)
        cleaned_data['G2'] = self.map_percentage_to_value(g2_percentage)

        return cleaned_data

    def map_percentage_to_value(self, percentage):
        percentage_mapping = {
            '0': 0,
            '1': 5,
            '2': 10,
            '3': 15,
            '4': 20,
        }
        return percentage_mapping.get(percentage, 0)

    def map_value_to_percentage(self, value):
        if value <= 5:
            return '0'
        elif value <= 10:
            return '1'
        elif value <= 15:
            return '2'
        elif value <= 18:
            return '3'
        else:
            return '4'