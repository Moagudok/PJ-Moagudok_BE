package org.payment.DTO;

import java.time.LocalDate;

import lombok.Getter;
import lombok.NoArgsConstructor;
import org.payment.entity.Payment;

@Getter
@NoArgsConstructor
public class PaymentRequestDTO {
    private Integer price;
    private LocalDate subscription_date;
    private LocalDate expiration_date;
    private String payment_due;
    private Long consumerId;
    private Long sellerId;

    public Payment toEntity() {
        return Payment.builder()
                .price(this.price)
                .subscription_date(this.subscription_date)
                .expiration_date(this.expiration_date)
                .payment_due(this.payment_due)
                .consumerId(this.consumerId)
                .sellerId(this.sellerId)
                .build();
    }
}
