#include <iostream>
#include <cstdint>
#include <cmath>

auto divisors(const uint64_t n) -> uint32_t {
	uint32_t total = 2;

	const double root = std::sqrt(n);
	const uint64_t introot = (uint64_t)root;

	if (root == introot) {
		total++;
	}

	for (uint64_t i = 2; i <= introot; ++i) {
		if (n % i == 0) {
			total += 2;
		}
	}
	
	return total;
}

constexpr auto triangle(const uint64_t n) -> uint64_t {
	return n * (n - 1) / 2;
}

int main(int argc, char *argv[]) {
	constexpr uint64_t over = 500;

	for (uint64_t i = 2;; i++) {
		const uint64_t tri = triangle(i);
		const uint64_t div = divisors(tri);
		if (div > over) {
			std::cout << "(" << tri << ", " << div << ")" << std::endl;
			break;
		}
	}
	return 0;
}
