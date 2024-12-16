from typing import Callable

from django.http import HttpRequest, HttpResponse


class DisableCSRFMiddleware(object):
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        setattr(request, '_dont_enforce_csrf_checks', True)
        response = self.get_response(request)
        response["cross-origin-opener-policy"] = "same-origin-allow-popups"
        return response
