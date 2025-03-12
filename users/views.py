from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
User = get_user_model()


@api_view(['POST'])
def register(request):
    name = request.data.get('name')  
    email = request.data.get('email')
    password = request.data.get('password')

    if not name or not email or not password:
        return Response({"error": "All fields (name, email, password) are required"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email=email).exists():
        return Response({"error": "Email already registered"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create(
        username=name,  
        email=email,
        password=make_password(password)
        
    )

    return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)




@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = User.objects.filter(email=email).first()

    if user and user.check_password(password):
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_200_OK)

    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)