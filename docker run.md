

# Docker run 환경 설정

# 사용자 1

### mysql Run

mysql : 172.17.0.2

```
docker run -d -p 3306:3306 --name restapimysql -e "MYSQL_ROOT_PASSWORD=mysql" -e "MYSQL_DATABASE=csv2sql" -e "MYSQL_USER=user" -e "MYSQL_PASSWORD=user" mysql:5.7 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```

- mysql의 포트번호가 바뀌어야한다.

### RestApi Run

```
docker build --tag=dlrjsapdlf622/restapi --force-rm=true .
```



[volume mount1](https://jungwoon.github.io/docker/2019/01/13/Docker-3/)

[volume mount2]([https://woonizzooni.tistory.com/entry/Docker-mysql-%EC%84%A4%EC%B9%98-DB%EC%83%9D%EC%84%B1-%ED%85%8C%EC%9D%B4%EB%B8%94%EC%83%9D%EC%84%B1-%EC%98%88%EC%8B%9C](https://woonizzooni.tistory.com/entry/Docker-mysql-설치-DB생성-테이블생성-예시))

```
docker run -d -e "server.port=40000" -p 40000:40000 -e "spring.datasource.url=jdbc:mysql://172.17.0.2:3306/csv2sql?serverTimezone=Asia/Seoul" -e "spring.datasource.drvier-class-name=com.mysql.cj.jdbc.Driver" -e "spring.datasource.username=user" -e "spring.datasource.password=user" -v "C:\Users\HPE\shared folder:/var/lib/restapi/" dlrjsapdlf622/restapi
```

- **mysql**의 **docker ip**, **port**가 사용자 별로 바뀌어야한다.









# 사용자 2

```
docker run -d -p 3308:3306 -e "MYSQL_ROOT_PASSWORD=mysql" -e "MYSQL_DATABASE=csv2sql" -e "MYSQL_USER=user1" -e "MYSQL_PASSWORD=user1" mysql:5.7 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```



```
docker build --tag=dlrjsapdlf622/user1 --force-rm=true .
```



```
docker run -d -e "server.port=40001" -p 40001:40001 -e "spring.datasource.url=jdbc:mysql://172.17.0.5:3308/csv2sql?serverTimezone=Asia/Seoul" -e "spring.datasource.drvier-class-name=com.mysql.cj.jdbc.Driver" -e "spring.datasource.username=user1" -e "spring.datasource.password=user1" -v "C:\Users\HPE\shared folder\user1:/var/lib/user1/" dlrjsapdlf622/user1
```





