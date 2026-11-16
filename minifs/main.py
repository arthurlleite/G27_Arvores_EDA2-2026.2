from filesystem import FileSystem


def main():
    filesystem = FileSystem()

    while True:
        line = input("mfs > ").strip()
        if not line:
            continue

        parts = line.split()
        command = parts[0]
        arguments = parts[1:]

        if command == "exit":
            break
        elif command == "help":
            print("Comandos disponíveis:")
            print("  help - Exibe os comandos disponíveis")
            print("  exit - Encerra o terminal")
            print("  mkdir NOME - Cria um diretório no diretório atual")
            print("  touch NOME - Cria um arquivo vazio no diretório atual")
            print("  ls - Lista os filhos do diretório atual")
        elif command == "mkdir":
            if len(arguments) != 1:
                print("Uso: mkdir NOME")
                continue
            try:
                filesystem.mkdir(arguments[0])
            except ValueError as error:
                print(error)
        elif command == "touch":
            if len(arguments) != 1:
                print("Uso: touch NOME")
                continue
            try:
                filesystem.touch(arguments[0])
            except ValueError as error:
                print(error)
        elif command == "ls":
            if arguments:
                print("Uso: ls")
                continue
            for name in filesystem.ls():
                print(name)
        else:
            print("Comando desconhecido")


if __name__ == "__main__":
    main()
