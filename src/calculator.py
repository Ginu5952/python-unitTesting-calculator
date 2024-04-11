from src.custom_ex import IncorrectInputError

class Calculator:
    def add(self,*args: float) -> float:
        return sum(args)
    
    def multiply(self, *args:float) -> float:
        try:
            result: float = 1
            for i in args:
                result *= i
            return result    
        except TypeError:
            raise IncorrectInputError('wrong input')
        
    def division(self,x:float,y:float) -> float:
        try:
            result:float = x/y
            return result
        except ZeroDivisionError:
            raise ZeroDivisionError("Can't divide by 0")
        
    def substraction(self,x:float,y:float) -> float:
        try:
            result = x - y
            return result
        except TypeError:
            raise IncorrectInputError('wrong input')   

