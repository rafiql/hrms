
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializers import EmployeeSerializer
from .helpers import get_user_details
from rest_framework.response import Response


class UserViewSet(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.create(serializer.validated_data)
            data = {
                'user': get_user_details(user),
            }
            return Response(data, status=200)
        return Response({'detail': str(serializer.errors)}, status=400)
