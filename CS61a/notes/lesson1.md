# 1.1 Getting Started 

## Guiding principles of debugging are:

**Test incrementally **  增量测试

**Isolate errors**  隔离错误

**Check your assumptions**  检查假设

**Consult others** 询问他人

Incremental testing, modular design, precise assumptions, and teamwork are themes that persist throughout this text.

# 1.2 Elements of Programming



# 1.3 Defining New Functions

定义新函数

结构

```python
def name(formal parameters):
    """
    函数作用注释
    """
    函数内容
    return 值或表达式
```

调用函数

`name(值或表达式)`

可以使用如下语句将一个函数用另一个name表示

`new_name = name #该语句将函数name的内容赋给了函数new_name`

# 1.5 Control

## statements 语句

pure function

non-pure function 非纯语句，

## Compound Statements复合语句

结构

```python
<header>:
	<statement>
	<statement>
<separating header>:
	<statement>
	<statement>
	...
...
```

  注意缩进

## Conditional Statements 状态语句

if语句

结构

```python
if 判断表达式:
	<suite>
elif 判断表达式:
    <suite>
else:
    <suite>
```

Boolean operators 布尔运算符

“and 与”  “or 或”  “not 非”

执行布尔运算的函数名常以is开头，如

```python
isfinite 是否有限
isdigit 是否全是数字
isinstance 是否是实例
```

## Iteration 循环

while语句

结构

```python
while <expression>:
    <suite>
```

## Assertions 校验语句

如`assert fib(8) == 13`

When writing Python in files, rather than directly into the interpreter, tests are typically written in the same file or a neighboring file with the suffix `_test.py`.

测试写入   同名_test.py   文件中 

简易测试

Python provides a convenient method for placing simple tests directly in the docstring of a function. The first line of a docstring should contain a one-line description of the function, followed by a blank line. A detailed description of arguments and behavior may follow. 

e.g.

```py
>>> def sum_naturals(n):
        """Return the sum of the first n natural numbers.

        >>> sum_naturals(10)
        55
        >>> sum_naturals(100)
        5050
        """
        total, k = 0, 1
        while k <= n:
            total, k = total + k, k + 1
        return total
```

Then, the interaction can be verified via the [doctest module](http://docs.python.org/py3k/library/doctest.html). Below, the `globals` function returns a representation of the global environment, which the interpreter needs in order to evaluate expressions.

```py
>>> from doctest import testmod
>>> testmod()
TestResults(failed=0, attempted=2)
```

To verify the doctest interactions for only a single function, we use a `doctest` function called `run_docstring_examples`. This function is (unfortunately) a bit complicated to call. Its first argument is the function to test. The second should always be the result of the expression `globals()`, a built-in function that returns the global environment. The third argument is `True` to indicate that we would like "verbose" output: a catalog of all tests run.

```py
>>> from doctest import run_docstring_examples
>>> run_docstring_examples(sum_naturals, globals(), True)
Finding tests in NoName
Trying:
    sum_naturals(10)
Expecting:
    55
ok
Trying:
    sum_naturals(100)
Expecting:
    5050
ok
```

When writing Python in files, all doctests in a file can be run by starting Python with the doctest command line option:

`python3 -m doctest <python_source_file>`

加在代码中 ：

```py
if __name__==__main__
	import doctest
    doctest.testmod()
    doctest.run_docstring_examples(<function's name>,globals(),True)
```



**Exhaustive unit testing is a hallmark of good program design.** 

**详尽的测试是好程序的标志**

