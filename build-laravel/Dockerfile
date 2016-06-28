FROM ubuntu:trusty

MAINTAINER Sven Dowideit <SvenDowideit@docker.com>

RUN apt-get update && \
	apt-get install -y apache2 php5 curl php5-mcrypt php5-json php5-mysql supervisor && \
	rm -rf /var/lib/apt/lists/* && \
	apt-get clean

ENV APACHE_LOG_DIR /var/log/apache2

RUN rm -f /etc/apache2/apache2.conf && \
	rm -f /etc/apache2/sites-available/* && \
	rm -rf /var/www/html/

ADD 000-default.conf /etc/apache2/sites-available/000-default.conf
ADD apache2.conf /etc/apache2/

RUN /usr/sbin/a2enmod rewrite
RUN /usr/sbin/a2enmod socache_shmcb || true

RUN echo Asia/Taipei > /etc/timezone

RUN /usr/bin/curl -sS https://getcomposer.org/installer | /usr/bin/php
RUN /bin/mv composer.phar /usr/local/bin/composer

RUN mkdir -p /var/log/supervisor && \
	mkdir -p /var/log/apache2

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80

CMD ["/usr/bin/supervisord"]
