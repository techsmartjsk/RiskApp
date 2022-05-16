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
    score_bef_miti = []
    score_aft_miti = []
    project_names = []
    prob_bef_miti = []
    prob_aft_miti = []
    imp_bef_miti = []
    imp_aft_miti = []
    project_name = ''
    projects_all = []
    for project in projects:
        project_name = Projects.objects.get(project_number=project.project_number)
        projects_all.append(project.project_number)
        for risk in project_name.risks_set.all():
            project_names.append(project.project_name)
            prob_bef_miti.append(int(risk.prob_bef_miti))
            prob_aft_miti.append(int(risk.prob_aft_miti))
            imp_bef_miti.append(int(risk.imp_bef_miti))
            imp_aft_miti.append(int(risk.imp_aft_miti))

    for i in range(len(project_names)):
        score_bef_miti.append(imp_bef_miti[i] * prob_bef_miti[i])
        score_aft_miti.append(imp_aft_miti[i] * prob_aft_miti[i])
    

    #Chart 1
    buf2 = io.BytesIO()
    # img = Image.open('/home/jaskiratsingh/RiskTool/bg_.png')
    img = Image.open('/Users/jaskiratsingh/Desktop/ITPEnergisedApps/RiskTool/bg_.png')
    fig, ax = plt.subplots() 
    
    plt.xlabel('Impact Before Mitigation')
    plt.ylabel('Probability Before Mitigation')

    text = []

    for n in range(len(projects_all)):
        text.append('R' + str(projects_all[n]))

    for i, txt in enumerate(text):
        ax.annotate(txt, (imp_bef_miti[i], prob_bef_miti[i]))
    
    #Plot some data
    plt.scatter(imp_bef_miti, prob_bef_miti,c='blue')
    ax.imshow(img,extent=[0, 5, 0, 5])
    plt.show()

    plt.savefig(buf2,format = 'png')
    buf2.seek(0)
    string2 = base64.b64encode(buf2.read())
    uri2 = urllib.parse.quote(string2)

    #Chart 2
    buf3 = io.BytesIO()
    # img = Image.open('/home/jaskiratsingh/RiskTool/bg_.png')
    fig2, ax2 = plt.subplots() 
    
    plt.xlabel('Impact After Mitigation')
    plt.ylabel('Probability After Mitigation')

    text2 = []

    for n in range(len(projects_all)):
        text2.append('R' + str(projects_all[n]))

    for i, txt in enumerate(text):
        ax2.annotate(txt, (imp_aft_miti[i], prob_aft_miti[i]))
    
    #Plot some data
    plt.scatter(imp_aft_miti, prob_aft_miti,c='blue')
    ax2.imshow(img,extent=[0, 5, 0, 5])
    plt.show()

    plt.savefig(buf3,format = 'png')
    buf3.seek(0)
    string3 = base64.b64encode(buf3.read())
    uri3 = urllib.parse.quote(string3)


    return render(request,'show_projects.html',{
        'nav':'show_projects',
        'projects':projects,
        'risks':risks,
        'score_bef_miti':score_bef_miti,
        'score_aft_miti':score_aft_miti,
        'project_names':project_names,
        'prob_bef_miti':prob_bef_miti,
        'prob_aft_miti':prob_aft_miti,
        'imp_bef_miti':imp_bef_miti,
        'imp_aft_miti':imp_aft_miti,
        'chart':uri2,
        'chart2':uri3,
    })

def get_risk(request,project_name):
    risks = Risks.objects.filter(project_no__project_name=project_name)
    score = int(risks[0].prob_bef_miti) * int(risks[0].imp_bef_miti)
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
        prob_bef_miti = request.POST['prob_bef_miti']
        prob_aft_miti = request.POST['prob_aft_miti']
        imp_bef_miti = request.POST['imp_bef_miti']
        imp_aft_miti = request.POST['imp_aft_miti']
        mitigation = request.POST['mitigation']
        cl_costs = request.POST['cl_costs']
        pl_activities = request.POST['pl_activities']
        cont_acts = request.POST['cont_acts']
        owner  = request.POST['owner']
        owner_of_mitigation  = request.POST['owner_of_mitigation']
        status = request.POST['status']
        nearest_month = request.POST['nearest_month']
        cont_bud = request.POST['cont_bud']
        quality_impact = request.POST['quality_impact']
        rep_impact = request.POST['reputation_impact']

        risks = Risks(projects=projects_,
        category=category,
        desc=desc,
        prob_bef_miti=prob_bef_miti,
        prob_aft_miti=prob_aft_miti,
        imp_bef_miti=imp_bef_miti,
        imp_aft_miti=imp_aft_miti,
        mitigation=mitigation,
        costs_in_budget=cont_bud,
        cl_costs=cl_costs,
        planned_costs=pl_activities,
        cont_costs=cont_acts,
        owner=owner,
        owner_of_mitigation = owner_of_mitigation,
        status=status,
        nearest_month=nearest_month,
        quality_impact=quality_impact,
        rep_impact=rep_impact)

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
        prob_bef_miti = request.POST['prob_bef_miti']
        prob_aft_miti = request.POST['prob_aft_miti']
        imp_bef_miti = request.POST['imp_bef_miti']
        imp_aft_miti = request.POST['imp_aft_miti']
        mitigation = request.POST['mitigation']
        cl_costs = request.POST['cl_costs']
        pl_activities = request.POST['pl_activities']
        cont_acts = request.POST['cont_acts']
        owner  = request.POST['owner']
        owner_of_mitigation  = request.POST['owner_of_mitigation']
        status = request.POST['status']
        nearest_month = request.POST['nearest_month']
        cont_bud = request.POST['cont_bud']
        quality_impact = request.POST['quality_impact']
        rep_impact = request.POST['reputation_impact']

        risks = Risks(projects=projects,
        category=category,
        desc=desc,
        prob_bef_miti=prob_bef_miti,
        prob_aft_miti=prob_aft_miti,
        imp_bef_miti=imp_bef_miti,
        imp_aft_miti=imp_aft_miti,
        mitigation=mitigation,
        costs_in_budget=cont_bud,
        cl_costs=cl_costs,
        planned_costs=pl_activities,
        cont_costs=cont_acts,
        owner=owner,
        owner_of_mitigation = owner_of_mitigation,
        status=status,
        nearest_month=nearest_month,
        quality_impact=quality_impact,
        rep_impact=rep_impact)

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
            'prob_bef_miti':r.prob_bef_miti,
            'imp_bef_miti':r.imp_bef_miti,
            'mitigation':r.mitigation,
            'costs_in_budget':r.costs_in_budget,
            'cl_costs':r.cl_costs,
            'planned_costs':r.planned_costs,
            'cont_costs':r.cont_costs,
            'owner':r.owner,
            'status':r.get_status_display(),
            'nearest_month':r.nearest_month,
            'score':int(r.prob_bef_miti) * int(r.imp_bef_miti),
        })

    return JsonResponse(projects_arr, safe=False)
