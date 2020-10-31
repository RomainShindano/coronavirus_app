# from django.views.generic import ListView
from django.views.generic import TemplateView


# from .forms import ReportForm


class ReportTemplateView(TemplateView):
    template_name = "reports/map.html"

    # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)


#
#    context["form"] = ReportForm()
#
#    return context
