#include <iostream>
#include <cmath>

int main() {
    double angle = 60; // Maximum value of the angle
    for (int i = 60; i < 75; i++) {
        double c = sin(angle * M_PI / 180);
        double length = 400 / c;
        double beta_rad = asin(0.45 * c); // Angle in radians of minimum angle
        double beta_degree = beta_rad * 180 / M_PI; // Convert angle to degrees of minimum angle
        angle += 1;
        std::cout << "if angle = " << angle << ", length = " << std::round(length * 100) / 100 << " and beta = " << std::round(beta_degree * 100) / 100 << "\n";
    }
    return 0;
}
