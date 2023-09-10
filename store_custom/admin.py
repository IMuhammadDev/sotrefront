from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProducktAdmin
from store.models import Produckt
from tags.models import TaggedItem

class TagInLine(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem

class CustomProducktAdmin(ProducktAdmin):
    inlines = [TagInLine]

admin.site.unregister(Produckt)
admin.site.register(Produckt, CustomProducktAdmin)
