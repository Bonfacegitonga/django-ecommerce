from django import forms
from .models import Order
from django.forms import TextInput, EmailInput


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["first_name", "last_name", "email", "address", "postal_code", "city"]

        widgets = {
            "first_name": TextInput(
                attrs={"class": "w-full px-2 py-2 text-gray-700 bg-gray-200 rounded"}
            ),
            "last_name": TextInput(
                attrs={"class": "w-full px-2 py-2 text-gray-700 bg-gray-200 rounded"}
            ),
            "email": EmailInput(
                attrs={"class": "w-full px-2 py-2 text-gray-700 bg-gray-200 rounded"}
            ),
            "address": TextInput(
                attrs={"class": "w-full px-2 py-2 text-gray-700 bg-gray-200 rounded"}
            ),
            "postal_code": TextInput(
                attrs={"class": "w-full px-2 py-2 text-gray-700 bg-gray-200 rounded"}
            ),
            "city": TextInput(
                attrs={
                    "class": "w-full px-2 py-2 text-gray-700 bg-gray-200 rounded",
                }
            ),
        }

    # def __init__(self, *args, **kwargs):
    #     super(OrderCreateForm, self).__init__(*args, **kwargs)

    #     # Add Tailwind CSS classes to form fields
    #     self.fields["first_name"].widget.attrs.update(
    #         {"class": "w-full px-2 py-2 text-gray-700 bg-gray-200 rounded"}
    #     )
    #     self.fields["last_name"].widget.attrs.update(
    #         {"class": "w-full px-2 py-2 text-gray-700 bg-gray-200 rounded"}
    #     )
    #     self.fields["email"].widget.attrs.update(
    #         {"class": "w-full px-2 py-2 text-gray-700 bg-gray-200 rounded"}
    #     )
    #     self.fields["address"].widget.attrs.update(
    #         {"class": "w-full px-2 py-2 text-gray-700 bg-gray-200 rounded"}
    #     )
    #     self.fields["postal_code"].widget.attrs.update(
    #         {"class": "w-full px-2 py-2 text-gray-700 bg-gray-200 rounded"}
    #     )
    #     self.fields["city"].widget.attrs.update(
    #         {"class": "w-full px-2 py-2 text-gray-700 bg-gray-200 rounded"}
    #     )
