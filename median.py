"""Median calculator."""
def median_calc(arr):
   arr_sorted = sorted(arr)
   length_arr = len(arr)
   median_id = length_arr//2
   print(median_id)
   if length_arr % 2 == 0:
       
       median = (arr_sorted[median_id] + arr_sorted[median_id -1])/2
       return median
   else:
       median = (arr_sorted[median_id])
       return median 




       
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

median_value = median_calc(numbers)

print(f"The median is: {median_value}")