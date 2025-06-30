import re

def converter_python_para_c(codigo_py):
    linhas = codigo_py.splitlines()
    saida = []

    # Cabeçalhos padrão do C
    saida.append("#include <stdio.h>")
    saida.append("#include <stdlib.h>")
    saida.append("#include <math.h>")
    saida.append("")
    saida.append("int main(){")
    saida.append("")
    for linha in linhas:
        linha_original = linha
        linha = linha.strip()

        # Ignorar linhas vazias
        if not linha:
            saida.append("")
            continue

        # Substituir print(...) por printf(...)
        linha = re.sub(r'\bprint\s*\((.*?)\)', r'printf(\1)', linha)

        # Substituir open(...) por fopen(...)
        linha = re.sub(r'\bopen\s*\(', 'fopen(', linha)

        # Substituir read(...) por fread(...)
        linha = re.sub(r'\bread\s*\(', 'fread(', linha)

        # Substituir write(...) por fwrite(...)
        linha = re.sub(r'\bwrite\s*\(', 'fwrite(', linha)

        # Substituir close(...) por fclose(...)
        linha = re.sub(r'\bclose\s*\(', 'fclose(', linha)

        # Adicionar ponto e vírgula ao fim se não existir
        if not linha.endswith(";"):
            linha += ";"

        saida.append(linha)
    saida.append("return 0;\n}\n")
    return "\n".join(saida)


def main():
    ficheiro_entrada = input("Nome do ficheiro Python (.py): ").strip()

    if not ficheiro_entrada.endswith(".py"):
        print("Erro: o ficheiro deve ter extensão .py")
        return

    ficheiro_saida = ficheiro_entrada.replace(".py", ".c")

    try:
        with open(ficheiro_entrada, 'r', encoding='utf-8') as f:
            codigo_py = f.read()

        codigo_c = converter_python_para_c(codigo_py)

        with open(ficheiro_saida, 'w', encoding='utf-8') as f:
            f.write(codigo_c)

        print(f"Conversão concluída. Ficheiro gerado: {ficheiro_saida}")

    except FileNotFoundError:
        print("Ficheiro não encontrado.")

print("\033c\033[43;30m\n")
if __name__ == "__main__":
    main()
