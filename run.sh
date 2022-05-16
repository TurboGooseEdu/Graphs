#!/usr/bin/bash
g++ $(find . -name '*.cpp' -printf "%P\n" | grep -v -e local -e data) -o main
