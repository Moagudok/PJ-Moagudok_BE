package org.payment.DTO;

import java.util.Date;

import lombok.Getter;
import org.payment.entity.Payment;
@Getter
public class PaymentResponseDTO {
    private Long id;
    private Integer price;
    private Date subscription_date;
    private Date expiration_date;
    private Date payment_due;
    private Long consumerId;
    private Long sellerId;

    public PaymentResponseDTO(Payment entity) {
        this.id = entity.getId();
        this.price = entity.getPrice();
        this.subscription_date = entity.getSubscription_date();
        this.expiration_date = entity.getExpiration_date();
        this.payment_due = entity.getPayment_due();
        this.consumerId = entity.getConsumerId();
        this.sellerId = entity.getSellerId();
    }

}
