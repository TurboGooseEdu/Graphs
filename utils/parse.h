#ifndef UTILS_PARSE_HEADER_16_05_2022
#define UTILS_PARSE_HEADER_16_05_2022

#include <sstream>

std::pair<int, int> parse_txt_line(std::string line);
std::pair<int, int> parse_csv_line(std::string line);
#endif
