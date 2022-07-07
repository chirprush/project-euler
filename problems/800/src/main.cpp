#include <cstdio>
#include <cstdint>
#include <cmath>
#include <vector>

#include <primesieve.hpp>

constexpr auto H1(uint32_t p, uint32_t q) -> double {
	return p * log2(q) + q * log2(p);
}

constexpr auto less_than_or_eq(double value, double bound) -> bool {
	constexpr double EPSILON = 0.000001;
	return value < bound + EPSILON;
}

int main(int argc, char *argv[]) {
	constexpr uint32_t MAX_N = 15704507;
	constexpr double max_bound = 800800 * log2(800800);
	uint64_t total = 0;

	std::vector<uint32_t> primes;
	primesieve::generate_primes(MAX_N, &primes);

	for (uint32_t i = 0; i < primes.size(); ++i) {
		for (uint32_t j = i + 1; j < primes.size(); ++j) {
			const double value = H1(primes[i], primes[j]);
			const bool greater = !less_than_or_eq(value, max_bound);
			if (greater && j == i + 1) goto end;
			if (greater) break;
			++total;
		}
	}

 end:
	printf("%ld\n", total);
	return 0;
}
