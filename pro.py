import math
Θ = 60    # Maximum value of the angle
for i in range(60, 75):
    c = math.sin(Θ)
    l = 400 / c
    β_rad = math.asin(0.45 * c)   # Angle in radians of minimum angle 
    β_degree = math.degrees(β_rad)  # Convert angle to degrees of minimum angle
    Θ += 1
    print(f"if Θ = {Θ}, l = {round(l,2)}  and β = {round(β_degree,2)} \n")
