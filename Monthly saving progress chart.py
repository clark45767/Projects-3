# Monthly Savings Progress Chart
 
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
 
# Create month numbers from 1 to 12
months = np.arange(1, 13)
 
# Create two savings plans using equations
regular_savings = 500 * months
goal_savings = 700 * months
 
# Plot the regular savings plan
plt.plot(
    months,
    regular_savings,
    linestyle="dashed",
    marker="o",
    linewidth=2,
    label="Regular Plan: 500 per month"
)
 
# Plot the goal savings plan
plt.plot(
    months,
    goal_savings,
    linestyle="solid",
    marker="D",
    linewidth=2,
    label="Goal Plan: 700 per month"
)
 
# Fill the area between both savings plans
plt.fill_between(
    months,
    regular_savings,
    goal_savings,
    alpha=0.3,
    label="Savings Difference"
)
 
# Add chart title and axis labels
plt.title("Monthly Savings Progress")
plt.xlabel("Month")
plt.ylabel("Total Savings")
 
# Set the axis ranges
plt.xlim(1, 12)
plt.ylim(0, 9000)
 
# Display all month numbers
plt.xticks(months)
 
# Add a legend to identify each line
plt.legend()
 
# Display the chart
plt.show()
