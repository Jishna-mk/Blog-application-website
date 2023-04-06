from django.shortcuts import redirect


def user_only(view_func):

    def wrapper_function(request, *args, **kwargs):
        print(request.user.is_active)
        if request.user.is_active == True:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('first')

    return wrapper_function
