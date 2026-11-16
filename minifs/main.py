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
        elif command == "mkdir":
            if len(arguments) != 1:
                print("Uso: mkdir NOME")
                continue
            try:
                filesystem.mkdir(arguments[0])
            except ValueError as error:
                print(error)
        else:
            print("Comando desconhecido")


if __name__ == "__main__":
    main()
