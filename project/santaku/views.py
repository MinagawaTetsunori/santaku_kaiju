from django.shortcuts import render
from django.views import View

# ajax処理確認用
# -----
from django.http import HttpResponse
from django.views.generic import FormView

from .original import sample_form
from .models import CustomerBotFlow
# -----

class IndexView(View):
    def get(self, request):
        test_text: str = 'ITest Hello'
        return render(
            request, 'santaku/index.html',
            {'test_text': test_text})

index = IndexView.as_view()


class SampleFormView(FormView):
    template_name = 'santaku/sample_form.html'
    form_class = sample_form.SampleForm
    success_url = '/sampleform'

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        if form.is_valid():
            if  request.headers.get('x-requested-with') == 'XMLHttpRequest':
                print('### ajax req')
                print(CustomerBotFlow.objects.get(id=1).id)
                return self.ajax_response(form)
            # ajax以外
            return super().form_valid(form)
        # 正しくない
        return super().form_invalid(form)

    def ajax_response(self, form):
        name = form.cleaned_data.get('name')
        return HttpResponse(f'get name is {name}')