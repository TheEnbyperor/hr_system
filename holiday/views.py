from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from . import models


@permission_required("holiday.view_holiday")
def index(request):
    holiday = models.Holiday.objects.all()
    return render(request, "holiday/index.html", {
        "holiday": holiday
    })
