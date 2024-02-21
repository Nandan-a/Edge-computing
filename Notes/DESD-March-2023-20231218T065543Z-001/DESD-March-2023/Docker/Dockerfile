FROM gcc:latest
LABEL organization="cdac"
WORKDIR /usr/docker/c-programming
COPY HelloWorld.c .
RUN gcc -o HelloWorld HelloWorld.c
CMD ["./HelloWorld"]
