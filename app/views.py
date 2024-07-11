from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SignupSerializer
from .models import Signup

@api_view(['GET', 'POST'])
def signup(request):
    if request.method == 'GET':
        users = Signup.objects.all()
        serializer = SignupSerializer(users, many = True)
        return Response(serializer.data)
    
    else:
        data = request.data
        serializer = SignupSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User signed up successfully!'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)