from django.db import models

category_choices = (
    ('1', 'Technical'),
    ('2', 'Commercial'),
    ('3', 'Performance'),
    ('4', 'Health and Safety'),
    ('5', 'External'),
    ('6', 'Subs'),
)

impact_choices = (
    ('1', 'Negligible'),
    ('2', 'Marginal'),
    ('3', 'Significant'),
    ('4', 'Critical'),
    ('5', 'Unacceptable/Crisis'),
)

status_choices = (
    ('1', 'Open'),
    ('2', 'In progress'),
    ('3', 'Closed'),
)

probability_choices = (
    ('1', 'Very Unlikely'),
    ('2', 'Unlikely'),
    ('3', 'Moderately Likely'),
    ('4', 'Likely'),
    ('5', 'Very Likely'),
)

riskaction_choices = (
    ('1','Treat'),
    ('2','Own'),
    ('3','Transfer'),
)

class Projects(models.Model):
    project_name = models.CharField(max_length=100)
    project_number = models.IntegerField(primary_key=True)
    client = models.CharField(max_length=100)
    project_manager = models.CharField(max_length=100)
    last_review = models.DateField(auto_now=False, auto_now_add=False)
    scope_of_work = models.TextField()

    def __str__(self):
        return self.project_name

    def get_risk_by_project(self):
        if self.risks_set.count():
            return self.risks_set.order_by('id')[0]

class Risks(models.Model):
    projects = models.ForeignKey(Projects,on_delete=models.CASCADE,blank=True, null=True)
    category = models.CharField(max_length=1, choices=category_choices)
    desc = models.TextField()
    prob_bef_miti = models.CharField(max_length=1, choices=probability_choices, default='1')
    prob_aft_miti = models.CharField(max_length=1, choices=probability_choices, default='1')
    imp_bef_miti = models.CharField(max_length=1, choices=impact_choices, default='1')
    imp_aft_miti = models.CharField(max_length=1, choices=impact_choices, default='1')
    status = models.CharField(max_length=1, choices=status_choices)
    mitigation = models.TextField(default='Mitigation')
    cost_of_mitigation = models.IntegerField(default=100000)
    cost_of_bef_mitigation = models.IntegerField(default=100000)
    cost_of_aft_mitigation = models.IntegerField(default=100000)
    riskaction = models.CharField(max_length=1, choices=riskaction_choices, default='1')
    cl_costs = models.IntegerField()
    planned_costs = models.IntegerField()
    cont_costs = models.IntegerField()
    costs_in_budget = models.IntegerField()
    owner = models.CharField(max_length=20)
    owner_of_mitigation = models.CharField(max_length=20,default='Owner')
    nearest_month = models.CharField(max_length=20)
    quality_impact = models.TextField(default='Quality Impact')
    rep_impact = models.TextField(default='Reputation Impact')

    def __str__(self):
        return self.category


