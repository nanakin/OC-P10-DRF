from django.contrib import admin
from .models import Project, Issue, Contributor, Comment


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "project")


@admin.register(Contributor)
class ContributorAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "contribute_to")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("uuid", "issue", "get_project")

    @admin.display(ordering='issue_project', description='Project')
    def get_project(self, obj):
        return obj.issue.project
