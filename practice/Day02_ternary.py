age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"

# its also called conditional expression, or same as ternary like java
message = "Eligible" if age >= 18 else "Not eligible"
print(message)