#include <iostream>
#include <math.h>

int discriminant(int a, int b, int c) {
  return (b * b - (4 * a * c));
}

double quadsolve(int a, int b, int c) {
  int d = discriminant(a, b, c);
  double root;
  if (d >= 0) {
    root = (-b + sqrt(d)) / (2 * a);
    return root;
  }
  
  else {
    return 0;
  }
}

int main() {
  // test discriminant, 2 positive 1 negative
  std::cout << discriminant(2, 5, 2) << std::endl;
  std::cout << discriminant(4, 7, 0) << std::endl;
  std::cout << discriminant(6, 4, 2) << std::endl;

  // expect -1/2
  std::cout << quadsolve(2, 5, 2) << std::endl;
  // expect 0
  std::cout << quadsolve(4, 7, 0) << std::endl;
  // expect 0 because negative discriminant
  std::cout << quadsolve(6, 3, 1) << std::endl;
  
  return 0;
}
