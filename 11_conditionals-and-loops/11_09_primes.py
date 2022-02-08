start = 1
stop = 1000

for number in range(start, stop + 1):
    for divisor in range(2, number):
        if number % divisor == 0:
           # print( f'{number} is not prime')
            break
        #else:
        #    print(number)
        #    break
       #if number % divisor - 1 != 0:
        #    print(number % divisor - 1)
        #    print( f'{number} is prime!')
        #    break
        if divisor == number - 1:
            print( f'{number} is prime!')
            break