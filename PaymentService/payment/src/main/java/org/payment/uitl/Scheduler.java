package org.payment.uitl;

import org.payment.entity.Payment;
import org.payment.entity.PaymentRepository;
import org.payment.service.PaymentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;
import org.springframework.web.reactive.function.client.WebClient;

import java.time.LocalDate;
import java.util.List;

@Component
public class Scheduler {
    @Autowired
    private PaymentRepository paymentRepository;
    @Autowired
    private PaymentService paymentService;


    // 가상 정기 결제
    // 실결제는 X , 일정 시간 paymentDueDate 조회하여
    // 날짜 한달 뒤인 새로운 payment 자동 생성
    @Scheduled(cron = "0 0 11 * * *") // 매일 오전 11시 마다
    public void scheduleRun(){
        List<Payment> paymentList = paymentRepository.findByPaymentDueDate(LocalDate.now());
        for(Payment data : paymentList){
            Payment entity = Payment.builder()
                    .price(data.getPrice())
                    .productId(data.getProductId())
                    .consumerId(data.getConsumerId())
                    .sellerId(data.getSellerId())
                    .subscriptionDate(LocalDate.now())
                    .expirationDate(LocalDate.now().plusMonths(1))
                    .paymentDueDate(LocalDate.now().plusMonths(1))
                    .build();
            Payment newPayment = paymentRepository.save(entity);
            // 해당 consumer의 이메일 주소 획득
            WebClient webClient = WebClient.create();
            String email = webClient.get()
                    .uri("http://"+Constants.AWS_IP+Constants.PORT_AUTH+"/user/"+newPayment.getConsumerId())
                    .retrieve()
                    .bodyToMono(String.class)
                    .block();
            // 메일 발송
            paymentService.emailSend(email.replaceAll("\"",""), newPayment);
        }
    }
}
