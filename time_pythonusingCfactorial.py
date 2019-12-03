import timeit

code="""
from ctypes import*

result=CDLL("w.so")

answer=result.factorial(4)

print(answer)
"""

t=timeit.timeit(code,number=1)
printf("time in seconds is : = ",t,".")
