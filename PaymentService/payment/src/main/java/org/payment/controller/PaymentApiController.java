package org.payment.controller;

import java.util.List;
import org.payment.DTO.PaymentRequestDTO;
import org.payment.DTO.PaymentResponseDTO;
import org.payment.service.PaymentService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping({"/payment"})
public class PaymentApiController {
//    @GetMapping
//    public String home(){
//        return "Hello World";
//    }
    private final PaymentService paymentService;

    public PaymentApiController(final PaymentService paymentService) {
        this.paymentService = paymentService;
    }

    @PostMapping
    public Long save(@RequestBody final PaymentRequestDTO params) {
        return this.paymentService.save(params);
    }

    @GetMapping
    public List<PaymentRequestDTO> findAll() {
        return this.paymentService.findAll();
    }

    @GetMapping({"/consumer/{id}"})
    public List<PaymentResponseDTO> findByConsumer_id(@PathVariable Long id) {
        return this.paymentService.findByConsumerId(id);
    }

    @GetMapping({"/seller/{id}"})
    public List<PaymentResponseDTO> findBySeller_id(@PathVariable Long id) {
        return this.paymentService.findBySellerId(id);
    }


}
