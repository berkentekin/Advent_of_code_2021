CC=gcc
CFLAGS=-I. -Wall -Wextra -pedantic-errors -ansi -g -lm
DEPS = ../cutils/utils.h
OBJ = ../cutils/utils.o $(NAME).o 
IN = ../inputs/$(NAME)_input.in

%.o: %.c
	$(CC) $(CFLAGS) $< -c -o $@ 
$(NAME).out: $(OBJ)
	$(CC) $^ $(CFLAGS) -o $@ 
run: $(NAME).out
	./$(NAME).out $(IN)


