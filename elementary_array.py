def element(array):
    elements = list(array)

    for i in array:
       if element(i) == 5:
         return element

array = [3,3,4,2,3,3,3]
print(element(array))