from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect, render
from Routes.models import Projects,Risks
import json
import io
import os
import urllib, base64
import numpy as np
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
from django.templatetags.static import static
from PIL import Image

def index(request):
    return render(request, 'disclaimer.html',{
        'nav':'disclaimer',
    })

def platform(request):
    return render(request, 'platform.html',{
        'nav':'platform',
    })

def show_projects(request):
    projects = Projects.objects.all()
    risks = Risks.objects.all()
    score = []
    project_names = []
    probability = []
    impact = []
    project_name = ''
    projects_all = []
    for project in projects:
        project_name = Projects.objects.get(project_number=project.project_number)
        projects_all.append(project.project_number)
        for risk in project_name.risks_set.all():
            project_names.append(project.project_name)
            probability.append(int(risk.probability))
            impact.append(int(risk.impact))

    for i in range(len(project_names)):
        score.append(impact[i] * probability[i])
    
    buf2 = io.BytesIO()
    img = Image.open('/home/jaskiratsingh/RiskTool/bg_.png')
    fig, ax = plt.subplots() 
    x = range(5)
    y = range(5)
    
    plt.xlabel('Impact')
    plt.ylabel('Probability')

    text = []

    for n in range(len(projects_all)):
        text.append('R' + str(projects_all[n]))

    for i, txt in enumerate(text):
        ax.annotate(txt, (impact[i], probability[i]))
    
    #Plot some data
    plt.scatter(impact, probability,c='blue')
    ax.imshow(img,extent=[0, 5, 0, 5])
    plt.show()

    plt.savefig(buf2,format = 'png')
    buf2.seek(0)
    string2 = base64.b64encode(buf2.read())
    uri2 = urllib.parse.quote(string2)


    return render(request,'show_projects.html',{
        'nav':'show_projects',
        'projects':projects,
        'risks':risks,
        'score':score,
        'project_names':project_names,
        'probability':probability,
        'impact':impact,
        'chart':uri2 
    })

def get_risk(request,project_name):
    risks = Risks.objects.filter(project_no__project_name=project_name)
    score = int(risks[0].probability) * int(risks[0].impact)
    return render(request,'get_risk.html',{
        'nav':'get_risk',
        'project_name':project_name,
        'risks':risks,
        'score':score,
    })

def existing_project(request):
    projects = Projects.objects.all()
    if request.method == 'POST':
        projects_ = Projects.objects.get(project_number=request.POST['project'])
        category = request.POST['category']
        desc = request.POST['desc']
        probability = request.POST['probability']
        impact = request.POST['impact']
        control_measures = request.POST['control_measures']
        cl_costs = request.POST['cl_costs']
        pl_activities = request.POST['pl_activities']
        cont_acts = request.POST['cont_acts']
        owner  = request.POST['owner']
        status = request.POST['status']
        nearest_month = request.POST['nearest_month']
        cont_bud = request.POST['cont_bud']

        risks = Risks(projects=projects_,
        category=category,
        desc=desc,
        probability=probability,
        impact=impact,
        control_measures=control_measures,
        costs_in_budget=cont_bud,
        cl_costs=cl_costs,
        planned_costs=pl_activities,
        cont_costs=cont_acts,
        owner=owner,
        status=status,
        nearest_month=nearest_month)

        risks.save()

        return redirect('/show_projects')

    return render(request,'existing_project.html',{
        'nav':'create_project',
        'projects':projects,
    })

def create_project(request):
    if request.method == 'POST':
        project_name = request.POST['projectName']
        project_number = request.POST['projectNumber']
        client = request.POST['client']
        project_manager = request.POST['project_manager']
        last_review = request.POST['review_date']
        scope_of_work = request.POST['scope']

        projects = Projects(project_name=project_name,
        project_number=project_number,
        client=client,
        project_manager=project_manager,
        last_review=last_review,
        scope_of_work=scope_of_work)

        projects.save()

        category = request.POST['category']
        desc = request.POST['desc']
        probability = request.POST['probability']
        impact = request.POST['impact']
        control_measures = request.POST['control_measures']
        cl_costs = request.POST['cl_costs']
        pl_activities = request.POST['pl_activities']
        cont_acts = request.POST['cont_acts']
        owner  = request.POST['owner']
        status = request.POST['status']
        nearest_month = request.POST['nearest_month']
        cont_bud = request.POST['cont_bud']

        risks = Risks(projects=projects,
        category=category,
        desc=desc,
        probability=probability,
        impact=impact,
        control_measures=control_measures,
        costs_in_budget=cont_bud,
        cl_costs=cl_costs,
        planned_costs=pl_activities,
        cont_costs=cont_acts,
        owner=owner,
        status=status,
        nearest_month=nearest_month)

        risks.save()

        return redirect('/show_projects')

    return render(request,'index.html',{
        'nav':'create_project',
    })

def check_project_number(request,project_number):
    response = 'done!'
    if(Projects.objects.filter(project_number=project_number).exists()):
        response = 'Project number already exists!'

    return HttpResponse(response)

def sort_by(request,sortBy):
    risks_arr = []
    projects_arr = []
    risks = Risks.objects.all().order_by(sortBy)
    for r in risks:
        projects_arr.append({
            'project_name':r.projects.project_name,
            'project_number':r.projects.project_number,
            'client':r.projects.client,
            'project_manager':r.projects.project_manager,
            'last_review':r.projects.last_review,
            'scope_of_work':r.projects.scope_of_work,
            'category':r.get_category_display(),
            'desc':r.desc,
            'probability':r.probability,
            'impact':r.impact,
            'control_measures':r.control_measures,
            'costs_in_budget':r.costs_in_budget,
            'cl_costs':r.cl_costs,
            'planned_costs':r.planned_costs,
            'cont_costs':r.cont_costs,
            'owner':r.owner,
            'status':r.get_status_display(),
            'nearest_month':r.nearest_month,
            'score':int(r.probability) * int(r.impact),
        })

    return JsonResponse(projects_arr, safe=False)
