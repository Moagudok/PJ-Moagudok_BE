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
    private Long productId;
    @Column
    private Integer price;
    @Column
    private LocalDate subscriptionDate;
    @Column
    private LocalDate expirationDate;
    @Column
    private String paymentDue;
    @Column
    private Long consumerId;
    @Column
    private Long sellerId;

    @Builder
    public Payment(Long productId,
                   Integer price,
                   LocalDate subscriptionDate,
                   LocalDate expirationDate,
                   String paymentDue,
                   Long consumerId,
                   Long sellerId) {
        this.productId = productId;
        this.price = price;
        this.subscriptionDate = subscriptionDate;
        this.expirationDate = expirationDate;
        this.paymentDue = paymentDue;
        this.consumerId = consumerId;
        this.sellerId = sellerId;
    }



}
