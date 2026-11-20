from django import forms


class LoginForm(forms.Form):
    login = forms.CharField(label="Логін", max_length=50)
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)


class NumbersForm(forms.Form):
    CHOICE_MIN = "min"
    CHOICE_MAX = "max"
    CHOICE_AVERAGE = "average"

    number1 = forms.FloatField(label="Перше число")
    number2 = forms.FloatField(label="Друге число")
    number3 = forms.FloatField(label="Третє число")
    operation = forms.ChoiceField(
        label="Що потрібно знайти",
        choices=[
            (CHOICE_MIN, "Мінімум"),
            (CHOICE_MAX, "Максимум"),
            (CHOICE_AVERAGE, "Середнє арифметичне"),
        ],
        widget=forms.RadioSelect,
    )


class RegistrationForm(forms.Form):
    GENDER_CHOICES = [
        ("Чоловіча", "Чоловіча"),
        ("Жіноча", "Жіноча"),
    ]

    first_name = forms.CharField(label="Ім’я", max_length=50)
    last_name = forms.CharField(label="Прізвище", max_length=50)
    age = forms.IntegerField(label="Вік", min_value=1, max_value=120)
    email = forms.EmailField(label="Email")
    gender = forms.ChoiceField(
        label="Стать",
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect,
    )
    address = forms.CharField(
        label="Адреса для доставки",
        widget=forms.Textarea(attrs={"rows": 3}),
        max_length=300,
    )
    subscribe = forms.BooleanField(
        label="Бажаєте підписатися на новини нашого інтернет-магазину?",
        required=False,
    )


class ProgrammerDayForm(forms.Form):
    year = forms.IntegerField(label="Рік", min_value=1, max_value=9999)
