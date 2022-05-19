#include "preprocess.h"

void preprocess(std::string filename, std::string outputFilename)
{
    std::ifstream in(filename);
    std::ofstream out(outputFilename);
    std::string line;

    bool isTxt = filename.find("txt") != std::string::npos;

    std::map<int, int> edges;

    int count_vertices = 0; // ! номер первой вершины будет равен 1, не 0 !

    if (in.is_open() && out.is_open())
    {
        while (getline(in, line))
        {
            if (isdigit(line[0]))
            {
                std::pair<int, int> vertices;
                if (isTxt)
                    vertices = parse_txt_line(line);
                else
                    vertices = parse_csv_line(line);

                int u = vertices.first;
                int v = vertices.second;

                if (edges[u] == 0)
                    edges[u] = ++count_vertices;
                if (edges[v] == 0)
                    edges[v] = ++count_vertices;

                out << edges[u] << " " << edges[v] << std::endl;
            }
        }
        in.close();
        out.close();

        // сохранить edges на всякий, мб в инвертированном виде
        // для легкого доступа к исходным номерам
    }
}