from django.conf import settings
from django.conf.urls.defaults import *

from django.views.generic.simple import direct_to_template

from django.contrib import admin

from pinax.apps.account.openid_consumer import PinaxConsumer

admin.autodiscover()

handler500 = "pinax.views.server_error"

urlpatterns = patterns("",
    url(r"^$", direct_to_template, {
        "template": "home.html",
    }, name="home"),
    url(r"^admin/invite_user/$", "pinax.apps.signup_codes.views.admin_invite_user", name="admin_invite_user"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^about/", include("about.urls")),
    url(r"^account/", include("pinax.apps.account.urls")),
    url(r"^openid/", include(PinaxConsumer().urls)),
    url(r"^profiles/", include("idios.urls")),
    url(r"^notices/", include("notification.urls")),
    url(r"^announcements/", include("announcements.urls")),
    url(r"^locationfinder/", include("geo.urls")),
    url(r"^businesses/", include("firms.urls")),
    url(r"^products/", include("products.urls")),
    url(r"^services/", include("services.urls")),
    url(r"^events/", include("events.urls")),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
