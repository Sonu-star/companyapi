from django.http import HttpResponse,JsonResponse


def home_page(request):
    print("Home Page Requested")

    friends=[
        'ankit','sonu','harsh' 
    ]
    return JsonResponse(friends, safe=False)
    # return HttpResponse("This is home page")
