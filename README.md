## 	[Python命名规范](https://www.cnblogs.com/EmptyRabbit/p/7679093.html)

		

**Google Python****命名规范**

module_name, &nbsp;模块

package_name, &nbsp;包

ClassName, &nbsp;类

method_name,&nbsp; 方法

ExceptionName, &nbsp;&nbsp;异常

function_name, &nbsp;函数

GLOBAL_VAR_NAME, 全局变量

instance_var_name,&nbsp; 实例

function_parameter_name, &nbsp;&nbsp;参数

local_var_name.&nbsp; 本变量

**&nbsp;**

**类**

总是使用首字母大写单词串。如MyClass。内部类可以使用额外的前导下划线。

**&nbsp;**

**函数****&amp;****方法**&nbsp; &nbsp;&nbsp;

小写+下划线

*注意*：混合大小写仅被允许用于这种风格已经占据优势的时候，以便保持向后兼容。

&nbsp;

**函数和方法的参数**<br>
如果一个函数的参数名称和保留的关键字冲突，通常使用一个后缀下划线

&nbsp;

**全局变量**<br>
对于from M import *导入语句，如果想阻止导入模块内的全局变量可以使用旧有的规范，在全局变量上加一个前导的下划线。<br>
*注意*:应避免使用全局变量

&nbsp;

**变量**

小写，由下划线连接各个单词。如color = WHITE，this_is_a_variable = 1<br>
*注意*：<br>
1.不论是类成员变量还是全局变量，均不使用 m 或 g 前缀。<br>
2.私有类成员使用单一下划线前缀标识。<br>
3.变量名不应带有类型信息，因为Python是动态类型语言。如 iValue、names_list、dict_obj 等都是不好的命名。

&nbsp;

**常量**<br>
常量名所有字母大写，由下划线连接各个单词如MAX_OVERFLOW，TOTAL。

&nbsp;

**异常**<br>
以“Error”作为后缀。

&nbsp;

**文件名**<br>
全小写,可使用下划线

&nbsp;

**包**<br>
应该是简短的、小写的名字。如果下划线可以改善可读性可以加入。如mypackage。

&nbsp;

**模块**<br>
与包的规范同。如mymodule。

&nbsp;

**缩写**<br>
命名应当尽量使用全拼写的单词，缩写的情况有如下两种：<br>
1.常用的缩写，如XML、ID等，在命名时也应只大写首字母，如XmlParser。<br>
2.命名中含有长单词，对某个单词进行缩写。这时应使用约定成俗的缩写方式。

例如：<br>
function 缩写为 fn<br>
text 缩写为 txt<br>
object 缩写为 obj<br>
count 缩写为 cnt<br>
number 缩写为 num，等。

<br>
**前导后缀下划线**<br>
一个前导下划线：表示非公有。<br>
一个后缀下划线：避免关键字冲突。<br>
两个前导下划线：当命名一个类属性引起名称冲突时使用。<br>
两个前导和后缀下划线：“魔”（有特殊用图）对象或者属性，例如__init__或者__file__。绝对不要创造这样的名字，而只是使用它们。<br>
*注意*：关于下划线的使用存在一些争议。

&nbsp;

**特定命名方式**<br>
主要是指 __xxx__ 形式的系统保留字命名法。项目中也可以使用这种命名，它的意义在于这种形式的变量是只读的，这种形式的类成员函数尽量不要重载。如<br>
class Base(object):<br>
def __init__(self, id, parent = None):<br>
self.__id__ = id<br>
self.__parent__ = parent<br>
def __message__(self, msgid):<br>
其中 __id__、__parent__ 和 __message__ 都采用了系统保留字命名法。<br>
<br>




			posted on 2017-10-16 21:55 [收藏](#)

		

### 导航


<li>

</li>

<li>

[首页](http://www.cnblogs.com/EmptyRabbit/)</li>

<li>

[新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)</li>

<li>

</li>

<li>





</li>

<li>

[管理](https://i.cnblogs.com/)</li>




	Powered by: 

	<br />

	

	[<font face="Verdana">博客园</font>](http://www.cnblogs.com/)

	<br />

	Copyright &copy; 跑跑兔


