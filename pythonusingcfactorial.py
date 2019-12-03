from ctypes import*

result=CDLL("w.so")

answer=result.factorial(4)

print(answer)
