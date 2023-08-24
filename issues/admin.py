from django.contrib import admin
from .models import Project, Issue, Contributor, Comment

admin.site.register(Issue)
admin.site.register(Contributor)
admin.site.register(Comment)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
