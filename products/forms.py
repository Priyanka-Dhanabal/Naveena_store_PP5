from django import forms
from .models import Product, Category, Review
from .widgets import CustomClearableFileInput
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'



class ReviewForm(forms.ModelForm):
    """
    Form for adding and editing reviews.
    """

    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]  # Choices from 1 to 5

    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(attrs={"class": "form-check-input"}),
        label="Rating",
    )

    class Meta:
        model = Review
        fields = ["rating", "comment"]
        widgets = {
            "comment": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Write your review here...",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        """Initialize form with optional user and product for validation."""
        self.user = kwargs.pop("user", None)
        self.product = kwargs.pop("product", None)
        super().__init__(*args, **kwargs)

    def clean(self):
        """
        Custom validation to prevent duplicate reviews by the same user
        for the same product.
        """

        cleaned_data = super().clean()

        if not self.instance.pk:  # Ensure this is a new review, not an edit
            if self.user and self.product:
                # Check if a review already exists
                if Review.objects.filter(
                    user=self.user, product=self.product
                ).exists():
                    raise ValidationError(
                        "You have already submitted a review for this product."
                    )

        return cleaned_data