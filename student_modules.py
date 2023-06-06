from subject_module import mark
class Student:

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.mark = [mark]
        self.mark_sum =0

    def add_mark(self, mark):
        self.mark.append(mark)
        self.mark_sum += mark



    def get_all_marks(self):
          for mark in self.mark:
              print(f'Get All Mark={mark}')
          return



    @property
    def Calc_avarege(self):
          if not self.mark:
              print("no mark")
              return
           mark_sum = sum(self.mark)
           mark_avg = mark_sum / len(self.mark)
            return mark_avg
