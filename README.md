## 📢 모아구독 서비스
- MSA 기반의 구독 모아 보기 서비스

<br>

## 🎓 INTRODUCTION
- 주제 : MSA 기반의 구독 상품 모아보기 서비스 (중계형 e-commerce 플랫폼)
- 기간 : 2022.10.25 ~ 2022.11.29
- 팀원 : 
  - BE - 김선민 ([Github](https://github.com/SeonminKim1)), 고현우 ([Github](https://github.com/khw7876)), 박재현 ([Github](https://github.com/Aeius))     
  - FE - 이민기([Github](https://github.com/coddy083)), 백선진([GitHub](https://github.com/tjswls5000))
- API 문서 : [링크](https://www.notion.so/c038c6b9accc4de4ac55323097d3bad5)

<br>   

## 🎁 MSA 서비스 목록
![svc목록](https://user-images.githubusercontent.com/33525798/204617968-3bb901b2-1aae-4962-a408-bc9c2d7599c9.png)

<br>

| :computer: Framework  | 🎉 서비스명 | 👓 서비스 개요 | 🧱 주요 기능 |🔑 서비스 포트 번호 |
| :---: | :---: | :---: | :---: | :---: |
| Django  | AuthService  | 인증  | 로그인, 회원가입, JWT  | 10000  |
| Django  | LookupService  | 상품 조회  | 상품 페이지네이션 조회, Dashboard  | 10001  |
| Django  | SellerService  | 상품 관리  | 상품 등록, 수정, 삭제  | 10002  |
| Django  | SearchService  | 검색 히스토리  | 최근 검색어, 추천 검색어 | 10003  |
| Spring Boot  | PaymentService  | 결제, 구독 관리  | 구독 갱신, 자동 결제(Cron), 결제 정보 조회  | 10004  |
| Node.js  | ChattingService  | 채팅  | 판매자-소비자 1대1 채팅, 채팅방 관리  | 10005  |
| FastAPI  | MailService  | 메일  | 소비자 메일 전송  | 10006  |

<br>

### 서비스 추가 설명
- UserGroup은 소비자/판매자 두 그룹으로 구성됨
- 소비자는 APP으로 구독 상품을 조회 및 결제 가능
- 소비자는 최근 검색어, 추천 검색어 등의 서비스 제공 받음
- 소비자가 결제한 구독 상품은 매 기간마다 자동 결제되고 알림 메일이 발송됨
- 소비자는 판매자에게 1대1 채팅 연결을 통해 구독한 상품에 대해 문의 가능
- 판매자는 WEB으로 구독 상품 관리 및 판매 내역 Dashboard 확인 가능
- 판매자는 한 번에 여러 상품을 등록/수정 할 수 있음
- 판매자의 구독 상품 내용이 변경시 자동으로 변경 내역이 소비자에게 발송됨

<br>

## 📚 Tech Stack
![image](https://user-images.githubusercontent.com/33525798/204652929-14d6a890-f067-4d65-afad-8e90f245aeca.png)

<br>

## 💡 Service Diagram
![image](https://user-images.githubusercontent.com/33525798/204677212-75a7b00e-1fea-4bd9-a020-033457afbb3c.png)


<br>

## ⚒ Trouble Shotting
- [Django Pagination 선택 및 Redis Caching 적용기](https://yubi5050.tistory.com/220)
- [조회수 구현하기 1 - 동시성 이슈 해결하기(부제 : ORM 부터 Transaction Isolation Level 까지)](https://yubi5050.tistory.com/221)
- [조회수 구현하기 2 - Cookie를 활용하여 중복 접근 해결하기](https://yubi5050.tistory.com/222)
- [Query 프로파일링을 통한 성능 개선하기](https://yubi5050.tistory.com/223)
- [검색 히스토리 서비스 구현하기 (NoSQL vs RDB, Singleton 적용기](https://yubi5050.tistory.com/225)
- [동기 기반 메일 서비스 비동기로 구현하기(by. FastAPI, RabbitMQ, Celery](https://yubi5050.tistory.com/227)
- [Spring cron을 이용한 가상 자동 결제 구현, WebClient를 이용한 외부 api 호출](https://psb6604.tistory.com/83)
- [Django simpleJWT 커스텀, spring에서의 JWT decode](https://psb6604.tistory.com/84)


<br>

## :handshake: Project-Rules
#### 🎉 Sprint & Scrum
- 한 주 단위 Sprint 기반 / 주 3회 Scrum 진행
#### 🎉 Git issue - TDD 작성
- Git Issue로 기능 개요 및 세부 Schedule 작성
- Issue 바탕으로 TestCode 작성
- TestCode 바탕으로 비즈니스 로직 작성
#### 🎉 Branch strategy
- feature/<기능> : 기능 개발 Branch
- main : 개발 Merge Branch (+Code Review)
- production : 배포 Branch

<br>

## 🚞 DB Modeling
![image](https://user-images.githubusercontent.com/33525798/204657362-0fd8e6ad-1e00-47c6-bbb3-dc27a7220c6f.png)


<br>

## 🚞 Figma Mock-up
![image](https://user-images.githubusercontent.com/87006912/204208509-3ec4cdc2-8e77-483a-a00a-155fbba359c9.png)


<br>

## 👉 Code Structure
```
Moagudok
├── _nginx            // reverse proxing
├── _utils            // DB & Infra Setting
├── Authservice       // Django        
├── ChattingService   // Node.js   
├── LookupService     // Django
├── MailService       // Fastapi
├── PaymentService    // Spring boot
├── SearchService     // Django
├── SellerService     // Django
├── .gitignore
├── docker-compose.yaml // Build & Deployment
├── README.md        
└── requirements.txt
```


## 🖥 시연 화면
