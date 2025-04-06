# Pierwsza kompilacja
Uruchamiam program na Windowsie 

```shell
python main.py test.lang > out.ll
```

Potem przechodzę na WSL i używam wykonuje następujące kroki
```shell
llc -filetype=obj --mtriple=x86_64-linux-gnu out.ll -o out.o
clang -no-pie out.o -o out.exe
./out.exe
```