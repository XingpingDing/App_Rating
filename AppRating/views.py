from django.shortcuts import render
from AppRating.forms import UserForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from AppRating.models import User, App, Category, Comment
import json

login_form = None

login_error = False
login_username_error = False
login_password_error = False
login_invalid_error = False


# Create your views here.
def index(request):
    registered = False
    error = False
    auto_password = None
    auto_username = None

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)

            auto_username = user.username
            auto_password = user.password


            user.save()

            registered = True

        else:
            print user_form.errors
            error = True

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        global login_form
        login_form = user_form

    context_dict = {
        'home': 'active',
        'user_form': user_form,
        'registered': registered,
        'error': error,
        'login_error': login_error,
        'login_username_error': login_username_error,
        'login_password_error': login_password_error,
        'login_invalid_error': login_invalid_error,
        'auto_n':auto_username,
        'auto_p':auto_password,
    }

    global login_error, login_invalid_error, login_password_error, login_username_error
    login_error = login_invalid_error = login_username_error = login_password_error = False

    appsLikeTop8 = (App.objects.all().order_by('-likecount'))[:8]

    context_dict['top8'] = appsLikeTop8

    # for a in appsLikeTop8:
    #     print "- {0}".format(str(a))

    return render(request, 'index.html', context_dict)


def rankList(request):
    context_dict = {
        'ranklist': 'active',
        'user_form': login_form,
        'login_error':login_error,
        'login_username_error': login_username_error,
        'login_password_error': login_password_error,
        'login_invalid_error': login_invalid_error,
    }

    category_list = Category.objects.all()
    context_dict['category_list'] = category_list

    all_list_top5 = (App.objects.all().order_by('-averscore'))[:5]
    context_dict['all_list'] = all_list_top5

    for c in category_list:
        category_list_top5 = (App.objects.filter(category=c).order_by('-averscore'))[:5]
        context_dict[c.name] = category_list_top5
        for a in category_list_top5:
            print "- {0}".format(str(a))

    return render(request, 'ranklist.html', context_dict)


def allapps(request):
    context_dict = {
        'categories': 'active',
        'user_form': login_form,
        'login_error':login_error,
        'login_username_error': login_username_error,
        'login_password_error': login_password_error,
        'login_invalid_error': login_invalid_error,
    }

    category_list = Category.objects.all()
    context_dict['category_list'] = category_list

    for c in category_list:
        app_list = App.objects.filter(category=c).order_by('appname')
        context_dict[c.name] = app_list
        for a in app_list:
            print "- {0}".format(str(a))

    return render(request, 'allApps.html', context_dict)

def about(request):
    context_dict = {
        'about': 'active',
        'user_form': login_form,
        'login_error':login_error,
        'login_username_error': login_username_error,
        'login_password_error': login_password_error,
        'login_invalid_error': login_invalid_error,
    }
    return render(request, 'about.html', context_dict)

def user_login(request):
    login_error = False
    # user = None

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username:
            global login_error, login_username_error
            login_error = True
            login_username_error = True

        if not password:
            global login_error, login_password_error
            login_error = True
            login_password_error = True

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.

        user = authenticate(username=username, password=password)
        print user

        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            global login_error
            login_error = True
            print "Invalid login details: {0}, {1}".format(username, password)

            if not username:
                print(password)
            elif not password:
                print(username)
            else:
                global login_invalid_error
                login_invalid_error = True

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'index.html', {})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def app(request, appid):
    app = App.objects.get(appid=appid)

    print (app)

    context_dict = {
        'user_form': login_form,
        'login_error':login_error,
        'login_username_error': login_username_error,
        'login_password_error': login_password_error,
        'login_invalid_error': login_invalid_error,
    }

    context_dict['app'] = app

    comment_list = Comment.objects.filter(app=app).order_by('-id')
    for comment in comment_list:
        if comment.content == '':
            comment.content = 'No content'
    context_dict['comment_list'] = comment_list

    likecount = app.likecount
    dislikecount = app.dislikecount

    likepercentage = 0
    dislikepercentage = 0
    if likecount == 0 and dislikecount == 0:
        likepercentage = 50
        dislikepercentage = 50
    elif likecount == 0:
        likepercentage = 0
        dislikepercentage = 100
    elif dislikecount == 0:
        likepercentage = 100
        dislikepercentage = 0
    else:
        likepercentage = int(likecount * 1.0 / (likecount + dislikecount) * 100)
        dislikepercentage = 100 - likepercentage

    context_dict['likepercentage'] = likepercentage
    context_dict['dislikepercentage'] = dislikepercentage

    return render(request, 'apps.html', context_dict)


