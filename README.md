# Graphs


Структура репозитория **предлагается** такая:


(upd - решили разбивать не по алгоритмам а по задачам, позже переделаю)

```cmd
.
├── algorithms
│   ├── basicAlgorithms.h
│   ├── connectedComponents.cpp
│   ├── connectedComponents.h
│   ├── graph.cpp
│   └── graph.h
├── data
│   ├── CA-AstroPh.txt
│   ├── vk.csv
│   └── web-Google.txt
├── local
│   ├── f
│   └── f.cpp
├── main
├── main.cpp
├── preprocess.cpp
├── preprocess.h
├── run.sh
└── utils
    ├── dfs.cpp
    ├── dfs.h
    ├── parse.cpp
    ├── parse.h
    ├── stack_dfs.cpp
    └── stack_dfs.h
```


Я компилю и запускаю всё через linux, поэтому написал bash-скрипт. Если у вас не линух, можно игнорировать и запускать по-своему.

Я запускаю через

```cmd
./run.sh
./main
```
