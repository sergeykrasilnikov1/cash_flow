from django import forms

class FlatPickrDateInput(forms.DateInput):
    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs.update({
            'type': 'date',
            'class': 'form-control',
            'data-input': ''
        })
        super().__init__(attrs=attrs) 