FROM gcc
WORKDIR /usr/src/c_app
COPY hello.c /usr/src/c_app/
COPY hello2.c /usr/src/c_app/

RUN gcc "/usr/src/c_app/hello2.c"
CMD [ "/usr/src/c_app/a.out" ]