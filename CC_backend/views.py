from CC_backend.serialization import serializationclass
from CC_backend.models import testdata
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def show(request):
    if request.method == 'GET':
        result = testdata.objects.all()
        serialize = serializationclass(result, many=True)
        return Response(serialize.data)