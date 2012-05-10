from django.shortcuts import render_to_response
from firms.models import Firm

def firm_index(request):
    return render_to_response('firms/firms.html',
                              'firm_list: Firm.objects.all()')