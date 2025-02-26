# ---------------------Error estimation of measurements----------------------
# read the line from the file and store them in a list
import os
current_path = os.path.dirname(__file__)
file_path = os.path.join(current_path, '3-1.txt')
data = []
with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()  # remove the whitespace characters
        if line:  # make sure that the line is not empty
            data.append(float(line))  # make string to float

# calculate the mean value
N = len(data)
mean_value = sum(data)/N

# calculate the variance and standard deviation
var = sum([(x-mean_value)**2 for x in data])
std_dev = (var/(N - 1))**0.5

# calculate the standard error
std_error = std_dev/(N ** 0.5)

# print the result
print(f"Optimal Estimation: {mean_value:.3f}")
print(f"Standard Error: ±{std_error:.3f}")
