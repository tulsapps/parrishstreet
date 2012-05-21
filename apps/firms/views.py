from django.shortcuts import get_object_or_404, render_to_response
from apps.firms.models import Firm, Sector


def firm_index(request):
    return render_to_response('firms/firm_index.html',
                              {'firm_list': Sector.objects.all()})
    
def firm_detail(request):
    firm = get_object_or_404(Firm)
    return render_to_response('firm/firm_detail.html', 
                              { 'firm_detail': 'firm_detail' })
    
def sectors_index(request):
    return render_to_response('firms/sector_list.html',
                              { 'sector_list': Sector.objects.all() })

#def sector_detail(reguest, slug):
    #sector = get_object_or_404(Sector, slug=slug)
    #return render_to_response('firm/sector_detail.html',
                              #{ 'object_list': Sector.firm_set.all(),
                              #'sector': sector })