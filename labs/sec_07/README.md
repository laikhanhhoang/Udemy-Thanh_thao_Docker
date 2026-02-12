## 01 - Build image với Dockerfile - FROM, WORKDIR, COPY, CMD

- Cách chạy:

    ```bash
    cd ....\labs\sec_07\lab_01
    docker build -t myimgname:v1 .
    docker image ls
    ```

- Kết quả:
    <p align="center">
        <img src="lab_01/07_01_image_ls.png" width="500" />
    </p>


## 02 - Build image với Dockerfile - RUN

- Cách chạy:

    ```bash
    cd ....\labs\sec_07\lab_02
    docker build -t demo_run:v1 .
    docker run demo_run:v1
    ```

## 03 - So sánh Docker instructions CMD và ENTRYPOINT
- CMD:
    - Chạy lệnh:
        ```bash
        cd ....\labs\sec_07\lab_03
        docker build -t myimage:v1 .
        docker run myimage:v1
        docker run myimage:v1 echo "Xin chao moi nguoi"
        ```
    - Kết quả:
        <p align="center">
            <img src="lab_03/07_03_cmd.png" width="500" />
        </p>


- ENTRYPOINT:
    - Chạy lệnh:
        ```bash
        # Chỉnh sang CMD
        cd ....\labs\sec_07\lab_03
        docker build -t myimage:v2 .
        docker run myimage:v2
        docker run myimage:v2 echo "Xin chao moi nguoi"
        docker run -it --entrypoint bash myimage:v2
        exit
        ```
    - Kết quả:
        <p align="center">
            <img src="lab_03/07_03_entrypoint.png" width="500" />
        </p>

    - Nhận xét: Có thể thấy khi override ENTRYPOINT thì nó sẽ được thêm vào đằng sau, do đó ENTRYPOINT SẼ TRỞ THÀNH
    **`["echo", "Hello world from ENTRYPOINT", "echo", "Hello world - override"]`** và cho ra kết quả **"Hello world from ENTRYPOINT echo Hello world - override"**.

# 04 - Tối ưu build Docker image dựa trên layered architecture
- Chạy lệnh:

    ```bash
    docker build -t layer_demo:v1 . # Tốn 20.4s
    docker run layer_demo:v1   

    # Thay đổi lệnh RUN echo
    docker build -t layer_demo:v2 . # Tốn 2.7s
    docker run layer_demo:v2 
    ```

- Kết quả:
        <p align="center">
            <img src="lab_04/07_04_docker_layer.png" width="500" />
        </p>
