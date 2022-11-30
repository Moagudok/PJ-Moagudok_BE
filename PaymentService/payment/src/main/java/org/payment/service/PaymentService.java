package org.payment.service;

import java.time.LocalDate;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.transaction.Transactional;

import lombok.RequiredArgsConstructor;
import org.json.JSONObject;
import org.payment.entity.Payment;
import org.payment.entity.PaymentRepository;
import org.payment.uitl.Constants;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.BodyInserters;
import org.springframework.web.reactive.function.client.WebClient;

@Service
@RequiredArgsConstructor
public class PaymentService {

    @Autowired
    private PaymentRepository paymentRepository;

    @Transactional
    public Payment save(Payment payment) {
        return paymentRepository.save(payment);
    }
    @Transactional
    public List<Payment> checkDup(Long consumerId, Long productId, LocalDate subscriptionDate){
        return paymentRepository.findByConsumerIdAndProductIdAndSubscriptionDate(consumerId, productId, subscriptionDate);
    }

    @Transactional
    public List<Payment> findAll() {
        return paymentRepository.findAll();
    }
    @Transactional
    public List<Payment> findByConsumerId(Long consumerId){
        return paymentRepository.findByConsumerId(consumerId);
    }
    @Transactional
    public List<Payment> findBySellerId(Long sellerId){
        return paymentRepository.findBySellerId(sellerId);
    }
    @Transactional
    public List<Payment> subProduct(Long consumerId, LocalDate localDate){
        return paymentRepository.findByConsumerIdAndExpirationDateGreaterThanEqual(consumerId, localDate);
    }
    @Transactional
    public List<Payment> expToday(Long consumerId, LocalDate localDate){
        return paymentRepository.findByConsumerIdAndExpirationDateIs(consumerId, localDate);
    }
    @Transactional
    public List<Payment> expProduct(Long consumerId, LocalDate localDate){
        return paymentRepository.findByConsumerIdAndExpirationDateLessThan(consumerId, localDate);
    }
    @Transactional
    public List<Payment> exp7ago(Long consumerId, LocalDate now, LocalDate ago){
        return paymentRepository.findByConsumerIdAndExpirationDateBetween(consumerId, now, ago);
    }
    // 가상 정기 결제
    // 실결제는 X , 일정 시간 paymentDueDate 조회하여
    // 날짜 한달 뒤인 새로운 payment 자동 생성
    @Scheduled(cron = "0 10 19 * * *") // 매일 오전 11시 마다
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
            emailSend(email, newPayment);
        }
    }
    @Transactional
    public List<Payment> salesOfMonth(Long sellerId, LocalDate first, LocalDate last){
        return paymentRepository.findBySellerIdAndSubscriptionDateBetween(sellerId,first,last);
    }
    @Transactional
    public List<Payment> salesOfProduct(Long sellerId, Long productId, LocalDate first, LocalDate last){
        return paymentRepository.findBySellerIdAndProductIdAndSubscriptionDateBetween(sellerId,productId,first,last);
    }
    @Transactional
    public List<Payment> subscriptionData(LocalDate first, LocalDate last){
        return paymentRepository.findBySubscriptionDateBetween(first, last);
    }

    // 구독자 수 증가 API 호출
    public void updateSubCount(Payment payment) {
        WebClient webClient = WebClient.create();
        webClient.put()
                .uri("http://"+ Constants.AWS_IP+Constants.PORT_LOOKUP+"/consumer/product/subscriber")
                .body(BodyInserters.fromFormData("product_id", payment.getProductId().toString()))
                .retrieve()
                .bodyToMono(String.class)
                .block();
    }
    // 메일발송
    public void emailSend(String user_email, Payment payment) {
        // product_id 를 이용해 product의 정보 조회
        WebClient findProduct = WebClient.create();
        String responseData = findProduct.get()
                .uri("http://"+ Constants.AWS_IP+Constants.PORT_LOOKUP+"/consumer/product/detail/"+ payment.getProductId())
                .retrieve()
                .bodyToMono(String.class)
                .block();
        JSONObject product_details = new JSONObject(responseData);
        JSONObject product_info = product_details.getJSONObject("detail_product_data");
        String product_name = (String) product_info.get("product_name");
        String subtitle = (String) product_info.get("subtitle");
        String product_group_name = (String) product_info.get("product_group_name");

        // 메일발송 API 호출
        Map<String, Object> mailData = new HashMap<>();
        mailData.put("subject", "결제가 완료되었습니다. - 모아구독");
        mailData.put("message", "결제가 완료되었습니다! - 모아구독 \n" +
                "상품 그룹 : " + product_group_name + "\n" +
                "구독 상품 명 : " + product_name +" - " + subtitle + "\n" +
                "결제 금액 : " + payment.getPrice() + "원 \n" +
                "구독 날짜 : " + payment.getSubscriptionDate() + "\n" +
                "만료 날짜 : " + payment.getExpirationDate() + "\n" +
                "갱신 날짜 : " + payment.getPaymentDueDate() + "\n" +
                "감사합니다.");
        mailData.put("recipient", Arrays.asList(user_email));
        WebClient mailReq = WebClient.create();
        mailReq.post()
                .uri("http://"+ Constants.AWS_IP+Constants.PORT_MAIL+"/mail/api")
                .accept(MediaType.APPLICATION_JSON)
                .body(BodyInserters.fromValue(mailData))
                .retrieve()
                .bodyToMono(String.class)
                .block();
    }
}
