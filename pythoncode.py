veg=['potato','brinjal','onion']
quantity=[25,20,19]
price=[30,20,25]
original_price=[25,15,15]
customer_vegtables=[]
customer_veg_quantity=[]
customer_name=[]
customer_number=[]
selling_price=[]
selling_vegtables=[]
profit=0
total_amount=0
sold_vegtables=[]
sold_quantity=[]

while True:
    print('1.SHOPKEEPER')
    print('2.CUSTOMER')
    choose=input('choose a option:')
    if choose=='1':
        while True:
            print('1.Add Item')
            print('2.Remove Item')
            print('3.Update Item')
            print('4.View Inventories')
            print('5.View User Details')
            print('6.Report')
            print('7.Total Revenue')
            print('8.Exit')
            option=input('choose a option:')
            if option=='1':
                while True:
                    
                    item = input('Which item do you want to add: ').strip().lower()
                    if not item.isalpha():
                        print("Invalid item name. Please enter alphabetic characters only.")
                        continue

                    if item not in veg:
                        while True:
                            qnty_input = input('How many kgs do you want to add: ')
                            if qnty_input.replace('.', '', 1).isdigit():
                                qnty = float(qnty_input)
                                break
                            else:
                                print("Invalid input. Please enter a valid number.")
    

                        while True:
                            price1=input('enter a price per KG:')
                            if price1.replace('.','',1).isdigit():
                                price=float(price1)
                                break
                            else:
                                print('invalid input.please enter a valid number:')
                        while True:    
                            original_price1=input('enter a original price price per KG:')
                            if original_price1.replace('.','',1).isdigit():
                                original_price=float(original_price1)
                                break
                            else:
                                print('invalid input.please enter a valid number:')
                        veg.append(item)
                        quantity.append(qnty)
                        price.append(price)
                        original_price.append(original_price1)
                        print(item,'is added')
                    else:
                        print(item,'is already in veg')
                    while True:
                        stop=input('do you want to add another item{yes/no}:')
                        if stop=='no':
                            break
                        else:
                            print('please enter correct option:')
            elif option=='2':
                while True:
                    item = input('Which item do you want to remove: ').strip().lower()
                    if not item.isalpha():
                        print("Invalid item name. Please enter alphabetic characters only.")
                        continue
                    if item in veg:
                        idx=veg.index(item)
                        veg.pop(idx)
                        quantity.pop(idx)
                        price.pop(idx)
                        original_price.pop(idx)
                        print(item,'is removed')
                    else:
                        print(item,'is not veg')
                    stop=input('do you want to remove another item{yes/no}:')
                    if stop=='no':
                        break
                    else:
                        print('please enter correct option:')
            elif option=='3':
                while True:
                    item = input('Which item do you want to update: ').strip().lower()
                    if not item.isalpha():
                        print("Invalid item name. Please enter alphabetic characters only.")
                        continue
                    if item in veg:
                        idx=veg.index(item)
                        item_quantity=input('do you want update quantity yes/no:')
                        if item_quantity=='yes':
                            new_quantity=float(input('how much quantity do you want increase:'))
                            quantity[idx]=quantity[idx]+new_quantity
                            print(item,'quantity is updated')
                        item_price=input('do you want update price yes/no:')
                        if item_price=='yes':
                            new_price=float(input('how much price do you update per kg:'))
                            price[idx]=new_price
                            print(item,'price is updated')
                        original_price2=input('do you update original price yes/no:')
                        if original_price2=='yes':
                            new_original1=float(input('how much oringinal_price do you want update per kg:'))
                            original_price[idx]=new_original1
                            print(item,'original price updated')
                    else:
                        print(item,'is not available in veg:')
                    stop=input('do you want to update another item yes/no:')
                    if stop=='no':
                        break
                    else:
                        print('please enter correct option:')
            elif option=='4':
                print('veg            quantity        price')
                for i,j,k in zip(veg,quantity ,price):
                    print(i,  '-',    j,    'kgs',   '-',  k,  'rupees')
            elif option=='5':
                print('customer_name     customer_number')
                for a,b in zip(customer_name   ,customer_number):
                    print(a,'-',b)
            elif option=='6':
                print('veg         quantity        price         original_price')
                for i,j,k,l in zip(veg,quantity,price,original_price):
                    print(i,  '-',     j,  'kgs',    '-',      k,  'ruppes',       l,'original_rupees')
            elif option=='7':
                print('totalprofit',profit)
                for i,j in zip(sold_vegtables,sold_quantity):
                    idx=veg.index(i)
                    totalprofit=j*(price[idx]-original_price[idx])
                    print(i,'-',totalprofit)
            elif option=='8':
                stop=input('do you want to close the shop yes/no:')
                if stop=='yes':
                    break
                else:
                        print('please enter correct option:')
            else:
                print('please choose the correct option:')
    elif choose=='2':
        while True:
            print('1.add cart')
            print('2.removecart')
            print('3.modifycart')
            print('4.viewcart')
            print('5.billing')
            print('6.exit')
            sel=input('select the option:')
            if sel=='1':
                while True:
                    print('veg  quantity  price')
                    for i,j,k in zip(veg,quantity,price):                                                                 
                        print(i,'-',j,'kgs','-',k,'rupees')
                    item=input('which item do u want add:')
                    if item in veg:
                        if item in customer_vegtables:
                            print(item,"is allready added:")
                            stop=input('do you want to add another item yes/no:')
                            if stop=='no':
                                break
                            else:
                               print('please enter correct option:')
                        else:
                            idx=veg.index(item)
                            qnty=float(input('how much do you want:'))
                            if qnty<=quantity[idx]:
                                customer_vegtables.append(item)
                                customer_veg_quantity.append(qnty)
                            else:
                                print('we dont have that much of quantity')
                        stop=input('do you want add another item yes/no:')
                        if stop=='no':
                            break
                        else:
                            print('please enter correct option:')
                    else:
                        print('item is outofstock')
                        stop=input('do you want add another item:')
                        if stop=='no':
                            break
                        else:
                           print('please enter correct option:')
            elif sel=='2':
                while True:
                    item=input('which item do you want remove:')
                    print
                    if item in customer_vegtables:
                        idx=customer_vegtables.index(item)
                        customer_vegtables.pop(idx)
                        customer_veg_quantity.pop(idx)
                        print('item is removed in your cart')
                    else:
                        print(item,'is not available to remove')
                    stop=input('do you want remove item yes/no:')
                    if stop=='no':
                        break
                    else:
                        print('please enter correct option:')
            elif sel=='3':
                while True:
                    item=input('which item do you want to modify:')
                    if item in customer_vegtables:
                        idx=customer_vegtables.index(item)
                        ch=input('do you want modify your quantity increase/decrease:')
                        qnty=float(input('how much quantity do you want to modify:'))
                        if ch=='increase':
                            customer_veg_quantity[idx]=customer_veg_quantity[idx]+qnty
                        else:
                            customer_veg_quantity[idx]=customer_veg_quantity[idx]-qnty
                    else:
                        print(item,'is not in your cart')
                    stop=input('do you want to modify another item yes/no:')
                    if stop=='no':
                        break
                    else:
                        print('please enter correct option:')
            elif sel=='4':
                print('customer_vegtables      customer_veg_quantity')
                for i,j in zip(customer_vegtables,customer_veg_quantity):
                    print(i,'-',j,'kgs')
            elif sel=='5':
                name=input('enter your name:')
                while True:
                    number=input('enter your number:')
                    if number.isdigit and len(number)==10:
                        break
                    print('please enter a valid number')
                customer_name.append(name)
                customer_number.append(number)
                total_amount=0
                for i,j in zip(customer_vegtables,customer_veg_quantity):
                    idx=veg.index(i)
                    amt=price[idx]*j
                    total_amount=total_amount+amt
                    quantity[idx]=quantity[idx]-j
                    sold_vegtables.append(i)
                    sold_quantity.append(j)
                    profit=profit+(price[idx]-original_price[idx])*j
                    print(i,'-',j,'kgs','-',amt,'rupees')
                print('total amount:',total_amount)
                customer_vegtables.clear()
                customer_veg_quantity.clear()
            elif sel=='6':
                break
            else:
                print('please choose the correct option:')
    else:
        print('please choose the correct option:')
