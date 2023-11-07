class SQLError(Exception):
    def __init__(self, message:str) -> None:
        super().__init__(f"Ocorreu um erro: {message}")

class RequestError(Exception):
    def __init__(self, message:str) -> None:
        super().__init__(f"Ocorreu um erro: {message}")