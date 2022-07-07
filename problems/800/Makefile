CC = g++
CFLAGS = -Werror -Wall -O3
LDFLAGS = `pkg-config --libs primesieve`

main:
	mkdir -p bin
	$(CC) -o bin/main src/main.cpp $(CFLAGS) $(LDFLAGS)
