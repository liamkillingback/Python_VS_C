import time, random
from ctypes import c_int, cdll
"""
__________________ _______  _______   _________ _______ _________ _______  _        _______ 
\__   __/\__   __/(       )(  ____ \  \__   __/(  ____ )\__   __/(  ___  )( \      (  ____ \\
   ) (      ) (   | () () || (    \/     ) (   | (    )|   ) (   | (   ) || (      | (    \/
   | |      | |   | || || || (__         | |   | (____)|   | |   | (___) || |      | (_____ 
   | |      | |   | |(_)| ||  __)        | |   |     __)   | |   |  ___  || |      (_____  )
   | |      | |   | |   | || (           | |   | (\ (      | |   | (   ) || |            ) |
   | |   ___) (___| )   ( || (____/\     | |   | ) \ \_____) (___| )   ( || (____/\/\____) |
   )_(   \_______/|/     \|(_______/     )_(   |/   \__/\_______/|/     \|(_______/\_______)
                                                                                            
"""
lib = cdll.LoadLibrary('C:/Users/liam/Documents/NewCodespace/finalProject/c_.so')
c_multiply = lib.c_multiply

def main():
    print()
    #List of mathematical functions
    math_list = [lambda x, y:x * y, lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x / y]
    
    #Random number between 1 and 10,000
    n = random.randint(1, 10000)
    m = random.randint(1, 10000)
    global py_time
    #Does math 1 million times per function and times it
    for func in math_list:
        global py_time
        time1 = float(time.time())
        ans = 0
        for i in range(1000000):
            ans = func(n, m)
            ans += ans
        time2 = float(time.time() - time1)
        py_time = time2
        
        print(f"{round(time2, 4)}s Py", end=' ')
    print()

    #Below are the times taken for the same equations in C
    time1 = float(time.time())
    c_multiply(n, m, 1000000)
    time2 = float(time.time() - time1)
    print(f"{round(time2, 4)}s C", end=' ')
    """
 __    ____    __    __  __ 
(  )  (_  _)  /__\  (  \/  )
 )(__  _)(_  /(__)\  )    ( 
(____)(____)(__)(__)(_/\/\_)
    """
    
    time1 = float(time.time())
    c_addition(n, m, 1000000)
    time2 = float(time.time() - time1)
    print(f"{round(time2, 4)}s C", end=' ')

    
    time1 = float(time.time())
    c_subtraction(n, m, 1000000)
    time2 = float(time.time() - time1)
    print(f"{round(time2, 4)}s C", end=' ')


    time1 = float(time.time())
    for i in range(1000000):
        ans = lib.c_div(c_int(n), c_int(m))
        ans += ans
    time2 = float(time.time() - time1)
    print(f"{round(time2, 4)}s C")
    print()

    """
   _____                  __                .__  .__        
  /  _  \  __ __  _______/  |_____________  |  | |__|____   
 /  /_\  \|  |  \/  ___/\   __\_  __ \__  \ |  | |  \__  \  
/    |    \  |  /\___ \  |  |  |  | \// __ \|  |_|  |/ __ \_
\____|__  /____//____  > |__|  |__|  (____  /____/__(____  /
        \/           \/                   \/             \/ 
    """

    #Python loop speed
    time1 = float(time.time())
    number = 1000000
    s = 0
    for i in range(number):
        s += 1
    time2 = float(time.time() - time1)
    print(f"{round(time2, 4)}s py loop speed 1 million loops")
    py = time2
    """
     _      _____ _     ____  ____  _     ____  _      _____
    / \__/|/  __// \   /  _ \/  _ \/ \ /\/  __\/ \  /|/  __/
    | |\/|||  \  | |   | | //| / \|| | |||  \/|| |\ |||  \  
    | |  |||  /_ | |_/\| |_\\| \_/|| \_/||    /| | \|||  /_ 
    \_/  \|\____\\____/\____/\____/\____/\_/\_\\_/  \|\____\\
                                                            
    """
    #C loop speed
    time1 = float(time.time())
    ans = lib.c_loop(c_int(number))
    time2 = float(time.time() - time1)
    C = time2
    print(f"{round(time2, 4)}s C loop speed 1 million loops")
    print(f'C is {round((py / C), 2)} times faster than Python at looping in this case')
    print()

    #Using C to do the looping for addition.
    time1 = float(time.time())
    ans = lib.c_looper(c_int(n), c_int(m), c_int(number))
    time2 = float(time.time() - time1)
    print(f"{round(time2, 4)}s When using C to loop instead of using python to call the C function")
    print(f'C is {round((py_time / time2), 2)} Times faster with 1,000,000 addition equations')
    print()
    return 0

def c_subtraction(x, y, z):
    ans = 0
    for i in range(z):
        ans = lib.c_sub(c_int(x), c_int(y))
        ans += ans
    return ans
def c_multiply(x, y, z):
    ans = 0
    for i in range(z):
        ans = lib.c_multiply(c_int(x), c_int(y))
        ans += ans
    return ans
def c_addition(x, y, z):
    ans = 0
    for i in range(z):
        ans = lib.c_add(c_int(x), c_int(y))
        ans += ans
    return ans

if __name__ == '__main__':
    main()
