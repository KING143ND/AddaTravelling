# Create your views here.
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from . models import Article, Contact, Place, Video, Hotel
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    models = {
        'Video': Video.objects.all().order_by("pk"),
        'Article': Article.objects.all().order_by("pk"),
        'Hotel': Hotel.objects.all().order_by("pk"),
        'Place': Place.objects.all().order_by("pk"),
    }
    paginated_data = {}
    for model_name, queryset in models.items():
        paginator = Paginator(queryset, 100)
        page_number = request.GET.get('page')
        try:
            paginated_data[model_name] = paginator.page(page_number)
        except PageNotAnInteger:
            paginated_data[model_name] = paginator.page(1)
        except EmptyPage:
            paginated_data[model_name] = paginator.page(paginator.num_pages)
    context = {'paginated_data': paginated_data}
    return render(request, "index.html", context)


@login_required(login_url="/login")
def about(request):
    return render(request,"about.html")


@login_required(login_url="/login")
def features(request):
    return render(request,"features.html")


@login_required(login_url="/login")
def news(request):
    return render(request,"news.html")


@login_required(login_url="/login")
def contact(request):
    if request.method=="POST":
        firstName=request.POST['firstName']
        lastName=request.POST['lastName']
        email=request.POST['email']
        massage =request.POST['massage']
        if len(firstName)==0:
            messages.error(request, "Your First Name cannot be Empty!😠")
            return redirect('/contact')
        elif len(lastName)==0:
            messages.error(request, "Your Last Name cannot be Empty!😠")
            return redirect('/contact')
        elif len(email)==0:
            messages.error(request, "Your Email cannot be Empty!😠")
            return redirect('/contact')
        elif len(massage)==0:
            messages.error(request, "Your Message Box cannot be Empty!😠")
            return redirect('/contact')
        elif len(firstName)>30:
            messages.error(request, "Your First Name must be under 30 Characters!😟")
            return redirect('/contact')
        elif len(firstName)<3:
            messages.error(request, "Your First Name must be atleast 3 Characters!😟")
            return redirect('/contact')
        elif len(lastName)>30:
            messages.error(request, "Your Last Name must be under 30 Characters!😟")
            return redirect('/contact')
        elif len(lastName)<3:
            messages.error(request, "Your Last Name must be atleast 3 Characters!😟")
            return redirect('/contact')
        elif len(email)<6:
            messages.error(request, "Your Email must be atleast 6 Characters!😟")
            return redirect('/contact')
        elif len(email)>50:
            messages.error(request, "Your Email must be under 50 Characters!😟")
            return redirect('/contact')
        elif len(massage)<4:
            messages.error(request, "Please fill atleast 4 Characters in Message Box!😟")
            return redirect('/contact')
        elif len(massage)>1000:
            messages.error(request, "Your Message must be under 1000 Characters!😟")
            return redirect('/contact')
        else:
            contact=Contact(firstName=firstName, email=email, lastName=lastName, massage=massage)
            contact.save()
            messages.success(request, "Your Message has been Successfully sent!🙂")
            return redirect('/')      
    return render(request, "contact.html")


@login_required(login_url="/login")
def team(request):
    return render(request,"team.html")


def login(request):
    if request.method == 'POST':  
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = auth.authenticate(username = loginusername, password = loginpassword)
        if user is not None:
            auth.login(request,user)
            messages.success(request, f"Successfully Logged In.. Welcome {loginusername}!🙂")
            next_param = request.POST.get('next')
            if next_param:
                return redirect(next_param)
        else:
            messages.error(request,"Invalid Credentials!😟")
            return redirect("/login")
    return render(request, "login.html")


def logout(request):
    try:
        auth.logout(request)
        messages.success(request, f"You have Successfully Logged Out!🙂")
        return redirect('/')
    except:
        return redirect("/")


