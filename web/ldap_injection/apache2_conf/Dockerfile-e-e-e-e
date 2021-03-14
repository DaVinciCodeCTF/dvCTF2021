FROM httpd:alpine

COPY ./httpd.conf /usr/local/apache2/conf/

RUN mkdir -p /var/www/dvctf_challenge/ \
    && chown -R www-data:www-data "/var/www/dvctf_challenge/"
