#Array 
def get_user_input():
    user_inputs = []
    for i in range(3):
        num = int(input(f"Enter number {i+1}:"))
        user_inputs.append(num)
    return user_inputs
def is_even(user_inputs):
    for num in user_inputs:
        if num % 2 != 0:
            return False
    return True
user_inputs = get_user_input()
result = is_even(user_inputs)
print(result)