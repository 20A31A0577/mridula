from abc import ABC, abstractmethod
class square(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def calculate_circle(self):
        pass
class area(square):
    def calculate_area(self):
        print("a")
    def calculate_circle(self):
        pass
class rectangle(square):
    def calculate_area(self):
        print("b")
    def calculate_circle(self):
        pass
obj=area()
obj.calculate_area()
