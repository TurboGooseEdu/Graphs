#include "parse.h"

std::pair<int, int> parse_txt_line(std::string line)
{
    int u, v;
    std::istringstream iss(line);

    iss >> u;
    iss >> v;

    return std::make_pair(u, v);
}

std::pair<int, int> parse_csv_line(std::string line)
{
    int u, v;
    char colon;
    std::istringstream iss(line);

    iss >> u;
    iss >> colon;
    iss >> v;

    return std::make_pair(u, v);
}
