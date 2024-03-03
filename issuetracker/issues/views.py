from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Issue,Comment
def index(request):
    issue_list = Issue.objects.order_by("-creation_date")
    context = {"issue_list": issue_list}
    return render(request, "issues/index.html", context)

def detail(request, issue_id):
    issue = get_object_or_404(Issue, pk=issue_id)
    return render(request, "issues/detail.html", {"issue": issue})

def comment(request, issue_id):
    return HttpResponse("You're adding a comment on issue %s." % issue_id)

def complete(request, issue_id):
    return HttpResponse("You're marking an issue as complete %s." % issue_id)