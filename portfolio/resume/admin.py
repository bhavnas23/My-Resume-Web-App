from django.contrib import admin
from resume.models import Education, Experience, Project, Achievement, Skill
# Register your models here.
class EducationAdmin(admin.ModelAdmin):
    pass
class ExperienceAdmin(admin.ModelAdmin):
    pass
class ProjectAdmin(admin.ModelAdmin):
    pass
class AchievementAdmin(admin.ModelAdmin):
    pass
class SkillAdmin(admin.ModelAdmin):
    pass

admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Skill, SkillAdmin)