def search(request):
    searchcontent = request.GET['searchcontent']

    context_dict = {
        'login_error':login_error,
        'login_username_error': login_username_error,
        'login_password_error': login_password_error,
        'login_invalid_error': login_invalid_error,
    }

    if searchcontent == '':
        context_dict['result_list'] = list
        context_dict['result_count'] = 0
    else:
        result_list = App.objects.filter(appname__icontains=searchcontent)
        context_dict['result_list'] = result_list
        context_dict['result_count'] = len(result_list)



    return render(request,"searchResults.html", context_dict)

def like(request):
    context_dict = {}

    if request.method == 'GET':
        appid = request.GET['appid']
        app = App.objects.get(appid=appid)

        if app:
            app.likecount += 1
            app.save()

            likecount = app.likecount
            dislikecount = app.dislikecount

            likepercentage = 0
            dislikepercentage = 0
            if likecount == 0 and dislikecount == 0:
                likepercentage = 50
                dislikepercentage = 50
            elif likecount == 0:
                likepercentage = 0
                dislikepercentage = 100
            elif dislikecount == 0:
                likepercentage = 100
                dislikepercentage = 0
            else:
                likepercentage = int(likecount * 1.0 / (likecount + dislikecount) * 100)
                dislikepercentage = 100 - likepercentage

            context_dict['success'] = '1'
            context_dict['likecount'] = likecount
            context_dict['dislikecount'] = dislikecount
            context_dict['likepercentage'] = likepercentage
            context_dict['dislikepercentage'] = dislikepercentage
        else:
           context_dict['success'] = '0'
    else:
        context_dict['success'] = '0'

    return HttpResponse(json.dumps(context_dict))

def dislike(request):
    context_dict = {}

    if request.method == 'GET':
        appid = request.GET['appid']
        app = App.objects.get(appid=appid)

        if app:
            app.dislikecount += 1
            app.save()

            likecount = app.likecount
            dislikecount = app.dislikecount

            likepercentage = 0
            dislikepercentage = 0
            if likecount == 0 and dislikecount == 0:
                likepercentage = 50
                dislikepercentage = 50
            elif likecount == 0:
                likepercentage = 0
                dislikepercentage = 100
            elif dislikecount == 0:
                likepercentage = 100
                dislikepercentage = 0
            else:
                likepercentage = int(likecount * 1.0 / (likecount + dislikecount) * 100)
                dislikepercentage = 100 - likepercentage

            context_dict['success'] = '1'
            context_dict['likecount'] = likecount
            context_dict['dislikecount'] = dislikecount
            context_dict['likepercentage'] = likepercentage
            context_dict['dislikepercentage'] = dislikepercentage
        else:
           context_dict['success'] = '0'
    else:
        context_dict['success'] = '0'

    return HttpResponse(json.dumps(context_dict))

def addComment(request):
    context_dict = {}

    if request.method == 'GET':
        username = request.GET['username']
        appid = request.GET['appid']
        score = (int)(request.GET['score'])
        content = request.GET['content']

        user = User.objects.get(username=username)
        app = App.objects.get(appid=appid)

        if app:
            app.averscore = (app.averscore * app.commentcount + score) / (app.commentcount + 1)
            app.commentcount = app.commentcount + 1
            app.save()

            comment = Comment.objects.create(user=user, app=app, score=score, content=content)
            comment.save()

            context_dict['success'] = '1'
            context_dict['averscore'] = app.averscore
        else:
            context_dict['success'] = '0'
    else:
        context_dict['success'] = '0'

    return HttpResponse(json.dumps(context_dict))

def history(request, username):
    user = User.objects.get(username=username)

    history_list = Comment.objects.filter(user=user).order_by('-id')

    for comment in history_list:
        if comment.content == '':
            comment.content = 'No content'

    context_dict = {
        'login_error':login_error,
        'login_username_error': login_username_error,
        'login_password_error': login_password_error,
        'login_invalid_error': login_invalid_error,
    }
    context_dict['history_list'] = history_list

    return render(request,'history.html', context_dict)




