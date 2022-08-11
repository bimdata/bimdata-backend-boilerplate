from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def plugin(request):
    return Response(
        f"Welcome {request.user.first_name}, you are logged on {{cookiecutter.project_name}}"
    )
