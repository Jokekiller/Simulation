class Crop:
    """A generic crop"""

    #constructor
    def __init___(self,growth_rate,light_need,water_need):
        #self attributes with an initalias value

        self._growth_rate = 0
        self._days_growing = 0
        self._growth_rate =  growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

def main():
    #instantiate the class
    new_crop = Crop(1,4,3)
    #test to see whether it works
    print(new_crop._status)
    print(new_crop._light_need)
    print(new_crop._water_need)

if __name__ == "__main__":
    main()
