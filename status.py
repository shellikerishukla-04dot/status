
import sys



if len(sys.argv) > 1:
    scores = sys.argv[1:]  # Read from system arguments
    print("User provided input values:")
else:
    print("No command-line input provided. Using default values:")
    scores = ["10", "20", "30", "40"]  # Default values

# Convert using eval() for calculations
total = sum(eval(x) for x in scores)
average = total / len(scores)

print("Sum of scores =", total)
print("Average of scores =", average)


