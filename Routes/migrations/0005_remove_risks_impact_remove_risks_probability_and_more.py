# Generated by Django 4.0 on 2022-05-16 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Routes', '0004_rename_project_no_risks_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='risks',
            name='impact',
        ),
        migrations.RemoveField(
            model_name='risks',
            name='probability',
        ),
        migrations.AddField(
            model_name='risks',
            name='cost_of_mitigation',
            field=models.IntegerField(default=100000),
        ),
        migrations.AddField(
            model_name='risks',
            name='imp_aft_miti',
            field=models.CharField(choices=[('1', 'Negligible'), ('2', 'Marginal'), ('3', 'Significant'), ('4', 'Critical'), ('5', 'Unacceptable/Crisis')], default='1', max_length=1),
        ),
        migrations.AddField(
            model_name='risks',
            name='imp_bef_miti',
            field=models.CharField(choices=[('1', 'Negligible'), ('2', 'Marginal'), ('3', 'Significant'), ('4', 'Critical'), ('5', 'Unacceptable/Crisis')], default='1', max_length=1),
        ),
        migrations.AddField(
            model_name='risks',
            name='owner_of_mitigation',
            field=models.CharField(default='Owner', max_length=20),
        ),
        migrations.AddField(
            model_name='risks',
            name='prob_aft_miti',
            field=models.CharField(choices=[('1', 'Very Unlikely'), ('2', 'Unlikely'), ('3', 'Moderately Likely'), ('4', 'Likely'), ('5', 'Very Likely')], default='1', max_length=1),
        ),
        migrations.AddField(
            model_name='risks',
            name='prob_bef_miti',
            field=models.CharField(choices=[('1', 'Very Unlikely'), ('2', 'Unlikely'), ('3', 'Moderately Likely'), ('4', 'Likely'), ('5', 'Very Likely')], default='1', max_length=1),
        ),
        migrations.AddField(
            model_name='risks',
            name='quality_impact',
            field=models.TextField(default='Quality Impact'),
        ),
        migrations.AddField(
            model_name='risks',
            name='rep_impact',
            field=models.TextField(default='Reputation Impact'),
        ),
        migrations.AddField(
            model_name='risks',
            name='riskaction',
            field=models.CharField(choices=[('1', 'Treat'), ('2', 'Own'), ('3', 'Transfer')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='risks',
            name='mitigation',
            field=models.TextField(default='Mitigation'),
        ),
    ]
