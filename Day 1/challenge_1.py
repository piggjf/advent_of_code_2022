input_file = open('input.txt', 'r')
lines = input_file.readlines()
elfs = [0]

for line in lines:
    calorie = line.strip()
    if len(calorie) == 0:
        elfs.append(0)
        continue
    else:
        elfs[-1] += int(calorie)

# Part 1 - Top calorie
print(max(elfs))

# Part 2 - Sum of top 3 calories
print(sum(sorted(elfs, reverse=True)[0:3]))