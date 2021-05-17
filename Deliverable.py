class Deliverable():
    # Properties
    __borrowed = False

    # Getters / Setters
    @property
    def is_delivered(self):
        return self.__borrowed

    # Methods
    def deliver(self):
        self.__borrowed = True

    def give_back(self):
        self.__borrowed = False

    def comparable_property(self):
        return False

    def compare_to(self, item):
        if type(self) == type(item):
            return self.comparable_property() > item.comparable_property()
        else:
            print('These items have different type and it\'s not possible to compare')
