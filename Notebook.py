

# 第 1 关：输出与注释 (Output & Comments)

# 核心： 让程序发出声音，同时给自己留小纸条。
# 这是单行注释，电脑会假装看不见我
"""
这是多行注释
可以写长篇大论的笔记
"""

"""
print("Hello Python!")  # 打印字符串（带引号）
print(2026)            # 打印数字（不带引号）
"""
# 第二关：变量 (Variables)
# 核心： 给数据取个名字，方便以后反复调用。
"""
name = "代码特工"    # 字符串变量
level = 1           # 整数变量
health = 95.5       # 浮点数变量

print(name)         # 通过名字找到数据
print(level + 5)    # 变量可以参与运算
"""

# 第 3 关：数据类型 (Data Types)

# 核心： 搞清楚数据的“性格”，文本和数字不能混为一谈。
"""
a = "666"  # 这是一个【字符串】，长得像数字的文本
b = 666    # 这是一个【整数】，真正的数字

# 尝试一下：
# print(a + 1)  # 报错！文本不能加数字
print(b + 1)    # 正常输出 667
"""

# 第 4 关：交互与类型转换 (Input & Casting)

# 核心： 获取用户的指令，并把它们转化成正确的格式。这是你写 if 和 while 之前的必经之路。
"""
# 1. 获取输入
user_input = input("请输入你的幸运数字：") 

# 2. 揭秘：此时 user_input 的类型是字符串 "10" 
print("你输入的数据类型是：", type(user_input))

# 3. 强制转换：不然没法做数学题
lucky_number = int(user_input) 
print(f"你的数字加 10 以后是：{lucky_number + 10}")
"""

# 第 5 关：逻辑判断 (If-Else) —— 让程序学会做选择题。
"""
limit = 18
age_input = input("请输入你的年龄：")
age = int(age_input)
if age >= limit:
  print("验证通过") 
  print("欢迎进入成年人的编程世界")
elif age>=12:
  print("你是青少年，建议在家长的陪同下学习")
else:
  print("小朋友，先去喝杯牛奶再来吧")
print("判断结束")
# > (大于), < (小于)
# >= (大于等于), <= (小于等于)
# == (等于 —— 注意是两个等号！ 一个等号是赋值，两个才是比较)
# != (不等于)
# += (加等于，比如 a += 1 等同于 a = a + 1)Python 里几乎所有的数学运算都有这种缩写形式
练习
score_input  = input("请输入你的分数：")
score = int(score_input)
if score >= 90:
  print("优秀")
elif 60 <= score < 90:
  print("合格")
else:
  print("不合格,加油哦。")
"""

# 第 6 关：循环入门 (For Loops) —— 让程序自动重复执行任务。
"""
print("我们要数五个数")
for i in range(5):
  print("当前数字是:", i)
print("-"*20)
"""
"""
number_input = input("请输入一个数字:")
number = int(number_input)
for i in range(1,11):
  print(number,"*",i ,"=",number*i)

#加号拼接   print("分数为:" + str(score))      是       拼接紧凑，没有多余空格
#逗号分隔   print("分数为:", score)    否       简单省事，但会自动加空格
#f-string       print(f"分数为:{score}")   否       最推荐，既简洁又精准
"""

# 第 7 关：条件循环 (While Loops) —— 只要条件满足，就一直运行下去。
"""
count = 5
while count > 0:
  print(f"当前数字是:{count}")
  count = count - 1
print("发射")
"""

# 第 8 关：列表 (Lists) —— 学习如何用一个变量装下一堆数据。
"""
#创建： 使用方括号 []，元素间用逗号隔开。
#访问： 计算机数数是从 0 开始的（索引）。
bag = []
bag.append("手机")
bag.append("电脑")
print(f"当前背包:{bag}")
bag[0]= "手电"
print(f"升级后:{bag}")
count = len(bag)
#[]     方括号     列表专用。创建列表或找位置。  bag[0]
#()     圆括号     函数专用。下达动作指令。    len(bag)
#{}     花括号     f-string 专用。在字符串里插变量。   f"{bag}"
"""

# 第 9 关：函数 (Functions) —— 把常用的代码打包，随调随用。
"""
def check_bag(owner_name, bag_list): 
#def 关键字：告诉 Python，“我要开始定义一个技能了”。括号里的名字：叫参数。它们就像占位符，等你在调用时往里传真正的物品
  print(f"---{owner_name}的背包检查中---")
  if len(bag_list) == 0:
    print("空空如也")
  else:
    print(f"里面的宝贝有:{bag_list}")

my_stuff = ["手机","电脑"]
check_bag("小明",my_stuff)

def add_numbers(a,b):
  result = a + b
  return result # return 的意思是：把结果吐出来，给外面用
#并不是所有函数都要 return。如果你的函数只是为了执行一个动作（比如 print 打印一句话），而不是为了计算一个结果，那就不需要 return。
sum_result = add_numbers(5,10)
print(f"计算结果是{sum_result}")

def make_hero(name,weapon):
  print(f"---{name}装备了{weapon}出发了！")
name = ""
weapon = ""
if name == "":
  name = input("请输入你的名字")
  weapon = input("请选择你的武器")
make_hero(name,weapon)
"""

# 第 10 关：综合实战 (Final Project) —— 独立敲出一个“数字炸弹”或“小游戏”。
"""
import random #random库
def start_game():
  secret_number = random.randint(1,100)
  guess = 0
  attempts = 0
  print("---💣欢迎来到数字炸弹游戏💣---")

  while guess != secret_number:
    user_input = input("请输入1到100之间的数字")
    if user_input == "":
      print("别发呆了，快输入数字！")
      continue  #continue (跳过本次，重新开始)，程序跑在 while 循环里，碰到 continue 时，它会立刻跳过下面所有的代码，直接回到 while 的开头重新检查条件
    guess = int(user_input)
    attempts =  attempts + 1
    if guess > secret_number:
      print("太大了，再小一点")
    elif  guess < secret_number:
      print("太小了，再大一点")
    else:
       print(f"🎉恭喜你猜对了！答案是{secret_number}，你用了{attempts}次猜中了！")        
start_game()
"""

# 第 11 关：字典 (Dictionaries) —— 像查字典一样存数据
# 语法： person = {"name": "小明", "age": 18, "weapon": "激光剑"}  key: value（Value（值）：什么都可以放！，Key（键）它必须是**不可变（Immutable）且可哈希（Hashable）**的）
"""
hero = {"名字":"齐天大圣", "生命值":"100", "攻击力":"50"}
print(f"英雄的名字是:{hero['名字']}")
# 1. 访问数据
print(f"玩家姓名: {player['name']}")
# 2. 修改数据
player["level"] = 11
# 3. 添加新数据
player["exp"] = 500
"""

# 第 12 关：布尔类型在数据录入分析中的应用
"""
score_list = [78, 55, 90, 45]
for score in score_list:
  is_good = score >= 60 #score >= 60这个判断会得出 True 或 False 然后赋值给is_good
  if is_good:
    print(f"{score}是合格的")
  else:
    print(f"{score}不合格")
"""

# 第 13 关：元组在数据录入分析中的应用
"""
programs = ["项目A", "项目B", "项目C"]
profit_list = [[10000, 20000, 15000, 30000], [5000, 10000, 15000, 20000],  [20000, 25000, 30000, 35000]]
for program in range(len(programs)): #range(len(programs)) 会生成 0, 1, 2，对应三个项目的索引。
  print(f"{programs[program]}的收益数据是{profit_list[program]}")
"""

# 第 14 关：集合在数据录入分析中的应用
"""
#集合是一个无序且不包含重复元素的容器，就好像一个神奇的盒子，相同的东西放进去只会保留一个，而且里面的东西没有特定顺序。
#集合的创建,可以使用花括号 {} 或者 set() 函数来创建集合。

#fruits_list = ['苹果', '香蕉', '苹果', '橙子', '香蕉']
#fruits_set = set(fruits_list)
#print(fruits_set)

#列表的删除 
#del() del 语句可以删除列表中的指定元素，通过索引来确定要删除的元素位置
#pop() pop方法默认删除并返回列表的最后一个元素。也可以指定索引删除并返回指定位置的元素。
#remove() remove方法用于删除列表中指定值的元素。如果列表中有多个相同值的元素，它只会删除第一个。如果元素不存在，会引发 ValueError 错误。
#集合的删除
#remove() remove方法用于删除列表中指定值的元素。如果元素不存在，会引发 KeyError 错误。
#discard() discard 方法也用于删除集合中的指定元素，但与 remove() 不同的是，如果元素不存在，不会引发错误。
#pop() pop() 方法用于随机删除并返回集合中的一个元素。因为集合是无序的，所以不能指定删除某个位置的元素。每次运行 pop() 方法返回的元素可能不同。

customer_ids = [101, 102, 101, 103, 102, 104]
ids_set= set(customer_ids)
ids_set.add(105)
print(str(ids_set))
"""

# 第 15 关 程序的“说明书”：模块化与文件处理
"""
1. 模块化 (Modules) 
# 1.数据的“百宝箱”：字典 (Dictionaries)
def calculate_sum_avg_score(student):
  math = student["数学成绩"]
  chinese = student["语文成绩"]
  sum_score = math + chinese
  avg_score = sum_score / 2
  return sum_score, avg_score
#当你调用一个返回多个值的 Python 函数时（比如 return sum_score, avg_score），实际上函数返回的是一个元组 (Tuple)。
#要获取其中的某一个结果，通常有以下 3 种常用的方法：
#1. 使用变量解包（最常用）
#即使你只需要一个值，也可以同时接收它们，然后只使用你感兴趣的那个。
#2. 使用占位符 _（最推荐）
#在编程习惯中，如果你想忽略某个返回值，可以使用下划线 _ 作为变量名。这告诉阅读代码的人：“我知道这里有个返回值，但我不需要它”。
#3. 使用索引下标
#因为返回的是元组，你可以像访问列表一样通过索引 [0] 或 [1] 来获取特定的值。
#[0] 对应第一个返回值
#[1] 对应第二个返回值#目前你的代码只要程序一关闭，数据就消失了。进阶的目标是：让你的程序具备“记忆力”，并且把臃肿的代码拆分成易于管理的小块。
student = {"名字":"小明", "数学成绩":98, "语文成绩":60}
sum_score, avg_score = calculate_sum_avg_score(student)
#print("总分："+ str(sum_score)) 
print(f"总分：{sum_score}")
print(f"平均分：{avg_score}")
"""

