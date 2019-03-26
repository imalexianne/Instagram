from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .forms import ProfileForm,ImageForm,CommentsForm
from .models import Image,Profile,Comments
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='/accounts/login/')
def welcome(request):
    images = Image.objects.all()
    return render(request, 'welcome.html',{"images":images})

@login_required(login_url='/accounts/login/')
def images(request,image_id):
    image = Image.objects.get(id = image_id)
    return render(request,"info.html", {"image":image})

@login_required(login_url='/accounts/login/')
def myProfile(request,id):
    user = User.objects.get(id = id)
    profiles = Profile.objects.get(user = user)
   
    return render(request,'my_profile.html',{"profiles":profiles,"user":user})

def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        return redirect(welcome)

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

def image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()

    else:
        form = ImageForm()
    return render(request, 'image.html', {"form": form})

def comments(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentsForm(request.POST, request.FILES)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.user = current_user
            comments.save()

            return redirect(welcome)

    else:
        form = CommentsForm()
    return render(request, 'comment.html', {"form": form})



   

# def all_images(request):
#     images = Image.objects.all()
#     return render(request, 'welcome.html',{"images":images})

# def search_results(request):

#     if 'category' in request.GET and request.GET["category"]:
#         search_term = request.GET.get("category")
#         searched_images = Image.search_image(search_term)
#         message = f"{search_term}"

#         return render(request, 'search.html',{"message":message,"images": searched_images})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'search.html',{"message":message})


# @login_required(login_url='/accounts/login/')
# def image(request,image_id):
#     try:
#         images = Image.objects.get(id = image_id)
#         locations = Location.objects.all()
#         image_category = Image.objects.filter(category__image_category = category_name)
#     except DoesNotExist:
#         raise Http404()
#     return render(request,"images.html", {"image":image,'image_category':image_category, 'locations':locations})

# def search_result(request):
#     if 'location' in request.GET and request.GET["location"]:
#         search_term = request.GET.get("location")
#         searched_images = Image.search_img(search_term)
#         message = f"{search_term}"

#         return render(request, 'location.html',{"message":message,"images": searched_images})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'location.html',{"message":message})


#     return render(request, 'location.html', { 'images':images, 'locations':locations})


