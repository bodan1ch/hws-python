from django.shortcuts import render


def index(request):
    cv = {
        "first_name": "[Ваше ім'я]",
        "last_name": "[Ваше прізвище]",
        "photo_url": "https://images.unsplash.com/photo-1534528741775-53994a69daeb"
        "?auto=format&fit=crop&w=500&q=80",
        "city": "[Ваше місто]",
        "email": "[ваша@email.com]",
        "phone": "[Ваш номер телефону]",
        "about": (
            "Напишіть кілька речень про себе, свої інтереси та досвід."
        ),
        "qualities": ["Відповідальність", "Уважність", "Готовність навчатися"],
        "goal": "Опишіть свою професійну мету.",
        "education": {
            "institution": "[Назва навчального закладу]",
            "specialty": "[Спеціальність]",
            "years": "[Роки навчання]",
        },
        "programming_languages": ["Python", "[Інші мови програмування]"],
        "software": ["Git", "Visual Studio Code", "[Інші програми]"],
        "languages": ["Українська — рідна", "[Іноземна мова та рівень]"],
        "projects": [
            {
                "name": "[Назва проєкту]",
                "description": (
                    "Опишіть завдання, використані технології та результат."
                ),
                "technologies": ["Python", "[Інші технології]"],
            }
        ],
    }
    return render(request, "main/index.html", {"cv": cv})
