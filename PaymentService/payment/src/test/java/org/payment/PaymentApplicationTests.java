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
	void testJPA() {
	}

}
