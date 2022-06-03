from django.shortcuts import render
from django.conf import settings

from django.shortcuts import render
from .forms import UploadForm


def media_example(request):
    instance = None
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        instance = form.save()
    else:
        form = UploadForm()

    return render(request, "media-example.html", {"form": form, "instance": instance})
