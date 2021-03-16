from django.shortcuts import render

from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'dormitory/index.html')


def vk_auth(request):
    return render(request, 'dormitory/vk_auth.html')
