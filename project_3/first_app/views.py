from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
  d = {'author' : 'Rahim', 'age' : 5, 'list':['python','is','best'],'birthday':datetime.datetime.now(),  'courses' : [

    {
      'id' : 1,
      'name' : 'Python',
      'fee' : 3000
    },
    {
      'id' : 2,
      'name' : 'Django',
      'fee' : 5000
    },
    {
      'id' : 3,
      'name' : 'java',
      'fee': 4000
    },
  ]}
  return render(request, 'home.html',d)