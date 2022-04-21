class Transportation():
    def travel(self):
        print("Travel from one place to another place.")
class Roadways(Transportation):
    def __init__(self, road_type, highway_name):
        self.road_type=road_type
        self.highway=highway_name
class Car(Roadways):
    def __init__(self,engine_size, fuel_type, capacity):
        super().__init__()
        self.engine=engine_size
        self.fuel=fuel_type
        self.capacity=capacity
class Railways(Transportation):
    pass

class Airways(Transportation):
    pass

class aeroplane(Airways):
    ticket_book_number=0
    def __init__(self, company,engine,capacity):
        self.company_name=company
        self.number_of_engine=engine
        self.passanger_capacity=capacity
    def seat_capacity(self):
        return self.passanger_capacity
    def available_seat(self):
        return self.passanger_capacity-self.ticket_book()
    def ticket_book(self):
        ticket_book_number+=1
        return ticket_book_number
    def fea(self):
        super().travel()
aero=aeroplane('boeing',4,250)
print(aero.seat_capacity())
