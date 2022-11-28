## 📢 모아구독 서비스
- MSA 기반의 구독 모아 보기 서비스

## 🎓 INTRODUCTION
- 주제 : 구독 상품을 판매하는 쇼핑몰(E-commece)
- 기간 : 2022.10.25 ~ 2022.11.29    
- 팀 :     
    - BE - 김선민 ([Github](https://github.com/SeonminKim1)), 고현우 ([Github](https://github.com/khw7876)), 박재현 ([Github](https://github.com/Aeius))     
    - FE - 이민기([Github](https://github.com/coddy083)), 백선진([GitHub](https://github.com/tjswls5000))
- 주요 기능 (중개형 플랫폼)    
    - 앱 기반 서비스 (위 링크 예시 동영상과 유사한 프로젝트)
    - 소비자/판매자로 그룹 구성되며, 제공 기능 서로 상이함
    - 상품 관리 : 소비자 - 상품 조회, 판매자 - 상품 등록, 삭제
    - 구독 관리 : 구독 갱신, 등록, 해지
    - 판매자 서비스 : 구독 관련 정보 Dashboard (통계)
    - 구독 상품 : ex) 뉴스 크롤링 메일, 알람 서비스 (lambda, fastapi 등)
    
## :handshake: Project-Rules
#### Branch strategy
- 각 기술 개발은 feature/기술 형태로 브랜치 생성
- main 으로 PR 하여 완성된 코드 리뷰 및 merge 진행
- 최종적으로 production branch에 main을 merge 함으로써 배포
- EC2에선 다른 branch 사용하지 않고 production branch만 연결해두고 pull 만 하여서 배포환경 구축
- EC2에서 docker-compose 를 이용하여 리소스 최대한 절약한 배포 방식

## 📚 Project Structure
![image](https://user-images.githubusercontent.com/87006912/204205755-a3cb20a8-9fb7-4f6c-931c-dd72cedd8fb4.png)

## 🚞 Figma Mock-up & DB Modeling
![image](https://user-images.githubusercontent.com/87006912/204208509-3ec4cdc2-8e77-483a-a00a-155fbba359c9.png)
![image](https://user-images.githubusercontent.com/87006912/204206176-3b6d44dd-eec2-4772-95fc-acd85468fc05.png)

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
- AuthService : 로그인, 회원가입 및 유저 Session Cookies 관련 전반 (Django)
- ChattingService : 판매자와 소비자 사이의 소통을 위한 채팅 서비스 (node.js)
- LookupService : 상품 조회 관련 (판매자, 구매자 둘다), 통계 Dashboard 서비스 (판매자) (Django)
- MailService : 메일 발송 서비스 (fastapi-mail)
- PaymentService : 결제(돈) 관련 전반 (Spring boot)
- SearchService : 상품 겅색 관련 (Django - mongo DB)
- SellerService : 상품 등록, 수정, 삭제(취소) 관련 (Django)


## :computer: Development
#### 🎉 로그인/회원가입
- Django simple jwt 를 이용한 토큰 발급
- 로그인 시 기본적인 validation 진행
#### 🎉 소비자(Apk 환경)
- 홈화면 등 각 화면에 맞는 필요 데이터 출력
- 통계 기반 API를 이용한 추천 검색어 구현
- 아임포트 결제 후 결제 정보 DB 저장 및 업데이트
- Spring cron을 이용한 가상 자동 결제 내역 저장 구현
- Spring WebClient를 이용한 다른 API와 통신하여 데이터 통신
- fastapi-mail 를 이용하여 메일 발송 구현
- node.js 를 이용한 채팅 서버 구축
#### 🎉 판매자(Web 환경)
- 화면에 맞는 필요 데이터 출력
- 상품 등록/변경/삭제 등 CRUD 구현 시 TDD 개발
- 판매자를 위한 통계화면 구현(dashboard)
- node.js 를 이용한 채팅 서버 구축 

#### 🎉 AWS Infra & CI-CD
- AWS EC2 내 docker container 기반 Publish 배포
- AWS S3 이용하여 정적 파일 관리
- AWS IAM 부여하여 Infra Team 공동 관리
- AWS RDS 이용하여 DataBase 속도와 안정성 확보 

#### 🎉 Nginx 
- Nginx : Proxy 역할 

## ⚒Trouble Shotting

## 🖥 시연 화면
