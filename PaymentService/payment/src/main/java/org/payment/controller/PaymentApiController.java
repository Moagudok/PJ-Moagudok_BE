package org.payment.controller;

import java.net.URI;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import lombok.RequiredArgsConstructor;
import org.payment.DTO.PaymentRequestDTO;
import org.payment.entity.Payment;
import org.payment.service.PaymentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.reactive.function.BodyInserter;
import org.springframework.web.reactive.function.BodyInserters;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

@RestController
@RequestMapping({"/payment"})
@RequiredArgsConstructor
public class PaymentApiController {
    private final PaymentService paymentService;

    // 결제 내역 생성
    @PostMapping
    public ResponseEntity<?> save(@RequestBody Payment params) {
        Payment payment = paymentService.save(params);
        // webclient
        WebClient webClient = WebClient.create();
        webClient.put()
                .uri("http://52.79.143.145:8001/consumer/product/subscriber")
                .body(BodyInserters.fromFormData("product_id", payment.getProductId().toString()))
                .retrieve()
                .bodyToMono(String.class)
                .block();
        return new ResponseEntity<>("결제 성공",HttpStatus.OK);
    }
//    // PRG pattern
//    @GetMapping("/success")
//    public ResponseEntity<?> success(){
//        return  new ResponseEntity<>("201", HttpStatus.CREATED);
//    }
    // 전체 결제 내역 조회
    @GetMapping
    public ResponseEntity<?> findAll() {
        return ResponseEntity.ok(paymentService.findAll());
    }
    // 소비자 결제 내역 조회
    @GetMapping("/consumer")
    public ResponseEntity<List<Payment>> findByConsumerId(@RequestParam Long consumerId) {
        return ResponseEntity.ok(paymentService.findByConsumerId(consumerId));
    }
    // 판매자 결제 내역 조회
    @GetMapping("/seller")
    public ResponseEntity<List<Payment>> findBySellerId(@RequestParam Long sellerId){
        return ResponseEntity.ok(paymentService.findBySellerId(sellerId));
    }
    // 마이페이지 조회용
    @GetMapping("/consumer/mypage")
    public List<Long> sub_product(@RequestParam Long consumerId, String type){
        switch (type) {
            // 소비자의 구독중인 상품
            default: {
                List<Payment> resultList = paymentService.sub_product(consumerId, LocalDate.now());
                List<Long> productList = new ArrayList<>();
                for (Payment payment : resultList) {
                    productList.add(payment.getProductId());
                }
                return productList;
            }
            // 소비자의 오늘 만료되는 구독상품
            case "now": {
                List<Payment> resultList = paymentService.exp_today(consumerId, LocalDate.now());
                List<Long> productList = new ArrayList<>();
                for (Payment payment : resultList) {
                    productList.add(payment.getProductId());
                }
                return productList;
            }
            // 소비자의 만료된 구독상품들
            case "exp": {
                List<Payment> expList = paymentService.exp_product(consumerId, LocalDate.now());
                List<Long> productList = new ArrayList<>();
                for (Payment payment : expList) {
                    productList.add(payment.getProductId());
                }
                // 증복제거
                List<Long> resultList = productList.stream().distinct().collect(Collectors.toList());
                // 현재 구독중인 상품 리스트 제거
                List<Payment> subList = paymentService.sub_product(consumerId, LocalDate.now());
                for (Payment payment : subList){
                    resultList.remove(payment.getProductId());
                }
                return resultList;
            }
            // 소비자의 상품중 만료가 7일 전인 상품들
            case "7ago": {
                List<Payment> resultList = paymentService.exp_7ago(consumerId, LocalDate.now(), LocalDate.now().plusWeeks(1));
                List<Long> productList = new ArrayList<>();
                for (Payment payment : resultList) {
                    productList.add(payment.getProductId());
                }
                return productList;
            }
        }
    }

}
