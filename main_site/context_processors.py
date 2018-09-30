from django.apps import apps as django_apps
from django import urls


def menu(request):
    menu = []
    for app in django_apps.get_app_configs():
        if getattr(app, 'in_menu', False):
            menu.append({"url": urls.reverse(f'{app.name}:index'), "name": app.verbose_name})

    return {
        "menu": menu,
    }
