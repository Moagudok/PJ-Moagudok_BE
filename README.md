## 📢 모아구독 서비스
- MSA 기반의 구독 모아 보기 서비스

## 🎓 INTRODUCTION
- 주제 : MSA 기반의 구독 상품 모아보기 서비스 (중계형 e-commerce 플랫폼)
- 기간 : 2022.10.25 ~ 2022.11.29
- 팀원 : 
  - BE - 김선민 ([Github](https://github.com/SeonminKim1)), 고현우 ([Github](https://github.com/khw7876)), 박재현 ([Github](https://github.com/Aeius))     
  - FE - 이민기([Github](https://github.com/coddy083)), 백선진([GitHub](https://github.com/tjswls5000))
- 서비스 정의
   - UserGroup은 소비자/판매자 두 그룹으로 구성
   - 소비자는 APP으로 구독 상품을 조회 및 결제 가능
   - 소비자는 최근 검색어, 추천 검색어 등의 서비스로 쉽게 검색 가능
   - 소비자가 결제한 구독 상품은 매 기간마다 자동 결제되고 알림 메일이 발송됨
   - 소비자는 판매자에게 1대1 채팅 연결을 통해 구독 상품에 대해 문의 가능
   - 판매자는 WEB으로 구독 상품 관리 및 판매 내역 Dashboard 확인 가능
   - 판매자는 한 번에 여러 상품을 등록/수정 할 수 있음
   - 판매자의 구독 상품 내용이 변경시 자동으로 변경 내역이 소비자에게 발송됨
   
<br>   

## 🎁 주요 서비스 및 기능
![svc목록](https://user-images.githubusercontent.com/33525798/204617968-3bb901b2-1aae-4962-a408-bc9c2d7599c9.png)

- (Django) AuthService : 인증 / 로그인, 회원가입 
- (Django) LookupService : 상품 조회 / Dashboard 서비스 (판매자) 
- (Django) SearchService : 검색 히스토리 / 최근 검색어, 추천 검색어 
- (Django) SellerService : 상품 관리 / 상품 등록, 수정, 삭제
- (Spring boot) PaymentService : 결제, 구독 관리 / 구독 갱신, 자동 결제, 결제 정보 조회
- (FastAPI) MailService : 메일 서비스
- (Node.js) ChattingService : 채팅 서비스 / 판매자-소비자 1대1 채팅

<br>

## 📚 Tech Stack
![image](https://user-images.githubusercontent.com/33525798/204646738-9e2dc267-891d-496f-ac10-7f07eebf39b6.png)

<br>

## 💡 Service Diagram



<br>

## :computer: Development
#### 🎉 로그인/회원가입
- Django simple jwt 를 이용한 토큰 발급
- 입력 정보 validation
#### 🎉 소비자(App 환경)
- 홈화면 등 각 화면에 맞는 필요 데이터 출력
- 통계 기반 API를 이용한 추천 검색어 구현
- 아임포트 결제 후 결제 정보 DB 저장 및 업데이트
- Spring cron을 이용한 가상 자동 결제 내역 저장 구현
- Spring WebClient를 이용한 타 서비스 API 호출
- fastapi-mail 를 이용하여 메일 발송 구현
- node.js 를 이용한 채팅 서버 구축
#### 🎉 판매자(Web 환경)
- 화면에 맞는 필요 데이터 출력
- 상품 등록/변경/삭제 등 CRUD 구현 시 TDD 개발
- 판매자를 위한 통계화면 구현(dashboard)
- node.js 를 이용한 채팅 서버 구축 

#### 🎉 Deployment & Build
- docker 기반 AWS EC2 배포
- AWS S3 이미지 정적 파일 관리

#### 🎉 Nginx 
- Nginx : Proxy 역할 

## ⚒Trouble Shotting


## :handshake: Project-Rules
#### Branch strategy
- 각 기술 개발은 feature/기술 형태로 브랜치 생성
- main 으로 PR 하여 완성된 코드 리뷰 및 merge 진행
- 최종적으로 production branch에 main을 merge 함으로써 배포
- EC2에선 다른 branch 사용하지 않고 production branch만 연결해두고 pull 만 하여서 배포환경 구축
- EC2에서 docker-compose 를 이용하여 리소스 최대한 절약한 배포 방식


## 🚞 DB Modeling

### RDB
![image](https://user-images.githubusercontent.com/87006912/204206176-3b6d44dd-eec2-4772-95fc-acd85468fc05.png)

### 

## 🚞 Figma Mock-up
![image](https://user-images.githubusercontent.com/87006912/204208509-3ec4cdc2-8e77-483a-a00a-155fbba359c9.png)



## 👉 Structure
```
Moagudok
├── _nginx
├── _utils            
├── .idea             
├── Authservice       // Django        
├── ChattingService   // Node.js   
├── LookupService     // Django
├── MailService       // fastapi-mail
├── PaymentService    // Spring boot
├── SearchService     // Django - mongo DB
├── SellerService     // Django
├── .gitignore
├── docker-compose.yaml // Doker-Compose
├── README.md        
└── requirements.txt
```




## 🖥 시연 화면
