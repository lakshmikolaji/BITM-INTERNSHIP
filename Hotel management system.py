HOTEL_NAMES = {"Ballai":"Pola paradise", "Manglore":"upasana","Mysore":"Hoysala","Banglore":"Nakshthra"}
AVAILABLE_ROOMS= {'101':'Single Room','102':'Double Room','103':'Single Room with AC','104':'Double Room with AC'}
ROOM_CHARGES={"101":250,"102":800, "103":1500,"104":2000}

class Hotel:
    def Register(self):
        self.data=[]
        name = input("Name: ")
        phone_no = input("Phone No.: ")
        address = input("Address: ")
        print("registered successfully")
        self.data.append(name)
        self.data.append(phone_no)
        self.data.append(address)
    
    def Booking(self):
        hotel_names = HOTEL_NAMES.values()
        for names in hotel_names:
            print(names,end=',')
        print()
        hotel_name = input("Enter the hotel name : ")
        available = AVAILABLE_ROOMS.keys()
        for room_no in available:
            print(room_no,end=',')
        print()
        room_no = input("enter the room no:")
        if(room_no in AVAILABLE_ROOMS.keys()):
            customer_name = input('Please enter your name: ')
            check_in = input('Please enter your check-in date (DD/MM/YYYY): ')
            check_out = input('Please enter your check-out date (DD/MM/YYYY): ')
            booking = {'hotel_name':hotel_name,'room_number': room_no, 'customer_name': customer_name, 'check_in': check_in, 'check_out': check_out}
            print(booking)
            print('Booking is done successful!')
        else:
            print("Invalid room number or room is not available.")
                
    def Room_Infomation(self):
        available = AVAILABLE_ROOMS.keys()
        for room_no in available:
            print(room_no,end=',')
        print()
        price=ROOM_CHARGES.items()
        for room_price in price:
            print(room_price,end=',')
        print()
        room_no = input("enter the room no:")
        if (room_no == 101 and room_no == 102):
            print("Room without AC and Room amenities include: 1 Double Bed, Television, Telephone,an attached washroom with hot/cold water")
        else:
            print("Room with AC and Room amenities include: 1 Double Bed, Television, Telephone,an attached washroom with hot/cold water")
        
        print("Room chareges :",ROOM_CHARGES[room_no])
        
    def update(self):
        room_no=input("enter your room no: ")
        if room_no in AVAILABLE_ROOMS.keys():
            new_room_no = input("enter new room no: ")
            if new_room_no in AVAILABLE_ROOMS.keys():
                AVAILABLE_ROOMS[room_no]= new_room_no
                print("Room details updated")
            else:
                print('Invalid room no')
    def delete(self):
        room_no = input("enter the room_no: ")
        if room_no in AVAILABLE_ROOMS:
            del AVAILABLE_ROOMS[room_no]
            print("Room deleted sucessfully")
        else:
            print("Room not found")
    
    def Payment(self):
        available = AVAILABLE_ROOMS.keys()
        price=ROOM_CHARGES.items()
        room_no = input("enter the room no")
        customer_name = input("name: ")
        phone_no = input("Phone No.: ")
        n= int(input("enter no of days"))
        bill_amount=(ROOM_CHARGES[room_no]*n)
        print("bill amount:",bill_amount)
        print("THANK YOU")
        print("Visit Again ")
def Home():
    while True:
        print("welcome to karnataka")
        print(" 1 Register")
        print(" 2 Booking")
        print(" 3 Room infomation")
        print(" 4 Payment")
        print(" 5 update")
        print(" 6 delete")
        print(" 0 Exit")
        n = int(input("Enter your choice:"))
        if(n == 1):
            obj.Register()
        elif(n == 2):
            obj.Booking()
        elif(n == 3):
            obj.Room_Infomation()
        elif(n == 4):
            obj.Payment ()
        elif(n == 5):
            obj.update()
        elif(n == 6):
            obj.delete()
        else:
            exit()
        
obj=Hotel()
Home()