"""
2. 文件操作 (File I/O)
核心语法：with open(...)

with open("scores.txt", "w", encoding="utf-8") as f:
    f.write("小明,98,60\n")
    f.write("小红,95,85\n")
print("成绩已成功保存到 scores.txt")


1. with open("scores.txt", "w", encoding="utf-8") as f:

with - 它是 Python 的“管家”。有了它，当你写完缩进里的代码，Python 会自动帮你把文件合上。
open - 打开 
"scores.txt" - 文件名 
"w" - 这是 Write（写） 的缩写  'w'：写入模式。会覆盖原文件，如果文件不存在就新建。
                            'a'：追加模式。在文件末尾增加内容，不删除旧内容。
                            'r'：读取模式。只能读取文件内容，不能修改。
encoding="utf-8" - 这叫“编码”。因为电脑只懂 0 和 1，而我们要写中文，utf-8 能保证中文不乱码。
as f - 这是给打开的这个文件起个临时外号，叫 f。后面我们对 f 操作，就是对这个文件操作。

2. f.write("小明,98,60\n")

f.write("内容") - 这就是把括号里的字符串“写”进刚才打开的那个 f（笔记本）里
\n - 换行符。就像按下键盘上的“回车”键，把光标移到下一行。
print("请输入你想保存的内容（输入 'q' 退出)")
with open("note.txt","a",encoding="utf-8") as f:
  while True:
    text_input = input(">")
    if text_input  == "q":
      break
    f.write(text_input+"\n")
"""

# 第 16 关：异常处理
# 使用 try - except 语句来处理异常
"""
try:
  num = 10
  result = num / 0  #try 块里的 num / 0 会引发 ZeroDivisionError 异常
except ZeroDivisionError:#当异常发生时，程序会立即跳转到 except 块执行其中的代码，而不会导致程序崩溃
  print("不能除以零")
else:              #else 子句在 try 块没有引发任何异常时执行。
  print(f"结果是: {result}")
finally:           #finally 子句无论 try 块中是否引发异常，都会执行。
  print("无论是否找到文件，都会执行这里")
"""
"""
练习
def divide_numbers(a, b):
  try:
    result = a/b
  except ZeroDivisionError:
     print("除数不能为零")  
  except TypeError:
     print("参数类型错误，只能接受数字")
  else:
    return result

a = int(input("请输入一个数字>"))
b = int(input("请输入另一个数字>"))
print(divide_numbers(a, b))
"""

# 第 17 关：迭代器与生成器
# 是处理数据流的核心工具。它们允许我们高效地遍历大型数据集，而无需将其全部加载到内存中。
"""
# 一 迭代器 (Iterator)
# __iter__() ： 返回迭代器对象本身
# __next__() ： 返回容器的下一个元素。如果没有元素了，则抛出 StopIteration 异常

my_list = [1, 2, 3, 4, 5]#可迭代对象，在 Python 中，列表是 Iterable
my_iterator = iter(my_list) #这会创建一个 迭代器对象 (Iterator)。对象不包含数据副本，它只包含一个指向原数据的指针和一个记录当前位置的计数器，一旦你有了 my_iterator你就获得了一个“翻页器”， 它的核心行为遵循以下逻辑A. 使用 next() 访问，每次对 my_iterator 调用 next()，它都会执行两件事：1.返回指针当前指向的元素。2.将指针移动到下一个位置。 
print(next(my_iterator))  #迭代器是一次性的。当指针移动到列表末尾后，再次调用 next() 会抛出 StopIteration 异常。这告诉 Python（或 for 循环）遍历已经结束。
"""
"""
练习1
my_list = [5, 10, 15, 20]
my_iterator = iter(my_list)
print(next(my_iterator))
print(next(my_iterator)) 
print(next(my_iterator))
print(next(my_iterator))
练习2
def simulate_iterator(data):
  index  = 0
  while index < len(data):
    yield data[index]
    index += 1
words = "who are you!"
my_iterator = simulate_iterator(words)
for char in my_iterator:  #********
  print(char)
#for 循环的“兼容性”逻辑
#场景 A：你丢给它一个列表 (my_list)
#1.for 发现这是个列表。
#2.for 伸手调用 iter(my_list)，列表给它派了一个全新的“翻页工人”（迭代器）。
#3.for 带着这个工人开始干活。
#场景 B：你丢给它一个迭代器 (my_iterator)
#for 发现这已经是个迭代器了。
#for 依然会习惯性地调用 iter(my_iterator)
#重点来了：迭代器的 __iter__ 方法会说：“别麻烦了，我就是那个工人，直接用我吧！”
#for 于是直接带着 my_iterator 开始干活
"""


# 二 生成器 (Generator)
# 生成器是一种特殊的迭代器，它使用 yield 关键字来生成值，而不是使用 return。生成器函数在每次调用 yield 时暂停执行

# 练习2
"""
def my_generator(n):
  for i in range(n):
    yield i+1  #yield 有点像 return，但它会暂停函数，下次调用时从暂停的地方继续。

n = 10 
print(next(my_generator(n)))


for num in my_generator(n):
  result = num * num
  print(result)
"""


# 第 18 关：装饰器（Decorators）
"""
def decorator_function(func): #是我们定义的装饰器函数，它接受一个函数 func 作为参数。
  def wrapper(): #在装饰器模式中，wrapper 是一个闭包函数。作用：
                 #包裹（Wrap）： 它把原始函数 func 包在里面。
                 #增强（Enhance）： 在不改变原有糖果（func）的情况下，通过外壳（wrapper）添加额外的逻辑（比如打印日志、计时、权限检查等）。
      print("在被装饰函数执行前执行的代码")
      func()
      print("在被装饰函数执行后执行的代码")
  return wrapper


def my_function():
  print("这是我的函数")
decorated_function = decorator_function(my_function)

decorated_function()  #调用函数

#语法糖形式: Python 提供了一种更简洁的方式来使用装饰器，即使用 @ 符号，上面的代码可以改写为：

# ==========================================
# @decorator_function
# def my_function():
#     print("这是我的函数")
#
# my_function()
# ==========================================
"""
"""
def decorator_function(func):
  def wrapper(a, b): #如果被装饰的函数有参数，装饰器的 wrapper 函数也需要接受相应的参数，并传递给被装饰函数。
      print(f"传入的参数是: {a}, {b}")
      result = func(a, b)
      print(f"函数执行结果是: {result}")
      return result #return 语句的作用域仅限于它所在的那个函数，这里如果调用wrapper没有返回值，那么add函数的返回值就无法传递给调用者，这是因为虽然func(a,b)的返回值被赋值给了result，但result的作用域仅限于wrapper函数内部，外部无法访问它。因此，如果wrapper函数没有返回result，那么add函数的返回值就会丢失。
  return wrapper


@decorator_function
def add(a, b):
  return a + b

result = add(3, 5)
"""
# wrapper 就像一个中转站，它不仅要传递输入（参数），还要传递输出（返回值）。

# 为了让装饰器更具通用性（即：让同一个装饰器能装饰任何函数，无论它有 0 个、2 个还是 100 个参数），Python 程序员通常会使用一对“魔法组合”：*args 和 **kwargs。

# 1. *args: args 是 arguments（参数）的缩写。前面的星号 * 是关键，它告诉 Python：“把所有传进来的位置参数打包成一个元组（Tuple）”
# 例子:
"""
def send_invitation(*args):
  for name in args:
      print(f"发送邀请函给: {name}")

send_invitation("小明", "小红", "老王") # args 此时是 ("小明", "小红", "老王")
"""
# 2. **kwargs: kwargs 是 keyword arguments（关键字参数）的缩写。双星号 ** 告诉 Python：“把所有以 key=value 形式传进来的参数打包成一个字典（Dictionary）”
"""
def show_profile(**kwargs):
    for key, value in kwargs.items():#.items() 是 Python 字典的一个方法，它返回一个视图对象，该对象包含字典的所有键值对，每个键值对以元组的形式表示。
        print(f"{key}: {value}")

show_profile(姓名="张三", 年龄=25, 城市="北京") # kwargs 此时是 {"姓名": "张三", "年龄": 25, "城市": "北京"}
"""
"""
def master_function(name, *args, **kwargs): #在函数定义中，它们的顺序必须是：普通参数 -> *args -> **kwargs。
    print(f"必填姓名: {name}")
    print(f"多余的普通参数: {args}")
    print(f"多余的关键字参数: {kwargs}")

master_function("Python", 1, 2, 3, 状态="学习中", 难度="中等")
"""
"""
#time 模块基础: 在 Python 里，time 模块用于处理时间相关的操作。其中常用的函数有 time.time()，它返回从 1970 年 1 月 1 日 00:00:00 UTC 到当前时刻所经过的秒数，返回值是一个浮点数，我们把这个值叫做时间戳。
#练习
def log_execution(func):#装饰器 log_execution，用于记录函数的执行时间。在被装饰函数执行前记录开始时间，执行后记录结束时间，并打印出函数执行花费的时间。
    def wrapper(a,b):
        import time #import 语句会放在 Python 文件的开头，这样可以使代码结构更清晰，一眼就能看出文件依赖的模块。
        start_time = time.time()
        print(f"开始时间是:{start_time}")
        result = func(a,b)
        end_time = time.time()
        print(f"结束时间是:{end_time}")
        elapsed_time = end_time - start_time
        print(f"函数执行花费的时间是:{elapsed_time}")
        return result
    return wrapper
  
@log_execution
def calculate_sum(a,b):
    result = a+b
    return result

result = calculate_sum(3,5)

#在 Python 里，函数内部的代码必须往右缩进（通常是 4 个空格）
#冒号是信号灯：每当你看到行尾有 :（如 def, if, for），下一行代码必须往右缩进。
#垂直对齐看归属：如果两行代码左边是对齐的，说明它们是平级的，按顺序执行。如果某行突然往左缩回去了（Unindent），说明上一个代码块结束了。    
"""

# 第 19 关：面向对象编程 - 类与对象基础

# 一、什么是面向对象编程（OOP）: 面向对象编程是一种编程范式，它将数据（属性）和操作数据的函数（方法）封装在一起，形成一个个独立的单元，这些单元被称为对象。可以把它想象成生活中的各种事物，比如一辆汽车，它有自己的颜色、品牌、速度等属性（数据），同时也有启动、加速、刹车等操作（方法）。通过这种方式，程序的结构更加清晰，代码的可维护性和可扩展性更强。

# 二、类（Class）: 一个类通常包含两个维度：

# 1. 属性 (Attributes/Properties)： 它是“什么”？（静态的数据）
# 例如： 颜色、品牌、最高时速、油箱容量。

# 2. 行为 (Methods/Functions)： 它能“做什么”？（动态的动作）
# 例如： 加速、刹车、鸣笛、开启雨刷。

# 三、对象（Object）： 类是蓝图，对象是根据蓝图制造出来的具体实物。也叫实例 (Instance)每个对象都拥有类定义的框架，但它们的数据是独立的：
# 对象 A： 红色、法拉利、时速 300km/h。
# 对象 B： 白色、特斯拉、时速 200km/h。

