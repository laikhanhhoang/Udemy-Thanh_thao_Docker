# Thành Thạo Docker Từ Cơ Bản Đến Nâng Cao

- [Section 02](#section-02)
- [Section 03](#section-03)
-

## Section 02

<p align="center">
    Tổng quan về Docker
</p>

- Docker là một nền tảng mã nguồn mở dùng để phát triển, đóng gói, và chạy các ứng dụng trong những môi trường cách ly gọi là container.

    <details>
    <summary></summary>

    Key concepts:
    - Containerization: Một hình thức ảo hóa nhẹ, dùng để đóng gói ứng dụng cùng với các thư viện/phụ thuộc của nó.
    - Docker Engine: Môi trường chạy (runtime) cho phép bạn build và run các container.
    - Docker Image: Một khuôn mẫu chỉ đọc (read-only) dùng để tạo ra container.
    - Docker Container: Một instance có thể chạy (runnable instance) của Docker image (đã chứa đầy đủ code và thư viện, sẵn sàng chạy).
    - Docker Hub: Một registry trên nền tảng đám mây dùng để lưu trữ và chia sẻ Docker image.

    - Ví dụ:

        ```
        - Dockerfile 	    = tờ giấy hướng dẫn cho đầu bếp
        - Docker Image 	    = kho nguyên liệu + nồi nước dùng đã nấu xong
        - Docker (Engine)   = hệ thống bếp + đầu bếp (Đọc Dockerfile - Nấu ra image - Dùng image để bưng phở)
        - Container 	    = tô phở đang được bưng ra bàn 
        ```

- Why Docker?

    <details>
    <summary></summary>

    - Giải quyết vấn đề chạy được trên máy mình, mà không chạy được trên máy đồng nghiệp.
    - Benefits of Docker:
        - Consistency: Chạy được trên các môi trường khác nhau.
        - Efficiency: Nhẹ, so với VM.
        - Isolation: Không bị xung đột giữa các containers với nhau.
        - Portability: Hoạt động trên mọi platform support Docker, kể cả không trùng OS.
        - Scalability: Scale ngang bằng cách deploy nhiều containers giống nhau.
        - Versioning: Support việc version các image, dễ dàng update và rollback.

- VMs and Docker Containers

    <details>
    <summary></summary>

    <p align="center">
        <img src="note_imgs/vms_con.jpg" width="500" />
    </p>

    <div align="center">

    | Virtual Machines (VMs) | Containers |
    |------------------------|------------|
    | Nặng (bao gồm toàn bộ hệ điều hành) | Nhẹ (chia sẻ hệ điều hành host) |
    | Khởi động chậm | Khởi động trong vài giây |
    | Sử dụng nhiều tài nguyên | Sử dụng tài nguyên tối thiểu |
    | Phù hợp khi bảo mật là ưu tiên hàng đầu | Phù hợp khi tốc độ là ưu tiên |

    </div>

    VMs có môi trường độc lập nên khó bị tấn công hơn. Trong khi đó Containers dựa trên Host OS do đó nếu Host OS bị tấn công, các containers vẫn có thể gặp nhiều rủi ro.


## Section 03

<p align="center">
    Cài đặt Docker và môi trường 
</p>

## Section 04

<p align="center">
    Kiến trúc Docker
</p>

- Các khái niệm chính

    <details>
    <summary></summary>

    - Docker Engine: runtime core giúp build, run và quản lý containers.
        <p align="center">
            Docker Engine = Docker Daemon + Docker CLI + API
        </p>

        - Docker CLI: Giao diện command-line (thường là terminal) để giao tiếp với Docker.
        - Docker CLI và Docker Daemon giao tiếp thông qua API.
        - Docker Daemon (dockered): Background service dùng để quản lý Docker containers, images, networks và volumes.
        - Docker Images: Read-only Templates gồm chồng (stack) các    
        filesystem layer bất biến (immutable) dùng để tạo container.
        - Docker Containers: Các instance của images - nhẹ và có thể chạy được.
        - Dockerfile: Một file text hướng dẫn build một Docker Image.
        - Docker Hub/ Docker Registry: Một kho lưu và chia sẻ Docker Images.
        - Docker Compose: Một tool dùng để định nghĩa và chạy ứng dụng nhiều containers sử dụng một file YAML.
        - Docker Volumes: Phương pháp lưu trữ lâu dài cho các containers.
        - Docker Networks: Quản lí giao tiếp giữa các containers và với thế giới bên ngoài.

- Kiến trúc Docker

    <details>
    <summary></summary>
    
    <p align="center">
        <img src="note_imgs/docker_arch.png" width="400" />
    </p>

    - Docker CLI:
        - Thường sẽ làm việc qua CLI (comman line interface)
        - User nhập lệnh qua CLI
        - Lệnh được chuyển thành request gửi đến Docker Daemon và đợi phản hồi.

    - Docker host: là máy (vật lý hoặc ảo) mà Docker Daemon đang chạy trên đó.

        Ví dụ: Chạy lệnh "docker run ..."
        - Nhận yêu cầu từ CLI.
        - Kiểm tra xem image có sẵn chưa.
        - Nếu chưa có thì pull từ Registry về rồi khởi tạo container.
        - Nếu có rồi thì khởi tạo Container luôn.
        - Gửi trả thông tin về CLI.

    - Docker Registry: Nơi lưu trữ và chia sẻ Docker Images, cho phép push sau khi build và pull về để chạy container.

        



