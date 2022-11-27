package org.payment.controller;

import java.time.LocalDate;
import java.time.temporal.TemporalAdjusters;
import java.util.*;
import java.util.stream.Collectors;

import lombok.RequiredArgsConstructor;
import org.json.JSONObject;
import org.payment.entity.Payment;
import org.payment.service.PaymentService;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.reactive.function.BodyInserters;
import org.springframework.web.reactive.function.client.WebClient;

import javax.servlet.http.HttpServletRequest;

@RestController
@RequestMapping({"/payment"})
@RequiredArgsConstructor
public class PaymentApiController {
    private final PaymentService paymentService;

    // 결제 내역 생성
    @PostMapping
    public ResponseEntity<?> save(@RequestBody Payment params, HttpServletRequest request) {
        Payment payment = paymentService.save(params);
        // 구독자 수 증가 API 호출
        WebClient webClient = WebClient.create();
        webClient.put()
                .uri("http://52.79.143.145:8001/consumer/product/subscriber")
                .body(BodyInserters.fromFormData("product_id", payment.getProductId().toString()))
                .retrieve()
                .bodyToMono(String.class)
                .block();

        // JWT 토큰 Decode를 통한 접속한 유저의 email 값 가져오기
        String authToken = request.getHeader(HttpHeaders.AUTHORIZATION);
        String[] chunks = authToken.split("\\.");
        Base64.Decoder decoder = Base64.getUrlDecoder();
        String payload = new String(decoder.decode(chunks[1]));
        JSONObject jObject = new JSONObject(payload);
        String user_email = jObject.getString("email");

        // 메일발송 API 호출
        Map<String, Object> mailData = new HashMap<>();
        mailData.put("subject", "결제가 완료되었습니다. - 모아구독");
        mailData.put("message", "결제가 완료되었습니다! - 모아구독 \n" +
                "결제 금액 : " + payment.getPrice() + "원 \n" +
                "구독 날짜 : " + payment.getSubscriptionDate() + "\n" +
                "만료 날짜 : " + payment.getExpirationDate() + "\n" +
                "갱신 날짜 : " + payment.getPaymentDueDate() + "\n" +
                "감사합니다.");
        mailData.put("recipient", Arrays.asList(user_email));
        WebClient mailReq = WebClient.create();
        mailReq.post()
                .uri("http://52.79.143.145:8002/mail/api")
                .accept(MediaType.APPLICATION_JSON)
                .body(BodyInserters.fromValue(mailData))
                .retrieve()
                .bodyToMono(String.class)
                .block();
        return new ResponseEntity<>("결제 성공",HttpStatus.OK);
    }
    // 전체 결제 내역 조회
    @GetMapping
    public ResponseEntity<?> findAll() {
        return ResponseEntity.ok(paymentService.findAll());
    }
    // 소비자 결제 내역 조회
    @GetMapping("/consumer")
    public List<Payment> findByConsumerId(@RequestParam Long consumerId) {
        return paymentService.findByConsumerId(consumerId);
    }
    // 판매자 결제 내역 조회
    @GetMapping("/seller")
    public ResponseEntity<List<Payment>> findBySellerId(@RequestParam Long sellerId){
        return ResponseEntity.ok(paymentService.findBySellerId(sellerId));
    }
    // 마이페이지 조회용
    @GetMapping("/consumer/mypage")
    public List<HashMap<Long, List<String>>> sub_product(@RequestParam Long consumerId, String type){
        switch (type) {
            // 소비자의 구독중인 상품
            default: {
                List<Payment> resultList = paymentService.sub_product(consumerId, LocalDate.now());
                List<HashMap<Long, List<String>>> productList = new ArrayList<>();
                HashMap<Long, List<String>> maps = new HashMap<Long, List<String>>();
                for (Payment payment : resultList) {
                    maps.put(payment.getProductId(), Arrays.asList(payment.getSubscriptionDate().toString(), payment.getExpirationDate().toString()));
                }
                productList.add(maps);
                return productList;
            }
            // 소비자의 오늘 만료되는 구독상품
            case "now": {
                List<Payment> resultList = paymentService.exp_today(consumerId, LocalDate.now());
                List<HashMap<Long, List<String>>> productList = new ArrayList<>();
                HashMap<Long, List<String>> maps = new HashMap<Long, List<String>>();
                for (Payment payment : resultList) {
                    maps.put(payment.getProductId(), Arrays.asList(payment.getSubscriptionDate().toString(), payment.getExpirationDate().toString()));
                }
                productList.add(maps);
                return productList;
            }
            // 소비자의 만료된 구독상품들
            case "exp": {
                List<Payment> expList = paymentService.exp_product(consumerId, LocalDate.now());
                List<HashMap<Long, List<String>>> productList = new ArrayList<>();
                HashMap<Long, List<String>> maps = new HashMap<Long, List<String>>();
                for (Payment payment : expList) {
                    maps.put(payment.getProductId(), Arrays.asList(payment.getSubscriptionDate().toString(), payment.getExpirationDate().toString()));

                }
                productList.add(maps);
                // 증복제거
                // 현재 구독중인 상품 리스트 제거
                List<Payment> subList = paymentService.sub_product(consumerId, LocalDate.now());
                for (Payment payment : subList){
                    for(HashMap<Long, List<String>> map : productList){
                        map.remove(payment.getProductId());
                    }
                }
                return productList;
            }
            // 소비자의 상품중 만료가 7일 전인 상품들
            case "7ago": {
                List<Payment> resultList = paymentService.exp_7ago(consumerId, LocalDate.now(), LocalDate.now().plusWeeks(1));
                List<HashMap<Long, List<String>>> productList = new ArrayList<>();
                HashMap<Long, List<String>> maps = new HashMap<Long, List<String>>();
                for (Payment payment : resultList) {
                    maps.put(payment.getProductId(), Arrays.asList(payment.getSubscriptionDate().toString(), payment.getExpirationDate().toString()));
                }
                productList.add(maps);
                return productList;
            }
        }
    }
    // 판매자의 선택한 월의 상품별 매출 및 구독자 수
    @GetMapping("/dashboard")
    public List<HashMap<String, Long>> salesOfMonth(@RequestParam Long sellerId, Integer month) {
        LocalDate init = LocalDate.of(LocalDate.now().getYear(), month, LocalDate.now().getDayOfMonth());
        LocalDate first = init.with(TemporalAdjusters.firstDayOfMonth());
        LocalDate last = init.with(TemporalAdjusters.lastDayOfMonth());

        List<Payment> monthList = paymentService.salesOfMonth(sellerId, first, last);
        List<HashMap<String, Long>> resultList = new ArrayList<>();

        List<Long> productList = new ArrayList<>();
        for (Payment payment : monthList){
            productList.add(payment.getProductId());
        }
        // 중복제거
        List<Long> idList = productList.stream().distinct().collect(Collectors.toList());

        for (long productId : idList){
            List<Payment> payments = paymentService.salesOfProduct(sellerId, productId, first, last);
            long total_price = 0;
            long total_count = 0;
            for(Payment data : payments){
                total_price += data.getPrice();
                total_count += 1;
            }
            HashMap<String, Long> maps = new HashMap<>();
            maps.put("product_id", productId);
            maps.put("total_price", total_price);
            maps.put("total_count", total_count);
            resultList.add(maps);
        }
        return resultList;
    }
}
