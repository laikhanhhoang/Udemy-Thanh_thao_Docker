# Thành Thạo Docker Từ Cơ Bản Đến Nâng Cao

- [Section 02 - Tổng quan về Docker](#section-02)
- [Section 03 - Cài đặt Docker và môi trường](#section-03)
- [Section 04 - Kiến trúc Docker](#section-04)
- [Section 05 - Docker Containers và Commands liên quan](#section-05)

## Section 02

<p align="center">
    Tổng quan về Docker
</p>

- Docker là một nền tảng mã nguồn mở dùng để phát triển, đóng gói, và chạy các ứng dụng trong những môi trường cách ly gọi là container.

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

    - Giải quyết vấn đề chạy được trên máy mình, mà không chạy được trên máy đồng nghiệp.
    - Benefits of Docker:
        - Consistency: Chạy được trên các môi trường khác nhau.
        - Efficiency: Nhẹ, so với VM.
        - Isolation: Không bị xung đột giữa các containers với nhau.
        - Portability: Hoạt động trên mọi platform support Docker, kể cả không trùng OS.
        - Scalability: Scale ngang bằng cách deploy nhiều containers giống nhau.
        - Versioning: Support việc version các image, dễ dàng update và rollback.

- VMs and Docker Containers

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

    - Docker Engine: runtime core giúp build, run và quản lý containers.
        <p align="center">
            Docker Engine = Docker Daemon + Docker CLI + API
        </p>

        - Docker CLI: Giao diện command-line (thường là terminal) để giao tiếp với Docker.
        - Docker CLI và Docker Daemon giao tiếp thông qua API.
        - Docker Daemon (dockered): Background service dùng để quản lý Docker containers, images, networks và volumes.
        - Docker Images: Read-only Templates gồm chồng (stack) các filesystem layer bất biến (immutable) dùng để tạo container.
        - Docker Containers: Các instance của images - nhẹ và có thể chạy được.
        - Dockerfile: Một file text hướng dẫn build một Docker Image.
        - Docker Hub/ Docker Registry: Một kho lưu và chia sẻ Docker Images.
        - Docker Compose: Một tool dùng để định nghĩa và chạy ứng dụng nhiều containers sử dụng một file YAML.
        - Docker Volumes: Phương pháp lưu trữ lâu dài cho các containers.
        - Docker Networks: Quản lí giao tiếp giữa các containers và với thế giới bên ngoài.

- Kiến trúc Docker

    <p align="center">
        <img src="note_imgs/docker_arch.png" width="550" />
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

## Section 05

<p align="center">
    Docker Commands và Containers
</p>

- Docker Container:

    - Docker Image là bản đóng gói bất biến gồm:
        - Code ứng dụng
        - Thư viện / dependencies
        - Runtime (Python, Node, Java…)
        - Cấu hình hệ thống cần thiết (OS layer, env, v.v.)

    - Docker Container là instance đang chạy của image.
    - Từ một image, có thể tạo nhiều container.
    - Để chạy một container từ container:
    
        ```
        docker run <image_name>
        docker run --name <container_name> <image_name>
        ```

        <details>
        <summary> Demo Docker container - hello-world </summary>

        - Chạy câu lệnh "demo run hello-world"

        <p align="center">
            <img src="note_imgs/docker_demo_hello_world.png" width="400" />
        </p>

        - Có thể thấy: Daemon không tìm thấy container trong Registry nên tìm kiếm trên Docker Hub.

        
        </details>

        <details>
        <summary> Demo Docker container - ubuntu </summary>

        - Chạy câu lệnh "demo run -it ubuntu bash"
            - **`-it`**: **`-i`**(interactive) cho phép gõ lệnh vào container và **`-t`** (tty) cho phép bạn thực hiện một số quyền khác (prompt đẹp, Ctrl+C, Clear screen và history,...)
            - **`-bash`**: override CMD, chạy bash

        <p align="center">
            <img src="note_imgs/docker_run_ubuntu.png" width="400" />
        </p>

        - Có thể thấy: Ta có thể thực hiện trực tiếp các câu lệnh như terminal.
        </details>

<br>

- Commands với Docker Container:

    |Lệnh|Hành động|
    |--------------|---------|
    |docker start <container_id_or_name>|**Chạy** container đã bị dừng, còn nếu container đang chạy thì sẽ không làm gì.|
    |docker restart <container_id_or_name>|**Khởi động** container khi nó đã dừng, còn nếu container đang chạy thì sẽ dừng rồi restart container. <br> Thường dùng khi Docker gặp lỗi không nhận GPUs.|
    |docker run -d <image_name>|**Chạy container** ở background|
    |docker run -it <image_name> /bin/bash <br> (hoặc bash)|**Chạy container** và thao tác với nó <br> **`-it`** là kết hợp của -i (interactive) và -t (psuedu-TTY), cho phép tương tác với container thông qua terminal, <br> thiếu một trong hai cái thì output sẽ không được định dạng hoặc chúng ta không tương tác được.|
    |docker exec -it <container_id_or_name> <command>|**Thực thi command** trong một container đang chạy (thường được sử dụng trong detached mode). <br> Xem thêm ở **Ghi chú**. <span style="color:red;"><strong>QUAN TRỌNG</strong></span> |
    |docker stop <container_id_or_name>|**Dừng** container.|
    |docker run -p <host_port>:<container_port> <image_name>|**Map cổng** của container tới cổng của máy host. <br> Xem thêm ở **Ghi chú**.|
    |docker ps|**Liệt kê** các docker đang chạy.|
    |docker ps -a|**Liệt kê** tất cả các docker đã sử dụng.|
    |docker inspect <container_id_or_name>|**Trả về** một file JSON lớn chứa metadata về container.|
    |docker logs <container_id_or_name>|**Xem** container **logs** (xem log** của container đến thời điểm hiện tại).|
    |docker logs -f <container_id_or_name>|**Theo dõi** container **log real-time** (xem log được update liên tục khi container đang chạy khi muốn monitor real-time).|
    |docker rm <container_id_or_name>|**Xóa** một container đã **không còn chạy** nữa.|
    |docker rm -f <container_id_or_name>|**Xóa** một container **đang chạy** (vì container vẫn running nên phải thêm option -f (force)).|
    |docker container prune|**Xóa** các container **đã dừng** (thêm "-f" sau "prune" để tự động đồng ý mà không cần xác nhận).|


    Labs: [Link](labs/sec_05/)

    <details>
    <summary><strong>Ghi chú</strong></summary>

    <ul>
        <li>
        Xem ví dụ về <strong>Port Mapping</strong> ở
        <a href="labs/sec_05/README.md/#port-mapping">đây</a>.
        </li>
        <li>
        <strong>Log của container</strong> là toàn bộ những gì ứng dụng bên trong container
        ghi ra <code>stdout</code> và <code>stderr</code> trong quá trình chạy.
        Docker không tự tạo log riêng, mà chỉ thu lại output của tiến trình chính
        trong container.
        <br>
        <em>Ví dụ:</em> bạn chạy một container Django, khi có request
        <code>/login</code>, Django in ra dòng như
        <code>POST /login 200</code>; hoặc khi lỗi, Python in traceback ra terminal.
        Tất cả những dòng đó được Docker gom lại và bạn xem bằng lệnh
        <code>docker logs &lt;container_name&gt;</code>.
        </li>
    </ul>

    </details>

<br>

- Restart Policy
    - Các option của Restart Policy:

        |Option|Chức năng|
        |------|---------|
        |**no**|Test, Dev bình thường <br> Mặc định khi không thêm flag --restart. <br> Container không tự khởi động lại|
        |**always**|Task rất quan trọng. <br> Container luôn khởi động lại khi dừng. <br> Nếu chúng ta chủ động dừng container qua lệnh **`docker stop`** thì container khởi động lại khi Docker Daemon khởi động lại.|
        |**on-failure[:max-retries]**|Chỉ khởi động lại khi container thoát với lỗi exit code # 0. <br> Có thể giới hạn số lần retry. <br> Nếu chúng ta chủ động dừng container qua lệnh **`docker stop`** thì container **không tự khởi động lại** khi Docker Daemon khởi động lại.|
        |**unless-stopped**|Giống **always** nhưng **không tự khởi động lại** nếu chủ động dừng container qua lệnh **`docker stop`**|

<br><br>

<p align="center">
    <img src="note_imgs/05_recap_con.png" width="600" />
</p>
