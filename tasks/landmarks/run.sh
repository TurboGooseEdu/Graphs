#!/usr/bin/bash
cd tasks/landmarks
g++ $(find . -name '*.cpp' -printf "%P\n" | grep -v -e local -e data) -o landmarks

