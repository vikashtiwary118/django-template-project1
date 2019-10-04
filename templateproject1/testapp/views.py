from django.shortcuts import render
# Create your views here.
import datetime
def template_view(request):
	dt=datetime.datetime.now()
	# my_dict={"date":dt}
	#return render(request,'testapp/results.html',context=my_dict)
	#return render(request,'testapp/results.html',{"date":dt})
	##now mjultiple value
	name="Vikash"
	roll_no=118
	marks=100
	my_dict={"date":dt,'name':name,'roll_no':roll_no,'marks':marks}
	return render(request,'testapp/results.html',my_dict)