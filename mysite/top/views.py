from django.http import HttpResponse
from mysite.top.models import Bug

# Create your views here.


# 添加数据方法
def add_bug(request):
    # 第一种方式插入数据
    tcpg = Bug(title='bug title', description='bug description3', task=1, category=1, state=1, owner=1, create_time=1)
    tcpg.save()   # 一定要记得保存，不然数据无法插入进去
    # # 第二种方式插入数据
    # lzj = Bug()
    # lzj.bug_name = '辣子鸡'
    # lzj.bug_author = '张三'
    # lzj.bug_money = '30'
    # lzj.bug_star = '超级美味'
    # lzj.save()   # 一定要记得保存，不然数据无法插入进去
    # # 第三种方式插入数据（该方法不需要保存，会自动保存）
    # sltds = Bug.objects.create(bug_name='酸辣土豆丝',bug_author='一一',bug_money=25,bug_star='美味')
    # # 第四种方式插入数据（该方法不需要保存，且不会插入重复数据）
    # clbc = Bug.objects.get_or_create(bug_name='醋溜白菜',bug_author='李四',bug_money=25,bug_star='很美味')
    return HttpResponse("添加数据成功")


# 查询数据方法
def select_bug(request):
    # 查询表中的所有数据
    rs = Bug.objects.all()
    print(rs)
    # 根据筛选条件查询出表中的单挑数据（注意如果条件查询出多条数据，使用该语句会报错）
    rs1 = Bug.objects.get(title='bug title1')
    print(rs1)
    # 根据筛选条件查询出表中的数据（可查询出多条）
    rs2 = Bug.objects.filter(state_id="1")
    rs2 = list(rs2)
    print(rs2)
    return HttpResponse("查询数据成功")


# 更新数据方法
def update_bug(request):
    # 根据条件查询后再修改再保存
    clbc = Bug.objects.get(title='bug')
    clbc.bug_star = '难吃'
    clbc.save()
    # 直接修改所有的数据
    Bug.objects.all().update(description='bug')
    return HttpResponse("修改数据成功")


# 删除数据方法
def delete_bug(request):
    Bug.objects.get(id=1).delete()
    return HttpResponse("删除数据成功")
