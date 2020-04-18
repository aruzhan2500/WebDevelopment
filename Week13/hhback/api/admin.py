from django.contrib import admin
from api.models import Company, Vacancy


admin.site.register(Vacancy)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by',)

