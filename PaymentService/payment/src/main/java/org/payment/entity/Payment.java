package org.payment.entity;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.util.Date;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "Payment")
@Getter
@NoArgsConstructor
public class Payment {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private Integer price;
    private Date subscription_date;
    private Date expiration_date;
    private Date payment_due;
    private Long consumerId;
    private Long sellerId;

    @Builder
    public Payment(Integer price, Date subscription_date, Date expiration_date, Date payment_due, Long consumerId, Long sellerId) {
        this.price = price;
        this.subscription_date = subscription_date;
        this.expiration_date = expiration_date;
        this.payment_due = payment_due;
        this.consumerId = consumerId;
        this.sellerId = sellerId;
    }

}