"""
#例如，我们要创建一个表示车的类：
        
#第一阶段：设计蓝图（定义类 class）: 定义了汽车长什么样，告诉电脑：“我要定义一个新物种，名字叫 Car”
class Car:
    def __init__(self, brand, color):
    #__init__ 是 Python 类的构造函数（Constructor）。
    #当你执行 my_car = Car("特斯拉", "黑色") 这行代码时，Python 内部会自动调用这个方法。
    #逻辑：它是“出生证明”。每辆车被造出来的一瞬间，电脑会自动调用这个函数。
    #参数：brand 和 color 是你要求在造车时必须提供的“配置信息”。
    #self 的逻辑：它是最关键的。你可以把它想成“这辆车自己”。self.brand = brand 的意思就是“把传进来的品牌名字，贴到这辆车自己的身上”。
        self.brand = brand  # 属性
        self.color = color  # 属性

    def drive(self):       # 行为
    #逻辑：定义车能做什么。它不需要额外的参数，因为它能通过 self 直接访问自己身上的 color 和 brand。
        print(f"这辆{self.color}的{self.brand}正在路上飞驰！")
              
# 第二阶段：工厂制造（实例化对象）
# 这就是【对象】：根据蓝图制造出具体的车
my_car = Car("特斯拉", "黑色")
neighbor_car = Car("比亚迪", "银色")

#第三阶段：投入使用（调用方法）
# 调用行为
my_car.drive() # 输出：这辆黑色的特斯拉正在路上飞驰！
"""

"""
#练习
class Dog:
      def __init__(self, name, breed):
          self.name = name
          self.breed = breed
      def bark(self):
          print(f"{self.name}在汪汪叫，它是一只{self.breed}")

my_dog = Dog("毛毛","博美")
my_dog.bark()
"""

# 第 20 关：面向对象编程 - 继承与多态
# 一、继承（Inheritance）:继承是面向对象编程中的一个重要概念，它允许一个类（子类）从另一个类（父类）获取属性和方法。通过继承，子类可以复用父类的代码，减少重复代码，同时还可以根据自身需求对继承来的属性和方法进行扩展或修改。
"""
#举例
#Animal 类是父类，它有一个 __init__ 方法用于初始化 name 属性，还有一个 speak 方法

class Animal:    
  def __init__(self, name):
      self.name = name
  def speak(self):
      print(f"{self.name} 发出声音")
    
#Dog 类是 Animal 类的子类，它们通过在类定义时将父类名放在括号内（如 class Dog(Animal):）来继承 Animal 类。

class Dog(Animal):
  def bark(self):
      print(f"{self.name} 汪汪叫")

#Dog类有自己特有的方法 bark。同时，它也继承了 Animal 类的 name 属性和 speak 方法。
dog = Dog("旺财")
dog.speak() 
dog.bark() 
"""

# 二、方法重写（Method Overriding）: 当子类需要对从父类继承来的方法进行不同的实现时，就可以在子类中重新定义这个方法，这就是方法重写。

"""
#举例
class Animal:    
  def __init__(self, name):
      self.name = name
  def speak(self):
      print(f"{self.name} 发出声音")

class Dog(Animal):
  def speak(self):
      print(f"{self.name} 汪汪叫")
      
class Cat(Animal):
  def speak(self):
      print(f"{self.name} 喵喵叫")
      
dog = Dog("旺财")
dog.speak()       #输出结果是：旺财 汪汪叫而不是旺财 发出声音，是因为Dog类重写了Animal 类的 speak 方法。

cat = Cat("咪咪")
cat.speak()       #输出结果是：咪咪 喵喵叫而不是咪咪 发出声音，是因为Cat类重写了Animal 类的 speak 方法。
"""

# 三、多态（Polymorphism）: 多态意味着同一个方法调用，根据对象的不同类型，会有不同的行为。在上面继承和方法重写的例子中就体现了多态。虽然 dog 和 cat 都是调用 speak 方法，但由于它们是不同类的对象，speak 方法表现出了不同的行为。
"""
class Animal:    
  def __init__(self, name):
      self.name = name
  def speak(self):
      print(f"{self.name} 发出声音")

class Dog(Animal):
  def speak(self):
      print(f"{self.name} 汪汪叫")

class Cat(Animal):
  def speak(self):
      print(f"{self.name} 喵喵叫")
    
#多态允许我们用同样的方式（调用 speak() 方法）去处理不同类型的对象（Dog 或 Cat），而每个对象会根据自己的“身份”给出不同的反馈。    
animals = [Dog("旺财"), Cat("咪咪")]
for animal in animals:
    animal.speak() 
#多态的优势:解耦：    主程序不需要知道每个子类的具体细节。
#         可扩展性： 如果你以后增加了一个 Bird 类，只要它也有 speak 方法，你原来的 for 循环代码 一行都不用改 就能直接支持小鸟。
#         灵活性：   你可以随时替换或添加新的子类，而不影响现有代码的逻辑。
"""
# 练习
"""
class Vehicle:
   def __init__(self,brand):
       self.brand = brand
   def show(self):
      print(f"这是一辆{self.brand}品牌的车")


class Car(Vehicle):
  def __init__(self,brand,num):
     self.brand = brand
     self.num = num
  def show(self):
     print(f"这是一辆{self.brand}品牌的车，它有{self.num}个车门")


class Motorcycle(Vehicle):
   def __init__(self,brand,is_sport):
     self.brand = brand
     self.is_sport = is_sport
   def show(self):
     if self.is_sport:    
#当执行 if self.is_sport: 时，Python 实际上是在检查这个变量的值。如果值为 True，代码块运行；如果值为 False，则跳到 else。
        print(f"这是一辆{self.brand}品牌的摩托车，它是运动型的")
     else:
        print(f"这是一辆{self.brand}品牌的摩托车，它不是运动型的")

car = Car("宝马",4)
motorcycle = Motorcycle("雅马哈",True) #加入布尔值 True or False

vehicles = [car,motorcycle]
for vehicle in vehicles:
   vehicle.show()
"""

# 第 21 关：面向对象编程 - 封装
# 一、封装（Encapsulation）：它指的是将数据（属性）和操作这些数据的方法包装在一起，对外隐藏对象的内部实现细节，只提供一些公共的接口来访问和修改数据。这就好比一个电视机，你只需要通过遥控器（公共接口）来操作它，比如换台、调节音量等，而不需要了解电视机内部复杂的电路结构（内部实现细节）。在 Python 中，虽然没有像其他一些编程语言那样严格的访问控制修饰符（如 private、public 等），但可以通过一些约定和命名规则来实现类似的封装效果。

# 二、属性的封装

# 1. 公有属性：在 Python 中，普通的属性默认就是公有属性，可以在类的内部和外部直接访问。例如：

"""
class MyClass:
  def __init__(self):
    
      self.public_attribute = "这是一个公有属性"

obj = MyClass()
print(obj.public_attribute)  


#在 __init__ 括号里写不写其他参数，取决于你是否需要**“外部传参”**。

#情况 A：需要外部传参 (如之前的 Motorcycle)

#你想让每一辆摩托车在出生时品牌都不一样，所以你得开个“窗口”收件： def __init__(self, brand): → 你在实例化时必须写 Motorcycle("Honda")。

#情况 B：不需要外部传参 (如现在的 MyClass)

#如果你觉得这个类的所有对象出生时属性都应该是一模一样的，那就不需要开“窗口”。

class MyClass:
  def __init__(self): # 括号里只有 self，说明不接收外部包裹
      self.public_attribute = "这是一个公有属性" # 内部直接写死内容

#当你实例化时，只需要写 obj = MyClass()，括号里必须留空。
"""

# 2. 私有属性：Python 中约定，以双下划线（__）开头的属性为私有属性，不能在类的外部直接访问。例如：

"""
class MyClass:
  #没有传参，所有的实例都一样拥有相同的私有属性
  def __init__(self):
      self.__private_attribute = "这是一个私有属性" 

obj = MyClass()
# print(obj.__private_attribute)  # 这行代码会报错

#虽然不能直接在类外部访问私有属性，但可以在类内部通过方法来间接访问和修改。例如：
class MyClass:
  def __init__(self):
      self.__private_attribute = "这是一个私有属性"
  #因为方法（Method）是类的一部分，它们拥有“内部通行证”；而你在类外部直接访问，就像是一个“没有门禁卡的外来访客”。
  def get_private_attribute(self): #getter 方法：用于获取私有属性的值。
      return self.__private_attribute

  def set_private_attribute(self, value):
      self.__private_attribute = value


obj = MyClass()

print(obj.get_private_attribute())  
obj.set_private_attribute("旧的值")
print(obj.get_private_attribute()) 

#Python 并没有从物理上封死私有属性，而是通过一种叫 “名称修饰”（Name Mangling） 的技术，玩了一个“捉迷藏”的游戏。当你定义一个以双下划线开头（且结尾没有双下划线）的属性时，Python 会按照以下公式进行重命名：_类名__属性名
#因此可以通过以下代码在外部获取私有属性

print(obj._MyClass__private_attribute)
"""

# 拓展
# 内置函数dir(): 是 Python 的一个内置函数，它的全称可以理解为 Directory（目录）。 它的作用是：列出一个对象拥有的所有“属性”和“方法”的名字。
# 1. 列出对象的所有属性和方法:  在 Python 中，方法本质上也是对象的一种属性。当你对类实例使用 dir() 时，它会把所有的函数名也列出来。
# 2.它可以看“内置魔法” (Magic Methods): 你会发现 dir() 返回的列表里有一大堆以 __ 开头和结尾的名字，比如 __init__, __str__, __dict__。 这些是 Python 的内置灵魂。即使你只写了一个空类，Python 也会默认给它塞进这些东西，让它具备作为“对象”的基本功能（比如被打印、被比较等）。
# 3.它可以看“模块内容” (Modules): 这是 dir() 非常强大的用法。当你 import 一个库但不知道里面有什么函数时，直接用 dir() 刷一遍：


# 三、方法的封装：类似地，方法也可以有公有和 “私有” 之分。以双下划线开头的方法被视为私有方法，一般不应该在类的外部调用。例如：
"""
class MyClass:
  def __private_method(self):
      print("这是一个私有方法")

  def public_method(self):
      print("这是一个公有方法，调用私有方法")
      self.__private_method()


obj = MyClass()
# obj.__private_method()  # 这行代码会报错
#__private_method 是私有方法，不能在类外部直接调用，但可以在类的公有方法 public_method 中调用
obj.public_method()  #现在类内部定义公有方法调用私有方法，然后调用公有方法。
"""

# 四、封装的优势: 1.数据保护：通过封装，将敏感数据设为私有属性，避免外部代码意外修改，提高数据的安全性和一致性。
#              2.简化接口：只向外部暴露必要的接口（公有方法），使外部代码与类的交互更简单，降低代码的耦合度，便于维护和扩展。

