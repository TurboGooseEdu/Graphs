#ifndef PREPROCESS_16_05_2022
#define PREPROCESS_16_05_2022

#include "utils/parse.h"
#include <fstream>
#include <string>

/**
 * @brief Просматривает строчки начинающиеся с цифры.
 * Отображает номера вершин в множество [1, V], где V - кол-во вершин.
 * Преобразование сохраняет структуру графа.
 *
 * Например граф [(100, 18), (18, 2000), (34, 100), (1700, 1700)] преобразуется в [(1, 2), (2, 3), (4, 1), (5, 5)].
 *
 * Cохраняет преобразованный файл в файл с новым названием.
 *
 * @param filename имя исходного "грязного" файла
 * @param outputFilename имя нового "чистого" файла
 *
 * @author egorgorban
 */
void preprocess(std::string filename, std::string outputFilename);

#endif
