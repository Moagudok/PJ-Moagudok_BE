# 3. ENV Settings (After App settings)
scp -i /c/aws_keys/moagudok_production.pem -r C:/Users/urse/Desktop/vscode/Django_Project/moagudok/SellerService/.local.env ubuntu@ec2-54-180-145-47.ap-northeast-2.compute.amazonaws.com:~/moagudok/SellerService/

scp -i /c/aws_keys/moagudok_production.pem -r C:/Users/urse/Desktop/vscode/Django_Project/moagudok/LookupService/.local.env ubuntu@ec2-54-180-145-47.ap-northeast-2.compute.amazonaws.com:~/moagudok/LookupService/

scp -i /c/aws_keys/moagudok_production.pem -r C:/Users/urse/Desktop/vscode/Django_Project/moagudok/AuthService/.local.env ubuntu@ec2-54-180-145-47.ap-northeast-2.compute.amazonaws.com:~/moagudok/AuthService/

scp -i /c/aws_keys/moagudok_production.pem -r C:/Users/urse/Desktop/vscode/Django_Project/moagudok/SearchService/.local.env ubuntu@ec2-54-180-145-47.ap-northeast-2.compute.amazonaws.com:~/moagudok/SearchService/

scp -i /c/aws_keys/moagudok_production.pem -r C:/Users/urse/Desktop/vscode/Django_Project/moagudok/PaymentService/payment/.pro.env ubuntu@ec2-54-180-145-47.ap-northeast-2.compute.amazonaws.com:~/moagudok/PaymentService/payment/

scp -i /c/aws_keys/moagudok_production.pem -r C:/Users/urse/Desktop/vscode/Django_Project/moagudok/ChattingService/secure.json ubuntu@ec2-54-180-145-47.ap-northeast-2.compute.amazonaws.com:~/moagudok/ChattingService/

scp -i /c/aws_keys/moagudok_production.pem -r C:/Users/urse/Desktop/vscode/Django_Project/moagudok/MailService/.env ubuntu@ec2-54-180-145-47.ap-northeast-2.compute.amazonaws.com:~/moagudok/MailService/