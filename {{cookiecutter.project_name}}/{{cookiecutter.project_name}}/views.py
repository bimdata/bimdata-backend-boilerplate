from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def plugin(request):
    return Response(
        "Welcome %s, you are logged on %s"
        % (request.user.first_name, {{cookiecutter.project_name}})
    )
