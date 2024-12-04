class shipping:
    def calculate_shipping_cost(self,weight):
        print(weight*5)
class express_shipping(shipping):
    def calculate_shipping_cost(self,weight):
        print(weight*20)
class stamdard_shipping(shipping):
    def calculate_shipping_cost(self,weight):
        print(weight*10)    
exp_instance=express_shipping()
exp_instance.calculate_shipping_cost(10)
std_instance=stamdard_shipping()
std_instance.calculate_shipping_cost(10)