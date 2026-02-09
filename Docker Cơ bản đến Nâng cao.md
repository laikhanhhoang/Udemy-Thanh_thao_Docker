# Thành Thạo Docker Từ Cơ Bản Đến Nâng Cao

- [Section 01](#section-01)
- [Section 02](#section-02)

## Section 01

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


## Section 02

