from django.contrib import admin

from server.wines.models import Wine, WineMarket, WineMarketStock


class WineMarketInline(admin.StackedInline):
    model = WineMarketStock
    show_change_link = True
    extra = 0


@admin.register(WineMarket)
class WineMarketAdmin(admin.ModelAdmin):
    inlines = (WineMarketInline,)
    list_display = ('name', 'city',)
    search_fields = ('name',)


@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    inlines = (WineMarketInline,)
    list_display = ('name', 'country', 'price',)
    search_fields = ('name', 'country',)
    exclude = ('name_vector', 'description_vector',)
