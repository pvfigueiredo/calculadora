
class Calculadora:
    def calcula(self, expressao: str)->float:
        try:
            return eval(expressao)
        except ZeroDivisionError as e:
            raise e
        except Exception as e:
            raise e("Oops... Algo está errado.")