# 练习
"""
class BankAccount: #生成一个BankAccount类
  def __init__(self,account_number): #初始化账户

    self.__balance = 0  #账户的第一个私有属性：账户余额,初始为0
    self.__account_number = account_number #账户的第二个私有属性：账号（作为参数传入）

  def deposit(self,amount):#定义账户方法存钱，存钱金额以参数amount导入
    self.__balance += amount

  def withdraw(self,amount):#定义账户方法取钱，取钱金额以参数amount导入
    if self.__balance - amount < 0:
      print("余额不足，取款失败")
    else:
      self.__balance -= amount

  def get_balance(self):
    print(f"账户{self.__account_number}的余额是{self.__balance}")

my_account = BankAccount("123456789")
his_account = BankAccount("987654321")

my_account.deposit(1000)
my_account.withdraw(300)
my_account.get_balance()

his_account.deposit(2000)
his_account.get_balance()
"""
# 第 22 关 ：类属性与实例属性

# 一、类属性（Class Attributes）：直接在类中定义的变量，所有实例共享，通过类名或实例访问（推荐使用类名）类属性是属于类的，而不是属于实例的。这意味着所有实例共享同一个类属性，并且可以通过类名或实例来访问和修改它。

# 二、实例属性（Instance Attributes）：在 __init__ 方法中定义的变量，每个实例独有，通过实例访问。实例属性是属于实例的，每个实例都有自己的实例属性，并且可以通过实例来访问和修改它。每个实例独立修改，不影响其他实例。
"""
#作用域实例：
class MyClass:
  class_attr = 10 #类属性
  def __init__(self,instance_attr): #实例属性
     self.instance_attr = instance_attr
#创建实例
obj1 = MyClass(20)
obj2 = MyClass(30)
#访问类属性
print(obj1.class_attr)
print(obj2.class_attr)
#通过类名修改类属性
MyClass.class_attr = 100
print(obj1.class_attr) #所有实例共享
print(obj2.class_attr)

#通过实例修改类属性(在 Python 中，当你执行 obj1.class_attr = 200 时，发生的不是对类变量的赋值，而是属性遮蔽（Attribute Shadowing）。类属性依然稳稳地坐在 MyClass.__dict__ 里，数值还是 100。实例属性被新建在 obj1.__dict__ 里，数值是 200)
obj1.class_attr = 200 #当你通过 obj1.class_attr = 200 给它赋值时，你并没有“修改”那个全局的类属性，而是在 obj1 这个实例的内存空间里新建了一个同名的实例属性。
print(obj1.class_attr) #创建的新的属于obj1的实例属性
print(obj2.class_attr) #类属性
print(obj1.instance_attr)
print(obj2.instance_attr)


#总结: 类属性是大家共享的“公家财产”。通过类名修改 (MyClass.attr = x)：修改公家财产，所有人看到的都变了。通过实例赋值 (obj.attr = x)：相当于员工领了一份私人物资。从此以后，这个员工谈到 attr 时指的就是自己的私人物资，不再关心公家的了。
"""

"""
#拓展: Python 是一门极其灵活的动态语言。即便你在类（MyClass）的定义里完全没提到某个属性，你依然可以在程序运行的过程中，随时随地给某个特定的实例塞进一个新的属性。这种行为在 Python 中被称为“动态属性赋值”（Dynamic Attribute Assignment）。

#如果你希望严格限制属性，不准别人在外部乱加，Python 提供了一个名为 __slots__ 的魔法变量：

class RestrictedClass:
  __slots__ = ("name", "age") # 只允许有这两个属性

obj = RestrictedClass()
obj.name = "Gemini"
# obj.hobby = "编程"  # 这行会直接报错 (AttributeError)
"""

# 练习
"""
class Car:
  total_cars = 0
  def __init__(self,brand,color):
     self.brand = brand
     self.color = color
     Car.total_cars += 1 #使用了 Car.total_cars += 1，精准地修改了类作用域下的变量。
  def change_color(self,new_color):
      self.change_color = new_color
  def display_info(self):
     print(f"这是一辆{self.brand}品牌的{self.color}颜色的车,总汽车数量:{Car.total_cars}")

car1 = Car("宝马","红色")  
car2 = Car("奔驰","黑色")
car4 = Car("奥迪","白色")

car4.display_info()

#定义在 class 下（创建存钱罐）： 在类层级声明 total_cars = 0。这相当于在柜台上放了一个大家都能看到的存钱罐。
#写在 __init__ 下（往里投钱）： __init__ 是“构造函数”，每当有一辆新车诞生，它都会被自动调用。把 += 1 写在这里，相当于每生产一辆车，就往存钱罐里投一枚硬币
"""

# 第 23 关：类方法与静态方法。


# 一、 类方法 (@classmethod)：类方法是属于类的方法，而不是属于实例的方法。类方法可以通过类名或实例来调用，但通常推荐使用类名调用。
# 定义：使用 @classmethod 装饰器，第一个参数固定为 cls（代表类本身）。
# 用途：A. 操作类变量: 当你需要修改或访问属于整个类的状态（比如计数器、配置信息），而不是某个具体对象的状态时，类方法是最佳选择。
#     B. 实现“工厂方法” (Factory Methods): 这是类方法最常见的实战场景。当 __init__ 提供的初始化方式不够用时，你可以用类方法提供多种创建对象的方式。


"""
#例如：假设你有一个 Date 类，默认接受 年, 月, 日。但有时你拿到的数据是字符串 "2026-02-07"
class Date:
  def __init__(self, year, month, day):
      self.year = year
      self.month = month
      self.day = day

  @classmethod
  def from_string(cls, date_str):
      # 预处理字符串
      year, month, day = map(int, date_str.split('-'))
      # 返回类的新实例 (cls 等同于 Date)
      return cls(year, month, day)

# 使用工厂方法创建实例
today = Date.from_string("2026-02-07")
print(today.year)  # 2026
"""
"""
split
作用： 寻找指定的“分隔符”，并把字符串切成一块块
语法： 字符串.split('分隔符')
产出： 永远是一个列表（List），里面装的是切开后的子字符串。
注意点： 即使切出来的内容全是数字，在 split 之后，它们依然是字符串类型（带引号的 '2024'），不能直接做加减法。

map
作用：把一个函数（比如 int）批量应用到一个序列（比如列表）的每一个成员身上。
语法： map(加工函数, 待处理的序列)
它的产出： 一个特殊的 map 对象（你可以把它看作是一个准备好输出的加工流水线）。
"""
"""
#“星际矿工机器人”**系统：

class MiningRobot:
  # 1. 类变量（墙后的电线）：记录全星系机器人总数
  __total_count = 0

  def __init__(self, name, iron_ore):
      self.name = name
      self.iron_ore = iron_ore  # 挖到的铁矿重量（公斤）
      # 每次买一个机器人，总数加1
      MiningRobot.__total_count += 1

  # ---------------------------------------------------------
  # 2. 类方法（工厂接口）：从字符串快速创建机器人
  # ---------------------------------------------------------
  @classmethod
  def from_string(cls, data_str):
  
      #输入格式: "名称,矿量" -> 例如 "瓦力,50"
      #使用 cls 而不是 MiningRobot，保证了子类继承时的灵活性   
      name, ore_str = data_str.split(",")
      return cls(name, int(ore_str))

  # ---------------------------------------------------------
  # 3. 类方法（统计接口）：获取全局信息
  # ---------------------------------------------------------
  @classmethod
  def get_system_report(cls):
  
      #就像插座：外部只管调用，内部我们可以随意修改统计逻辑
      
      return f"【星际总部报告】当前在线机器人：{cls.__total_count} 台"

  # ---------------------------------------------------------
  # 4. 属性方法（状态接口）：把逻辑伪装成变量
  # ---------------------------------------------------------
  @property
  def capacity_status(self):
  
      #针对每一个具体的机器人实例。
      外部调用 r.capacity_status，看起来像查变量，其实在跑逻辑。
      
      if self.iron_ore > 100:
          return "仓库已满"
      return "继续挖矿中..."

# ==================== 外部调用代码 ====================

# A. 使用类方法（工厂）生产机器人
r1 = MiningRobot.from_string("瓦力,50")
r2 = MiningRobot.from_string("伊娃,120")

# B. 使用类方法（接口）查看全局状态（不需要实例也能调）
print(MiningRobot.get_system_report()) 

# C. 使用属性方法（伪装变量）查看具体机器人的状态
print(f"{r1.name} 状态: {r1.capacity_status}")
print(f"{r2.name} 状态: {r2.capacity_status}")
"""
# 这段代码展示了三个层级的“行为”：
# 1. from_string(cls, ...)：这是**“造物主”的行为**。它拿着图纸（字符串），利用 cls 生产出具体的机器人。

# 2. get_system_report(cls)：这是**“上帝视角”的行为**。它不关心某个具体的机器人，它只关心 cls（整个机器人族群）的统计数据。

# 3.capacity_status(self)：这是**“个人档案”的行为**。它只关心 self（我这个机器人）有没有装满，而且它把复杂的 if-else 逻辑藏在了一个漂亮的“变量名”后面。


# 问： 为什么要用类方法将2026-2-7改为年，月，日，而不是将日期改成年，月，日之后再输入变量呢？？？？
# 答： 为了封装性（Encapsulation）和易用性
# 封装性：如果你在程序的 10 个不同地方都要从字符串转日期，你就得把这段 split 代码写 10 遍。维护困难：万一哪天日期格式变了（比如从 2026-02-07 变成 2026/02/07），你得去全局搜索并修改这 10 处代码。类方法的做法： 将这种“脏活累活”藏在类内部。外部只需要调用 Date.from_string(s)。如果以后格式变了，你只需要改类里面的一行代码。

