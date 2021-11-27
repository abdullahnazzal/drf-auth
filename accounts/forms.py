from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class PersonCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ('username', 'email', 'phone_number', 'address', 'city')  