FROM openjdk:8-jdk-alpine
CMD ["./gradlew","bootJar"]
ARG JAR_FILE=./build/libs/*.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]