"""
#“通过类方法访问”优于“直接访问属性”的几个核心理由：
#1. 直接访问属性是“死”的，而类方法是“活”的。
#直接访问：你拿到的是原始数据。
#类方法：你可以在返回数据前进行加工、过滤或格式化。
#例如：
class Website:
  user_count = 1050  # 原始数据

  @classmethod
  def get_user_count(cls):
      # 逻辑：如果是内部查看，显示精确数字；如果是外部展示，显示模糊数字
      if cls.user_count > 1000:
          return f"{cls.user_count // 1000}k+"
      return str(cls.user_count)

# 直接访问只能得到 1050
# 类方法可以得到 "1k+"

#2. 隐藏内部实现细节（解耦）
#例如：如果你在项目的 100 个地方都直接写了 Robot.population，万一哪天你觉得这个名字不好听，想改成 Robot.total_robots，你就得去改 100 处代码。但如果你使用的是类方法：

@classmethod
def get_count(cls):
    return cls.population  # 内部变量名随便改，只要方法名 get_count 不变，外部调用就不会崩
#这就像是插座接口：内部电线怎么走（类变量名）不重要，只要插座孔位（类方法）不变，你的电器（外部代码）就能一直用。

#3. 继承中的“多态”表现
#这是类方法最神奇的地方。cls 参数是动态绑定的，它能感知到是谁在调用它。
#例如：
class Parent:
    data = "父类数据"

    @classmethod
    def show_data(cls):
        print(f"当前访问的是: {cls.data}")

class Child(Parent):
    data = "子类数据"

# 调用同一个类方法
Parent.show_data() # 输出: 父类数据
Child.show_data()  # 输出: 子类数据 

#如果你直接访问属性，你必须明确知道你在访问谁；而使用类方法，逻辑可以自动适配子类。
"""
"""
#知识点
#在 Python 中，子类会自动继承父类的所有属性和方法。

#1. 继承的“搜索机制”：  当你调用 Child.show_data() 时，Python 的解释器会按照下面的顺序去找这个方法：第一步：在 Child 类自己的定义里找。结果：没找到。第二步：顺着继承链往上爬，去父类 Parent 里找。结果：找到了！于是，Python 就直接使用了父类的代码。
#2. 关键在于 cls 的动态绑定： 虽然代码是写在 Parent 类里的，但 @classmethod 有一个非常聪明的特性：它会记住是谁在调用它。当你执行 Parent.show_data() 时：cls 接收的是 Parent 类。当你执行 Child.show_data() 时：即使方法是在父类定义的，但因为发起调用的是 Child，Python 会把 Child 类本身作为第一个参数传给 cls。所以，在 Child.show_data() 执行时，f"{cls.data}" 实际上变成了 f"{Child.data}"，自然就拿到了子类的数据。
#3. 对比：如果不用类方法会怎样？如果我们硬编码类名，继承就会“失效”。看看这个反例：

class Parent:
    data = "父类数据"

    @classmethod
    def show_data(cls):
        # 如果我们不写 cls.data，而是写死 Parent.data
        print(f"写死了父类名: {Parent.data}")

class Child(Parent):
    data = "子类数据"

Child.show_data() 
# 即使是 Child 调用，输出依然是: 写死了父类名: 父类数据

#这就是为什么要强调使用 cls： 它保证了代码的灵活性。它允许父类定义一套逻辑框架，而具体的执行结果可以根据子类的不同而自动适配。
"""
"""
#知识点：
#硬编码： “硬编码”（Hard-coding）是编程中一个非常经典的概念。简单来说，它指的方案是：把数据或逻辑直接“写死”在代码里，而不是通过变量、参数或配置文件来动态获取。

#例如：
#硬编码：
def calculate_price(quantity):
  # 0.8 是硬编码。如果哪天打 9 折，你得满世界找这个 0.8 
  return quantity * 10.5 * 0.8
#非硬编码版本（使用变量或配置）：

DISCOUNT_RATE = 0.8  # 定义在一个统一的地方
UNIT_PRICE = 10.5
def calculate_price(quantity):
    return quantity * UNIT_PRICE * DISCOUNT_RATE

#为什么硬编码不好？
#1. 修改麻烦：如果你的代码里有 100 处都写了 0.8，当折扣变动时，你需要手动修改 100 个地方，漏掉一个就会出 Bug。

#2.语义不明：别人看到 0.8 可能不知道它代表折扣、税率还是损耗。但看到 DISCOUNT_RATE 瞬间就懂了。

#3. 环境依赖：比如你把数据库密码硬编码在代码里，当你从“测试环境”换到“生产环境”时，你必须修改源代码才能运行，这非常危险且低效。 
"""


"""
为了让你一眼看出类方法的威力，我们写一个“员工管理系统”。

这个例子展示了类方法的两个核心用法：

操作类变量（统一修改所有员工的薪资涨幅）。

作为“工厂方法”（处理不同格式的输入数据，比如把“张三-5000”这种字符串直接变成对象）。

代码示例：员工管理系统
Python
class Employee:
    # 类变量：所有员工共享的涨薪比例
    raise_amount = 1.04 

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # 实例方法：查看个人薪资
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    # 用法 1：使用类方法修改类变量
    @classmethod
    def set_raise_amt(cls, amount):
        统一调整全公司的涨薪比例
        cls.raise_amount = amount
        print(f"提示：全员涨薪系数已调整为: {amount}")

    # 用法 2：使用类方法作为“工厂方法”
    @classmethod
    def from_string(cls, emp_str):
        解析字符串并创建对象 (格式: '姓名-薪资')
        name, salary = emp_str.split('-')
        return cls(name, int(salary)) # 这里的 cls(..) 等同于 Employee(..)

# --- 实际使用 ---

# 1. 正常创建实例
emp_1 = Employee("Alice", 5000)

# 2. 使用【类方法】从字符串直接创建实例 (就像魔法入口)
emp_str_2 = "Bob-7000"
emp_2 = Employee.from_string(emp_str_2)

print(f"修改前：{emp_1.name} 薪资 {emp_1.salary}, {emp_2.name} 薪资 {emp_2.salary}")

# 3. 使用【类方法】统一修改涨薪比例
# 注意：我们不需要给每个员工单独改，只需要改类本身
Employee.set_raise_amt(1.10) 

# 4. 所有人应用新比例
emp_1.apply_raise()
emp_2.apply_raise()

print(f"修改后：{emp_1.name} 薪资 {emp_1.salary}, {emp_2.name} 薪资 {emp_2.salary}")
为什么这个例子好用？
关于 from_string： 如果没有类方法，你得先在外部自己把字符串 split 开，再传给 Employee。现在你直接调用 Employee.from_string()，逻辑被封装在类里面，代码瞬间变整洁了。

关于 set_raise_amt： 如果你直接用 Employee.raise_amount = 1.10 也能成，但通过类方法，你可以方便地加入日志打印（如上面的“提示...”）或者权限检查。

cls 的灵活性： 如果以后你写了一个子类 Developer(Employee)，你调用 Developer.from_string() 时，它返回的是一个开发人员对象，而不仅仅是普通的员工对象。这就是 cls 动态绑定的好处。

你能想到在你的项目中，有哪些数据是需要像这样“先处理格式再创建对象”的吗？（比如解析一个 CSV 文件行或数据库查询结果）



对比不使用类方法

为了让你看清差距，我们直接把刚才“员工管理”的代码，用**不使用类方法（硬改属性）**的方式重写一遍。通过对比，你会发现代码是如何一步步变得**“散乱”且“难以维护”**的。1. 对比：操作类变量如果我们不使用 @classmethod 的 set_raise_amt 方法。不使用类方法（直接硬改）：Python# 在代码的任何地方，任何人都可以改
Employee.raise_amount = 1.10
# 缺点：
# 1. 没有地方写“日志”或“校验”。如果有人改成 -5.0，程序直接崩掉。
# 2. 语义不明。如果不看注释，不知道这行代码是在做“全员调薪”。
使用类方法：Python@classmethod
def set_raise_amt(cls, amount):
    if amount < 1: 
        raise ValueError("涨薪系数不能小于1！") # 增加校验
    cls.raise_amount = amount
    logging.info(f"薪资系数调整为 {amount}") # 自动记录日志
2. 对比：解析数据（工厂模式）这是差别最大的地方。假设你有一堆格式为 "姓名-薪资" 的字符串。不使用类方法：你必须在类外部手动处理逻辑。Pythonemp_str = "Bob-7000"

# 你必须在主程序里写解析逻辑
name, salary = emp_str.split('-')
emp_2 = Employee(name, int(salary))

# 缺点：
# 1. 逻辑外泄。如果字符串格式变了（比如变成“姓名,薪资”），
#    你得去整个项目中寻找所有处理字符串的地方一个个修改。
# 2. 重复劳动。每次从字符串创建员工，都要写一遍 split。
使用类方法：逻辑被锁死在类内部。Python# 主程序只需要这一行，极其优雅
emp_2 = Employee.from_string("Bob-7000")

# 优点：
# 1. 封装性。如果格式变了，你只需要改类里的 from_string 方法，
#    外部调用者的代码一行都不用动。
3. 对比：继承时的表现（致命伤）这是很多新手会掉进去的坑。场景不使用类方法（写死类名）使用类方法（使用 cls）子类继承如果子类 Developer 想要一个不同的创建逻辑，你可能得重写整个函数。cls 会自动识别当前调用者。如果是 Developer 调用，它就返回 Developer 对象。灵活性如果你修改了父类的名字（比如从 Employee 改成 Staff），你得把函数里所有硬编码的 Employee 都改掉。cls 永远指向当前类，改名也不怕，代码更“耐造”。形象的比喻总结直接修改属性/外部处理逻辑：就像是**“自助餐厅”**。你自己去拿盘子、切肉、倒酒。如果餐厅换了盘子位置，你就找不到了（维护困难）。使用类方法：就像是**“点餐服务”**。你只需要告诉服务员（类方法）：“我要一份套餐 A”。至于肉是怎么切的、酒是怎么倒的，由服务员在后厨（类内部）完成。哪怕后厨换了厨师或菜谱，你手里的菜单（接口）依然有效。你会发现，随着代码量变大，类方法其实是在帮你“省事”。
"""


# 二、静态方法
# 定义：使用 @staticmethod 装饰器，无强制参数。
# 用途：1.执行与类相关但不需要访问类或实例属性的操作。
#     2.组织工具函数到类中。


"""
假设你有一个处理日期的类，你可以把“判断日期是否合法”这种通用逻辑设为静态方法


class DateProcessor:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def is_valid_date(day, month, year):
        # 纯逻辑判断，不依赖具体的 DateProcessor 实例
        return 1 <= day <= 31 and 1 <= month <= 12

# 无需实例化即可调用
if DateProcessor.is_valid_date(31, 2, 2026):
    print("日期合法")
else:
    print("日期无效") # 输出：日期无效
"""


# 三、练习任务
"""
需求：创建一个 Book 类，包含以下功能：
类属性：book_count，统计所有书籍实例的数量。
实例属性：title（书名）、author（作者）。
方法：
__init__：初始化书名和作者，并自动增加 book_count。
print_total（类方法）：打印当前书籍总数。
is_valid_author（静态方法）：判断作者名是否有效（例如，非空且长度大于 2）。
"""

"""
class Book:
  book_count = 0
  def __init__(self,title,author):
    self.title = title
    self.author = author
    Book.book_count += 1
  @classmethod
  def print_total(cls):
        return cls. book_count
  @staticmethod
  def is_valid_author(author):
        if author  == "" or len(author) <= 2:
            return False
        else:
            return True
"""


