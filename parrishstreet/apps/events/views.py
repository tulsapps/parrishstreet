from django.shortcuts import get_object_or_404, render_to_response
from apps.services.models import Service

def service_index(request):
    return render_to_response('services/service_index.html',
                              {'service_list': Service.objects.all()}
)
    
