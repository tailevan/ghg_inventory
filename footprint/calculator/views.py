from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView

from .models import OfficeOperationForm as OfficeOperationFormModel
from .forms import OfficeOperationForm as OfficeOperationFormForm

from .utils import EmissionCalculator 
from calculator.dash_app import create_dash_app
# Create your views here.

def office_operation_form_view(request):
    if request.method == "POST":
        form = OfficeOperationFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("view_data"))  # Updated line
        else:
            context = {"form": form, "errors": form.errors}
            return render(request, "calculator/index.html", context)
    else:
        form = OfficeOperationFormForm()
        context = {"form": form}
        return render(request, "calculator/index.html", context)

def dashboard(request):
    df = EmissionCalculator.calculate_emission()
    create_dash_app(df)
    return render(request, "calculator/dashboard.html")

# def view_data(request):
#     result_df = EmissionCalculator().calculate_emission()  # Updated line
#     result_html = result_df.to_html(index=False, classes='table table-striped')  # Convert DataFrame to HTML
#     context = {"result_html": result_html}
#     # print(context["result_html"])
#     return render(request, "calculator/view_data.html", context)

def view_data(request):
    office_operation_forms = OfficeOperationFormModel.objects.all()
    context = {"office_operation_forms": office_operation_forms}
    return render(request, "calculator/view_data.html", context)



class OfficeOperationFormUpdateView(UpdateView):
    model = OfficeOperationFormModel
    fields = ["year", "electricity", "water", "paper", "garbage", "commute"]
    template_name = 'calculator/officeoperationform_update.html'
    success_url = reverse_lazy('view_data')

class OfficeOperationFormDeleteView(DeleteView):
    model = OfficeOperationFormModel
    template_name = 'calculator/officeoperationform_confirm_delete.html'
    success_url = reverse_lazy('view_data')