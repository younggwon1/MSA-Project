### Postman이 아닌 curl을 이용해서 api server 구축하기

#### 1. Post 방식

- ClusterIp (10.96.162.149)

```
curl -d "user=user1&userKey=xyz" -X POST http://10.96.162.149:10004/start
```

- kuber1-server
  
  - 다음 주소를 프론트 쪽에서 보낸다.
    - kuber1-server IP (192.168.56.11)
  
  ```
  http://192.168.56.11:30007/start?user=user1&userKey=xyz
  ```
  
  - Linux 환경에서 curl을 이용한 POST 작업
  
  ```
  curl -d "user=user1&userKey=xyz" -X POST http://192.168.56.11:30007/start
  ```
  
  

#### 2. GET 방식



- ClusterIp (10.96.162.149)

```
curl 10.96.162.149:10004/abcd?key=xyz
```

- kuber1-server
  
  - 다음 주소를 프론트 쪽으로 보낸다.
    - kuber1-server IP (192.168.56.11)
  
  ```
  http://192.168.56.11:30007/abcd?key=xyz
  ```
  
  - Linux 환경에서 curl을 이용한 GET 작업
  
  ```
  curl 192.168.56.11:30007/abcd?key=xyz
  ```
  
  
  
  

#### 문제점

1. **mountPath: "/var/lib/shared_data"**로 설정되어 있다. 이렇게 설정이 되어있으면 shared_data에 있는 데이터를 마운트 시킨다. 하지만 업로드된 파일을 읽을 때는 /var/lib/shared_data/{userid} 밑에 있는 csv 파일을 읽는데  **mountPath: "/var/lib/shared_data"**부분을 사용자별로 배분시켜야하는데 어떻게 해야할까?









