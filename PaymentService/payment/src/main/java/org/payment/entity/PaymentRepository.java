//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by FernFlower decompiler)
//

package org.payment.entity;

import java.time.LocalDate;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PaymentRepository extends JpaRepository<Payment, Long> {
    List<Payment> findByConsumerId(Long consumerId);

    List<Payment> findBySellerId(Long sellerId);

    List<Payment> findBySubscriptionDateBetween(LocalDate first,LocalDate last);

    List<Payment> findByConsumerIdAndProductIdAndSubscriptionDate(Long consumerId, Long productId, LocalDate subscriptionDate);

    List<Payment> findByConsumerIdAndExpirationDateGreaterThanEqual(Long consumerId, LocalDate localDate);

    List<Payment> findByConsumerIdAndExpirationDateIs(Long consumerId, LocalDate localDate);

    List<Payment> findByConsumerIdAndExpirationDateLessThan(Long consumerId, LocalDate localDate);

    List<Payment> findByConsumerIdAndExpirationDateBetween(Long consumerId, LocalDate now, LocalDate ago);

    List<Payment> findByPaymentDueDate(LocalDate localDate);

    List<Payment> findBySellerIdAndSubscriptionDate(Long sellerId, LocalDate date);

    List<Payment> findBySellerIdAndSubscriptionDateBetween(Long sellerId, LocalDate first, LocalDate last);

    List<Payment> findBySellerIdAndProductIdAndSubscriptionDateBetween(Long sellerId, Long productId, LocalDate first, LocalDate last);
}
