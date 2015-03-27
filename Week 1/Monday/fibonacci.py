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

n = int(input("Enter num: "))

print (fibonacci(n))
