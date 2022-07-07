#include <cstdint>
#include <iostream>
#include <fstream>
#include <set>
#include <algorithm>

#define MAX_N 15704507

// I attepmted to implement this header generator myself that would
// create a header file with the primes needed, but I heavily
// underestimated the time it would take. After doing some light
// searching, I came to the conclusion that using
// https://github.com/kimwalisch/primesieve/ was multitudes
// faster. This file is just a remnant of my attempt.
int main() {
	std::ofstream file;
	file.open("src/primes.hpp");
	file << "#ifndef PRIMES_HPP\n";
	file << "#define PRIMES_HPP\n\n";
	file << "#include <cstdint>\n\n";
	file << "uint32_t primes[] = {2";

	std::set<uint32_t> primes;
	primes.insert(2);

	for (uint32_t i = 3; i <= MAX_N; ++i) {
		auto it = std::find_if(primes.cbegin(), primes.cend(), [&](const auto &n) { return i % n == 0; });
		if (it == primes.cend()) {
			primes.insert(i);
			file << "," << i;
		}
	}

	file << "};\n\n";
	file << "#endif";
	file.close();
	return 0;
}