"""
    1. 逻辑微调：is_valid_author
    你的静态方法逻辑没问题，但 Python 有更简洁的写法。在 Python 中，我们可以直接返回判断表达式的结果：

    Python
    @staticmethod
    def is_valid_author(author):
        # 直接返回布尔值，更简洁专业
        return bool(author and len(author) > 2)
    2. 初始化防御：先校验，再造书
    在现实开发中，我们通常会在 __init__ 里先调用静态方法校验。如果作者名不合格，就不该增加 book_count。

    🚀 优化后的代码版本
    你可以对比一下这个版本，看看在逻辑严密性上的提升：

    Python
    class Book:
        book_count = 0

        def __init__(self, title, author):
            # 在创建实例前，先用静态方法检查一下
            if not Book.is_valid_author(author):
                raise ValueError(f"无效的作者名: {author}")

            self.title = title
            self.author = author
            Book.book_count += 1

        @classmethod
        def print_total(cls):
            # 使用 f-string 直接打印，符合需求描述的“打印”功能
            print(f"当前书籍总数: {cls.book_count}")

        @staticmethod
        def is_valid_author(author):
            # 只要作者名不是 None，且去掉首尾空格后长度大于 2 就算有效
            return author is not None and len(author.strip()) > 2

    # --- 测试代码 ---
    try:
        b1 = Book("三体", "刘慈欣")
        b2 = Book("Python入门", "老王")
        Book.print_total()  # 输出：当前书籍总数: 2

        # 尝试创建一个无效作者的书
        b3 = Book("无名书", "阿强") # 长度为2，会触发校验失败（根据你的 len <= 2 逻辑）
    except ValueError as e:
        print(e)
    📝 知识点复盘
    Book.book_count += 1：你正确地在类作用域下修改了变量，保证了计数的唯一性。

    cls.book_count：你利用了类方法动态获取属性，这样即使以后你创建了一个 EBook 子类，它也能正常工作。

    is_valid_author：作为一个工具函数，它不依赖 self 或 cls，完美契合静态方法的身分。
"""

# 第 24 关 多重继承与 MRO

# 一、多重继承
# 定义：多重继承是指一个类可以同时继承多个父类。这意味着子类可以拥有所有父类的属性和方法。多重继承可以让代码更加灵活，但也可能会引入一些复杂性和潜在的问题。
# 语法：class Child(Parent1, Parent2)

"""
#例
class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.name}发出声音")
class Fly(Animal):
    def fly(self):
        print(f"{self.name}飞")
class Mammal(Animal):
    def walk(self):
        print("哺乳动物走路")
class Bat(Mammal,Fly):  # 继承自 Mammal 和 Bird
    pass

Rat = Animal("老鼠")
Rat.speak()
bat_1 = Bat("蝙蝠")
bat_1.speak()
bat_1.fly()
bat_1.walk()
"""

"""
KP
pass: 占位符（Placeholder），特殊的空语句（Null Statement）。它的存在不是为了执行任何逻辑，而是为了满足语法结构的完整性。
"""

# 二 方法解析顺序（MRO）
# 定义：方法解析顺序。在 Python 中，当你在一个对象上调用方法或访问属性时，Python 会按照一个预定义的列表顺序去寻找这个属性。
# 核心算法：Python 3 使用的是 C3 线性化 (C3 Linearization) 算法。
# 三大原则: #1. 子类优先于父类：永远先在当前类找，找不到再找父类。
# 2. 从左到右：class A(B, C): 会先搜索 B 再搜索 C。
# 3. 最后找祖先：如果多个父类继承自同一个基类（菱形继承），该基类最后才被搜索。
# 查看方式：使用 ClassName.mro() 或 ClassName.__mro__

# super()：MRO 的最佳拍档，super()不是简单地调用“父类”，而是根据 MRO（方法解析顺序） 列表，找到当前类在排队序列中的 下一个角色，并把当前的调用请求（属性或方法）传递给它。
# super() 必须放在方法内部执行,也就是说子类在继承父类的方法时需要先自己声明方法，而不能直接写在类的主体中。
# 如果不写super()，而子类还有必须继承自父类的属性或者方法，你就必须手动指定父类名，但这样会导致硬编码，当继承链变化时，你必须手动修改代码。如果两者都不写，链条则会断掉，代码会因为找不到属性和方法报错。



#属性继承实例
"""
class Animal:
    def __init__(self):
        print("进入 Animal")
        self.alive = True
        print("离开 Animal")

class Mammal(Animal):
    def __init__(self):
        print("进入 Mammal")
        super().__init__() 
        self.has_fur = True
        print("离开 Mammal")

class WingedAnimal(Animal):
    def __init__(self):
        print("进入 WingedAnimal")
        super().__init__()
        self.can_fly = True
        print("离开 WingedAnimal")

class Bat(Mammal, WingedAnimal):
    def __init__(self):
        print("--- 蝙蝠初始化开始 ---")
        super().__init__()
        print("--- 蝙蝠初始化结束 ---")

my_bat = Bat()
"""

#super() 能够跨越到“兄弟类”（如 Mammal 到 WingedAnimal ），是因为它始终引用的是**最初触发调用的那个实例（ Bat 的实例）**的 MRO。


"""
#方法继承实例：
class Animal: 
    def move(self):
        print("[Animal] 消耗体力...")

class Mammal(Animal):
    def move(self):
        super().move()  # 先消耗体力
        print("[Mammal] 用四肢奔跑")

class WingedAnimal(Animal):
    def move(self):
        super().move()  # 先消耗体力
        print("[Winged] 振动翅膀")

class Bat(Mammal, WingedAnimal):
    def move(self):
        print("=== 蝙蝠准备出发 ===")
        super().move()  # 触发菱形继承的动作链
        print("=== 蝙蝠到达目的地 ===")

my_bat = Bat()
my_bat.move()
"""


# 三、练习
# 创建一个动物类层次，包含以下类：
# Animal：基类，方法 eat()。
# Mammal：继承自 Animal，方法 walk()。
# Bird：继承自 Animal，方法 fly()。
# Bat：继承自 Mammal 和 Bird，添加方法 echolocation()。
# 验证 MRO：打印 Bat 的 MRO，并调用所有父类的方法。
"""
class Animal:
    def eat(self):
        print("吃东西")

class Mammal(Animal):
    def walk(self):
        super().eat()
        print("走路")

class Bird(Animal):
    def fly(self):
        super().eat()
        print("飞")

class Bat(Mammal, Bird):
    def echolocation(self):
        super().eat()
        print("回声定位")


print(Bat.mro())
bat = Bat()
bat.echolocation()
"""

# 第 25 关 魔法方法（Magic Mathods）
# 一、核心知识点
# 1. 魔法方法基础
# 定义：以__开头和结尾的方法，用于实现Python的特殊行为。
# 常见用途：
# 1.对象初始化: (__init__)
# 2.字符串表示: (__str__, __repr__)
# 3.运算符重载: (__add__, __len__, __sub__， __eq__)
# 4.上下文管理: (__enter__, __exit__)
# __eq__: 定义当两个对象使用 == 运算符比较时，到底该怎么算“相等”？

# 二、关键魔法方法实例
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    
    问：为什么感觉self在两个定义中扮演的角色不同？
    答：
    在 __init__(self, x, y) 中：self 是“待装修的毛坯房”
    状态：此时对象刚刚被创建（出生），属性 x 和 y 还没挂上去。
    任务：赋值。你的任务是把传进来的参数 x 和 y 强行绑定到这个空壳 self 上。
    你可以理解为：self 是一个接收者。
    在 __add__(self, other) 中：self 是“成熟的参与者”
    状态：此时 v1 已经是一个完整的、有数据的对象了（它已经有了 self.x 和 self.y）。
    任务：计算。它拿着自己已有的数据，去和另一个对象 other 的数据做加法。
    你可以理解为：self 是一个操作发起者。
    
    
    问：为什么return Vector对象Vector(self.x + other.x, self.y + other.y)而不是return 元组(self.x + other.x, self.y + other.y)

    答：
    1. 链式调用 (Chaining)
    如果你返回的是 Vector，你可以连续进行加法运算。如果返回的是元组，程序会报错。
    返回 Vector 时：
    v1 + v2 + v3 实际上等同于 (v1 + v2) + v3。
    因为 v1 + v2 产生了一个新的 Vector，所以它可以继续和 v3 相加。
    返回元组时：
    v1 + v2 会得到 (4, 6)。当你试图执行 (4, 6) + v3 时，Python 会报错，因为元组不知道如何与 Vector 对象相加。
    2. 保留“能力”（方法和属性）
    Vector 类不仅仅有坐标，它还有你定义的其他功能，比如 len()。
    返回 Vector：可以计算模长
    返回元组：只能计算长度
    3. 类型的一致性 (Consistency)
    在数学上，两个向量相加的结果依然是一个向量。如果你的加法运算改变了结果的类型（从 Vector 变成了 tuple），这会违反开发者的直觉，导致代码难以维护。
    

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
        # 当你直接在交互式环境（如 Python Shell）中输入一个对象名时，__repr__ 会被调用。
        # 当你使用 print() 函数打印一个对象时，如果定义了__str__ 会被调用。
        # 如果你没有定义 __str__，Python 会默认使用 __repr__ 的结果

    def __len__(self):
        return int((self.x**2 + self.y**2) ** 0.5)
        # 知识点： 单星号 (*)：乘法
        #     ： 双星号 (**)：幂运算（次方）。


v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = v1 + v2
print(v1 + v2) 
#运算阶段：执行 v1.__add__(v2)，创建并返回了一个全新的对象：Vector(4, 6)
#转换阶段：print 函数需要把这个对象转换成“人能看懂的字符串”。它会自动去调用你类里定义的 __str__ 方法。
print(len(v1))
print(str(v1)) #声明了__str__方法，所以print(v1)也会调用__str__方法
print(repr(v1))
"""

# 三、练习任务
# 创建一个 Person 类，包含以下功能：
# 魔法方法：
# __init__：初始化 name 和 age。
# __str__：返回 "姓名：{name}，年龄：{age}"。
# __repr__：返回 "Person('{name}', {age})"。
# __eq__：比较两个人是否同名且同龄。
# __lt__：比较两个人的年龄大小。
# 普通方法：
# say_hello()：打印 "你好，我是{name}，今年{age}岁。"。
"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"姓名:{self.name},年龄:{self.age}"
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"
#Python 如何构造一个合法的字符串，以及 __repr__ 方法的核心目标。简单来说：self.name 是一个字符串，而 self.age 是一个数字。在 Python 代码中，表示字符串必须带引号，表示数字则不需要。
    def __eq__(self,other):
        return self.name == other.name and self.age == other.age #当我相比较self和other时，返回一个self.name和other.name是否相等并且self.age和other.age是否相等的结果


        
#知识点： 1. == (等于运算符)
#       含义：检查左右两边的值是否相等。
#       读作：“等于”。
#       注意：不要和单个等号 = 混淆（单个 = 是用来赋值的，比如 x = 5）
#       2. != (不等于运算符)
#       含义：检查左右两边的值是否不相等。
#       读作：“不等于”。
#       逻辑：它是 == 的反面。如果两边不一样，它就返回 True。

    def __lt__(self,other):
        return self.age < other.age

    def say_hello(self):
        print(f"你好，我是{self.name}，今年{self.age}岁。")

p1 = Person("小明",25)
p2 = Person("小红",20)
print(p1)
print(repr(p1))
print(p1 == p2)
print(p1 < p2)
"""


