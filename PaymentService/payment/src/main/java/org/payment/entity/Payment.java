package org.payment.entity;

import java.util.Date;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(
        name = "Payment"
)
public class Payment {
    @Id
    @GeneratedValue(
            strategy = GenerationType.IDENTITY
    )
    private Long id;
    private Integer price;
    private Date subscription_date;
    private Date expiration_date;
    private Date payment_due;
    private Long consumerId;
    private Long sellerId;

    public Payment(Integer price, Date subscription_date, Date expiration_date, Date payment_due, Long consumerId, Long sellerId) {
        this.price = price;
        this.subscription_date = subscription_date;
        this.expiration_date = expiration_date;
        this.payment_due = payment_due;
        this.consumerId = consumerId;
        this.sellerId = sellerId;
    }

    public static PaymentBuilder builder() {
        return new PaymentBuilder();
    }

    public Payment() {
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

    public String toString() {
        return "Payment(id=" + this.getId() + ", price=" + this.getPrice() + ", subscription_date=" + this.getSubscription_date() + ", expiration_date=" + this.getExpiration_date() + ", payment_due=" + this.getPayment_due() + ", consumerId=" + this.getConsumerId() + ", sellerId=" + this.getSellerId() + ")";
    }

    public static class PaymentBuilder {
        private Integer price;
        private Date subscription_date;
        private Date expiration_date;
        private Date payment_due;
        private Long consumerId;
        private Long sellerId;

        PaymentBuilder() {
        }

        public PaymentBuilder price(final Integer price) {
            this.price = price;
            return this;
        }

        public PaymentBuilder subscription_date(final Date subscription_date) {
            this.subscription_date = subscription_date;
            return this;
        }

        public PaymentBuilder expiration_date(final Date expiration_date) {
            this.expiration_date = expiration_date;
            return this;
        }

        public PaymentBuilder payment_due(final Date payment_due) {
            this.payment_due = payment_due;
            return this;
        }

        public PaymentBuilder consumerId(final Long consumerId) {
            this.consumerId = consumerId;
            return this;
        }

        public PaymentBuilder sellerId(final Long sellerId) {
            this.sellerId = sellerId;
            return this;
        }

        public Payment build() {
            return new Payment(this.price, this.subscription_date, this.expiration_date, this.payment_due, this.consumerId, this.sellerId);
        }

        public String toString() {
            return "Payment.PaymentBuilder(price=" + this.price + ", subscription_date=" + this.subscription_date + ", expiration_date=" + this.expiration_date + ", payment_due=" + this.payment_due + ", consumerId=" + this.consumerId + ", sellerId=" + this.sellerId + ")";
        }
    }
}
