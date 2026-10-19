#shooping bill
def shopping_bill():
     name=input("enter your name:")
     price=float(input("enter the product amount:"))
     quantity=int(input("enter the quantity:"))
     total=price*quantity
     if total>=2000:
          discount=total*0.1         
     else:
         discount=0
         

     final=total-discount
     print("shopping enjoy")
     print("name",name)
     print("price",price)
     print("quantity",quantity)
     print("total",total)
     print("final amount",final)
shopping_bill()

