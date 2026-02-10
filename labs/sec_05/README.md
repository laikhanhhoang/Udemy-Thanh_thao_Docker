## Liệt kê các containers

<p align="center">
    <img src="05_ls_cons.png" width="550" />
    <br>
    <em>Sử dụng <strong><code>docker ps</code></strong> và <strong><code>docker ps -a</code></strong> để liệt kê các containers</em>
</p>

## Xóa các containers

<p align="center">
  <img src="05_del_cons.png" width="550" />
</p>

<p align="center" style="margin-top: 6px; line-height: 1.6;">
  <em>
    Sử dụng <strong><code>docker rm {container_id}</code></strong> và
    <strong><code>docker rm -f {container_id}</code></strong>
    để xóa các containers
  </em>
</p>

## Stop, start, restart Docker Containers

<p align="center">
  <img src="05_stop_start_res_cons.png" width="550" />
</p>

<p align="center" style="margin-top: 6px; line-height: 1.6;">
  <em>
    Sử dụng <strong><code>docker stop</code></strong>,  <strong><code>docker start</code></strong> và
    <strong><code>docker restart</code></strong>
    để sử dụng các containers
  </em>
</p>


## Port mapping 

- Chạy **`docker run -p 8080:80 nginx`**

    <p align="center">
    <img src="05_port_map_cons.png" width="550" />
    </p>
    
    - nginx: là tên image, chạy một webserver mặc định trên cổng 80 bên trong container.
    - -p 8080:80: ánh xạ cổng 8080 trên máy host với cổng 80 trên container.

- Chạy **`http://localhost:8080`**

    <p align="center">
    <img src="05_nginx_web.png" width="400" />
    </p>

## Chạy lệnh trong Docker Container

<p align="center">
  <img src="05_exec_con.jpg" width="550" />
</p>

<p align="center" style="margin-top: 6px; line-height: 1.6;">
    <em>
        Sử dụng <strong><code>docker exec -it <container_id_or_name> <command></code></strong> để chạy lệnh bất kì trong containers.
    </em>
</p>

**Lưu ý:** **`docker run -d -it my_con ubuntu bash`** phải có **`-it`** vì bạn đã override bash là lệnh CMD mặc định trong container, do đó nó cần TTY từ **`-it`** để container không bị hủy.


