def my_callback(input):
    printStr = "function my_callback was called with %s input" % (input,)
    print(printStr)
    return printStr


def caller(input, func):
    return func(input)


# for i in range(5):
print("ffffffffff"+caller(123, my_callback))
