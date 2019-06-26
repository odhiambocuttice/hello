class Company:

    def __init__(self, location, areaname, distance):
        self.location = location
        self.areaname = areaname
        self.distance = distance
        pass


class Safaricom(Company):

    def __init__(self, location, areaname, distance, fname, position):
        super().__init__(location, areaname, distance)
        self.fname = fname
        self.position = position

    def __repr__(self):
        return '{} {}'.format(self.fname, self.position)
    

    def __add__(self, summ):
        return self.distance + summ.distance

      



details_1 = Safaricom("Muthaiga", "Kiambu", 100, "Davinci", "artist")
details_22 = Safaricom("kileleshwa", "Nairobi", 300, "Collo", "designer" )


print(details_1.fname)
print(details_1.areaname)
print(details_1.__repr__())
print(details_1 + details_22)
