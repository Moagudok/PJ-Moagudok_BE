import json

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from sharedb.models import Product

from .serializers import ProductSerializer

# Create your views here.
STANDARD_NUM_OF_PRODUCTS = 10

from utils import (get_userinfo, get_monthly_payment_by_year,
                   get_daily_payment_by_month, get_product_newbie)


class ProductView(APIView):
    # url = /seller/product/1?page=1&filter="views"&?"group_name"="돼지좋아"
    def get(self, request: Request, seller_id) -> ProductSerializer:

        page_num = int(request.query_params["page"])
        filter = request.query_params["filter"]
        firter_list = ["recent", "views", "subscribers"]

        # 만약 판매중인 구독 상품에서 그룹을 누른다면 그룹별 수정 페이지로 전환
        group_name = request.query_params.get("group_name", None)

        if group_name:
            sellers_product_all_query = Product.objects.select_related("seller").filter(
                seller=seller_id, product_group_name=group_name)
            is_grouped = True
        else:
            sellers_product_all_query = Product.objects.select_related("seller").filter(
                seller=seller_id)
            is_grouped = False
        sellers_product_count = sellers_product_all_query.count()

        # 최대 페이지 수, 필터링 단어 제한
        total_page = sellers_product_count // STANDARD_NUM_OF_PRODUCTS + 1
        if total_page < page_num or filter not in firter_list:
            return Response({"detail": "해당 페이지에 데이터가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

        # filtering
        if filter == "recent":
            filtering_product_query = sellers_product_all_query.order_by(
                "-update_date")
        elif filter == "views":
            filtering_product_query = sellers_product_all_query.order_by(
                "-views")
        elif filter == "subscribers":
            filtering_product_query = sellers_product_all_query.order_by(
                "-num_of_subscribers")

        # Pagenation
        if sellers_product_count <= STANDARD_NUM_OF_PRODUCTS:
            pagenated_sellers_product_query = filtering_product_query
        else:
            pagenated_sellers_product_query = filtering_product_query[(
                page_num-1) * STANDARD_NUM_OF_PRODUCTS: (page_num-1) * STANDARD_NUM_OF_PRODUCTS + STANDARD_NUM_OF_PRODUCTS]
        sellers_product_serializer = ProductSerializer(
            pagenated_sellers_product_query, many=True).data
        return Response({
            "sellers_products": sellers_product_serializer,
            "total_page": total_page,
            "is_grouped": is_grouped
        }, status=status.HTTP_200_OK)
        
        
class DashBoardSalesInfoView(APIView):
    def get(self, request: Request, year: int, month: int) -> Response:

        this_year_total_sales = 0
        this_month_total_sales = 0
        seller_id = get_userinfo(request)

        # 해당 연도의 전체 매출 구하기
        this_year_total_sales_response = get_monthly_payment_by_year(
            seller_id, year)
        this_year_total_sales_dict = json.loads(
            this_year_total_sales_response.text)
        for key, val in this_year_total_sales_dict.items():
            this_year_total_sales += val

        # 해당 연도, 해당 월에 일별 매출 구하기
        response = get_daily_payment_by_month(seller_id, year, month)
        daily_sales_dict = json.loads(response.text)

        # 해당 월에 수익 구하기
        for key, val in daily_sales_dict.items():
            this_month_total_sales += val

        return Response({"daily_sales_dict": daily_sales_dict, "this_year_total_sales": this_year_total_sales, "this_month_total_sales": this_month_total_sales}, status=status.HTTP_200_OK)


class DashBoardCustomerINfoView(APIView):
    def get(self, request: Request) -> Response:

        seller_id = get_userinfo(request)

        new_bie_response = get_product_newbie()
        new_bie_dict = json.loads(new_bie_response.text)

        query_count_list = []
        query_set = Product.objects.select_related(
            "seller").filter(seller=seller_id)
        all_count = 0

        for query in query_set:
            all_count += query.num_of_subscribers
            product_percent_dict = {
                "product_name": query.product_name, "subscribe_percent": query.num_of_subscribers}
            query_count_list.append(product_percent_dict)

        for index, query in enumerate(query_count_list):
            if query["subscribe_percent"]:
                query_count_list[index]["subscribe_percent"] = round(
                    query["subscribe_percent"] / all_count, 2) * 100
            else:
                query_count_list[index]["subscribe_percent"] = 0
        return Response({"query_count_list": query_count_list, "new_bie_dict": new_bie_dict}, status=status.HTTP_200_OK)
