import unittest, list_comparator

class TestListComparator(unittest.TestCase):
    def test4nodata(self):
        lc = list_comparator.ListComparator([1])
        self.assertEqual(str(lc),'Второй список отсутствует')
        lc = list_comparator.ListComparator()
        self.assertEqual(str(lc),'Оба списка отсутствуют')

    def test4empty(self):
        lc = list_comparator.ListComparator([], [1,2,3])
        self.assertEqual(str(lc),"Второй список имеет большее среднее значение")
        lc = list_comparator.ListComparator([1,2,3], [])
        self.assertEqual(str(lc),'Первый список имеет большее среднее значение')
        lc = list_comparator.ListComparator([], [])
        self.assertEqual(str(lc),"Средние значения равны")

    def test4elements(self):        
        lc = list_comparator.ListComparator([None,'9', 2], [1, 2, 3])
        self.assertEqual(str(lc),"Средние значения равны")
        lc = list_comparator.ListComparator([None,'9', 2], [1, 3, True])
        self.assertEqual(str(lc),"Средние значения равны")
        lc = list_comparator.ListComparator([False, 2], [1, 2, 3])
        self.assertEqual(str(lc),"Средние значения равны")
        
    def test4values(self):
        lc = list_comparator.ListComparator([1,9], [1,2,3])
        self.assertEqual(str(lc),'Первый список имеет большее среднее значение')
        lc = list_comparator.ListComparator([1,2,3], [1,7])
        self.assertEqual(str(lc),"Второй список имеет большее среднее значение")
        lc = list_comparator.ListComparator([2,3,4], [1,2,3,4,5])
        self.assertEqual(str(lc),"Средние значения равны")     


if __name__ == '__main__' :
    unittest.main()
