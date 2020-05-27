FROM nginx:1.18.0-alpine

RUN cd /etc/apk/keys && wget http://alpine.adiscon.com/rsyslog@lists.adiscon.com-5a55e598.rsa.pub \
    && echo 'http://alpine.adiscon.com/3.7/stable' >> /etc/apk/repositories \
    && apk update && apk add rsyslog

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d

