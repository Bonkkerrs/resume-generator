from django.contrib import admin
from myresume.models import User, Subsection, Section, Item, Entry


# Register your models here.
class UserAdminModel(admin.ModelAdmin):
    list_display = ['username', 'username_eng', 'phone_number', 'email', 'github']
    search_fields = ('username', 'username_eng')


class ItemInline(admin.StackedInline):
    model = Item
    extra = 0


class EntryInline(admin.StackedInline):
    model = Entry
    extra = 0


class SubsectionAdminModel(admin.ModelAdmin):
    list_display = ['subsection_name', 'subsection_name_eng', 'by_section', 'period', 'period_eng', 'user']
    search_fields = ('subsection_name', 'subsection_name_eng')
    list_filter = ['by_section']
    inlines = [ItemInline, EntryInline]


class SectionAdminModel(admin.ModelAdmin):
    list_display = ['section_name','section_name_eng']


class ItemAdminModel(admin.ModelAdmin):
    list_display = ['title', 'title_eng', 'text', 'text_eng', 'by_subsection', 'user']
    list_filter = ['by_subsection']


class EntryAdminModel(admin.ModelAdmin):
    list_display = ['text', 'text_eng', 'by_subsection', 'user']
    list_filter = ['by_subsection']


admin.site.register(User, UserAdminModel)
admin.site.register(Subsection, SubsectionAdminModel)
admin.site.register(Section, SectionAdminModel)
admin.site.register(Item, ItemAdminModel)
admin.site.register(Entry, EntryAdminModel)