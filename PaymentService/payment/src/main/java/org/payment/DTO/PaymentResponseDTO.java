package org.payment.DTO;

import java.time.LocalDate;

import lombok.Getter;
import org.payment.entity.Payment;
import org.springframework.format.annotation.DateTimeFormat;

@Getter
public class PaymentResponseDTO {
    private Long id;
    private Long productId;
    private Integer price;
    private LocalDate subscriptionDate;
    private LocalDate expirationDate;
    private String paymentDue;
    private Long consumerId;
    private Long sellerId;

    public PaymentResponseDTO(Payment entity) {
        this.productId = entity.getProductId();
        this.id = entity.getId();
        this.price = entity.getPrice();
        this.subscriptionDate = entity.getSubscriptionDate();
        this.expirationDate = entity.getExpirationDate();
        this.paymentDue = entity.getPaymentDue();
        this.consumerId = entity.getConsumerId();
        this.sellerId = entity.getSellerId();
    }

}
