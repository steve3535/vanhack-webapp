FROM mysql:5.7
ENV MYSQL_DATABASE=APPDB MYSQL_ROOT_PASSWORD=123456
COPY ./createtable.sql /docker-entrypoint-initdb.d/
EXPOSE 3306
