from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, request
from django.contrib.auth.models import User, auth
from store.models import book
from store.models import Cart, Category
from django.contrib.sessions.models import Session
from .forms import UserRegisterForm,UserCreationForm,UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser, logout as logoutUser
from accounts.forms import ProfileUpdateForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f'Account created  for {username}!')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        # next_page=request.GET.get('next')
        # if next_page is not None:
        #     request.session['next_page']=next_page
        return render(request, 'login.html', context={'form': form})
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                loginUser(request, user)
                cart = Cart.objects.filter(user=user)
                session_cart = []
                for c in cart:
                    obj = {
                        'book': c.Book.id,
                        'category': c.Book.category.name,
                        'quantity': c.quantity
                    }
                    session_cart.append(obj)
                request.session['cart'] = session_cart
                # next_page=request.GET.get('next_page')
                # if next_page is None:
                #     next_page='main1'
                # return redirect('next_page')
                return redirect('main1')

        else:
            return render(request, 'login.html', context={'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)


def search(request):
    search = request.GET.get('search')
    books = book.objects.filter(name__icontains=search)
    params = {'books': books}
    return render(request, 'search.html', params)

   # print(books)

    #print('name:', request.session.get('user_name'))
    # print(User.get_short_name())
    

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             #print("login done")
#             request.session['is_logged'] = True
#             request.session['user_id'] = user.id
#             request.session['user_email'] = user.email
#            # request.session['user_name'] = user.username

#             return redirect('main1')
#         else:
#             messages.info(request, 'wrong credentials!')
#             #print("login fail")
#             return redirect('login')

#     else:
#         return render(request, 'login.html')


# def signup(request):

#     if request.method == 'POST':

#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']

#         if password1 == password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, "this username is taken")
#                 return redirect('signup')
#             elif User.objects.filter(email=email).exists():
#                 # print("email taken")
#                 messages.info(request, "this email is taken")
#                 return redirect('signup')

#             else:
#                 user = User.objects.create_user(
#                     username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
#                 user.save()
#                 return redirect('main1')
#         else:
#             # print("password not matching")
#             messages.info(request, "password not matching")
#             return redirect('signup')
#         return redirect('/')
#     else:
#         return render(request, 'signup.html')

def logout(request):
    logoutUser(request)
    return redirect('/')


def main1(request):

    books = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        books = book.get_all_books_by_categoriesid(categoryID)
    else:
        books = book.get_all_books()
    data = {}
    data['books'] = books
    data['categories'] = categories

   # print(books)

    #print('name:', request.session.get('user_name'))
    # print(User.get_short_name())
    return render(request, 'main1.html', data)
    # return redirect('login')
