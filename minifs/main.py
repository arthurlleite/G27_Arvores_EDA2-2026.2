def main():
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
        else:
            print("Comando desconhecido")


if __name__ == "__main__":
    main()
