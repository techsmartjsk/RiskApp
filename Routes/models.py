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

class Projects(models.Model):
    project_name = models.CharField(max_length=100)
    project_number = models.IntegerField(primary_key=True)
    client = models.CharField(max_length=100)
    project_manager = models.CharField(max_length=100)
    last_review = models.DateField(auto_now=False, auto_now_add=False)
    scope_of_work = models.TextField()

    def __str__(self):
        return self.project_name

class Risks(models.Model):
    project_no = models.OneToOneField(Projects,on_delete=models.CASCADE)
    category = models.CharField(max_length=1, choices=category_choices)
    desc = models.TextField()
    probability = models.CharField(max_length=1, choices=probability_choices)
    impact = models.CharField(max_length=1, choices=impact_choices)
    status = models.CharField(max_length=1, choices=status_choices)
    control_measures = models.TextField()
    cl_costs = models.IntegerField()
    planned_costs = models.IntegerField()
    cont_costs = models.IntegerField()
    costs_in_budget = models.IntegerField()
    owner = models.CharField(max_length=20)
    nearest_month = models.CharField(max_length=20)

    def __str__(self):
        return self.project_no


