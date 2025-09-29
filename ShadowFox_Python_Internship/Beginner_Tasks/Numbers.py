# Task 1: Format function with octal representation
def format_example(num, code):
    result = format(num, code)
    return result

print(f"Task 1 Output: {format_example(145, 'o')}")


# Task 2: Area of circular pond + total water
r = 84
pi = 3.14
area = pi * (r ** 2)
water_per_sq_m = 1.4
total_water = area * water_per_sq_m

print(f"Task 2 - Area of the pond = {int(area)}")
print(f"Task 2 - Total water in the pond = {int(total_water)}")


# Task 3: Speed calculation
distance = 490
time_minutes = 7
time_seconds = time_minutes * 60
speed = distance / time_seconds

print(f"Task 3 - Speed = {int(speed)} m/s")
