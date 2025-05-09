#!/bin/bash

python3 main.py $1
llc -filetype=obj --mtriple=x86_64-linux-gnu out.ll -o out.o
clang -no-pie out.o -o out.exe
./out.exe
