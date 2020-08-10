from django.db import DatabaseError
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from proffy_api.core.models import ClassSchedule, Connection, ProffyUser
from proffy_api.core.serializers import (
    ClassScheduleSerializer,
    ClassSerializer,
    ConnectionSerializer,
)
from proffy_api.core.utils import save_data, str_hour_to_minutes


class ClassCreateListAPIView(APIView):

    permission_classes = [AllowAny]

    def get(self, request, format=None):
        filters = request.query_params

        if ('week_day' not in filters or 'subject' not in filters or 'time' not in filters):
            return Response(
                {'error': 'Não há filtros para procurar aulas'},
                status=status.HTTP_400_BAD_REQUEST)

        qs_class_schedule = ClassSchedule.objects.filter(
            klass__subject=filters['subject'],
            week_day=filters['week_day'], start_at__lte=str_hour_to_minutes(filters['time']),
            end_at__gt=str_hour_to_minutes(filters['time']))

        data = []

        for class_schedule in qs_class_schedule:
            serializer = ClassScheduleSerializer(class_schedule)
            data.append(serializer.data['klass'])

        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            try:
                save_data(serializer.data)

            except DatabaseError:
                return Response(
                    {'error': 'Falha ao persistir os dados. Por favor contate o suporte.'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            except Exception:
                return Response(
                    {'error': 'Uma falha inesperada aconteceu. Por favor contate o suporte.'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConnectionListCreateAPIView(APIView):

    permission_classes = [AllowAny]

    def get(self, request, format=None):
        count_connections = Connection.objects.count()
        return Response({'total': count_connections}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ConnectionSerializer(data=request.data)

        if serializer.is_valid():
            Connection.objects.create(
                proffy_user=ProffyUser(id=request.data['proffy_user']))
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
