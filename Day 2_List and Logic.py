# DAY 2: List Operations & Conditional Logic
# ==============================================================================

# 4. LIST METHOD: .append()
# Core Use: Dynamically adding a new item to the end of an existing list.
# Explanation: Modifies the original list by inserting the new element at the final position.

zones = ["charminar", "khairatabad"]
zones.append("secunderabad")
print(zones)


# 5. BUILT-IN FUNCTION: len()
# Core Use: Counting the total number of items inside a collection or list.
# Explanation: Evaluates the list and returns an integer representing its total size, which is then stored in a variable.

zones = ["charminar", "khairatabad", "secunderabad"]
total_zones = len(zones)
print(total_zones)


# 6. KEYWORDS: if - else
# Core Use: Branching code execution based on a single condition (True or False).
# Explanation: Runs the 'if' block if the condition is met, otherwise falls back to the 'else' block.

total_count = 349

if total_count > 100:
    print("This is a big zone")
else:
    print("This is a small zone")

