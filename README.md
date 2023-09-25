# discoreg

A Django app to manage invites to a Discord server based on conference registrations.

# Building the docker image(s)

Ensure Docker Deskop is running locally and run this command. It will build the image and tag it with the name discoreg. (This will only build the web server)

```
docker build . -t discoreg
```

To build the nextupbot image, point to the specific Dockerfile for it

```
docker build . -t nextupbot -f Dockerfile.nextupbot
```

# Running disoreg with Docker Compose locally after building the images

```
docker-compose up --build
```
