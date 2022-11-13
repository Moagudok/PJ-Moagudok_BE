package org.payment.entity;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.time.LocalDate;
import javax.persistence.*;

@Entity
@Table(name = "Payment")
@Getter
@NoArgsConstructor
public class Payment {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @Column
    private Integer price;
    @Column
    private LocalDate subscription_date;
    @Column
    private LocalDate expiration_date;
    @Column
    private String payment_due;
    @Column
    private Long consumerId;
    @Column
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
