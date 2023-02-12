from django.apps import apps
from .models import *

# Register your models here.

from django.contrib import admin
from django.core.paginator import Paginator
from django.db import connection, transaction, OperationalError
from django.utils.functional import cached_property


# Register your models here.
class TimeLimitedPaginator(Paginator):
    """
    Paginator that enforces a timeout on the count operation.
    If the operations times out, a fake bogus value is
    returned instead.
    """

    @cached_property
    def count(self):
        # We set the timeout in a db transaction to prevent it from
        # affecting other transactions.
        with transaction.atomic(), connection.cursor() as cursor:
            cursor.execute('SET LOCAL statement_timeout TO 200;')
            try:
                return super().count
            except OperationalError:
                return 999999999


class BaseAdmin(admin.ModelAdmin):
    paginator = TimeLimitedPaginator
    list_per_page = 10
    select_related = prefetch_related = None

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if self.select_related:
            qs = qs.select_related(*self.select_related)
        if self.prefetch_related:
            qs = qs.prefetch_related(*self.prefetch_related)
        return qs


@admin.register(Employee)
class UserAdmin(BaseAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone']
    list_filter = ['email']
    search_fields = ('email', 'first_name', 'last_name', 'phone',)
