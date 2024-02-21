FROM nginx:1.10.1-alpine

LABEL developer="diot2023"

WORKDIR /usr/share/nginx/html

COPY index.html /usr/share/nginx/html/

EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]


#docker build -t mynginnx .
#docker run -it -p 2024:80 mynginnx