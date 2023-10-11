#calculate hypotenuse
import math 
def calulate_hypotenuse(length1, length2):
    hypo = math.sqrt(length1**2 + length2**2)
    return hypo
#triangle info
def triangle_info(length1,length2):
    hypotenuse = calulate_hypotenuse(length1,length2)
    return hypotenuse
result = triangle_info(4,5)
print(result)