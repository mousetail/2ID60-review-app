from django.forms import widgets

class StarWidget(widgets.Widget):
    template_name = 'widget/starWidget.html'