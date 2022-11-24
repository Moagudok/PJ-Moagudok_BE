package org.payment;

import org.junit.jupiter.api.Test;
import org.payment.entity.Payment;
import org.payment.entity.PaymentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.time.LocalDate;

@SpringBootTest
class PaymentApplicationTests {

	@Autowired
	private PaymentRepository paymentRepository;

	@Test
	public void insert() {
		Payment payment = Payment.builder()
				.price(1000)
				.consumerId(2L)
				.subscriptionDate(LocalDate.now())
				.paymentDueDate(LocalDate.now())
				.expirationDate(LocalDate.now())
				.sellerId(3L)
				.productId(1L)
				.build();
		paymentRepository.save(payment);

	}

}