# 第 26 关：OOP 设计原则：封装与接口设计
# 一、封装（Encapsulation）: 将数据和操作封装在类中，通过访问控制（私有属性、公有方法）保护数据。
# 访问控制：
# 公有（Public）：默认，外部可直接访问。
# 私有（Private）：以 __ 开头，外部不可直接访问（Python 通过名称改写实现伪私有）。
# 受保护（Protected）：以 _ 开头，约定俗成的内部使用。
# 二、接口设计（Interface Design）：类提供的一组公共方法，明确类的行为和协作方式。
# 原则：
# 单一职责：每个类只负责一项任务。
# 高内聚、低耦合：类内部功能紧密关联，类之间依赖最小化。
# 依赖倒置：依赖抽象而非具体实现。

# 封装与接口设计实例：
"""
class BankAccount:
    def __init__(self, account_number):
        self.__balance = 0  # __私有属性
        self.__account_number = account_number

    def deposit(self, amount):  # 公有方法
        if amount > 0:
            self.__balance += amount

    def get_balance(self):  # 接口方法
        return self.__balance #类内部能够访问self.__balance，因为它是类的内部成员。通过公有方法传递私有属性实现接口方法

acct1 =  BankAccount("123456789")
print(acct1._BankAccount__balance)
acct1.deposit(1000)
print(acct1.__balance) #因为 __balance 是私有的。在类定义的外部（也就是在 acct1 后面），Python 假装这个属性不存在。你不能直接通过 .点 来读取它。
print(acct1.get_balance())
"""


# 三、练习任务
# 需求：设计一个简单的图书馆系统，包含以下类：
# Book：
# 私有属性：title、author、is_borrowed（是否被借阅）。
# 接口方法：
# borrow()：将 is_borrowed 设为 True。
# return_book()：将 is_borrowed 设为 False。
# get_info()：返回图书信息（标题、作者、借阅状态）。
# Library：
# 私有属性：books（图书列表）。
# 接口方法：
# add_book(book)：添加图书到图书馆。
# find_book(title)：根据标题查找图书。
# list_available_books()：列出所有可借阅的图书。
"""
class Book:
    def __init__(self,title,author):
        self.__title = title
        self.__author = author
        self.__is_borrowed = False #初始值是默认没借走的
    def borrow(self):
        if self.__is_borrowed:
#为什么 if 后面没有写 == True？这可能是让你最困惑的地方。
#在 Python 中：if self.__is_borrowed:等价于 if self.__is_borrowed == True:
            print ("已被借阅")
        else: #如果没被借走
            print("借阅成功")#则借阅成功
            self.__is_borrowed = True #并且将借阅状态改为已被借阅
    def return_book(self):
        self.__is_borrowed = False #调用还书，将借阅状态改回未借阅
    def get_info(self):
            
        return (self.__title,self.__author,self.__is_borrowed)
#{} 集合是无序的， 列表 (List) [...] or 元组 (Tuple) (...,)是有序的

class Library:
    def __init__(self):
        self.__books = [] #定义一个新的私有属性，以列表的形式存储图书
    def add_book(self,book):
        self.__books.append(book)
    def find_book(self,title):
        for book in self.__books:
            if book.get_info()[0] == title:
                print(f"找到图书:{book.get_info()[0]}")
#find_book 方法中，目前的逻辑会遍历所有书。如果找到了书，程序应该停止寻找并返回结果，否则会显得逻辑混乱。要实现“找到目标后立即停止寻找”，最简单且最标准的方法是使用 return 关键字。在循环中，一旦执行到 return，整个函数会立即结束，并跳出循环，不再执行后续的任何代码。  
            if book.get_info()[2] == False:
                print("可借阅")
            else:
                print("已借阅")
            return book #找到后直接返回该对象
        
    
        

book1 = Book("三体","刘慈欣")
book2 = Book("Python","老王")
school_library =  Library()
school_library.add_book(book1)#这里可以是两个吗？
school_library.find_book("三体")
book1.borrow()
school_library.find_book("三体")
"""

# 第 27 关：OOP 设计原则：继承的艺术与组合优于继承

# 一、继承的利弊
# 利：代码复用、逻辑复用：子类可以直接使用父类的属性和方法。
#    实现多态：不同子类可以有不同的实现。
# 弊：强耦合（子类依赖父类实现细节）：父类变化会影响所有子类。
#    继承链过深导致代码僵化（"继承爆炸"）：“菱形继承”问题。


# 二、组合优于继承（Composition Over Inheritance）
# 定义：通过将对象嵌入到另一个对象中，而非继承，实现功能复用。
# 优势：低耦合（组合对象间独立）
#      灵活性强（动态替换组合对象）


# 三、区别： 继承是“我是什么”（Is-a），而组合是“我有什么”（Has-a）


# 组合优于继承实例：


# 继承写法：让一个类同时继承多个父类
"""
class Robot:
    def move(self):
        print("机器人正在移动")


class Cleaner(Robot):  # 专门负责打扫的机器人分支
    def clean(self):
        print("正在打扫...")


class Printer(Robot):  # 专门负责打印的机器人分支
    def print_task(self):
        print("正在打印...")


# 既能打扫又能打印的机器人
class SuperRobot(Cleaner, Printer):
    pass


# 使用
bot = SuperRobot()
bot.move()  # 来自 Robot
bot.clean()  # 来自 Cleaner
bot.print_task()  # 来自 Printer
"""


# 结构僵化： 如果你以后又增加了 Flyer（飞行）、Waiter（送餐）等功能，为了排列组合出各种型号（如：能飞的打扫机器人、能送餐的打印机器人），你需要定义无数个像 SuperRobot 这样的小类。
# 命名冲突： 如果 Cleaner 和 Printer 都有一个同名方法 work()，Python 会根据 MRO（方法解析顺序） 只执行其中一个，这会导致另一个功能被意外“淹没”。


# 组合写法：
"""
class Cleaner:
    def work(self):
        print("正在打扫...")


class Printer:
    def work(self):
        print("正在打印报表...")


class Robot:
    def __init__(self, tools=None):
        # 核心：将功能组件作为属性传入
        self.tools = tools or []

    def move(self):
        print("机器人正在移动")

    def perform_tasks(self):
        for tool in self.tools:
            tool.work()


# 动态组装：想要什么功能就塞进什么组件
sweeper = Robot(tools=[Cleaner()])
super_bot = Robot(tools=[Cleaner(), Printer()])
super_bot.perform_tasks()
"""

# 知识点： 在 Python 中，函数参数不仅可以写变量名，还可以给它一个默认值。如果在创建这个类的时候，你没有主动提供 tools，那么程序就默认 tools 等于 None。
# 例：
"""
class Robot:
    def __init__(self, tools=None):
        # 如果用户没给工具，我们就给它一个空列表
        if tools is None:
            self.tools = []
        else:
            self.tools = tools

# 场景 A：创建一个“白手起家”的机器人（不传参数）
bot1 = Robot() 
print(bot1.tools)  # 输出 []

# 场景 B：创建一个“带了扳手”的机器人（传参数）
bot2 = Robot(tools=['wrench', 'hammer'])
print(bot2.tools)  # 输出 ['wrench', 'hammer']
"""
# 问一: 为什么在 Python 中，不要使用可变对象（如列表或字典）作为默认参数。比如：tools=[]
# 答: 默认参数的值只在函数“定义”时计算一次，而不是在每次“调用”时计算。如果你使用列表（List）或字典（Dict）作为默认参数，这个对象会变成一个**“全局共享”的常驻对象**。且这个值会被所有后续的函数调用共享。
# 例：
"""
def add_item(item, basket=[]): # 这里的 [] 在函数定义那一刻就创建了
    basket.append(item)
    return basket

print(add_item("苹果"))  # 输出: ['苹果'] - 没问题
print(add_item("香蕉"))  # 输出: ['苹果', '香蕉'] - 诶？苹果怎么还在？
print(add_item("橘子"))  # 输出: ['苹果', '香蕉', '橘子'] - 炸裂，它们共用了一个篮子
"""

# 问二：为什么直接写self.tools = tools or []

"""
class Robot:
    def __init__(self, tools=None):
        self.tools = tools or []
"""

# 知识点：逻辑运算符 or 的 “短路求值（Short-circuit evaluation）” 特性
# 1.在 Python 中， A or B 的运算逻辑是：
# · 如果 A 为 真（True），则直接返回 A，不再看 B。
# · 如果 A 为 假（False），则返回 B。
# 2.在 Python 中，以下值被认为是“假”（False）：
# · None
# · [] (空列表)
# · {} (空字典)
# · "" (空字符串)
# · 0

# 情况一、当你调用 Robot() 不传参数时：tools 的默认值是 None，表达式变成 None or []，因为 None 是假，所以返回右边的 []，elf.tools 最终被赋值为一个全新的空列表

# 情况二、当你调用 Robot(tools=['扳手']) 时：tools 是 ['扳手']，表达式变成 ['扳手'] or 因为 ['GPS']（非空列表）是真，所以直接返回它, self.tools 最终指向你传入的列表。


# 注意：虽然这种写法很常用，但它有一个微妙的副作用, 如果用户故意传了一个 空列表 [] 进去，or 也会判定为“假”，从而执行右边的代码，再给你创建一个新的 []。
# 写法 A (tools or []): 如果你传了空列表，它会丢弃你的空列表，换成一个新的空列表。
# 写法 B (if tools is None): 只有当你完全没传（即 None）时，才会创建新列表。

# 问三：为什么 or 后面写 []
# 答： 因为你希望 self.tools 在任何时候都保持一致的数据类型（即：它应该始终是一个列表）

# 假设你的 Robot 类后面有一个功能是“列出所有工具”，代码可能是这样的：

"""
def list_tools(self):
    for item in self.tools:  # 只有 self.tools 是列表，这里才能循环
        print(f"正在使用: {item}")

如果用了tools or []：
即便你创建机器人时什么都没传，self.tools 也会拿到一个 []。执行 for item in [] 不会报错，只是什么都不打印，程序很安全。

如果不写 or []：
self.tools 就会变成 None。当你运行 for item in None 时，Python 会直接抛出错误：TypeError: 'NoneType' object is not iterable（None 对象不可迭代）。
"""
# 问四：or 后面可以换成别的吗?
# 答： 可以！or 后面的内容取决于你希望这个变量默认是什么
# ·如果 tools 应该是一串名字（字符串）：self.name = name or "无名氏"
# ·如果 tools 应该是一个分数（数字）：self.score = score or 0
# ·如果 tools 应该是一组配置（字典）：self.config = config or {}

