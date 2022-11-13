package org.payment.service;

import java.util.ArrayList;
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

@Service
@RequiredArgsConstructor
public class PaymentService {
    @Autowired
    private PaymentRepository paymentRepository;

    @Transactional
    public Long save(final PaymentRequestDTO params) {
        Payment entity = (Payment)this.paymentRepository.save(params.toEntity());
        return entity.getId();
    }

    @Transactional
    public List<PaymentRequestDTO> findAll() {
        List<Payment> paymentList = paymentRepository.findAll();
        List<PaymentRequestDTO> paymentRequestDTOList = new ArrayList<>();

        for (Payment payment : paymentList){
            PaymentRequestDTO paymentRequestDTO = PaymentRequestDTO.builder()
                    .price(payment.getPrice())
                    .subscription_date(payment.getSubscription_date())
                    .expiration_date(payment.getExpiration_date())
                    .payment_due(payment.getPayment_due())
                    .consumerId(payment.getConsumerId())
                    .sellerId(payment.getSellerId())
                    .build();
            paymentRequestDTOList.add(paymentRequestDTO);
        }
        return paymentRequestDTOList;
    }

    @Transactional
    public List<PaymentResponseDTO> findByConsumerId(Long consumerId) {
        List<Payment> list = this.paymentRepository.findAllByConsumerId(consumerId);
        return list.stream().map(PaymentResponseDTO::new).collect(Collectors.toList());
    }

    @Transactional
    public List<PaymentResponseDTO> findBySellerId(Long sellerId) {
        List<Payment> list = this.paymentRepository.findAllBySellerId(sellerId);
        return list.stream().map(PaymentResponseDTO::new).collect(Collectors.toList());
    }

}
