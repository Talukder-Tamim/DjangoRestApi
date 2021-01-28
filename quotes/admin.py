from django.contrib import admin

from . models import QuoteCategory
from . models import Quote, Country

admin.site.register(QuoteCategory)
admin.site.register(Quote)
admin.site.register(Country)
