FROM openjdk:8-jdk-alpine
COPY target/csvtosql-0.1.jar apiServerWindows.jar
VOLUME /tmp
CMD ["java", "-jar", "apiServerWindows.jar"]