from django.urls import path
from resume.views import resume_index\
    # , education_index, experience_index, project_index, achievement_index

urlpatterns = [
    path("", resume_index, name="resume_index"),
    # path("education", education_index, name="education_index"),
    # path("experience", experience_index, name="experience_index"),
    # path("project", project_index, name="project_index"),
    # path("achievement", achievement_index, name="achievement_index"),
]