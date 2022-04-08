# Todos
#### [reverse]
<br/><br/>

## 2022-04-08(Fri)
<br/>

### 이후 수행할 내용
#### ㅇㅇㅇ
<br/>

### Server 작업
#### config/settings.py
##### * DRF 및 DRF 인증관련 내용 설정
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
