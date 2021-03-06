# Generated by Django 2.2.6 on 2019-12-20 04:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('survey', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estrogen_dominance_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estrogen_dominance_sets', to='survey.EstrogenDominance')),
                ('estrogen_pregnancy_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estrogen_pregnancy_sets', to='survey.EstrogenPregnancy')),
                ('high_androgen_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='high_androgen_sets', to='survey.HighAndrogen')),
                ('high_cortisol_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='high_cortisol_sets', to='survey.HighCortisol')),
                ('high_insulin_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='high_insulin_sets', to='survey.HighInsulin')),
                ('low_androgen_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='low_androgen_sets', to='survey.LowAndrogen')),
                ('low_cortisol_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='low_cortisol_sets', to='survey.LowCortisol')),
                ('low_thyroid_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='low_thyroid_sets', to='survey.LowThyroid')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_result', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IndivisualValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='single_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
