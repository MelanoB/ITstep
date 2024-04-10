# 1
# lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#
# with open("text.txt", "w") as file:
#     for i in lst:
#         file.write(f"{i}\n")

# 2
count = 0

file = open("text1.txt")
print(file.read())
file.close()

with open("text1.txt") as file:
    for i in file:
        if i == i.capitalize():
            count += 1

print(f"მაღალ რეგისტრში სიტყვების რაოდენობა: {count}")