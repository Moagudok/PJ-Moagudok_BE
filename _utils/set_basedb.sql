INSERT INTO public."SignupMethod"(id, method)
	VALUES 
	(1, 'basic'),
	(2, 'google');

INSERT INTO public."Category"(id, name, image)
	VALUES 
	(1, 'IT 서비스', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_it_service.jpg'),
	(2, '육류', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_meat.jpg'),
	(3, '가공식품', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_processed_food.jpg'),
	(4, '커피 및 음료', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_coffee.jpg'),
	(5, '주류', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_alcohol.jpg'),
	(6, '도시락', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_luch_box.jpg'),
	(7, '샐러드', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_salad.jpg'),
	(8, '채소 및 과일', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_vegetables_fruits.jpg'),
	(9, '유제품', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_dairy_product.jpg'),
	(10, '식물', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_plant.jpg'),
	(11, '안주', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_munchies.jpg'),
	(12, '가전제품', 'https://moagudok.s3.ap-northeast-2.amazonaws.com/base_image/category_base_appliances.jpg');

INSERT INTO public."PaymentTerm"(id, unit)
	VALUES 
	(1, '일'),
	(2, '주'),
	(3, '월'),
	(4, '분기');

INSERT INTO public."User"(id, email, password, name, address, is_seller, signup_method_id, join_date, is_active, is_admin)
 VALUES 
 (1, 'consumer1@mail.com', 1234, '구매자1', '구매자의주소', false, 1, '2022-11-19', true, false),
 (2, 'seller1@mail.com', 1234, '판매자1', '판매자의주소', true, 1, '2022-11-19', true, false);

INSERT INTO public."Product"(
	id, seller_id, category_id, product_group_name, product_name, subtitle, payment_term_id, register_date, update_date, price, image, description, views, num_of_subscribers)
	VALUES 
        (1, 1, 1, '뉴스 크롤링', 'IT TOP 10', '매주 IT Top 뉴스 받아보기!', 2, '2022-11-07', '2022-11-07', 10000, 
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_it.jpg','주간 IT 헤드라인 TOP 10 뉴스 크롤링하여 전달해드립니다.',
			5, 2),
        (2, 1, 1, '뉴스 크롤링', '정치 TOP 10', '매일 정치 Top 뉴스 받아보기!', 1, '2022-11-08', '2022-11-08', 10000, 
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics.jpg','일일 정치 헤드라인 TOP 10 뉴스 크롤링하여 전달해드립니다.',
			10, 0),
        (3, 1, 1, '증권 주가 통계 정보', '식량관련주', '매일 증권 HOT 뉴스 받아보기!', 1, '2022-11-06', '2022-11-06', 5000,
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_stock_food.jpg','일일 식량관련주 통계 분석 하여 제공해드립니다.',
			35, 1),
        (4, 1, 1, '증권 주가 통계 정보', '엔터관련주', '매월 증권 HOT 뉴스 받아보기!', 3, '2022-11-08', '2022-11-08', 5000,
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_stock_entertainment.jpg','월간 엔터관련주 통계 분석 하여 제공해드립니다.',
			77, 98),
        (5, 1, 2, '돼지좋아', '삼목살', '매주 신선한 삼겹살과 목살 배송!', 2, '2022-11-05', '2022-11-06', 30000, 
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_meat_porkbelly.jpg','삼겹살 300g과 목살 300g 조합의 고기셋트',
			15, 42),
        (6, 1, 2, '돼지좋아', '등심럽', '등심좋아하는 사람들 모여라~', 2, '2022-11-03', '2022-11-04', 40000, 
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_meat_sirloinjpg.jpg','등심 600g 조합의 고기셋트',
			13, 7),
        (7, 1, 3, '통조림가공식품', '스팸셋트', '흰 쌀밥에 스팸 한입 먹고 싶은 사람~', 3, '2022-11-03', '2022-11-04', 25000,
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_processed_food_spam.jpg','스팸에 쌀밥 먹고 싶은 사람만~', 
			31, 4),
        (8, 1, 3, '통조림가공식품', '참치셋트', '만능 참치! 매월 편하게 구입하세요~', 3, '2022-11-05', '2022-11-08', 15000,
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_processed_food_tuna.jpg','참치 통조림 다양하게 먹고 싶은 사람만~',
			22, 5),
        (9, 1, 1, '뉴스 크롤링2', 'IT TOP 10', '매주 IT Top 뉴스 받아보기!', 2, '2022-11-07', '2022-11-07', 10000, 
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_it.jpg','주간 IT 헤드라인 TOP 10 뉴스 크롤링하여 전달해드립니다.',
			16, 5),
        (10, 1, 1, '뉴스 크롤링2', '정치 TOP 10', '매일 정치 Top 뉴스 받아보기!', 1, '2022-11-08', '2022-11-08', 10000, 
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics.jpg','일일 정치 헤드라인 TOP 10 뉴스 크롤링하여 전달해드립니다.',
			8, 1),
        (11, 1, 1, '증권 주가 통계 정보2', '식량관련주', '매일 증권 HOT 뉴스 받아보기!', 1, '2022-11-06', '2022-11-06', 5000,
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_stock_food.jpg','일일 식량관련주 통계 분석 하여 제공해드립니다.',
			35, 1),
        (12, 1, 1, '증권 주가 통계 정보2', '엔터관련주', '매월 증권 HOT 뉴스 받아보기!', 3, '2022-11-08', '2022-11-08', 5000,
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_stock_entertainment.jpg','월간 엔터관련주 통계 분석 하여 제공해드립니다.',
			16, 17),
        (13, 1, 2, '돼지좋아2', '삼목살', '매주 신선한 삼겹살과 목살 배송!', 2, '2022-11-05', '2022-11-06', 30000, 
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_meat_porkbelly.jpg','삼겹살 300g과 목살 300g 조합의 고기셋트',
			19, 10),
        (14, 1, 2, '돼지좋아2', '등심럽', '등심좋아하는 사람들 모여라~', 2, '2022-11-03', '2022-11-04', 40000, 
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_meat_sirloinjpg.jpg','등심 600g 조합의 고기셋트',
			10, 9),
        (15, 1, 3, '통조림가공식품2', '스팸셋트', '흰 쌀밥에 스팸 한입 먹고 싶은 사람~', 3, '2022-11-03', '2022-11-04', 25000,
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_processed_food_spam.jpg','스팸에 쌀밥 먹고 싶은 사람만~', 
			11, 10),
        (16, 1, 3, '통조림가공식품2', '참치셋트', '만능 참치! 매월 편하게 구입하세요~', 3, '2022-11-05', '2022-11-08', 15000,
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_processed_food_tuna.jpg','참치 통조림 다양하게 먹고 싶은 사람만~',
			4, 9),
        (17, 1, 1, '뉴스 크롤링3', 'IT TOP 10', '매주 IT Top 뉴스 받아보기!', 2, '2022-11-07', '2022-11-07', 10000, 
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_it.jpg','주간 IT 헤드라인 TOP 10 뉴스 크롤링하여 전달해드립니다.',
			6, 8),
        (18, 1, 1, '뉴스 크롤링3', '정치 TOP 10', '매일 정치 Top 뉴스 받아보기!', 1, '2022-11-08', '2022-11-08', 10000, 
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics.jpg','일일 정치 헤드라인 TOP 10 뉴스 크롤링하여 전달해드립니다.',
			4, 5),
        (19, 1, 1, '증권 주가 통계 정보3', '식량관련주', '매일 증권 HOT 뉴스 받아보기!', 1, '2022-11-06', '2022-11-06', 5000,
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_stock_food.jpg','일일 식량관련주 통계 분석 하여 제공해드립니다.',
			10, 5),
        (20, 1, 1, '증권 주가 통계 정보3', '엔터관련주', '매월 증권 HOT 뉴스 받아보기!', 3, '2022-11-08', '2022-11-08', 5000,
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_stock_entertainment.jpg','월간 엔터관련주 통계 분석 하여 제공해드립니다.',
			71, 22),
        (21, 1, 2, '돼지좋아3', '삼목살', '매주 신선한 삼겹살과 목살 배송!', 2, '2022-11-05', '2022-11-06', 30000, 
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_meat_porkbelly.jpg','삼겹살 300g과 목살 300g 조합의 고기셋트',
			1, 4),
        (22, 1, 2, '돼지좋아3', '등심럽', '등심좋아하는 사람들 모여라~', 2, '2022-11-03', '2022-11-04', 40000, 
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_meat_sirloinjpg.jpg','등심 600g 조합의 고기셋트',
			7, 8),
        (23, 1, 3, '통조림가공식품3', '스팸셋트', '흰 쌀밥에 스팸 한입 먹고 싶은 사람~', 3, '2022-11-03', '2022-11-04', 25000,
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_processed_food_spam.jpg','스팸에 쌀밥 먹고 싶은 사람만~', 
			9, 3),
        (24, 1, 3, '통조림가공식품3', '참치셋트', '만능 참치! 매월 편하게 구입하세요~', 3, '2022-11-05', '2022-11-08', 15000,
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_processed_food_tuna.jpg','참치 통조림 다양하게 먹고 싶은 사람만~',
			17, 2),
        (25, 1, 1, '뉴스 크롤링4', 'IT TOP 10', '매주 IT Top 뉴스 받아보기!', 2, '2022-11-07', '2022-11-07', 10000, 
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_it.jpg','주간 IT 헤드라인 TOP 10 뉴스 크롤링하여 전달해드립니다.',
			44, 5),
        (26, 1, 1, '뉴스 크롤링4', '정치 TOP 10', '매일 정치 Top 뉴스 받아보기!', 1, '2022-11-08', '2022-11-08', 10000, 
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics.jpg','일일 정치 헤드라인 TOP 10 뉴스 크롤링하여 전달해드립니다.',
			7, 1),
        (27, 1, 1, '증권 주가 통계 정보4', '식량관련주', '매일 증권 HOT 뉴스 받아보기!', 1, '2022-11-06', '2022-11-06', 5000,
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_stock_food.jpg','일일 식량관련주 통계 분석 하여 제공해드립니다.',
			6, 15),
        (28, 1, 1, '증권 주가 통계 정보4', '엔터관련주', '매월 증권 HOT 뉴스 받아보기!', 3, '2022-11-08', '2022-11-08', 5000,
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_stock_entertainment.jpg','월간 엔터관련주 통계 분석 하여 제공해드립니다.',
			15, 4),
        (29, 1, 2, '돼지좋아4', '삼목살', '매주 신선한 삼겹살과 목살 배송!', 2, '2022-11-05', '2022-11-06', 30000, 
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_meat_porkbelly.jpg','삼겹살 300g과 목살 300g 조합의 고기셋트',
			15, 2),
        (30, 1, 2, '돼지좋아4', '등심럽', '등심좋아하는 사람들 모여라~', 2, '2022-11-03', '2022-11-04', 40000, 
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_meat_sirloinjpg.jpg','등심 600g 조합의 고기셋트',
			10, 4),
        (31, 1, 3, '통조림가공식품4', '스팸셋트', '흰 쌀밥에 스팸 한입 먹고 싶은 사람~', 3, '2022-11-03', '2022-11-04', 25000,
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_processed_food_spam.jpg','스팸에 쌀밥 먹고 싶은 사람만~', 
			20, 9),
        (32, 1, 3, '통조림가공식품4', '참치셋트', '만능 참치! 매월 편하게 구입하세요~', 3, '2022-11-05', '2022-11-08', 15000,
        	'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_processed_food_tuna.jpg','참치 통조림 다양하게 먹고 싶은 사람만~',
			11, 2);

INSERT INTO public."ProductImages"(id, image, product_id)
	VALUES
	(1, 'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail1.jpg', 2),
	(2, 'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_politics_detail2.jpg', 2),
	(3, 'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_it_detail1.jpg', 1),
	(4, 'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_crawling_news_it_detail2.jpg', 1),
	(5, 'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_processed_food_spam_detail1.jpg', 7),
	(6, 'https://moagudok.s3.ap-northeast-2.amazonaws.com/test_image/product_processed_food_tuna_detail1.jpg', 8);

INSERT INTO public."payment"(id, consumer_id, seller_id, product_id, price, subscription_date, expiration_date, payment_due_date)
	VALUES
	(1, 1, 2, 1, 10000, '2022-10-29', '2022-11-04', '2022-11-05'),
	(2, 1, 2, 1, 10000, '2022-11-06', '2022-11-12', '2022-11-13'), 
	(3, 1, 2, 1, 10000, '2022-11-13', '2022-11-19', '2022-11-20'), -- (구독중), (오늘만료) 
	(4, 1, 2, 5, 30000, '2022-11-17', '2022-11-23', '2022-11-24'), -- (구독중), (만료 7일 전)
	(5, 1, 2, 6, 40000, '2022-09-14', '2022-10-13', '2022-10-20'), -- (구독만료)
	(6, 1, 2, 3, 5000, '2022-10-12', '2022-10-13', '2022-10-12'), -- (구독만료)
	(7, 1, 2, 4, 5000, '2022-10-25', '2022-11-24', '2022-11-25'), -- (구독중), (만료 7일 전)
	(8, 1, 2, 7, 25000, '2022-09-20', '2022-10-19', '2022-10-20'),
	(9, 1, 2, 7, 25000, '2022-10-20', '2022-11-19', '2022-11-20'), -- (구독중), (오늘만료)
	(10, 1, 2, 8, 15000, '2022-09-23', '2022-10-22', '2022-10-23'),
	(11, 1, 2, 8, 15000, '2022-10-23', '2022-11-22', '2022-11-23'); -- (구독중), (만료 7일 전)