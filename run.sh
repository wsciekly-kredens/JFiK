#!/bin/bash

llc -filetype=obj --mtriple=x86_64-linux-gnu out.ll -o out.o
clang -no-pie out.o -o out.exe
./out.exe