def signup(request):
    if request.method == 'POST':
        fname = request.POST.get("fname","default")
        lname = request.POST.get("lname","default")
        username = request.POST.get("username","default")
        email = request.POST.get("email","default")
        pass1 = request.POST.get("pass1","default")
        pass2 = request.POST.get("pass2","default")
        if pass1==pass2:
            if User.objects.filter(username = username).exists():
                messages.error(request,"Username has been already taken!😔")
                return redirect("/signup")
            elif User.objects.filter(email = email).exists():
                messages.error(request,"Email has been already taken!😔")
                return redirect("/signup")
            elif len(username)==0:
                messages.error(request, "Your Username cannot be Empty!😟")
                return redirect('/signup')
            elif len(fname)==0:
                messages.error(request, "Your First Name cannot be Empty!😟")
                return redirect('/signup')
            elif len(lname)==0:
                messages.error(request, "Your Last Name cannot be Empty!😟")
                return redirect('/signup')
            elif len(email)==0:
                messages.error(request, "Your Email cannot be Empty!😟")
                return redirect('/signup')
            elif len(pass1)==0:
                messages.error(request, "Your Password cannot be Empty!😟")
                return redirect('/signup')
            elif len(username)<3:
                messages.error(request, "Your Username cannot be less than 3 Characters!😠")
                return redirect('/signup')
            elif len(username)>15:
                messages.error(request, "Your Username must be under 15 Characters!😠")
                return redirect('/signup')
            elif not username.isalnum():
                messages.error(request, "Special Characters are not allowed!😠")
                return redirect('/signup')
            elif len(fname)>30:
                messages.error(request, "Your First Name must be under 30 Characters!😠")
                return redirect('/signup')
            elif len(fname)<2:
                messages.error(request, "Your First Name must be atleast 2 Characters!😠")
                return redirect('/signup')
            elif len(lname)>30:
                messages.error(request, "Your Last Name must be under 30 Characters!😠")
                return redirect('/signup')
            elif len(lname)<2:
                messages.error(request, "Your Last Name must be atleast 2 Characters!😠")
                return redirect('/signup')
            elif len(email)<6:
                messages.error(request, "Your Email must be atleast 6 Characters!😠")
                return redirect('/signup')
            elif len(email)>100:
                messages.error(request, "Your Email must be under 100 Characters!😠")
                return redirect('/signup')
            elif len(pass1)<6:
                messages.error(request, "Your Password must be atleast 6 Characters!😠")
                return redirect('/signup')
            elif len(pass1)>20:
                messages.error(request, "Your Password must be atmost 20 Characters!😠")
                return redirect('/signup')
            else:
                myuser = User.objects.create_user(username=username, email=email, password=pass1, first_name=fname, last_name=lname)
                messages.success(request, f"Congratulations...{fname} {lname}! Your Account has been Created Sucessfully!🙂")
                myuser.save()
                myuser = auth.authenticate(username = username, password = pass1)
                auth.login(request,myuser)
                return redirect("/")
        else:
            messages.error(request,"Password do not Match!😯")
            return redirect("/signup")
    return render(request, "signup.html")


@login_required(login_url="/login")
def search(request):
    query = request.GET['query']
    if len(query)==0:
        messages.error(request, "Your Search Result cannot be Empty!😟")
        return redirect('/')
    elif len(query)<3:
        messages.error(request, "Your Search Query cannot be less than 3 Characters!😠")
        return redirect('/')
    elif len(query)>30:
        messages.error(request, "Your Search Query cannot be more than 30 Characters!😠")
        return redirect('/')
    search_place = Place.objects.filter(location__icontains = query)
    places = Place.objects.filter(place_title__icontains = query)
    allvideo = Video.objects.filter(title__icontains = query)
    allarticle = Article.objects.filter(title__icontains = query)
    allhotel = Hotel.objects.filter(hotel_title__icontains = query)
    
    search_results = {'search_place': search_place,'places':places,'video':allvideo,'article':allarticle,'hotels':allhotel}
    
    return render(request,"search.html", search_results)


