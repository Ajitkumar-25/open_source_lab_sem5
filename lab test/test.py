import matplotlib.pyplot as plt

# Test data
GMAT_score = [87, 91, 79, 88, 99, 79, 59, 99, 79, 33]
GRE_score = [34, 78, 78, 47, 99, 87, 31, 44, 19, 29]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Create the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(GMAT_score, GRE_score, color='b', marker='o')
plt.title("GMAT vs GRE Scores")
plt.xlabel("GMAT Score")
plt.ylabel("GRE Score")

# Annotate points with student marks
for i in range(len(GMAT_score)):
    plt.annotate(marks_range[i], (GMAT_score[i], GRE_score[i]))

# Set axis limits
plt.xlim(0, 110)
plt.ylim(0, 110)

# Display the plot
plt.grid(True)
plt.show()
