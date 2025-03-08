class Establish:
    def __init__(self,id_table,name, address, contact,
                 working_hours, description,rating, feedback ):
        self.id_table=id_table
        self.name = name
        self.address = address
        self.contact = contact
        self.working_hours = working_hours
        self.description = description
        self.rating = rating
        self.feedback = feedback

    def __repr__(self):
        return (f"Establish({self.name}, {self.address},"
                f" {self.contact}, {self.working_hours},"
                f" {self.description}, {self.rating}, {self.feedback})")



class Restaurant(Establish):
    def __init__(self,id_table='', name='', address='', contact='',
                 working_hours='',delivery='', description='', special='',rating='', feedback='' ):
        super().__init__(id_table,name, address, contact,
                 working_hours, description, rating, feedback)
        self.delivery = delivery
        self.special = special


    def is_open(self, day, time):
        pass


    def __repr__(self):
        return (f"Restaurant({self.id_table},{self.name}, {self.address},"
                f" {self.contact}, {self.working_hours},"
                f" {self.description}, {self.delivery}, {self.special}, {self.rating}, {self.feedback})")
