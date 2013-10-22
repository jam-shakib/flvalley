from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from mezzanine.core.views import direct_to_template


admin.autodiscover()


urlpatterns = patterns("",
    ("^admin/", include(admin.site.urls)),

	# Cartridge URLs.
    ("^shop/", include("cartridge.shop.urls")),
    url("^account/orders/$", "cartridge.shop.views.order_history",
        name="shop_order_history"),
	
    #url("^$", direct_to_template, {"template": "index.html"}, name="home"),
    url("^$", "mezzanine.pages.views.page", {"slug": "/"}, name="home"),
    # url("^$", "mezzanine.blog.views.blog_post_list", name="home"),

    ("^", include("mezzanine.urls")),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler500 = "mezzanine.core.views.server_error"
