class Crop:
    '''A generic crop'''

    #constructor
    def __init__(self,growth_rate,light_need,water_need):
        #self attributes with an initalias value

        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

    def needs(self):
        #return a dictionary for needs
        return{'light need':self._light_need, 'water need':self._water_need}

    def report(self):
        #return a dictionary for type, status , growth and days growing
        return {'type':self._type, 'status':self._status, 'growth':self._growth, 'days growing':self._days_growing}

def main():
    #instantiate the class
    new_crop = Crop(1,4,3)
    #test to see whether it works
    print(new_crop.needs()['light need'])
    print(new_crop.report())
    
if __name__ == "__main__":
    main()
