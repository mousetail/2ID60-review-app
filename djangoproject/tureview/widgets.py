from django.forms import widgets

class CounterWidget(widgets.Widget):
    template_name = 'widget/counterWidget.html'

class StarWidget(widgets.Widget):
    template_name = 'widget/starWidget.html'
