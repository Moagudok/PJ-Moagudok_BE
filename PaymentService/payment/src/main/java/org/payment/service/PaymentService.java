package org.payment.service;

import java.util.List;
import java.util.stream.Collectors;
import javax.transaction.Transactional;

import lombok.RequiredArgsConstructor;
import org.payment.DTO.PaymentRequestDTO;
import org.payment.DTO.PaymentResponseDTO;
import org.payment.entity.Payment;
import org.payment.entity.PaymentRepository;
import org.springframework.data.domain.Sort;
import org.springframework.data.domain.Sort.Direction;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class PaymentService {
    private final PaymentRepository paymentRepository;

    @Transactional
    public Long save(final PaymentRequestDTO params) {
        Payment entity = (Payment)this.paymentRepository.save(params.toEntity());
        return entity.getId();
    }

    public List<PaymentResponseDTO> findAll() {
        Sort sort = Sort.by(Direction.DESC, "id");
        List<Payment> list = this.paymentRepository.findAll(sort);
        return list.stream().map(PaymentResponseDTO::new).collect(Collectors.toList());
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
