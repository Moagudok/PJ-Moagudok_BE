package org.payment.DTO;

import java.util.Date;
import org.payment.entity.Payment;

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

    public Long getId() {
        return this.id;
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
}
