FROM openjdk:8-jdk-alpine
COPY target/csvtosql-0.1.jar csvToSql.jar
VOLUME /tmp
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
CMD ["java", "-jar", "csvToSql.jar"]