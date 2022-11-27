package org.payment.entity;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDate;
import javax.persistence.*;

@Entity
@Getter
@NoArgsConstructor
@Setter
@Table(schema = "public", name = "payment")
public class Payment {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private Long productId;
    private Integer price;
    private LocalDate subscriptionDate;
    private LocalDate expirationDate;
    private LocalDate paymentDueDate;
    private Long consumerId;
    private Long sellerId;

    @Builder
    public Payment(Long productId,
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
