# aeris-flask-project
1. For Linux, install Docker Engine onto your machine.

https://docs.docker.com/engine/install/

On Windows or Mac, you should install Docker Desktop as well.

https://docs.docker.com/desktop/install/windows-install/

https://docs.docker.com/desktop/install/mac-install/

Open Docker Desktop application to start Docker

Ensure Docker Engine has been installed and running properly by using:
```
docker run hello-world
```

If you get a permission error on Linux, run this
```
sudo docker run hello-world
```

2. Navigate to the root directory of the project.

3. Run the following command to build the Docker container
```
docker build -t aeris-app . 
```
If you get a permission error on Linux, run this
```
sudo docker build -t aeris-app . 
```

4. Run the following command to start the Docker container
```
docker run -p 5001:5001 aeris-app
```
If you get a permission error on Linux, run this
```
sudo docker run -p 5001:5001 aeris-app
```

5. Enter the following urls into a web browser depending on which resource you want to access

Get Mean:
http://127.0.0.1:5001/get-mean

Get Sum:
http://127.0.0.1:5001/get-sum

Get Standard Deviation:
http://127.0.0.1:5001/get-std-deviation

Get Image:
http://127.0.0.1:5001/get-image

You can access the Flask web application from any machine. To do this, find the IP address of your container host machine and enter that into your web browser along with the appropriate port and path. For example, if your container host machine IP address is 192.168.1.7, then the url should be
http://192.168.1.7:5001/get-mean
