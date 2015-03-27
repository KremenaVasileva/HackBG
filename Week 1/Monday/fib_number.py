def fibonacci(n):
    fib_list = []
    previous_num = 1
    current_num = 1
    new_num = 1
    if n == 1:
        fib_list.append(current_num)
        return fib_list
    else:
        while n >= 1:
            fib_list.append(current_num)
            previous_num = current_num
            current_num = new_num
            new_num = previous_num + current_num
            n -= 1
        return fib_list


def fib_number(n):
    fib_list = fibonacci(n)
    result = ''
    for i in range(0, len(fib_list)):
        result += str(fib_list[i])
    return int(result)


n = int(input("Enter num: "))

print (fib_number(n))
