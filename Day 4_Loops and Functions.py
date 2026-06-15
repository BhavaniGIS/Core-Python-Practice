# DAY 4: Loops, Ranges & Functions
# ==============================================================================

# 10. KEYWORD / LOOP: for
# Core Use: Iterating over elements of a sequence step-by-step.
# Explanation: Automatically extracts each item from a list one-by-one and executes the block.

zones = ["charminar", "khairatabad", "secunderabad"]
for z in zones:
    print(z)


# 11. BUILT-IN FUNCTION / TYPE: range()
# Core Use: Generating an arithmetic sequence of numbers over a specific interval.
# Explanation: Often used in for loops to repeat a specific action a fixed number of times.

for i in range(3):
    print(i)


# 12. KEYWORD / FUNCTION DEFINITION: def (Without Return)
# Core Use: Wrapping a reusable segment of code into a named function block.
# Explanation: Defines a block of code that executes only when the function is explicitly called.

def show_available_zones():
    zones = ["Charminar", "Khairatabad", "Secunderabad"]
    print("Available Zones are:")
    print(zones)

show_available_zones()


# 13. KEYWORD: return (Inside a Function)
# Core Use: Terminating a function and sending a calculated result back to the caller.
# Explanation: Passes the output value out of the function block so it can be saved in a variable.

def double_the_zones(count):
    total = count * 2
    return total

result = double_the_zones(5)
print(result)
