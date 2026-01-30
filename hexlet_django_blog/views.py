from django.shortcuts import render


def index(request):
    return render(
        request,
        "index.html",
        context={
            "who": "World",
        },
    )

def about(request):
    tags = ['обучение', 'python', 'django']
    # Передаем словарь (context) третьим аргументом
    return render(request, 'about.html', {'tags': tags})