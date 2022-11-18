package org.payment.service;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.stream.Collectors;
import javax.transaction.Transactional;

import lombok.RequiredArgsConstructor;
import org.payment.DTO.PaymentRequestDTO;
import org.payment.DTO.PaymentResponseDTO;
import org.payment.entity.Payment;
import org.payment.entity.PaymentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.data.domain.Sort.Direction;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.client.RestTemplate;

@Service
@RequiredArgsConstructor
public class PaymentService {
    private final PaymentRepository paymentRepository;

    @Transactional
    public Long save(PaymentRequestDTO params) {
        return paymentRepository.save(params.toEntity()).getId();
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
