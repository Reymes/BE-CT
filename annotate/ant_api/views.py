from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AntDoc
from .serializers import AntDocSerializer


class AntDocApiView(APIView):

    def get(self, request, *args, **kwargs):
        doc = AntDoc.objects.filter()
        serializer = AntDocSerializer(doc, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'document': request.data.get('document'),
        }
        serializer = AntDocSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AntDocDetailApiView(APIView):

    def get_object(self, doc_id):
        try:
            return AntDoc.objects.get(id=doc_id)
        except AntDoc.DoesNotExist:
            return None

    def get(self, request, doc_id, *args, **kwargs):
        doc_instance = self.get_object(doc_id)
        if not doc_instance:
            return Response(
                {"res": "Object with doc id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AntDocSerializer(doc_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, doc_id, *args, **kwargs):
        doc_instance = self.get_object(doc_id)
        if not doc_instance:
            return Response(
                {"res": "Object with doc id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'document': request.data.get('document'),
        }
        serializer = AntDocSerializer(
            instance=doc_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, doc_id, *args, **kwargs):
        doc_instance = self.get_object(doc_id)
        if not doc_instance:
            return Response(
                {"res": "Object with doc id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        doc_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
