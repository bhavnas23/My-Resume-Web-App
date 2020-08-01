from django.shortcuts import render
from resume.models import Skill, Education, Experience, Project, Achievement
# Create your views here.
def resume_index(request):
    skills = Skill.objects.all()
    experience = Experience.objects.all()
    education = Education.objects.all()
    projects = Project.objects.all()
    achievements = Achievement.objects.all()
    context = {
        'skills' : skills,
        'experience': experience,
        'education': education,
        'projects': projects,
        'achievements': achievements
    }
    return render(request, 'main_template.html', context)

# def education_index(request):
#     education = Education.objects.all()
#     context = {
#         'education' : education
#     }
#     return render(request, 'education.html', context)
#
# def experience_index(request):
#     experience =  Experience.objects.all()
#     context = {
#         'experience' : experience
#     }
#     return render(request, 'main_template.html#experience', context)
#
# def project_index(request):
#     projects = Project.objects.all()
#     context = {
#         'projects' : projects
#     }
#     return render(request, 'project.html', context)
#
# def achievement_index(request):
#     achievements = Achievement.object.all()
#     context = {
#         'achievements': achievements
#     }
#     return render(request, 'achievement.html')
#
