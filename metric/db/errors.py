class AddQueryInvalid(Exception):
    def __init__(self, exception, message="Parameter Add condition is invalid"):
        self.message = message
        self.exception = exception
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.exception}'