# 四： 继承的合理使用场景
# ·接口继承（实现“必须有”的功能）
# ·垂直扩展（在旧功能上“加新”功能）
# ·行为多态（把旧功能“改出”新花样）



# 五、练习任务
"""
设计一个音乐播放器，包含以下功能：
MediaPlayer（基类）：
方法 play()：打印 "播放媒体"。
AudioPlayer（子类）：
继承自 MediaPlayer。
新增方法 adjust_volume()：调整音量。
VideoPlayer（子类）：
继承自 AudioPlayer。
新增方法 adjust_resolution()：调整分辨率。
优化版本：
使用组合替代继承，将播放功能解耦。
"""

# 继承写法：
"""
class MediaPlayer:
    def __init__(self): 
        pass
    def play(self):
        print("播放媒体")
class AudioPlayer(MediaPlayer):
    def __init__(self):
        super().__init__()
    def play(self):
        super().play()
    def adjust_volume(self):
        print ("调整音量")
class VedioPlayer(AudioPlayer,MediaPlayer):
    #修正点 1: 在 Python 中，如果 VideoPlayer 继承自 AudioPlayer，
    # 而 AudioPlayer 已经继承了 MediaPlayer，那么 VideoPlayer 自动拥有两者的功能。
    # 不需要写成 (AudioPlayer, MediaPlayer)，这叫冗余继承。
    def __init__(self):
        super().__init__()
    def play(self):
        super().play()
    def adjust_resolution():
        # 修正点 2: 所有的类方法必须带 self 参数
        print ("调整分辨率")

audioplayer1 = AudioPlayer()
audioplayer1.play()
audioplayer1.ajust_volume()
vedioplayer1 = VedioPlayer()
vedioplayer1.play()
"""
#组合写法: 
"""
class Audio:
    def play(self):
        print("播放音频")
    def adjust_volume(self):
        print ("调整音量")
        
    def adjust_resolution(self):
    #如果你运行 audioplayer1.adjust_resolution()（它里面装的是 Audio），程序依然会崩溃。
    # 音频没有分辨率，我们写个提示或者干脆 pass
        pass
        
class Video:
    def play(self):
        print("播放视频")
    def adjust_resolution(self):
        print ("调整分辨率")
        
    def adjust_volume(self):
        print ("调整音量")

class MediaPlayer:
    def __init__(self,players=None):
        self.players = players or []
        
    def play(self):
        for player in self.players:
            player.play()
            
    def adjust_volume(self):
        for player in self.players:
            player.ajust_volume()
            
    def adjust_resolution(self):
        for player in self.players:
            player.adjust_resolution()


audioplayer1 = MediaPlayer(players = [Audio()])
audioplayer1.play()
audioplayer1.ajust_volume()
vedioplayer1 = MediaPlayer(players = [Video()])
vedioplayer1.adjust_resolution()
"""

# 第 28 关：OOP 实战：构建可复用的类库。

# 一、知识点
#1. 鸭子类型(Duck Typing)
#核心理念： “如果它走起来像鸭子，叫起来也像鸭子，那它就是鸭子。”
#我们不关心对象的类型是什么，只关心它能做什么（即它有哪些方法或属性）。
"""
class Duck:
    def quack(self):
        print("嘎嘎嘎！")

class Person:
    def quack(self):
        print("我在模仿鸭子叫：嘎嘎！")

def make_it_quack(animal):
    # 我们不在乎 animal 是 Duck 还是 Person
    # 只要它有 quack 方法就行
    animal.quack()

make_it_quack(Duck())    # 输出: 嘎嘎嘎！
make_it_quack(Person())  # 输出: 我在模仿鸭子叫：嘎嘎！
"""

#2. 抽象基类 (Abstract Base Classes/ABC)
#核心理念： “你必须先证明你是鸭子，我才让你进场。”。 抽象基类（通过 abc 模块实现）为类提供了一种合同制。它定义了一套规范，子类必须实现这些规范才能被实例化。
#使用必要性：强制约束： 确保子类实现了所有必须的方法，否则在实例化时就会报错。
#          类型检查： 允许使用 isinstance(obj, MyABC) 来做更有把握的判断。
#          接口设计： 适合大型项目，明确定义各个组件之间的交互协议。
#语法：
"""
#一行代码：
    from abc import ABC, abstractmethod  #这行代码其实是去 Python 的**法律库（abc 模块）**里请了两个“专员”过来

#两个角色： (父类模板，子类产品)

    #1. 角色A
    class 模板(ABC): #ABC：它是“身份专员”。它的作用是告诉 Python：“注意了，接下来的这个类不是普通的类，它是一个模板，不许直接拿来用（实例化）。
    """
"""
    当你写下 class 模板(ABC): 时，这个 模板（父类） 就是模板。
    它的身份： 它是“抽象”的。
    它的限制： Python 不允许你直接用它。你执行 s = Shape() 会直接报错。
    它的作用： 它像一张底稿，规定了后代必须长什么样。
"""
    """
    @abstractmethod #它是“考核专员”。它是一个装饰器（@），专门贴在方法头上。它的作用是告诉 Python：“这个方法是必考题，子类要是没写这道题，直接判不及格（报错）。”
    def 必须实现的方法(self):
        pass
     
    #2. 角色B
    class 具体实现(模板):
        def 必须实现的方法(self):
            print("我正在干活")
    """
"""
    当你写下 class Circle(Shape): 时，这个 Circle（子类） 是根据模板生产出来的具体产品。
    它的身份： 它是“具体”的。
    它的限制： 只要它把模板里的必考题（抽象方法）都做完了，它就可以被实例化。你执行 c = Circle() 是完全没问题的。
    它的作用： 它是真正的执行者，负责把模板里的构思变成现实。
"""
    """
        
#三个死理：
        
#1.父亲不能实例化：你不能执行 a = 模板()。因为它是抽象的，Python 不允许一个“半成品”存在。
#2.儿子不准偷懒：如果“具体实现”类没有写 必须实现的方法，那么儿子也会被封印，无法实例化。
#3.不继承 ABC 就没用：如果你忘了写 (ABC)，那么 @abstractmethod 就像普通的注释一样，起不到任何强制约束作用。
"""

#总结：鸭子类型是“随缘”，重在当下能不能用。抽象基类 (ABC) 是“契约”，重在事前的强制规范。    


#二、 类库设计原则
# ·单一职责：每个类只负责一个功能。
# ·低耦合高内聚：类之间依赖最小化，内部功能紧密关联。
# ·扩展性：通过抽象类或接口支持未来扩展。
# ·提供清晰的使用说明和完善的测试用例。
        
# 三、 实战技巧
# ·模块化拆分：将功能拆分为独立的模块（如 logger.py, config.py）。
# ·依赖注入：通过构造函数传递依赖，避免硬编码。
# ·配置管理：使用类属性或配置文件管理全局参数。



# 可复用类库实例：可复用的日志系统
"""

# logger.py
class Logger: 
    """
"""
    【指挥官类】
     它不关心日志具体怎么写（写文件还是发邮件），它只负责“下达命令”。
     这就是“低耦合”：Logger 不需要知道 FileHandler 的具体实现。
"""
    """
    def __init__(self,handlers): 
        # 这里的 handlers 是通过外部传进来的（依赖注入）
        # 就像给机器人装上不同的工具手，装上手电筒它就能照明，装上电钻它就能打洞。
        self.handlers = handlers
    def log(self,message): 
        #Logger 类的核心方法，用于记录日志。它会遍历所有的 handlers，并调用它们的 write 方法。
        
        for handler in self.handlers:
            handler.write(message): 
        #【关键点】它假定每个 handler 都有 write 方法。
        # 只要你能写(write)，你就是我的处理器(handler)。这就是“鸭子类型”。

# handlers.py
class FileHandler: 
    """
"""
    【专业工人 A：文件搬运工】
    专门负责把文字塞进硬盘里的文件。
"""
    """
    def __init__(self, filename): # 这里的 filename 是这个工人私有的属性
        self.filename = filename
    def write(self, message): # 具体的苦力活在这里实现
        with open(self.filename, "a") as f: #打开以传入参数filename命名的文件
            f.write(f"{message}\n")  #写入日志信息

# 1. 准备工具（实例化具体的功能类） 创建一个文件写入器，它会把日志写到 app.log 文件里
file_handler = FileHandler("app.log")

# 2. 组建团队（将工具注入到指挥官类中）
# 注意这里传的是 [列表]，意味着你可以放好几个不同的 handler 进去
logger = Logger([file_handler])# 创建一个日志记录器，它的 handlers 列表里装着 file_handler

# 3. 发射指令
# logger 只喊了一声“log”，底下的 file_handler 就默默去翻开文件写字了。
logger.log("系统启动") 

"""



# 四、单元测试 & 版本管理

# 1. 单元测试：使用 unittest 或 pytest 测试每个类的功能。
#pytest:(优先学习，unittest复杂)

"""
#假设你写了一个简单的加法函数，放在 calc.py 里：

# calc.py
def add(a, b):
    return a + b
#你只需要新建一个文件 test_calc.py（注意：文件名必须以 test_ 开头）：

# test_calc.py
from calc import add #从 calc.py 这个文件里，把 add 这个功能搬过来（不需要写 .py 后缀）。
def test_add_function():
    # 我们“断言” 1+1 应该等于 2
    assert add(1, 1) == 2

def test_add_negative():
    # 测试一下负数
    assert add(-1, 1) == 0
    
#在终端运行 pytest，它会自动找到所有 test_ 开头的文件，并执行里面的测试函数。如果屏幕是绿色的，恭喜你，代码没问题。如果屏幕是红色的，它会清晰地告诉你哪一行错了，结果是什么。
"""

#知识点一： 如果你想在一个文件里使用另一个文件定义的代码，就必须用 import。你可以把它理解为**“代码搬运语法”**。

#1. import+文件名： 这种方式是把整个文件（模块）搬过来。
#   写法：import calc
#   使用：调用时必须带上文件名的前缀。
#   例子：calc.add(1, 1)
#2. from+文件名+import+功能名： 这种方式是把文件里的某个具体功能搬过来。
#   写法：from calc import add
#   使用：直接用函数名即可，不需要加前缀。
#   例子：add(1, 1)

#知识点二：assert
#assert 语句是 Python 的“断言”语法。它的作用是：当你觉得某个条件应该成立时，就写一个 assert，如果条件不成立，程序会立刻报错
#assert 的常用写法：
# · 查相等：assert a == b （最常用）
# · 查不相等：assert a != b
# · 查包含：assert "apple" in ["apple", "banana"] （检查苹果在不在水果摊里）
# · 查真假：assert True / assert False




# 2. 版本管理：使用 Git 管理代码版本，遵循语义化版本号（Semantic Versioning）。/通过 __version__ 类属性标识库版本。
