# Đây là base image sẽ sử dụng để tạo Docker image mới
FROM ubuntu:latest

# WORKDIR - giúp chúng ta thiết lập thư mục làm việc trong môi trường tạo Docker Image
# /app sẽ là thư mục làm việc trong docker container - coi như đứng trong thư mục này
WORKDIR /app

# Thực hiện copy file script.sh từ máy host vào thư mục làm việc trong docker container
COPY script.sh .

# Setup câu lệnh mặc định khi chạy docker container từ docker image được build từ dockerfile này
# nó sẽ chạy bash script.sh
CMD ["bash", "script.sh"]