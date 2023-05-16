from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profile, Meep

# import form.py meepsview(styleing)
from .form import MeepForm, UserSignUp, ProfilePicForm
from django.contrib.auth import authenticate, login, logout

# import user from models
from django.contrib.auth.models import User


# Create your views here.

def Home(request):
    if request.user.is_authenticated:
        form = MeepForm(request.POST or None)
        if request.method == "POST":
            meep = form.save(commit=False)
            meep.user = request.user
            meep.save()
            messages.success(request,('Your Meeps Has Been Posted!!....'))
            return redirect('home')
        
        meeps = Meep.objects.all().order_by('-created_at') # useing "-" before created_at in order_by for when we want to order sort woth last time this meeps add
        return render(request, "musker/home.html", {"meeps":meeps, "form":form}) #<-- don't forget to give value in return code                                                             # if we want to send value to html code we should give value with dict method
    else:
        meeps = Meep.objects.all().order_by('-created_at') # useing "-" before created_at in order_by for when we want to order sort woth last time this meeps add
        return render(request, "musker/home.html", {"meeps":meeps})

def ProfileList(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'musker/profile_list.html',{"profiles":profiles})
    else:
        messages.success(request, ("You Must be Logged In To view this Page .... "))
        return redirect('home')
    
def ProfileView(request,pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        # add meep in profile page (using filter for get meeps with own meeps)
        meeps = Meep.objects.filter(user_id=pk)
        
        # Post Form Logic
        if request.method == "POST":
            # Get current user
            current_user_profile = request.user.profile
            # get form data
            action = request.POST['follow'] # get from form name
            # Decide to follow or unfollow
            if action == "unfollow": # get from form value
                current_user_profile.follows.remove(profile)
            elif action == "follow":
                current_user_profile.follows.add(profile)
            # save the profile
            current_user_profile.save()
        
        return render(request, "musker/profile.html", {"profile":profile, "meeps":meeps})
    else:
        messages.success(request, ("You Must be Logged In To view this Page .... "))
        return redirect('home')
    

def login_user(request):
    if request.method == "POST":
        username = request.POST['username'] #<-- get from name of input username
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('You Have been Logged in! GET MEEPING!!'))
            return redirect('home')
        else:
            messages.success(request,('there was an error loggin in. Pelase Try Again...'))
            return redirect('login')
    else:
        return render(request, "musker/login.html", {}) 


def logout_user(request):
    logout(request)
    messages.success(request, ('You Have been logged Out !!. Sorry to Meep You Go....'))
    return redirect('home')

def RegisterView(request):
    form = UserSignUp() #<-- used to get form stylr from form.py
    if request.method == "POST":
        form = UserSignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You success for registration, and you in home page now'))
            return redirect('home')
        
    return render(request, 'musker/register.html', {'form':form}) #<-- get form above (( form = UserSignUp() ))

def UpdateUser(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_pic = Profile.objects.get(user_id=request.user.id)
        form = UserSignUp(request.POST or None ,request.FILES or None, instance = current_user)
        forms = ProfilePicForm(request.POST or None ,request.FILES or None, instance = profile_pic)
        # I change code little in env
        #form = UpdateProfile(request.POST or None , instance = current_user)
            # for save the change of update profile
        if form.is_valid() and forms.is_valid():
            form.save()
            forms.save()
            # and after we save this change, we're Must be Loggin again
            login(request, current_user)
            messages.success(request, ('Your Profile has been Updated!'))
            return redirect('home')
        return render(request, 'musker/update_register.html', {'form':form, 'forms':forms})
    else:
        messages.success(request, ('You must be Loggin to Update Your Profile....'))
        return redirect('home')
    

# for likes views
def MeepLiks(request, pk):
    if request.user.is_authenticated:
        meep = get_object_or_404(Meep, id=pk)
        if meep.likes.filter(id=request.user.id):
            meep.likes.remove(request.user)
        else:
            meep.likes.add(request.user)
        
        #return redirect('home')
        # for when we finished likes or unlikes we're will redirect to this page, we'll don't cabk to home page when we on other page
        return redirect(request.META.get('HTTP_REFERER'))
    
    else:
        messages.success('You must be loggin to Likes this meeps...')
        return redirect('home')
    

def MeepShow(request, pk):
    meep = get_object_or_404(Meep, id=pk)
    if meep:
        return render(request, 'musker/meep_show.html', {'meep':meep})
    else:
        messages.success('That meeps does not exist...')
        return redirect('home')
    