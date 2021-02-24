import csv
from collections import Counter

with open("tests.csv", "r", newline="") as f:
    csv_reader = csv.reader(f)
    file_data = list(csv_reader)
    file_data.pop(0)
    new_data = []
    for i in range(len(file_data)):
        n = file_data[i][1]
        new_data.append(float(n))

#mean calculation
leng = len(new_data)
total = 0

for x in new_data:
    total += x

mean = total/leng
print(f"The mean of the data is: {mean}")

#median calculation
new_data.sort()
if leng % 2 == 0:
    median1 = new_data[leng//2-1]
    median2 = new_data[leng//2]
    median = (median1+median2)/2
else:
    median = new_data[leng//2]

print(f"The median of the data is {median}")

# mode calculation
data = Counter(new_data)
mode__range = {"50-60": 0, "60-70": 0, "70-80": 0}
for height ,occurence in data.items():
    if 50 < float(height) < 60:
        mode__range["50-60"] += occurence
    elif 60 < float(height) < 70:
        mode__range["60-70"] += occurence
    elif 70 < float(height) < 80:
        mode__range["70-80"] += occurence

mode_range = 0
mode_occurence = 0

for range, occurence in mode__range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

mode = float((mode_range[0]+mode_range[1])/2)

print(f"The mode is {mode}")