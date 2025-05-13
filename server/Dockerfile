FROM maven:3.8.6-amazoncorretto-17 as build

WORKDIR /pi-ods3

COPY . /pi-ods3

RUN mvn clean package -X -DskipTests

FROM openjdk:17-ea-10-jdk-slim

WORKDIR /pi-ods3

COPY --from=build /pi-ods3/target/*.jar ./spring.jar

ENTRYPOINT ["java", "-jar", "spring.jar"]