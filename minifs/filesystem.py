from node import Node


class FileSystem:
    def __init__(self):
        self.root = Node("/")
        self.current_directory = self.root

    def mkdir(self, name):
        if (
            not name
            or name in (".", "..")
            or "/" in name
            or any(character.isspace() for character in name)
        ):
            raise ValueError("Nome inválido: use um nome simples, sem espaços ou barras.")

        for child in self.current_directory.children:
            if child.name == name:
                raise ValueError(f"Já existe um arquivo ou diretório com o nome '{name}'.")

        directory = Node(name, parent=self.current_directory)
        self.current_directory.children.append(directory)
