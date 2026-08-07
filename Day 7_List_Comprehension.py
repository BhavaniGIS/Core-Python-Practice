# ==============================================================================
# ADVANCED PYTHON: List Comprehension & Nested List Comprehension
# ==============================================================================

# 1. Filtering Even Numbers using 'if' condition
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)
# Output: [2, 4, 6]


# 2. Conditional Transformation using 'if-else'
scores = [3, 8, 2, 9]
result = ["High" if s > 5 else "Low" for s in scores]
print(result)
# Output: ['Low', 'High', 'Low', 'High']


# 3. Nested List Comprehension (Flattening a 2D Matrix)
matrix = [[1, 2], [3, 4]]
flat_list = [num for sublist in matrix for num in sublist]
print(flat_list)
# Output: [1, 2, 3, 4]


# 4. Basic List Comprehension (Simple Iteration)
zones = ["Charminar", "Kairatabad", "Secundarabad"]
new_list = [z for z in zones]
print(new_list)
# Output: ['Charminar', 'Kairatabad', 'Secundarabad']


# 5. Filtering Specific Strings using 'if' condition
zones = ["Charminar", "Kairatabad", "Secundarabad"]
new_list = [z for z in zones if z == "Charminar"]
print(new_list)
# Output: ['Charminar']
