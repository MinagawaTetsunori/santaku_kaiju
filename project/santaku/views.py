from django.shortcuts import render
from django.views import View

class IndexView(View):
    def get(self, request):
        test_text: str = 'ITest Hello'
        return render(
            request, 'santaku/index.html',
            {'test_text': test_text})


index = IndexView.as_view()
