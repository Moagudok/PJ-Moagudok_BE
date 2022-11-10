package org.payment.entity;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.time.LocalDate;
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
    private LocalDate subscription_date;
    private LocalDate expiration_date;
    private String payment_due;
    private Long consumerId;
    private Long sellerId;

    @Builder
    public Payment(Integer price,
                   LocalDate subscription_date,
                   LocalDate expiration_date,
                   String payment_due,
                   Long consumerId,
                   Long sellerId) {
        this.price = price;
        this.subscription_date = subscription_date;
        this.expiration_date = expiration_date;
        this.payment_due = payment_due;
        this.consumerId = consumerId;
        this.sellerId = sellerId;
    }



}
