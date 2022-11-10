FROM openjdk:8-jdk-alpine
COPY build/libs/*.jar dockerservice.jar
ENTRYPOINT ["java","-jar","/dockerservice.jar"]