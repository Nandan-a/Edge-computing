#!/bin/bash
a = `gcc hello.c && ./a.out`
b = `gcc hello2.c && ./a.out`
echo $a
echo $b