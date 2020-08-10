from django.contrib import admin

from proffy_api.core.models import Class, ClassSchedule, ProffyUser


@admin.register(ProffyUser)
class ProffyUserAdmin(admin.ModelAdmin):

    list_display = ["name", "whatsapp"]


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):

    list_display = ["proffy_user", "subject", "cost"]


@admin.register(ClassSchedule)
class ClassScheduleAdmin(admin.ModelAdmin):

    list_display = ["klass", "week_day", "start_at", "end_at"]
