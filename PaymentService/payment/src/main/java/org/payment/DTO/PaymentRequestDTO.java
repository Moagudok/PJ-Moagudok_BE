package org.payment.DTO;

import java.util.Date;
import org.payment.entity.Payment;

public class PaymentRequestDTO {
    private Integer price;
    private Date subscription_date;
    private Date expiration_date;
    private Date payment_due;
    private Long consumerId;
    private Long sellerId;

    public Payment toEntity() {
        return Payment.builder().price(this.price).subscription_date(this.subscription_date).expiration_date(this.expiration_date).payment_due(this.payment_due).consumerId(this.consumerId).sellerId(this.sellerId).build();
    }

    public Integer getPrice() {
        return this.price;
    }

    public Date getSubscription_date() {
        return this.subscription_date;
    }

    public Date getExpiration_date() {
        return this.expiration_date;
    }

    public Date getPayment_due() {
        return this.payment_due;
    }

    public Long getConsumerId() {
        return this.consumerId;
    }

    public Long getSellerId() {
        return this.sellerId;
    }

    public PaymentRequestDTO() {
    }
}
