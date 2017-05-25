from django import forms

class NominationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra')
        super(QuestionForm, self).__init__(*args, **kwargs)

        for i, values in enumerate(extra):
            label, klass, field_args = values
            k=label
            self.fields['%s' % k] = klass(label=label, **field_args)




class BuidForm(forms.Form):
    NominationName = forms.CharField()
    description = forms.CharField()
