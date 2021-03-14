FROM php:7-fpm-alpine

RUN apk add --no-cache --virtual .persistent-deps libldap
RUN apk update && \
         apk add --no-cache --virtual .build-deps $PHPIZE_DEPS openldap-dev && \
         docker-php-ext-install ldap && \
         apk del .build-deps



