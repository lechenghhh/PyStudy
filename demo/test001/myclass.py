class MyClass:
    """一个简单的类实例"""
    i = 12345

    def sayHello(self):
        return 'hello world'

    def hahah(self):
        return 'let go'

# 实例化类
myClass = MyClass()

# 访问类的属性和方法
print("MyClass 类的属性 i 为：", myClass.i)

print("MyClass 类的方法 f 输出为：" + myClass.sayHello())
