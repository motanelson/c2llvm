printf "\033c\033[43;30m\n"
clang -c -emit-llvm -o $1.bc $1
