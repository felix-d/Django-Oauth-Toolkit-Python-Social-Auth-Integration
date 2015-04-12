from django.http import HttpResponse
from django.contrib.auth import login

from social.apps.django_app.utils import psa

from .tools import get_access_token


@psa('social:complete')
def register_by_access_token(request, backend):
    # This view expects an access_token GET parameter, if it's needed,
    # request.backend and request.strategy will be loaded with the current
    # backend and strategy.
    token = request.GET.get('access_token')
    user = request.backend.do_auth(token)
    if user:
        login(request, user)
        return get_access_token(user)
    else:
        return HttpResponse("error")
