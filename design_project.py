import math

def function():
    output_str = ""
    Θ = 60
    for i in range(60, 75):
        c = math.sin(Θ)
        l = 400 / c
        β_rad = math.asin(0.45 * c)   # Angle in radians
        β_deg = math.degrees(β_rad)   # Convert angle to degrees
        Θ += 1
        output_str += f"if Θ = {Θ}, l = {round(l, 2)} and β = {round(β_deg, 2)} degrees \n"
    return output_str

output = function()

# Print the output to console
print(output)

# Write the output to a file
with open('output.txt', 'w') as file:
    file.write(output)
