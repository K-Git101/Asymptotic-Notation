students = ["Johnny", "Riya", "Arjun", "Maya", "Aarav"]
scores = [92, 85, 78, 95, 88]

print("Students:", students)
print("Scores:", scores)

input("Direct Access: O(1). Press Enter ")

position = int(input("Enter student position (1-5): "))
if 1 <= position <= len(scores):
    print("Score:", scores[position - 1], "-> O(1)")

input("Linear Search: O(n). Press Enter ")

target = input("Enter student name: ")
steps = 0

for i in range(len(students)):
    steps += 1
    if students[i].lower() == target.lower():
        print("Score:", scores[i], "Position:", i + 1)
        break
else:
    print("Student not found!")

print("Checks:", steps, "-> O(n)")

input("Pair Comparison: O(n^2). Press Enter ")

n = len(students)
steps = 0

for i in range(n):
    for j in range(i + 1, n):
        steps += 1

print("Comparisons:", steps, "-> O(n^2)")

input("Review Big-O, Omega, and Theta. Press Enter ")

print("Best case: O(1)")
print("Average case: O(n)")
print("Worst case: O(n)")
print("Omega Ω: Lower bound")
print("Theta Θ: Tight bound")