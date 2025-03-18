FROM php:8.2-apache

COPY httpd.conf /usr/local/apache2/conf/httpd.conf
COPY html/ /var/www/html

CMD ["apache2ctl", "-D", "FOREGROUND"]
