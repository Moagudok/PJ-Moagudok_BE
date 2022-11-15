package org.payment.controller;

import java.time.LocalDate;
import java.util.Date;
import java.util.List;

import lombok.RequiredArgsConstructor;
import org.payment.DTO.PaymentRequestDTO;
import org.payment.DTO.PaymentResponseDTO;
import org.payment.entity.Payment;
import org.payment.service.PaymentService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

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
    @GetMapping("/consumer/{consumerId}")
    public ResponseEntity<List<Payment>> findByConsumerId(@PathVariable Long consumerId) {
        return ResponseEntity.ok(paymentService.findByConsumerId(consumerId));
    }
    // 판매자 결제 내역 조회
    @GetMapping("/seller/{sellerId}")
    public ResponseEntity<List<Payment>> findBySellerId(@PathVariable Long sellerId){
        return ResponseEntity.ok(paymentService.findBySellerId(sellerId));
    }
    // 소비자의 구독중인 상품
    @GetMapping("/consumer/{consumerId}/sub")
    public ResponseEntity<List<Payment>> findByConsumerIdAndExpirationDateGreaterThan(@PathVariable Long consumerId){
        return ResponseEntity.ok(paymentService.findByConsumerIdAndExpirationDateGreaterThan(consumerId, LocalDate.now()));
    }
    // 소비자의 오늘 만료되는 구독상품
    @GetMapping("/consumer/{consumerId}/now")
    public ResponseEntity<List<Payment>> findByConsumerIdAndExpirationDateIs(@PathVariable Long consumerId){
        return ResponseEntity.ok(paymentService.findByConsumerIdAndExpirationDateIs(consumerId, LocalDate.now()));
    }
    // 소비자의 만료된 구독상품들
    @GetMapping("/consumer/{consumerId}/exp")
    public ResponseEntity<List<Payment>> findByConsumerIdAndExpirationDateLessThan(@PathVariable Long consumerId){
        return ResponseEntity.ok(paymentService.findByConsumerIdAndExpirationDateLessThan(consumerId, LocalDate.now()));
    }
    // 소비자의 상품중 만료가 7일 전인 상품들

}
