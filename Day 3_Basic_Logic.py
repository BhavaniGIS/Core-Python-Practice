# DAY 3: Advanced Rules & Multiple Conditions
# ==============================================================================

# 7. KEYWORDS: if - elif - else
# Core Use: Evaluating multiple conditions sequentially until a match is confirmed.
# Explanation: Checks conditions one after another; executes the first True block it encounters.

total_count = 349

if total_count > 500:
    print("Mega zone")
elif total_count > 100:
    print("Big zone")
else:
    print("Small zone")


# 8. LOGICAL OPERATOR: and
# Core Use: Combining multiple conditions where ALL individual checks must pass.
# Explanation: Evaluates to True only if both the left and right conditions are True.

total_count = 349

if total_count > 100 and total_count < 500:
    print("This is a Medium to Big zone")


# 9. LOGICAL OPERATOR: or
# Core Use: Combining multiple conditions where AT LEAST ONE individual check must pass.
# Explanation: Evaluates to True if either of the conditions (or both) are True.

total_count = 349
zone_type = "special"

if total_count > 100 or zone_type == "special":
    print("High Priority Zone")

