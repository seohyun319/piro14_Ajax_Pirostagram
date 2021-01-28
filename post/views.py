from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Subject
import json
# Create your views here.



class AjaxView(View):
    template_name = 'post/layout.html'
    

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AjaxView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        subject_list = Subject.objects.all()
        ctx = {"subjects": subject_list}
        return render(request, self.template_name, ctx)

    def post(self, request):
        request = json.loads(request.body)
        subject_id = request['id']

        subject = Subject.objects.get(id=subject_id)
        if subject.like == False:
            subject.like = True
        else: subject.like = False
        subject.save()

        return JsonResponse({'id': subject_id})



Ajaxview = AjaxView.as_view()