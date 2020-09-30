import json
import logging
import os

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from ..models import DiscordRole, EmailRole, Registration


logger = logging.getLogger(__name__)

REGISTRATION_WEBHOOK_TOKEN = settings.REGISTRATION_WEBHOOK_TOKEN

@csrf_exempt
def webhook_handler(request):
    if not REGISTRATION_WEBHOOK_TOKEN:
        raise Exception("No webook token set")
    if request.META.get("HTTP_AUTHORIZATION") != f"Bearer {REGISTRATION_WEBHOOK_TOKEN}":
        return HttpResponse("Unauthorized", status=401)

    payload = json.loads(request.body.decode("utf-8"))
    logger.warning(payload)

    default_roles = DiscordRole.objects.filter(assign_by_default=True)

    try:
        email_role = EmailRole.objects.get(email__iexact=payload["email"])
    except ObjectDoesNotExist:
        email_role = EmailRole(email=payload["email"].lower())
        email_role.save()

    logger.error(email_role)
    email_role.discord_roles.add(*default_roles)
    email_role.save()
    registration = Registration(email=email_role, reference_id=payload["reference_id"])
    registration.save()

    return HttpResponse(status=201)
