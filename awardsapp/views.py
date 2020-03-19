from django.shortcuts import render,redirect,Http404,HttpResponse
from .forms import ProfileUpdateForm,ProjectForm,CreatePollForm
from django.contrib.auth.decorators import login_required
from . models import Profile,Projects,Poll
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import MerchSerializer,MerchSerializer2


def homepage(request):
    projects=Projects.objects.all()
    return  render(request, 'home.html',{"projects":projects})

@login_required
def home(request):
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'home2.html', context)
@login_required
def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = CreatePollForm()
    context = {
        'form' : form
    }
    return render(request, 'create.html', context)
@login_required
def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)


    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        elif selected_option == 'option4':
            poll.option_three_count += 1
        elif selected_option == 'option5':
            poll.option_three_count += 1
        elif selected_option == 'option6':
            poll.option_three_count += 1
        elif selected_option == 'option7':
            poll.option_three_count += 1
        elif selected_option == 'option8':
            poll.option_three_count += 1
        elif selected_option == 'option9':
            poll.option_three_count += 1
        elif selected_option == 'option10':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('results', poll.id)

    context = {
        'poll' : poll
    }
    return render(request, 'vote.html', context)
@login_required
def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'results.html', context)

@login_required
def updatemyprofile(request):
    current_user = request.user
    try:
        myprofile = Profile.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = ProfileUpdateForm(request.POST,request.FILES)

            if form.is_valid():
                myprofile.profile_photo = form.cleaned_data['profile_photo']
                myprofile.bio = form.cleaned_data['bio']
                myprofile.username = form.cleaned_data['username']
                myprofile.save_profile()
                return redirect( myprofile )
        else:
            form = ProfileUpdateForm()
    except:
        if request.method == 'POST':
            form = ProfileUpdateForm(request.POST,request.FILES)

            if form.is_valid():
                createprofile= Profile(profile_photo= form.cleaned_data['profile_photo'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'],user = current_user)
                createprofile.save_profile()




        else:
            form = ProfileUpdateForm()


    return render(request,'createprofile.html',{"current_user":current_user,"form":form})


@login_required
def myprofile(request):
    current_user = request.user
    try:
        profile = Profile.objects.get(user_id=current_user)
        project=Projects.objects.filter(user_id=current_user)

    except:
        profile = Profile.objects.filter(user_id=current_user)
        project = Projects.objects.filter(user_id=current_user)
    return render(request, 'profile.html',{"profile": profile,"project": project,  "current_user": current_user})


@login_required
def createproject(request):
    current_user=request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            createproject = Projects(project_name=form.cleaned_data['project_name'], project_description=form.cleaned_data['project_description'],
                                    project_link=form.cleaned_data['project_link'], user=current_user,    project_photo=form.cleaned_data['project_photo'])
            createproject.save_project()

            return redirect(myprofile)
    else:
        form = ProjectForm()

    return render(request, 'createproject.html', {"form": form})


@login_required
def updatemyprojects(request,sasa):

    myprojects=Projects.objects.get(id=sasa)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            myprojects.project_photo = form.cleaned_data['project_photo']
            myprojects.project_description= form.cleaned_data['project_description']
            myprojects.project_link= form.cleaned_data['project_link']
            myprojects.project_name = form.cleaned_data['project_name']
            myprojects.save_project()
            return redirect( myprofile )
    else:
        form = ProjectForm()


    return render(request,'createproject.html',{"form":form})


@login_required
def editproject(request,projectid):
    current_user=request.user
    try:
        project = Projects.objects.get(id=projectid)
    except Exception:
        raise Http404()
    return render(request, "projectid.html", {"project": project,"current_user":current_user})



def search_project(request):
    if 'name' in request.GET and request.GET["name"]:
        search_term=request.GET.get("name")
        searchednames=Projects.search_project(search_term)
        message=f"{search_term}"
        return render(request,"search.html",{"message":message,"searched":searchednames})

    else:
        message="you haven't searched"
    return render(request,"search.html",{"message":message})

class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = Profile.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)


class MerchList2(APIView):
    def get(self, request, format=None):
        all_merch = Projects.objects.all()
        serializers = MerchSerializer2(all_merch, many=True)
        return Response(serializers.data)

# Create your views here.
