FROM nginx:latest


COPY html/ /var/www
COPY default.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY ssl/certs/nginx-selfsigned.crt /etc/ssl/certs/nginx-selfsigned.crt
COPY ssl/private/nginx-selfsigned.key /etc/ssl/private/nginx-selfsigned.key

