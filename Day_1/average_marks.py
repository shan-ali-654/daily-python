def average_marks(students):
    avg_marks = []
    for items in students:
        marks = items.get("marks")
        if type(marks) == int or type(marks) == float:
            avg_marks.append(marks)
    if len(avg_marks) == 0:
        return 0
    result = sum(avg_marks) / len(avg_marks)
    return result

t1 = [
    {"name": "ali", "marks": 80},
    {"name": "sara", "marks": "ninety"},
    {"name": "bilal"},
    {"name": "hina", "marks": 45}
]
t2 = [{"name": "Ali"}, {"name": "Sara", "marks": "eighty"}]
t3 = []
t4 = [{"name": "A", "marks": 40.0}, {"name": "B", "marks": 60.0}]
t5 = [{"name": "A", "marks": 50}, {"name": "B", "marks": 500}, {"name": "C", "marks": -20}]

print("Test 1:", average_marks(t1))
print("Test 2:", average_marks(t2))
print("Test 3:", average_marks(t3))
print("Test 4:", average_marks(t4))
print("Test 5:", average_marks(t5))