package org.payment.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.http.HttpMethod;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")
                .allowedOrigins("http://0.0.0.0:8000")
                .allowedOrigins("http://0.0.0.0:8001")
                .allowedOrigins("http://0.0.0.0:8002")
                .allowedOrigins("http://0.0.0.0:8003")
                .allowedMethods(HttpMethod.GET.name());
    }
}