

from django.contrib.sites.models import Site

admin.site.unregister(Site)

class Site_Admin(admin.ModelAdmin):
    list_display = ('id',
                    'domain',
                    'name'
                    )

admin.site.register(Site, Site_Admin)
