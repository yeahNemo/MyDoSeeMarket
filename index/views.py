from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from index import models
import json
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import auth
from django.contrib.auth.models import User


# todo 添加未登录限制访问
# Create your views here.
def index(request):
    return render(request, "index.html")


def btTest(request):
    return render(request, "btTest.html")


def allItems(request):
    resultSet = models.Item.objects.all()
    print(type(resultSet))
    data = []
    for i in range(len(resultSet)):
        data.append(model_to_dict(resultSet[i]))
    json_data = json.dumps(data, ensure_ascii=False)
    return HttpResponse(json_data)


def itemPage(request):
    # itemList = models.Item.objects.all()
    supplyList = models.Supply.objects.all()
    return render(request, "itemPage.html", locals())


def test02(request):
    # from django.contrib.auth.models import User
    # User.objects.create_user(username='morney', password='123')
    return HttpResponse("HI")


@login_required
def itemToOrder(request):
    # 使用查询语法进行查询
    supply = models.Supply.objects.all().values("true_price", "item_code__item_name", "item_code__item_stock",
                                                "item_code_id")
    """
    objects.all().values(....) 和 models.Supply.objects.all() 返回值不同
    前者返回一个 dict 后者返回QuerySet 需要 model_to_dice() 进行转换
    """
    data = []
    # 以 json 格式返回我的可够商品
    for s in supply:
        s["orderCount"]=0
        # print(s)
        data.append(s)
    json_data = json.dumps(data, ensure_ascii=False)
    # print(json_data)
    return HttpResponse(json_data)


def orderItem(request):
    id = request.GET.get("id")
    number = request.GET.get("number")
    ordercode = request.GET.get("ordercode")
    # print(id)
    # print(number)
    # print(ordercode)

    supply = models.Supply.objects.filter(item_code__item_code=request.GET.get("id")).first()
    # 1、通过 ordercode 拿到订单号
    order = models.Order.objects.filter(order_code=ordercode).first()
    print(model_to_dict(order))
    # 2、添加 orderdetail 订单明细
    orderdetail = models.OrderDetail.objects.create(order_count=number,order_code=order,supply_code=supply)
    # 加总金额
    order = models.Order.objects.filter(order_code=ordercode).first()
    models.Order.objects.filter(order_code=ordercode).update(order_totalCost=int(number) * int(supply.true_price) + int(order.order_totalCost))
    # 减库存
    item = models.Item.objects.filter(item_code=supply.item_code.item_code).first()
    # 很奇怪 更新操作只能像这样链式调用 否则会报错 找不到update方法
    stockUpdate = str(int(item.item_stock) - int(number))
    models.Item.objects.filter(item_code=supply.item_code.item_code).update(item_stock=str(int(item.item_stock) - int(number)))
    return JsonResponse({"stockUpdate": stockUpdate})


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if (user == None):
        return HttpResponse("密码错误！")
    # 保持登录状态
    django_login(request, user)
    nameDict = {"username": user.username}
    return render(request, "customerOrder.html", nameDict)


def loginPage(request):
    return render(request, "login.html")


@login_required
def createOrder(request):
    user_id = request.session.get("_auth_user_id")
    user = models.CustomerInfo.objects.filter(customer_code=user_id).first()
    # 添加订单
    order = models.Order.objects.create(order_totalCost=0, order_postalCode="10011", customer_code=user)
    return JsonResponse({"ordercode":order.order_code})

@login_required
def allOrder(request):
    orders = models.Order.objects.all().values("order_code","order_totalCost") # todo order_date是无法序列化为json 因此前端无法接收
    data = []
    for o in orders:
        data.append(o)
    json_data = json.dumps(data, ensure_ascii=False)
    # print(json_data)
    return HttpResponse(json_data)

@login_required
def orderPage(request):
    return render(request, "orders.html")