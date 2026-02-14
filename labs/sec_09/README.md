## 01 - Host Network

```bash
CHỈ CHẠY ĐƯỢC TRÊN UBUNTU


cd ....\labs\sec_09\lab_01

docker run --name con1 --network host myapp:v1

docker run --name con2 --network host myapp:v1
# Sẽ bị lỗi port conflict (error while trying to bind on address)

docker docker run --name con3 --network host myapp:v1 uvicorn main:app --host 0.0.0.0 --port 700 
# Chạy ổn
```

## 02 - Default Bridge Network

```bash
BASH 1

docker run -it --name ubun2 ubuntu:latest bash
apt-get update
apt-get install -y iputils-ping
ping {ubun2_IP_ADDRESS}
```

```bash
BASH 1
```

```bash
BASH 2

docker run -it --name ubun2 ubuntu:latest bash
apt-get update
apt-get install -y iputils-ping
```

```bash
BASH 3

docker ps -a
docker inspect {UBUN2_Id}
# Lấy ubun2 Ip Adrress trong Bridge Network
```