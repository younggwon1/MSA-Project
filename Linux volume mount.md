# User1

## h2db volume mount

####  1. PersistentVolume

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: h2db-pv
spec:
  capacity:
    storage: 2Gi
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  storageClassName: h2db
  persistentVolumeReclaimPolicy: Delete
  hostPath:
    path: /var/lib/h2dbmount
```



#### 2. PersistentVolumeClaim

```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: h2db-pvc
spec:
  accessModes:
  - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 2Gi
  storageClassName: h2db
```



## upload_data volume mount

#### 1. PersistentVolume

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: upload-pv
spec:
  capacity:
    storage: 2Gi
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  storageClassName: shared
  persistentVolumeReclaimPolicy: Delete
  hostPath:
    path: /var/lib/shared_data_mount
```



#### 2. PersistentVolumeClaim

```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: upload-pvc
spec:
  accessModes:
  - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 2Gi
  storageClassName: shared
```



#### 3. Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: apiserver-deployment
  labels:
    app: apiserver-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: apiserver-deployment
  template:
    metadata:
      labels:
        app: apiserver-deployment
    spec:
      containers:
      - name: apiserver-deployment
        image: whdvlf94/api-server-linux
        ports:
        - containerPort: 10004
        volumeMounts:
        - mountPath: "/var/lib/h2db"
          name: h2-volume
        - mountPath: "/var/lib/shared_data/cyb"
          name: shared-volume
      volumes:
      - name: h2-volume
        persistentVolumeClaim:
          claimName: h2db-pvc
      - name: shared-volume
        persistentVolumeClaim:
          claimName: upload-pvc
```



### 4. Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: apiserverservice
spec:
  clusterIP: 10.96.162.149
  type: NodePort
  selector:
    app: apiserver-deployment
  ports:
      # 기본적으로 그리고 편의상 `targetPort` 는 `port` 필드와 동일한 값으로 설정된다.
    - name: http
      port: 10004
      protocol: TCP
      targetPort: 10004
      # 선택적 필드
      # 기본적으로 그리고 편의상 쿠버네티스 컨트롤 플레인은 포트 범위에서 할당한다(기본값: 30000-32767)
      nodePort: 30007
```



# User2

## h2db volume mount

####  1. PersistentVolume

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: h2db-pv-1
spec:
  capacity:
    storage: 2Gi
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  storageClassName: h2db
  persistentVolumeReclaimPolicy: Delete
  hostPath:
    path: /var/lib/h2dbmount1
```



#### 2. PersistentVolumeClaim

```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: h2db-pvc1
spec:
  accessModes:
  - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 2Gi
  storageClassName: h2db
```



## upload_data volume mount

#### 1. PersistentVolume

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: upload-pv1
spec:
  capacity:
    storage: 2Gi
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  storageClassName: shared
  persistentVolumeReclaimPolicy: Delete
  hostPath:
    path: /var/lib/shared_data_mount1
```



#### 2. PersistentVolumeClaim

```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: upload-pvc1
spec:
  accessModes:
  - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 2Gi
  storageClassName: shared
```



#### 3. Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: apiserver-deployment1
  labels:
    app: apiserver-deployment1
spec:
  replicas: 1
  selector:
    matchLabels:
      app: apiserver-deployment1
  template:
    metadata:
      labels:
        app: apiserver-deployment1
    spec:
      containers:
      - name: apiserver-deployment1
        image: whdvlf94/api-server-linux
        ports:
        - containerPort: 10004
        volumeMounts:
        - mountPath: "/var/lib/h2db"
          name: h2-volume
        - mountPath: "/var/lib/shared_data/yjp"
          name: shared-volume
      volumes:
      - name: h2-volume
        persistentVolumeClaim:
          claimName: h2db-pvc1
      - name: shared-volume
        persistentVolumeClaim:
          claimName: upload-pvc1
```



### 4. Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: apiserverservice1
spec:
  clusterIP: 10.96.162.150
  type: NodePort
  selector:
    app: apiserver-deployment1
  ports:
      # 기본적으로 그리고 편의상 `targetPort` 는 `port` 필드와 동일한 값으로 설정된다.
    - name: http
      port: 10004
      protocol: TCP
      targetPort: 10004
      # 선택적 필드
      # 기본적으로 그리고 편의상 쿠버네티스 컨트롤 플레인은 포트 범위에서 할당한다(기본값: 30000-32767)
      nodePort: 30008
```

