from datetime import date, timedelta

from django.shortcuts import render

from .forms import LoginForm, NumbersForm, ProgrammerDayForm, RegistrationForm


USERS = {
    "admin": ("admin123", "Адміністратор"),
    "user": ("user123", "Користувач"),
}


def index(request):
    return render(request, "main/index.html")


def login_view(request):
    message = ""
    form = LoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        login = form.cleaned_data["login"]
        password = form.cleaned_data["password"]

        if login in USERS and USERS[login][0] == password:
            message = f"Вітаємо, {login}! Рівень доступу: {USERS[login][1]}."
        else:
            message = "Неправильний логін або пароль."

    return render(
        request,
        "main/login.html",
        {"form": form, "message": message},
    )


def numbers_view(request):
    form = NumbersForm(request.POST or None)
    result = None

    if request.method == "POST" and form.is_valid():
        numbers = [
            form.cleaned_data["number1"],
            form.cleaned_data["number2"],
            form.cleaned_data["number3"],
        ]
        operation = form.cleaned_data["operation"]

        if operation == NumbersForm.CHOICE_MIN:
            result = min(numbers)
        elif operation == NumbersForm.CHOICE_MAX:
            result = max(numbers)
        else:
            result = sum(numbers) / len(numbers)

    return render(
        request,
        "main/numbers.html",
        {"form": form, "result": result},
    )


def registration_view(request):
    form = RegistrationForm(request.POST or None)
    registration = None

    if request.method == "POST" and form.is_valid():
        registration = form.cleaned_data

    return render(
        request,
        "main/registration.html",
        {"form": form, "registration": registration},
    )


def programmer_day_view(request):
    form = ProgrammerDayForm(request.POST or None)
    result = None

    if request.method == "POST" and form.is_valid():
        year = form.cleaned_data["year"]
        day_number = date(year, 1, 1) + timedelta(days=255)
        weekday_names = [
            "понеділок",
            "вівторок",
            "середа",
            "четвер",
            "п’ятниця",
            "субота",
            "неділя",
        ]

        months = [
            "січня",
            "лютого",
            "березня",
            "квітня",
            "травня",
            "червня",
            "липня",
            "серпня",
            "вересня",
            "жовтня",
            "листопада",
            "грудня",
        ]
        result = (
            f"{day_number.day} {months[day_number.month - 1]} "
            f"({weekday_names[day_number.weekday()]})"
        )

    return render(
        request,
        "main/programmer_day.html",
        {"form": form, "result": result},
    )
