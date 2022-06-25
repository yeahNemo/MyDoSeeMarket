from django.http import HttpResponse
from index.models import Student

def testdb(request):
    listAll = Student.objects.all()
    response=""
    print(listAll)
    for var in listAll:
        response+=var.name+" "
    return HttpResponse("<p>"+response+"</p>")

def testdbAdd(req):
    SQL = Student(name='Link',id='2')
    SQL.save()
    return HttpResponse("记录添加成功")

def testdbRmv(req):
    record = Student.objects.get(id='2')
    record.delete()
    return HttpResponse("删除记录成功")



