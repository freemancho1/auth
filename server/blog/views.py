from django.core import serializers
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Post


@api_view(['GET'])
@permission_classes((IsAuthenticated,))                 # 권한 확인 클래스 지정(인증여부 확인)
@authentication_classes((JWTAuthentication,))           # 인증 클래스 지정(JWT 지정)
def posts(request):
    posts = Post.objects \
                .filter(published_at__isnull=False) \
                .order_by('-published_at')
    context = serializers.serialize('json', posts)
    return HttpResponse(context, content_type='text/json-comment-filtered')
    