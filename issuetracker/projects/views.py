from django.shortcuts import get_object_or_404, render
from .models import Project

def index(request):
    project_list = Project.objects.order_by("-creation_date")
    context = {"project_list": project_list}
    return render(request, "project/index.html", context)

def detail(request, project_id):
    issue = get_object_or_404(Project, pk=project_id)
    return render(request, "project/detail.html", {"issue": issue})