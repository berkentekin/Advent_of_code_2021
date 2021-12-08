CC=gcc
CFLAGS=-I.
DEPS = cutils/utils.h

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

day7: cutils/utils.o day7.o
	$(CC) -o day7 cutils/utils.o day7.o
