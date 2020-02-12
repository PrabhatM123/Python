#overriding
class employee:
    def add(self,salary,incentive):
        print('total salary in base class=',salary+incentive)

class department(employee):
    temp = 'i am employee of department class'
    def add(self,salary,incentive):
        print(self.temp)
        print('total salary in department classs=',salary+incentive)
        super(department,self).add(salary,incentive)

dept = department()
dept.add(45000,5000)
