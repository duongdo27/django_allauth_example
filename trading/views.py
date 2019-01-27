from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class PortfolioView(TemplateView):
    template_name = "portfolio.html"
