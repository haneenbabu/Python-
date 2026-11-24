color_list1 = input("Enter colors for list 1 separated by commas: ").split(",")
color_list2 = input("Enter colors for list 2 separated by commas: ").split(",")

print("Colors not contained in color list 2:")

for color in color_list1:
    if color not in color_list2:
        print(color.strip())