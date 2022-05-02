#include <stdio.h>
#include <stdint.h>
#include <math.h>

int main(int argc, char *argv[]) {
	const uint64_t limit = 2000000;
	for (uint64_t num = 2; num < limit; ++num) {
		const uint64_t root = sqrt((double) num);
		for (uint64_t div = 2; div <= root; ++div) {
			if (num % div == 0) {
				// A necessary evil
				goto outer_loop;
			}
		}
		printf("%ld\n", num);
	outer_loop:;
	}
	return 0;
}
