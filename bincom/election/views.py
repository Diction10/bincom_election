from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    form = PUForm()
   
    if request.method == 'POST':
        PU_ID = PUForm(request.POST)
        PU_ID = PU_ID.data['pollingunit_uniqueid']
        pu_result = PUResult.objects.filter(pollingunit_uniqueid=PU_ID)
      

        return render (request, 'election/index.html', {
            'results' : pu_result,
            'PU_ID' : PU_ID,
            'form' : form
        })
    else:
        return render (request, 'election/index.html', {
        'form' : form,
    })



def total(request):
    form = LGForm()
    if request.method == 'POST':
        res = LGForm(request.POST)
        lg_name = int(res.data['lga_name'])
        
        #   get all the words in that lg
        pu_name = PollingUnitName.objects.filter(lga_id=lg_name)
        print(len(pu_name))
        ls = set()
        if not pu_name:
            return HttpResponse('<h1> LG does not have a result, Click Back </h1>')
        for i in pu_name:
            ls.add(i.polling_unit_id)
        for number in ls:
            lg_result = PUResult.objects.filter(pollingunit_uniqueid=number)
            print(lg_result)
        
        return render(request, 'election/total.html', {
            'form' : form,
            'pu_name' : pu_name,
            'lg_result' : lg_result,
            'pu_name' : pu_name
        })

    else:
        return render(request, 'election/total.html', {
            'form' : form,
        })
      

def new_result(request):
    form = NewResultForm()

    if request.method == 'POST':
        # GEt what the user has filled in the form
        result = NewResultForm(request.POST)

        # Check if form is valid
        if form.is_valid():
            # save to database
            obj = result.save(commit=False)
            # obj.item_image
            obj.user = request.user
            obj.save()

            # after submission redirect to the home page
            return HttpResponseRedirect(reverse("home"))
        
    return render(request, 'election/new_result.html', {
        'form' : form
    })





   
