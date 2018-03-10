############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.pairings = []
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType("musk", 1998, "green", True, True, "muskmelon")
    muskmelon.add_pairing("mint")

    casaba = MelonType("cas", 2003, "orange", False, False, "casaba")
    casaba.add_pairing("mint")
    casaba.add_pairing("strawberries")

    crenshaw = MelonType("cren", 1996, "green", False, False, "crenshaw")
    crenshaw.add_pairing("proscuitto")

    yellow_watermelon = MelonType("yw", 2013, "yellow", False, True, "yellow_watermelon")
    yellow_watermelon.add_pairing("ice cream")

    all_melon_types.extend([muskmelon, casaba, crenshaw, yellow_watermelon])

    return all_melon_types

all_melon_types = make_melon_types()


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon_type in melon_types:
        print "{} pairs with ".format(melon_type.name)
        print "{}".format(melon_type.pairings)


print_pairing_info(all_melon_types)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    #create an empty dictionary
    melon_dict = {}
    #iterate through all_melon_types
    for melon_type in melon_types:
        #set all_melon_types[0] = all_melon_types[0].name
        melon_dict[melon_type.code] = melon_type
    #return dictionary

    return melon_dict

    #another method: for melon_count in range(len(melon_types)):

melon_code_dict = make_melon_type_lookup(all_melon_types)

############
# Part 2   #
############


class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, field, harvested_by):
        self.melon_type = melon_code_dict[melon_type]
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvested_by = harvested_by

    def is_sellable(self):
        if (self.shape_rating >= 5 and self.color_rating >= 5 and self.field != 3):
                return True


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melon_1 = Melon('yw', 8, 7, 2, "Sheila")
    melon_2 = Melon('yw', 3, 4, 2, "Sheila")
    melon_3 = Melon("yw", 9, 8, 3, "Sheila")
    melon_4 = Melon("cas", 10, 6, 35, "Sheila")
    melon_5 = Melon("cren", 8, 9, 35, "Michael")
    melon_6 = Melon("cren", 8, 2, 35, "Michael")
    melon_7 = Melon("cren", 2, 3, 4, "Michael")
    melon_8 = Melon("musk", 6, 7, 4, "Michael")
    melon_9 = Melon("yw", 7, 10, 3, "Sheila")
    melon_instance_list = [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9]

    return melon_instance_list


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        print "{} harvested this melon from field {}.".format(melon.harvested_by, melon.field)
        if melon.is_sellable():
            print "This melon will sell!"


get_sellability_report(make_melons(melon_code_dict))