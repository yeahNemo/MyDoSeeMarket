from django.contrib import admin
from django.contrib.admin import ModelAdmin

from django.db import models

# Create your models here.
from django.db.models import CASCADE


class qiao(models.Model):
    name = models.CharField(max_length=120, verbose_name="类型编号")
    age = models.IntegerField(verbose_name="类型名称")

    def __str__(self):
        return self.name


class regist(ModelAdmin):
    pass


class qiao2(models.Model):
    name = models.CharField(max_length=120, verbose_name="桥梁名称")
    age = models.IntegerField(verbose_name="寿命")
    waijian = models.ForeignKey(qiao, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class haizi(models.Model):
    name = models.CharField(max_length=120, verbose_name="name")
    qiao = models.ForeignKey(qiao, on_delete=CASCADE)
    qiao2 = models.ForeignKey(qiao2, on_delete=CASCADE)

    class Meta:
        unique_together = (("qiao", "qiao2"),)


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    stu = models.ForeignKey("Student",verbose_name="学生",related_name="stu2",on_delete=CASCADE)


# 订单明细表
class OrderDetail(models.Model):
    orderDetail_code = models.AutoField(verbose_name="订单明细编号", primary_key=True)
    order_count = models.CharField(max_length=255, verbose_name="订购数量")
    order_code = models.ForeignKey("Order",on_delete=CASCADE, verbose_name="订单号")
    supply_code = models.ForeignKey("Supply", on_delete=CASCADE, verbose_name="上架的供应商品", null=True)
    def __str__(self):
        return str(self.pk)
    class Meta:
        verbose_name_plural = '订单明细'
        verbose_name = '订单明细'

# 客户信息表
class CustomerInfo(models.Model):
    customer_code = models.AutoField(verbose_name="客户编号", primary_key=True)
    customer_name = models.CharField(max_length=255, verbose_name="客户姓名")
    customer_phone = models.CharField(max_length=255, verbose_name="客户电话")
    customer_address = models.CharField(max_length=255, verbose_name="客户地址")
    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name_plural = '客户信息'
        verbose_name = '客户信息'


# 订单表
class Order(models.Model):
    order_code = models.AutoField(verbose_name="订单编号", primary_key=True)
    order_totalCost = models.CharField(max_length=255, verbose_name="订单总金额")
    order_date = models.DateTimeField(verbose_name="订购时间",auto_now=True)
    order_postalCode = models.CharField(max_length=255, verbose_name="邮编")
    customer_code = models.ForeignKey(CustomerInfo,on_delete=CASCADE,verbose_name="客户", null=True)

    def __str__(self):
        return str(self.order_code)

    class Meta:
        verbose_name_plural = '订单'
        verbose_name = '订单'



# 商品供应商表
class ItemSupplier(models.Model):
    supplier_code = models.CharField(max_length=255, verbose_name="供应商编号", primary_key=True)
    supplier_name = models.CharField(max_length=255, verbose_name="供应商名称")
    supplier_contact = models.CharField(max_length=255, verbose_name="供应商联系人")
    supplier_phone = models.CharField(max_length=255, verbose_name="供应商电话")
    supplier_profile = models.CharField(max_length=255, verbose_name="供应商简介")
    def __str__(self):
        return self.supplier_name

    class Meta:
        verbose_name_plural = '商品供应商'
        verbose_name = '商品供应商'


# 商品分类分级表
class ItemClassify(models.Model):
    classify_code = models.CharField(max_length=255, verbose_name="分类编号", primary_key=True)
    classify_name = models.CharField(max_length=255, verbose_name="分类名称")
    classify_icon = models.CharField(max_length=255, verbose_name="分类图片路径")
    # ？如何进行自关联？用 self
    # classify_super = models.ForeignKey("self", on_delete=models.CASCADE, verbose_name="父级分类")
    classify_super = models.CharField(max_length=255,verbose_name="父级编号",default='0')

    def __str__(self):
        return self.classify_name

    class Meta:
        verbose_name_plural = '商品分类分级'
        verbose_name = '商品分类分级'


# 商品规格 表
class ItemSpec(models.Model):
    spec_code = models.CharField(max_length=255, verbose_name="商品规格编号", primary_key=True)
    spec_name = models.CharField(max_length=255, verbose_name="商品规格名称")

    def __str__(self):
        return self.spec_name

    class Meta:
        verbose_name_plural = '商品规格'
        verbose_name = '商品规格'


# 商品品牌表
class Brand(models.Model):
    brand_name = models.CharField(max_length=255, verbose_name="品牌名称")
    brand_site = models.CharField(max_length=255, verbose_name="品牌官网")
    brand_icon = models.CharField(max_length=255, verbose_name="品牌图片路径")
    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name_plural = '商品品牌'
        verbose_name = '商品品牌'


# 商品表
class Item(models.Model):
    item_code = models.CharField(max_length=255, verbose_name="商品代码", primary_key=True)
    item_name = models.CharField(max_length=255, verbose_name="商品名称")
    # item_spec = models.CharField(max_length=255, verbose_name="商品规格")
    item_model = models.CharField(max_length=255, verbose_name="商品型号")
    item_unit = models.CharField(max_length=255, verbose_name="计量单位")
    item_marketPrice = models.CharField(max_length=255, verbose_name="市场价")
    item_costPrice = models.CharField(max_length=255, verbose_name="成本价")
    item_icon = models.CharField(max_length=255, verbose_name="略缩图路径")
    item_introduction = models.CharField(max_length=255, verbose_name="商品介绍")
    item_stock = models.CharField(max_length=255, verbose_name="商品库存")
    # 商品 商品品牌之间的联系
    item_brand = models.ForeignKey(Brand, on_delete=CASCADE, verbose_name="商品品牌")
    # 商品 商品分类分级的联系
    item_classify = models.ForeignKey(ItemClassify, on_delete=CASCADE, verbose_name="商品分类分级")
    # 商品 商品规格 多对多隐藏规格表 未加依赖 以更新为中间表
    # item_spec = models.ManyToManyField("ItemSpec")
    # 商品 商品供应商 多对多 我觉得应该还是 显式地 构造中间表！否则中间表插入数据将变得异常困难！
    # item_supplier = models.ManyToManyField("ItemSupplier")

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name_plural = '商品'
        verbose_name = '商品'


# 多对多 商品--商品规格
class ItemToItemSpec(models.Model):
    spec_value = models.CharField(max_length=255, verbose_name="规格值")
    item_code = models.ForeignKey(Item, on_delete=CASCADE, verbose_name="商品代码")
    spec_code = models.ForeignKey(ItemSpec, on_delete=CASCADE, verbose_name="规格编号")

    def __str__(self):
        return str(self.id)

    class Meta:
        unique_together = (("item_code", "spec_code"),)
        verbose_name = "商品--商品规格"
        verbose_name_plural = "商品--商品规格"


# 供应表 拥有复杂的依赖关系
class Supply(models.Model):
    true_price = models.CharField(max_length=255, verbose_name="真实价格")
    item_code = models.ForeignKey(Item, related_name="myItem", on_delete=CASCADE, verbose_name="商品编号")
    supplier_code = models.ForeignKey(ItemSupplier, on_delete=CASCADE, verbose_name="供应商编号")
    item_spec = models.ForeignKey("ItemToItemSpec", related_name="test", on_delete=CASCADE, verbose_name="商品规格")

    def __str__(self):
        # 通过外键正向查询到关联的 item 的 item_name
        return self.item_code.item_name
        # return ((Item.objects.filter(item_code = self.item_code_id)).first()).item_name
        # return self.item_code_id

    class Meta:
        unique_together = (("item_code", "supplier_code", "item_spec"),)
        verbose_name = "正在供应的商品"
        verbose_name_plural = "正在供应的商品"


class regist2(ModelAdmin):
    pass


class regist3(ModelAdmin):
    pass


class Register01(ModelAdmin):
    pass


class Register02(ModelAdmin):
    pass


class Register03(ModelAdmin):
    pass


class Register04(ModelAdmin):
    pass


class Register05(ModelAdmin):
    pass


class Register06(ModelAdmin):
    pass


class Register07(ModelAdmin):
    pass


class Register08(ModelAdmin):
    pass


class Register09(ModelAdmin):
    pass


class Register10(ModelAdmin):
    pass


class Register11(ModelAdmin):
    pass


admin.site.site_header = '电商系统'
admin.site.site_title = '电商系统'
admin.site.index_title = '电商系统'

# admin.site.register (Student, regist)
# admin.site.register(Course, regist2)
# admin.site.register(haizi, regist3)
admin.site.register(OrderDetail, Register01)
admin.site.register(Order, Register02)
admin.site.register(CustomerInfo, Register03)
admin.site.register(ItemSupplier, Register04)
admin.site.register(ItemClassify, Register05)
admin.site.register(ItemSpec, Register06)
admin.site.register(Brand, Register07)
admin.site.register(Item, Register08)
admin.site.register(ItemToItemSpec, Register09)
admin.site.register(Supply, Register10)
# admin.site.register(OrderDetailToSupply, Register11)
