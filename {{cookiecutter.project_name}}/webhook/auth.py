import hmac
import hashlib
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import ValidationError


class BimdataSignatureAuthentication(BaseAuthentication):
    def authenticate(self, request):
        req_signature = request.META.get("HTTP_X_BIMDATA_SIGNATURE")
        if not req_signature:
            raise ValidationError(detail={"x-bimdata-signature": "Header required"})

        body_signature = hmac.new(
            settings.WEBHOOKS_SECRET.encode(), request.body, hashlib.sha256
        ).hexdigest()

        if not hmac.compare_digest(req_signature, body_signature):
            raise ValidationError(detail={"x-bimdata-signature": "Bad request signature"})

        return (req_signature, req_signature)
