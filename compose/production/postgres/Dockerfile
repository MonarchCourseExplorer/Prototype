FROM postgres:15

COPY ./compose/production/postgres/maintenance /usr/local/bin/maintenance
COPY ./scrapers /home
RUN chmod +x /usr/local/bin/maintenance/*
RUN mv /usr/local/bin/maintenance/* /usr/local/bin \
    && rmdir /usr/local/bin/maintenance
RUN apt update -y
RUN apt install firefox-esr -y
RUN apt install python3-pip -y 
RUN apt install python3-bs4 -y 
RUN apt install python3-selenium -y
RUN apt install python3-requests -y
