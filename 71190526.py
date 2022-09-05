import random
import timeit

#generate list berukuran n
def generate_list(n):
    batas_atas = n * 100
    randomlist = random.sample(range(0, batas_atas), n)
    randomlist.sort()
    return randomlist

def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1) + fibo(n-2))
    
for i in range(1, 10+1):
    data = generate_list(i)
    start = timeit.default_timer() #waktu mulai
    hasil = fibo(i) #pasangan yang memenuhi target
    end = timeit.default_timer() #waktu selesai
    print('Fibonacci ke', i,'=', hasil, ':', end-start, 'second')