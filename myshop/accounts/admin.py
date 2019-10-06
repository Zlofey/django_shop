from django.contrib import admin
from accounts.models import Profile


def devil_post(modeladmin, request, queryset):
    # for obj in queryset:
    #     do_something_with(obj)
    queryset.update(postal_code='666')

devil_post.short_description = "Send all orders to the Dark Lord"

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','address', 'postal_code', 'city')#'first_name', 'last_name', 'email',
    actions = [devil_post]

admin.site.register(Profile, ProfileAdmin)
