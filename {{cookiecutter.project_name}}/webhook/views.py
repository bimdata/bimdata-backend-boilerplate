from rest_framework.views import APIView
from webhook.auth import BimdataSignatureAuthentication
from rest_framework import status, permissions
from rest_framework.response import Response


class WebHookHandler(APIView):
    authentication_classes = (BimdataSignatureAuthentication,)
    permission_calsses = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        print(request.data)
        return Response(status=status.HTTP_204_NO_CONTENT)
