from django.contrib import admin
from .models import Project, Issue, Contributor, Comment


admin.site.register(Contributor)
admin.site.register(Comment)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "project")
