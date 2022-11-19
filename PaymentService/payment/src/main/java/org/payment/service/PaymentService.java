package org.payment.service;

import java.time.LocalDate;
import java.util.List;
import javax.transaction.Transactional;

import lombok.RequiredArgsConstructor;
import org.payment.DTO.PaymentRequestDTO;
import org.payment.entity.Payment;
import org.payment.entity.PaymentRepository;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class PaymentService {
    private final PaymentRepository paymentRepository;

    @Transactional
    public Payment save(Payment payment) {
        return paymentRepository.save(payment);
    }
    @Transactional
    public List<Payment> findAll() {
        return paymentRepository.findAll();
    }
    @Transactional
    public List<Payment> findByConsumerId(Long consumerId){
        return paymentRepository.findByConsumerId(consumerId);
    }
    @Transactional
    public List<Payment> findBySellerId(Long sellerId){
        return paymentRepository.findBySellerId(sellerId);
    }
    @Transactional
    public List<Payment> sub_product(Long consumerId, LocalDate localDate){
        return paymentRepository.findByConsumerIdAndExpirationDateGreaterThan(consumerId, localDate);
    }
    @Transactional
    public List<Payment> exp_today(Long consumerId, LocalDate localDate){
        return paymentRepository.findByConsumerIdAndExpirationDateIs(consumerId, localDate);
    }
    @Transactional
    public List<Payment> exp_product(Long consumerId, LocalDate localDate){
        return paymentRepository.findByConsumerIdAndExpirationDateLessThan(consumerId, localDate);
    }
    @Transactional
    public List<Payment> exp_7ago(Long consumerId, LocalDate now, LocalDate ago){
        return paymentRepository.findByConsumerIdAndExpirationDateBetween(consumerId, now, ago);
    }


}
