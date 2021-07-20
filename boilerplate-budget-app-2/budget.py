class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=list()

    def __str__(self):
        title=f"{self.name:*^30}\n"
        item=""
        totlal=0
        for items in self.ledger:
            item+=f"{items['description'][0:23]:23}"+f"{items['amount']:>7.2f}"+"\n"
            totlal+=items['amount']
        output=title+item+"Total: "+str(totlal)
        print(output)
        return output

        
    def deposit(self,amount,description=""):
        self.ledger.append({"amount":amount,"description":description})
        return None

    def withdraw(self,amount,description=""):
        if(self.check_funds(amount)):
            self.ledger.append({"amount":-amount,"description":description})
            return True
        return False

    def get_balance(self):
        balance=0
        for amount in self.ledger:
            balance+=amount["amount"]
        return balance
    
    def transfer(self,amount,category):
        if(self.check_funds(amount)):
            self.withdraw(amount,"Transfer to "+ category.name)
            category.deposit(amount,"Transfer from "+ self.name)
            return True
        return False

    def check_funds(self,amount):
        if (self.get_balance() >= amount):
            return True
        return False

    # def get_withdrawls(self):
    #     total=0
    #     for item in self.ledger:
    #         if item['amount']<0:
    #             total+=item['amount']
    #     return total 

# def truncate(n):
#     multiplier=10
#     return int(n * multiplier)/multiplier


# def gettotals(categories):
#     total=0
#     breakdown=[]
#     for category in categories:
#         total+= category.get_withdrawls()
#         breakdown.append(category.get_withdrawls())
#     rounded=list(map(lambda x:truncate(x/total),breakdown))
#     return rounded


# def create_spend_chart(categories):
#     res="Percentage spend by category\n"
#     i=100
#     totals=gettotals(categories)
#     while i>=0:
#         cat_space=" "
#         for total in totals:
#             if total*100>=i:
#                 cat_space+="o "
#             else:
#                 cat_space=" "
#         res+=str(i).rjust(3)+"|"+cat_space+("\n")
#         i-=10

#     dashes="-"+"---"*len(categories)
#     names=[]
#     x_axis=""
#     for category in categories:
#         names.append(category.name)
    
#     maxi=max(names, key=len)

#     for x in range(len(maxi)):
#         nameStr='    '
#         for name in names:
#             if x>=len(name):
#                 nameStr+="  "
#             else:
#                 nameStr+=name[x]+"  "
#         if(x!=len(maxi)-1):
#             nameStr+='\n'

#         x_axis+=nameStr
    
#     res+=dashes.rjust(len(dashes)+4)+"\n"+x_axis
        
#     return res
def create_spend_chart(categories):
  category_names = []
  spent = []
  spent_percentages = []

  for category in categories:
    total = 0
    for item in category.ledger:
      if item['amount'] < 0:
        total -= item['amount']
    spent.append(round(total, 2))
    category_names.append(category.name)

  for amount in spent:
    spent_percentages.append(round(amount / sum(spent), 2)*100)

  graph = "Percentage spent by category\n"

  labels = range(100, -10, -10)

  for label in labels:
    graph += str(label).rjust(3) + "| "
    for percent in spent_percentages:
      if percent >= label:
        graph += "o  "
      else:
        graph += "   "
    graph += "\n"

  graph += "    ----" + ("---" * (len(category_names) - 1))
  graph += "\n     "

  longest_name_length = 0

  for name in category_names:
    if longest_name_length < len(name):
      longest_name_length = len(name)

  for i in range(longest_name_length):
    for name in category_names:
      if len(name) > i:
        graph += name[i] + "  "
      else:
        graph += "   "
    if i < longest_name_length-1:
      graph += "\n     "

    

  return(graph)