from django.shortcuts import render

from django.shortcuts import get_object_or_404
from .models import Nomination

# Create your views here.
def show_form(request,pk):
    questionnaire = get_object_or_404(Nomination, id=pk)
    form = questionnaire.get_form(request.POST or None)
    if form.is_valid():
        questionnaire.add_answer(request.user, form.cleaned_data)

    return render(request, 'd_form.html', context={'form': form})

def build_form(request):