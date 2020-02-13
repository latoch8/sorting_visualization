class bubble_sort(object):
  def __init__(self):
    self.i = 0
    self.j = 0
    self.prev_i=0
    self.swapped = False

  def sort(self, list, sorting):
    lenght = len(list)
    if sorting:
      if self.i < lenght:
        if self.i != self.prev_i:
          self.swapped = False
          self.prev_i = self.i
        if self.j < lenght:
          if list[self.j] > list[self.j+1]:
            list = self.swap(list,self.j,self.j+1)
            self.swapped = True
          self.j += 1
          if self.j == (lenght-1):
            self.j = 0
            self.i += 1
            if not self.swapped:
              sorting = False
              self.j = -1
    return (list, sorting, self.j+1)
            
  def swap(self, list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]
    return list