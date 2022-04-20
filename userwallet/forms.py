from django import forms

class UploadFileForm(forms.Form):

    ID_TYPE = (
        ("1", "Driving Licence"),
        ("2", "National Id card"),
        ("3", "{Passport}"),

    )

    id_type = forms.ChoiceField(choices=ID_TYPE)
    id_image = forms.FileField()
    selfie = forms.FileField()
