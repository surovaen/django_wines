from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class BaseUserView(GenericAPIView):
    """Базовый класс вью работы с пользователем."""

    permission_classes = tuple()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
