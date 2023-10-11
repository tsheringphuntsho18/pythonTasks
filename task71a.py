#calculate area of rectangle
def calculate_area(length, width):
    area = length * width
    return area


#calculate perimeter of rectangle
def calculate_perimeter(length, width):
    perimeter = 2*(length+width)
    return perimeter


#rectangle information
def rectangle_info(length,width):
    a = calculate_area(length,width)
    p = calculate_perimeter(length,width)
    print(f"Area of rectangle is {a} square units")
    print(f"perimeter of rectangle is {p} units")
rectangle_info(4,5)
    