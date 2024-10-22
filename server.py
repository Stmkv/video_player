from livereload import Server


def rebuild():
    print("Rebuild complite")


rebuild()

server = Server()

server.watch("index.html", rebuild)

server.serve(root=".")
