# prototype-v1.2
The web service uses an image that’s built from the Dockerfile in the current directory. It then binds the container and the host machine to the exposed port, 8000. This example service uses the default port for the Flask web server, 5000. The redis service uses a public Redis image pulled from the Docker Hub registry.

##Build and run your app with Compose
Compose pulls a Redis image, builds an image for your code, and starts the services you defined. In this case, the code is statically copied into the image at build time.

Enter http://localhost:8000/ in a browser to see the application running.

If you’re using Docker natively on Linux, Docker Desktop for Mac, or Docker Desktop for Windows, then the web app should now be listening on port 8000 on your Docker daemon host. Point your web browser to http://localhost:8000 to find the Hello World message. If this doesn’t resolve, you can also try http://127.0.0.1:8000.
