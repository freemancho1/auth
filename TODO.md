# Todos
#### [reverse]
<br/><br/>

## 2022-04-08(Fri)

### Server 작업 완료
#### config/settings.py
* INSTALLED_APPS에 DRF, SimpleJWT, CORS, MyApp 지정
```python
# Django
'rest_framework',
'rest_framework_simplejwt',

# CORS
'corsheaders',

# Local Apps
'blog',
```
* MIDDLEWARE에 CORS관련 내용 추가
* CORS관련 허용 도메인:포트 지정(http://localhost:8080)
