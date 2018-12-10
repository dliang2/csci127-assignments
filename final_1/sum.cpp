#include <iostream>

// a less than b
int sumofsquares(int a, int b) {
  int sum = 0;
  int i;
  int square;
  for (i = a; i <= b; i++) {
    square = i * i;
    sum = sum + square;
  }
  return sum;
}


int main() {
  // expect 355
  std::cout << sumofsquares(5, 10) << std::endl;
  // expect 55
  std::cout << sumofsquares(1, 5) << std::endl;
  // expect 421
  std::cout << sumofsquares(14, 15) << std::endl;
  return 0;
}
