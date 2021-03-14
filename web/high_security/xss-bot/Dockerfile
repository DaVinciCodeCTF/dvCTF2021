FROM ubuntu

ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y wget build-essential chrpath libssl-dev libxft-dev libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev


COPY . /bot/
WORKDIR /bot/


RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 
RUN tar -xvf ./phantomjs-2.1.1-linux-x86_64.tar.bz2 
RUN chmod +x ./phantomjs-2.1.1-linux-x86_64/bin/phantomjs

RUN adduser bot --disabled-password
USER bot

CMD while sleep 1; do ./phantomjs-2.1.1-linux-x86_64/bin/phantomjs --ignore-ssl-errors=true --local-to-remote-url-access=true --web-security=false --ssl-protocol=any ./bot/xss-bot.js; done;
