package org.payment.DTO;

import java.time.LocalDate;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.payment.entity.Payment;

import javax.persistence.Table;

@Getter
@NoArgsConstructor
public class PaymentRequestDTO {
    private Long productId;
    private Integer price;
    private LocalDate subscriptionDate;
    private LocalDate expirationDate;
    private LocalDate paymentDueDate;
    private Long consumerId;
    private Long sellerId;

    public Payment toEntity() {
        return Payment.builder()
                .productId(this.productId)
                .price(this.price)
                .subscriptionDate(this.subscriptionDate)
                .expirationDate(this.expirationDate)
                .paymentDueDate(this.paymentDueDate)
                .consumerId(this.consumerId)
                .sellerId(this.sellerId)
                .build();
    }
    @Builder
    public PaymentRequestDTO(
                   Long productId,
                   Integer price,
                   LocalDate subscriptionDate,
                   LocalDate expirationDate,
                   LocalDate paymentDueDate,
                   Long consumerId,
                   Long sellerId) {
        this.productId = productId;
        this.price = price;
        this.subscriptionDate = subscriptionDate;
        this.expirationDate = expirationDate;
        this.paymentDueDate = paymentDueDate;
        this.consumerId = consumerId;
        this.sellerId = sellerId;
    }
}
