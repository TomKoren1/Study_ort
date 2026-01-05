def shoppingkart_sum(prices,shopping_list):
    sum=0
    for item in shopping_list:
        sum+=prices[item[0]]*item[1]
    return sum
def exist_in_store(prices,item_names):
    missing=[]
    for item in item_names:
        if item not in prices.keys():
            missing.append(item)
    return missing



class Client():
    def __init__(self,address,persons,current,prev):
        self.address=address
        self.persons=persons
        self.current=current
        self.prev=prev
    def __str__(self):
        return f"address: {self.address} | persons count: {self.persons} | current: {self.current} | prev: {self.prev}"
    
    def updateCurrent(self,new_current):
        self.prev=self.current
        self.current=new_current

    def payment(self,rate1,rate2):
        amount=self.current-self.prev
        return min(self.persons*7,amount)*rate1 + max(0,amount-self.persons*7)*rate2
    

def proposal(clients_arr,num,rate1,rate2):
    new_list=[]
    sum=0
    for client in clients_arr:
        if client.persons == num:
            new_list.append(client)
            sum+=client.payment(rate1,rate2)

    avg=sum/len(new_list)

    for client in new_list:
        if client.payment(rate1,rate2) > avg:
            print(client)
    