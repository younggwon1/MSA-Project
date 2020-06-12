####  1. PersistentVolume

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: dev-pv
spec:
  capacity:
    storage: 2Gi
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  storageClassName: manual
  persistentVolumeReclaimPolicy: Delete
  hostPath:
    path: /tmp/apiserver
```



#### 2. PersistentVolumeClaim

```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: dev-pvc
spec:
  accessModes:
  - ReadWriteOnce
  volumeMode: Filesystem
  resources:
    requests:
      storage: 2Gi
  storageClassName: manual
```



#### 3. Deployment

```yaml
apiVersion: v1
kind: Service
metadata:
  name: apiserverservice
spec:
  type: LoadBalancer
  ports:
  - port: 10004
    targetPort: 10004
  selector:
    app: test-deployment
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: test-deployment
  labels:
    app: test-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: test-deployment
  template:
    metadata:
      labels:
        app: test-deployment
    spec:
      containers:
      - name: test-deployment
        image: whdvlf94/api-server-h2-linux
        ports:
        - containerPort: 10004
        volumeMounts:
        - mountPath: "/var/lib/h2db"
          name: dev-volume
      volumes:
      - name: dev-volume
        persistentVolumeClaim:
          claimName: dev-pvc
```

