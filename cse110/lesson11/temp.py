f = open('names.txt')
lines = f.readlines()[1:]
favorite_number_list = []
girl_name_list = []
for line in lines:
    line_list = line.split()
    girl_name_list.append(line_list[1])
    favorite_number_list.append(float(line_list[4]))


minVal, minIdx = min((val, idx) for (idx, val) in enumerate(favorite_number_list))
maxVal, maxIdx = max((val, idx) for (idx, val) in enumerate(favorite_number_list))

print(f"The smallest number: {girl_name_list[minIdx]}'s number is: {minVal}")
print(f"The largest number: {girl_name_list[maxIdx]}'s number is: {maxVal}")

f.close()
