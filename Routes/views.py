from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect, render
from Routes.models import Projects,Risks

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
    return render(request,'show_projects.html',{
        'nav':'show_projects',
        'projects':projects,
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

        risks = Risks(project_no=projects,
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
    for risk in risks:
        risks_arr.append(risk.project_no)
    for r in risks_arr:
        projects = Projects.objects.get(project_name=r)
        projects_arr.append({
            'project_name':projects.project_name,
            'project_number':projects.project_number,
            'client':projects.client,
            'project_manager':projects.project_manager,
            'last_review':projects.last_review,
            'scope_of_work':projects.scope_of_work,
        })

    return JsonResponse(projects_arr, safe=False)
