FROM openjdk:8-jdk-alpine
COPY gradlew .
COPY gradle gradle
COPY build.gradle .
COPY settings.gradle . 
COPY src src
RUN dos2unix ./gradlew
RUN chmod +x ./gradlew
RUN ./gradlew bootjar
COPY build/libs/*.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]