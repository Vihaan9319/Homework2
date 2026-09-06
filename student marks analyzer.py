empty_list = []
print(empty_list)
marks = [100, 85, 90, 72, 50]
print(f"Student marks: {marks}")
sample = [1, 2, 3]*2
print(f"Repeated sample marks: {sample}")
print(f"Number of marks: {len(marks)}")
print(f"First mark: {marks[0]}")
print(f"Last mark: {marks[-1]}")
print(f"The first three marks are, {marks[0:3]}")
print(f"The marks reversed: {marks[::-1]}")
def match_mark(list_provided):
    count = 0
    matched_marks = []
    for mark in list_provided:
        mark = str(mark)
        if len(mark) > 1 and mark[0] == mark[-1]:
            count += 1
            matched_marks.append(mark)
    return count and matched_marks
total = 0
for i in marks:
    total += i
marks.sort()
average = total/ len(marks)
print(f"The total of all the marks is {total}")
print(f"The average of all the marks is {average}")
print(f"The lowest numbers in the marks is {marks[0]}, and the highest number in the marks is {marks[-1]}")
print("=================STUDENT MARKS SUMMARY===============")
print(f"Sorted marks: {marks}")
print(f"Total marks: {total}")
print(f"Average marks: {average}")
print(f"Lowest mark: {marks[0]}")
print(f"Highest mark: {marks[-1]}")
print(f"=====================================================")