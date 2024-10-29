import copy
from django.conf import settings
from django import template

register = template.Library()


@register.inclusion_tag("django_xsession/loader.html", takes_context=True)
def xsession_loader(context):

    try:
        request = context["request"]
    except KeyError:
        return {}

    if not hasattr(request, "xsession"):
        return {}

    if request.session.keys() or request.user.is_authenticated:
        return {}

    cookie = getattr(settings, "SESSION_COOKIE_NAME", "sessionid")
    if request.COOKIES.get(cookie, None):
        return {}

    host = request.META.get("HTTP_HOST", "").split(":")[0]
    if not host:
        return {}

    if request.is_secure():
        proto = "https"
    else:
        proto = "http"

    port = request.META.get("SERVER_PORT", None)
    if port == "80" and proto == "http":
        port = None
    elif port == "443" and proto == "https":
        port = None
    else:
        port = str(port)

    domains = copy.copy(settings.XSESSION_DOMAINS)
    for domain in settings.XSESSION_DOMAINS:
        if host.endswith(domain):
            domains.remove(domain)

    render_context = {
        "path": getattr(settings, "XSESSION_FILENAME", "xsession_loader.js"),
        "domains": domains,
        "proto": proto,
        "port": port,
    }

    return render_context
