from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from track.models import WeightData
from django.db.models import Max, Min, Avg

def start(request):
    latest_measure_list = WeightData.objects.order_by('-check_date')[:1]
    history = WeightData.objects.order_by('-check_date')[:10]
    absolute_max = WeightData.objects.all().aggregate(Max('weight_value'))
    absolute_min = WeightData.objects.all().aggregate(Min('weight_value'))
    average = WeightData.objects.all().aggregate(Avg('weight_value'))
    
    if latest_measure_list: context = { 'latest_measure': latest_measure_list[0], 
          'history' : history,
          'absolute_max' : absolute_max,
          'absolute_min' : absolute_min,
          'average' : average          
        }
    else: context = {}
    return render(request, 'track/start.html', context)

def save(request):

    date = datetime.strptime(request.POST['date'], '%d.%m.%Y')
    value = request.POST['value']
    
    data, created = WeightData.objects.get_or_create(check_date=date, defaults={'check_date': date,'weight_value': value})
    
    data.weight_value = value
    data.save()
    return HttpResponseRedirect(reverse('track:start'))

    
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))    
    
    