@login_required(login_url="/login")
def search_places(request, place_title):
    places = Place.objects.filter(place_title = place_title)
    index_places = {'places':places}
    
    allvideo = Video.objects.filter(title = place_title)
    index_videos = {'video':allvideo}
    
    allarticle = Article.objects.filter(title = place_title)
    index_articles = {'article':allarticle}
    
    allhotel = Hotel.objects.filter(hotel_title = place_title)
    index_hotels = {'hotels':allhotel}
    
    return render(request,"allplaces.html",index_videos|index_articles|index_hotels|index_places)
   
    
@login_required(login_url="/login")
def search_hotels(request, hotel_title):
    hotels = Hotel.objects.filter(hotel_title = hotel_title)
    index_hotels = {'hotels':hotels}
    
    return render(request,"allhotels.html",index_hotels)


@login_required(login_url="/login")
def tour(request):
    allvideo = Video.objects.all().defer('url')
    paginator = Paginator(allvideo,15)
    page_number = request.GET.get('page')
    try:
        allvideo = paginator.page(page_number)
    except PageNotAnInteger:
        allvideo = paginator.page(1)
    except EmptyPage:
        allvideo = paginator.page(paginator.num_pages)
    index_videos = {'allvideo':allvideo,'page':page_number}
    
    return render(request,"tour.html",index_videos)


@login_required(login_url="/login")
def hotels(request):
    allhotel = Hotel.objects.all()
    paginator = Paginator(allhotel,60)
    page_number = request.GET.get('page')
    try:
        allhotel = paginator.page(page_number)
    except PageNotAnInteger:
        allhotel = paginator.page(1)
    except EmptyPage:
        allhotel = paginator.page(paginator.num_pages)
    index_hotels = {'allhotel':allhotel,'page':page_number}
    
    return render(request,"hotels.html",index_hotels)

@login_required(login_url="/login")
def allhotels(request, hotel_title):
    hotels = Hotel.objects.filter(hotel_title = hotel_title)
    allhotel = Hotel.objects.all()
    index_hotels = {'allhotel':allhotel,'hotels':hotels}
    
    return render(request,"allhotels.html",index_hotels)


@login_required(login_url="/login")
def allplaces(request, place_title):
    places = Place.objects.filter(place_title = place_title)
    index_places = {'places':places}
    
    allvideo = Video.objects.filter(title = place_title)
    index_videos = {'video':allvideo}
    
    allarticle = Article.objects.filter(title = place_title)
    index_articles = {'article':allarticle}
    
    allhotel = Hotel.objects.filter(hotel_title = place_title)
    index_hotels = {'hotels':allhotel}
    
    return render(request,"allplaces.html",index_videos|index_articles|index_hotels|index_places)
    
    
@login_required(login_url="/login")
def places(request):
    allplace = Place.objects.all()
    paginator = Paginator(allplace,100)
    page_number = request.GET.get('page')
    try:
        allplace = paginator.page(page_number)
    except PageNotAnInteger:
        allplace = paginator.page(1)
    except EmptyPage:
        allplace = paginator.page(paginator.num_pages)
    index_places = {'allplace':allplace,'page':page_number}
    
    return render(request,"places.html",index_places)


@login_required(login_url="/login")
def articles(request):
    allarticle = Article.objects.all()
    paginator = Paginator(allarticle,5)
    page_number = request.GET.get('page')
    try:
        allarticle = paginator.page(page_number)
    except PageNotAnInteger:
        allarticle = paginator.page(1)
    except EmptyPage:
        allarticle = paginator.page(paginator.num_pages)
    index_articles = {'allarticle':allarticle,'page':page_number}
    
    return render(request,"articles.html",index_articles)


@login_required(login_url="/login")
def faq(request):
    return render(request,"faq.html")


@login_required(login_url="/login")
def support(request):
    return render(request,"support.html")


@login_required(login_url="/login")
def terms(request):
    return render(request,"terms.html")


@login_required(login_url="/login")
def privacy(request):
    return render(request,"privacy.html")