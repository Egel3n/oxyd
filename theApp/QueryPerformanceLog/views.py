from django.shortcuts import render
from .models import QueryPerformanceLog
from django.views.decorators.csrf import csrf_exempt
from .queryManager import queryManager
import json 
# Create your views here.

@csrf_exempt
def index(request):
    headers = ["EventDate", "DatabaseID","Hostname","AppName","SessionID","Username","SqlText","Duration"]

    if request.method == "GET":
        records = QueryPerformanceLog.objects.all()


    elif request.method == "POST":
        content = request.POST
        querier = queryManager()
        querier.addHostnameFilter(content.get("hostname"))
        querier.addUsernameFilter(content.get("username"))
        querier.addQueryFilter(content.get("query"))
        querier.addAppnameFilter(content.get("appname"))
        querier.addDurationFilter(content.get("durationFrom"),content.get("durationTo"))
        querier.addDateFilter(content.get("dateFrom"),content.get("dateTo"))
        querier.addDatabaseIDFilter(content.get("databaseID"))
        querier.addSessionIDFilter(content.get("sessionID"))

        query = str(querier)
        print(query)
        records = QueryPerformanceLog.objects.raw(query)


    context = {"records": records,"headers":headers}
    return render(request,"index.html",context)
    
