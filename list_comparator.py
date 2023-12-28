"""Рассчитывает среднее значение 2 списков.
Сравнивает эти средние значения и выводит соответствующее сообщение:
""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
""Средние значения равны"", если средние значения списков равны."""
import numbers

class ListComparator():
    """принимает 2 списка 
       вычисляет среднее значение чисел, содержащихся в них
       возвращает строку, среднее какого списка больше 
    """
    avg1 = None
    avg2 = None


    @staticmethod
    def is_number(x):
        """ takes x: anytype returns bool: if x is numner """
        return not isinstance(x, bool) and isinstance(x,numbers.Number)


    def list_average(self, lst) -> float:
        """takes list returns avrage for numbers in it"""
        avg = i = 0
        for num in lst:
            if self.is_number(num):
                avg += num
                i += 1
        return avg/i if avg!=0 else avg

    def __init__(self, list1=None, list2=None) -> None:
        self.list1 = list1
        self.list2 = list2

        if list1 is not None:
            self.avg1 = self.list_average(list1)
        if list2 is not None:
            self.avg2 =  self.list_average(list2)

    def __str__(self) -> str:
        if (self.avg1 is None) and (self.avg2 is None):
            return 'Оба списка отсутствуют'
        if self.avg2 is None:
            return 'Второй список отсутствует'
        if self.avg2 == self.avg1:
            return "Средние значения равны"
        if self.avg2 > self.avg1:
            return "Второй список имеет большее среднее значение"
        return "Первый список имеет большее среднее значение"
