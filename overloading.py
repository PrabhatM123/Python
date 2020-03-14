#Method Overloading with Classes(using super)

class Overloading_sum:

    def area(self,a,b):
        print('area of box =',a*b)

class derived_sum(overloading_sum):
    
    def area(self,a,b,c):
        super(derived_sum,self).area(10,20)
        print('volume of box =',a*b*c)        # print the volume of box

derived_sum_obj=derived_sum()
derived_sum_obj.area(10,20,30)
