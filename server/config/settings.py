from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f9wak8692%gnx%7ubm!cfww_7r*8^^z!=6+1gc6gu3rf^lw&k1'

# SECURITY WARNING: don't run with debug turned on in production!
# 실 서버에 배포할 경우 False로 수정 필요               # 중요!!!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Django
    'rest_framework',
    'rest_framework_simplejwt',
    
    # CORS
    'corsheaders',
    
    # Local Apps
    'blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',                        # CORS append
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS 가능 URL
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8080',
    'http://127.0.0.1:8080',
]
# CORS_ALLOW_ALL_ORIGINS = True                                       # All Allow(Not recommended)

ROOT_URLCONF = 'config.urls'

## REST & JWT 관련 추가된 설정들. [start]
# REST_FRAMEWORK = {
#     # 기본 권한 확인 클래스 지정
#     'DEFAULT_PERMISSION_CLASSES': (
#         # 로그인 여부로 권한 확인
#         'rest_framework.permissions.IsAuthenticated',
#     ),
#     # 인증(로그인) 클래스
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.BasicAuthentication',
#     ),
# }
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# JWT 관련 설정
JWT_AUTH = {
    # JWT용 secret key: 간단히 장고의 SECRET_KEY를 사용했지만,
    # 운영중에는 별도키(별도 파일의) 이용
    'JWT_SECRET_KEY': SECRET_KEY,
    # JWT 암호화 알고리즘
    'JWT_ALGORITHM': 'HS256',
    # REFRESH token 사용 여부 설정
    'JWT_ALLOW_REFRESH': True,
    # JWT token 소멸 시간 지정: days=7(생성후 7일 지난 후)
    'JWT_EXPIRATION_DELTA': timedelta(days=1),
    # JWT REFRESH token 소멸 시간 지정
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
}

## REST & JWT 관련 추가된 설정들. [end]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
## MySQL(or Mariadb)
## MySQL을 사용하기 위해서는 아래와 같이 mysqlclient를 설치해야 함
## $ pip install mysqlclient
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'DATABASE-NAME',
#         'USER': 'USERNAME',
#         'PASSWORD': '',
#         'HOST': '127.0.0.1',            # 아래 localhost와 미세하게 차이가 있음
#         # 'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'                   

TIME_ZONE = 'Asia/Seoul'
# TIME_ZONE = 'UTC'                         # Default

USE_I18N = True

# True: view관련 모듈(templates, forms)에서만 위 TIME_ZONE을 사용,
# False: view 및 models 등 모든 곳에서 TIME_ZONE을 사용
USE_TZ = False
# USE_TZ = True                             # Default

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
