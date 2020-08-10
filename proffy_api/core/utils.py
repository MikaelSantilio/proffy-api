from datetime import datetime

from django.db import transaction

from proffy_api.core.models import Class, ClassSchedule, ProffyUser


def str_hour_to_minutes(time):
    object_time = datetime.strptime(time, '%H:%M')
    return (object_time.hour * 60) + object_time.minute


@transaction.atomic
def save_data(data):
    proffy_user = ProffyUser.objects.create(
        name=data['name'],
        avatar=data['avatar'],
        whatsapp=data['whatsapp'],
        bio=data['bio']
    )

    class_user = Class.objects.create(
        subject=data['subject'],
        cost=data['cost'],
        proffy_user=proffy_user
    )

    list(map(
        lambda schedule: ClassSchedule.objects.create(
            week_day=schedule["week_day"],
            start_at=str_hour_to_minutes(schedule["start_at"]),
            end_at=str_hour_to_minutes(schedule["end_at"]),
            klass=class_user
        ),
        data['schedule']
    ))
