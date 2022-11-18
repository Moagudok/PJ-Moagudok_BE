package org.payment.controller;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import lombok.RequiredArgsConstructor;
import net.bytebuddy.asm.Advice;
import org.payment.DTO.PaymentRequestDTO;
import org.payment.DTO.PaymentResponseDTO;
import org.payment.entity.Payment;
import org.payment.service.PaymentService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

@RestController
@RequestMapping({"/payment"})
@RequiredArgsConstructor
public class PaymentApiController {
    private final PaymentService paymentService;

    // 결제 내역 생성
    @PostMapping
    public ResponseEntity<Long> save(@RequestBody final PaymentRequestDTO params) {
        return ResponseEntity.ok(paymentService.save(params));
    }
    // 전체 결제 내역 조회
    @GetMapping
    public ResponseEntity<List<Payment>> findAll() {
        return ResponseEntity.ok(paymentService.findAll());
    }
    // 소비자 결제 내역 조회
    @GetMapping("/consumer")
    public ResponseEntity<List<Payment>> findByConsumerId(@RequestParam Long consumerId) {
        return ResponseEntity.ok(paymentService.findByConsumerId(consumerId));
    }
    // 판매자 결제 내역 조회
    @GetMapping("/seller/")
    public ResponseEntity<List<Payment>> findBySellerId(@RequestParam Long sellerId){
        return ResponseEntity.ok(paymentService.findBySellerId(sellerId));
    }
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
                List<Payment> resultList = paymentService.exp_7ago(consumerId, LocalDate.now().plusDays(1), LocalDate.now().plusWeeks(1));
                List<Long> productList = new ArrayList<>();
                for (Payment payment : resultList) {
                    productList.add(payment.getProductId());
                }
                return productList;
            }
        }
    }

}
