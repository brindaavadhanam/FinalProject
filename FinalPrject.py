"""
pseudocode

- define a class called 'room'
- define its attributes
create 5 models of each room
- ex: kitchen 1, kitchen2, ..., kitchen 5
- define each model
"""

class room:
  def _init_(self):
    print("Inside __init__ function")
    self.name = 0
    self.type_of_room = 0
    self.color = 0
    self.type_of_floor = 0
    self.num_of_windows = 0
    self.num_of_lights = 0
    self.num_of_fans = 0
    self.num_of_doors = 0

  def setName(self, name):
      self.Name = name

  def setTypeOfRoom(self, temp_var):
      self.TypeOfRoom = temp_var

  def setColor(self, color):
      self.Color = color

  def setTypeOfFloor(self, type_of_floor):
      self.TypeOfFloor = type_of_floor

  def setNumOfWindows(self, num_of_windows):
      self.NumOfWindows = num_of_windows

  def setNumOfLights(self, num_of_lights):
      self.NumOfLights = num_of_lights

  def setNumOfFans(self, num_of_fans):
      self.NumOfFans = num_of_fans

  def setNumOfDoors(self, num_of_doors):
      self.NumOfDoors = num_of_doors


  def getName(self):
     # print("The name of this room is {}".format(self.name))
      return self.Name

  def getTypeOfRoom(self):
     # print("The type of this room is {}".format(self.type_of_room))
      return self.TypeOfRoom

  def getColor(self):
     # print("The color of this room is {}".format(self.color))
      return self.Color

  def getTypeOfFloor(self):
     # print("The type of floor in this room is {}".format(self.type_of_floor))
      return self.TypeOfFloor

  def getNumOfWindows(self):
     # print("The number of windows in this room is {}".format(self.num_of_windows))
      return self.NumOfWindows

  def getNumOfLights(self):
      # print("The number of lights in this room is {}".format(self.num_of_lights))
      return self.NumOfLights

  def getNumOfFans(self):
     # print("The number of fans in this room is {}".format(self.num_of_fans))
      return self.NumOfFans

  def getNumOfDoors(self):
      # print("The number of doors in this room is {}".format(self.num_of_doors))
      return self.NumOfDoors

class Kitchen(room):
  def __init__(self):
      self.num_of_sinks = 0
      self.type_of_island = "none"
      self.type_of_stove = 0
      self.type_of_fridge = 0

  def setNumOfSinks(self, num_of_sinks):
      self.NumOfSinks = num_of_sinks

  def setTypeOfIsland(self, type_of_island):
      self.TypeOfIsland = type_of_island

  def setTypeOfStove(self, type_of_stove):
      self.TypeOfStove = type_of_stove

  def setTypeOfFridge(self, type_of_fridge):
      self.TypeOfFridge = type_of_fridge


  def getNumOfSinks(self):
    # print("The number of sinks in this kitchen is{}".format(self.num_of_sinks))
      return self.NumOfSinks

  def getTypeOfIsland(self):
    # print("The type of island in this kitchen is{}".format(self.type_of_island))
      return self.TypeOfIsland

  def getTypeOfStove(self):
     #print("The type of stove in this kitchen is{}".format(self.type_of_stove))
      return self.TypeOfStove

  def getTypeOfFridge(self):
    # print("The type of fridge in this kitchen is{}".format(self.type_of_fridge))
      return self.TypeOfFridge


class MasterBedroom(room):
    def __init__(self):
        self.num_of_nightstands = 0
        self.type_of_dresser = 0
        self.type_of_closet = 0
        self.type_of_bathroom = 0

    def setNumOfNightstands(self, num_of_nightstands):
        self.NumOfNightstands = num_of_nightstands

    def setTypeOfDresser(self, type_of_dresser):
        self.TypeOfDresser = type_of_dresser

    def setTypeOfCloset(self, type_of_closet):
        self.TypeOfCloset = type_of_closet

    def setTypeOfBathroom(self, type_of_bathroom):
        self.TypeOfBathroom = type_of_bathroom


    def getNumOfNightstands(self):
       #print("The number of nightstands in this master bedroom is{}".format(self.num_of_nightstands))
        return self.NumOfNightstands

    def getTypeOfDresser(self):
       #print("The type of dresser in this master bedroom is{}".format(self.type_of_dresser))
        return self.TypeOfDresser

    def getTypeOfCloset(self):
       #print("The type of closet in this master bedroom is{}".format(self.type_of_closet))
        return self.TypeOfCloset

    def getTypeOfBathroom(self):
       #print("The type of bathroom in this master bedroom is{}".format(self.type_of_bathroom))
        return self.TypeOfBathroom


class LivingRoom(room):
    def __init__(self):
        self.num_of_sofas = 0
        self.num_of_carpets = 0
        self.type_of_TV = 0
        self.type_of_table = 0

    def setNumOfSofas(self, num_of_sofas):
        self.NumOfSofas = num_of_sofas

    def setNumOfCarpets(self, num_of_carpets):
        self.NumOfCarpets = num_of_carpets

    def setTypeOfTV(self, type_of_TV):
        self.TypeOfTV = type_of_TV

    def setTypeOfTable(self, type_of_table):
        self.TypeOfTable = type_of_table


    def getNumOfSofas(self):
       #print("The number of sofas in this living room is{}".format(self.num_of_sofas))
        return self.NumOfSofas

    def getNumOfCarpets(self):
       #print("The number of carpets in this living room is{}".format(self.num_of_carpets))
        return self.NumOfCarpets

    def getTypeOfTV(self):
       #print("The type of TV in this living room is{}".format(self.type_of_TV))
        return self.TypeOfTV

    def getTypeOfTable(self):
       #print("The type of table in this living room is{}".format(self.type_of_table))
        return self.TypeOfTable


class GuestRoom(room):
    def __init__(self):
        self.num_of_lamps = 0
        self.type_of_desk = 0
        self.type_of_computer = 0
        self.type_of_mattress = 0

    def setNumOfLamps(self, num_of_lamps):
        self.NumOfLamps = num_of_lamps

    def setTypeOfDesk(self, type_of_desk):
        self.TypeOfDesk = type_of_desk

    def setTypeOfComputer(self, type_of_computer):
        self.TypeOfComputer = type_of_computer

    def setTypeOfMattress(self, type_of_mattress):
        self.TypeOfMattress = type_of_mattress



    def getNumOfLamps(self):
       #print("The number of lamps in this guest room is{}".format(self.num_of_lamps))
        return self.NumOfLamps

    def getTypeOfDesk(self):
       #print("The type of desk in this guest room is{}".format(self.type_of_desk))
        return self.TypeOfDesk

    def getTypeOfComputer(self):
       #print("The type of computer in this guest room is{}".format(self.type_of_computer))
        return self.TypeOfComputer

    def getTypeOfMattress(self):
       #print("The type of mattress in this guest room is{}".format(self.type_of_mattress))
        return self.TypeOfMattress


class Loft(room):
    def __init__(self):
        self.num_of_sofas = 0
        self.num_of_work_areas = 0
        self.projector_present = "none"

    def setNumOfSofas(self, num_of_sofas):
        self.NumOfSofas = num_of_sofas

    def setNumOfWorkAreas(self, num_of_work_areas):
        self.NumOfWorkAreas = num_of_work_areas

    def setProjectorPresent(self, projector_present):
        self.ProjectorPresent = projector_present



    def getNumOfSofas(self):
       #print("The number of sofas in this loft is{}".format(self.num_of_sofas))
        return self.NumOfSofas

    def getNumOfWorkAreas(self):
       #print("The number of work areas in this loft is{}".format(self.num_of_work_areas))
        return self.NumOfWorkAreas

    def getProjectorPresent(self):
       #print("There is {} projector in this loft.".format(self.projector_present))
        return self.ProjectorPresent


def createandupdate(object1):
    print("entering createandupdate function")
    # we are going to describe the room here.
    #print("exiting createandupdate function")
    nameofobject = object1.getName()
    print("this room is {}.".format(nameofobject))
    typeofroom = object1.getTypeOfRoom()
    colorofroom = object1.getColor()
    typeoffloor = object1.getTypeOfFloor()
    numofwindows = object1.getNumOfWindows()
    numoflights = object1.getNumOfLights()
    numoffans = object1.getNumOfFans()
    numofdoors = object1.getNumOfDoors()

    headerdescrip = "<h1 style=color:tomato;>Here is the description of the room you chose.\n<h1>"
    print(headerdescrip)
    genroomdescrip = "<h3 style=color:violet;>Welcome to {}!\nThis room is a {}.</h3><h3 style=color:orange;>The walls of this room are {}.</h3><h3 style=color:violet;>This room contains {} flooring.</h3><h3 style=color:orange;>It consists of {} windows and {} doors.</h3><h3 style=color:violet;>This room has {} lights. It also has {} fans!</h3>".format(nameofobject, typeofroom, colorofroom, typeoffloor, numofwindows, numofdoors, numoflights, numoffans)
    print(genroomdescrip)


    if nameofobject == "Kitchen 1" or nameofobject == "Kitchen 2" or nameofobject == "Kitchen 3":
        numofsinks = object1.getNumOfSinks()
        typeofisland = object1.getTypeOfIsland()
        typeofstove = object1.getTypeOfStove()
        typeoffridge = object1.getTypeOfFridge()
        specialroomdescrip = "<h3 style=color:orange;>This kitchen has {} sinks.</h3><h3 style=color:violet;>The stove in this kitchen is {}.</h3><h3 style=color:orange;> The fridge is a {}.</h3><h3 style=color:violet;>Lastly, the type of island in this kitchen is a {}.</h3>".format(numofsinks, typeofstove, typeoffridge, typeofisland)
        print(specialroomdescrip)

    elif nameofobject == "MB 1" or nameofobject == "MB 2" or nameofobject == "MB 3":
        numofnightstands = object1.getNumOfNightstands()
        typeofdresser = object1.getTypeOfDresser()
        typeofcloset = object1.getTypeOfCloset()
        typeofbathroom = object1.getTypeOfBathroom()
        specialroomdescrip = "<h3 style=color:orange;>This master bedroom has {} nightstands.</h3><h3 style=color:violet;>The dresser in this master bedroom is {}.</h3><h3 style=color:orange;>The closet is a {}.</h3><h3 style=color:violet;>Lastly, the type of bathroom in this kitchen is a {}.</h3>".format(numofnightstands, typeofdresser, typeofcloset, typeofbathroom)
        print(specialroomdescrip)

    elif nameofobject == "LR 1" or nameofobject == "LR 2" or nameofobject == "LR 3":
        numofsofas = object1.getNumOfSofas()
        numofcarpets = object1.getNumOfCarpets()
        typeofTV = object1.getTypeOfTV()
        typeoftable = object1.getTypeOfTable()
        specialroomdescrip = "<h3 style=color:orange;>This living room has {} sofas.</h3><h3 style=color:violet;>There are {} carpets in this living room.</h3><h3 style=color:orange;>The TV is a {}.</h3><h3 style=color:violet;>Lastly, the type of table in this living room is a {}.</h3>".format(numofsofas, numofcarpets, typeofTV, typeoftable)
        print(specialroomdescrip)

    elif nameofobject == "GR 1" or nameofobject == "GR 2" or nameofobject == "GR 3":
        numoflamps = object1.getNumOfLamps()
        typeofdesk = object1.getTypeOfDesk()
        typeofcomputer = object1.getTypeOfComputer()
        typeofmattress = object1.getTypeOfMattress()
        specialroomdescrip = "<h3 style=color:orange;>This guest room has {} lamps.</h3><h3 style=color:violet;>The desk in this guest room is {}.</h3><h3 style=color:orange;>The computer is a {}.</h3><h3 style=color:violet;>Lastly, the type of mattress in this guest room is a {}.</h3>".format(numoflamps, typeofdesk, typeofcomputer, typeofmattress)
        print(specialroomdescrip)

    elif nameofobject == "Loft 1" or nameofobject == "Loft 2" or nameofobject == "Loft 3":
        numofsofas = object1.getNumOfSofas()
        numofworkareas = object1.getNumOfWorkAreas()
        projectorpresent = object1.getProjectorPresent()
        specialroomdescrip = "<h3 style=color:orange;>This loft has {} sofas.</h3><h3 style=color:violet;>The number of work areas in this loft is {}.</h3><h3 style=color:orange;>This room {} have a projector.</h3>".format(numofsofas, numofworkareas, projectorpresent)
        print(specialroomdescrip)

    footerdescrip = "<h2 style=color:tomato;>Thank you for visiting Brinda's Build-A-House! We hope you come back next time.</h2>"
    print(footerdescrip)

    """
    declare a variable called file_nameg
    get the name of object into file_name
    print file_name
    create a file named with contents of file_name
    dump contents of headeerdescrip, gendescrip, specialdescrip, and footer into file
    close the file
    """

    file_name = nameofobject + ".html"
    print(file_name)
    f = open(file_name, "w+")
    """
    create a temp variable 
    call it temphtml
    assign standard html header info to temp html
    write it into file
    """
    temp_html = "<html>\n <head>\n <title> Hello </title>\n <head>\n </html>"

    f.write(temp_html)
    f.write(headerdescrip)
    f.write(genroomdescrip)
    f.write(specialroomdescrip)
    f.write(footerdescrip)
    f.close()


# main function starts here
print("Welcome to Brinda's Build-A-House!\n We have 3 different models for each room for you to choose!\n In the end, we will join all five rooms you selected to create your dream home.")

# creating first model for kitchen
kitchen1 = Kitchen()
kitchen1.setName("Kitchen 1")
kitchen1.setTypeOfRoom("Kitchen")
kitchen1.setColor("Black and White")
kitchen1.setTypeOfFloor("Tile")
kitchen1.setNumOfWindows("2")
kitchen1.setNumOfLights("8")
kitchen1.setNumOfFans("1")
kitchen1.setNumOfDoors("1")
kitchen1.setNumOfSinks("2")
kitchen1.setTypeOfIsland("Wooden Table")
kitchen1.setTypeOfStove("Stainless Steel")
kitchen1.setTypeOfFridge("Smart Fridge")
# done creating first model

print("``````````````````````````````````````````````````````````````````````````````````````````````")
createandupdate(kitchen1)


# creating second model for kitchen
kitchen2 = Kitchen()
kitchen2.setName("Kitchen 2")
kitchen2.setTypeOfRoom("Kitchen")
kitchen2.setColor("Light blue and white")
kitchen2.setTypeOfFloor("Wood")
kitchen2.setNumOfWindows("3")
kitchen2.setNumOfLights("6")
kitchen2.setNumOfFans("2")
kitchen2.setNumOfDoors("2")
kitchen2.setNumOfSinks("1")
kitchen2.setTypeOfIsland("Fully Functional")
kitchen2.setTypeOfStove("gas cook top")
kitchen2.setTypeOfFridge("Mini Fridge, followed by drinks fridge")
#done creating second model

print("``````````````````````````````````````````````````````````````````````````````````````````````")
createandupdate(kitchen2)

#creating last model for kitchen
kitchen3 = Kitchen()
kitchen3.setName("Kitchen 3")
kitchen3.setTypeOfRoom("Kitchen")
kitchen3.setColor("Light purple and white")
kitchen3.setTypeOfFloor("Tile")
kitchen3.setNumOfWindows("1")
kitchen3.setNumOfLights("4")
kitchen3.setNumOfFans("4")
kitchen3.setNumOfDoors("2")
kitchen3.setNumOfSinks("3")
kitchen3.setTypeOfIsland("Portable Counter-top")
kitchen3.setTypeOfStove("Electric Stove top")
kitchen3.setTypeOfFridge("Bottom Freezer")
#done creating last model

print("``````````````````````````````````````````````````````````````````````````````````````````````")
createandupdate(kitchen3)

# creating first model for master bedroom
mb1 = MasterBedroom()
mb1.setName("MB 1")
mb1.setTypeOfRoom("Master Bedroom")
mb1.setColor("Light brown and white")
mb1.setTypeOfFloor("Wood")
mb1.setNumOfWindows("4")
mb1.setNumOfLights("4")
mb1.setNumOfFans("1")
mb1.setNumOfDoors("2")
mb1.setNumOfNightstands("2")
mb1.setTypeOfDresser("Double Dresser")
mb1.setTypeOfCloset("Walk-in closet")
mb1.setTypeOfBathroom("Full Bath")
# done creating first model

print("``````````````````````````````````````````````````````````````````````````````````````````````")
createandupdate(mb1)

# creating second model for master bedroom
mb2 = MasterBedroom()
mb2.setName("MB 2")
mb2.setTypeOfRoom("Master Bedroom")
mb2.setColor("Off-white")
mb2.setTypeOfFloor("Carpet")
mb2.setNumOfWindows("3 1/2")
mb2.setNumOfLights("2")
mb2.setNumOfFans("2")
mb2.setNumOfDoors("3")
mb2.setNumOfNightstands("2")
mb2.setTypeOfDresser("Vertical Chest")
mb2.setTypeOfCloset("Shelved")
mb2.setTypeOfBathroom("Half Bath")
#done creating second model

print("``````````````````````````````````````````````````````````````````````````````````````````````")
createandupdate(mb2)

#creating last model for master bedroom
mb3 = MasterBedroom()
mb3.setName("MB 3")
mb3.setTypeOfRoom("Master Bedroom")
mb3.setColor("Light orange")
mb3.setTypeOfFloor("Wood")
mb3.setNumOfWindows("4")
mb3.setNumOfLights("6")
mb3.setNumOfFans("2")
mb3.setNumOfDoors("2")
mb3.setNumOfNightstands("0")
mb3.setTypeOfDresser("Horizontal Dresser")
mb3.setTypeOfCloset("Reach-in Closet")
mb3.setTypeOfBathroom("Porcelain Floored")
#done creating last model

print("``````````````````````````````````````````````````````````````````````````````````````````````")
createandupdate(mb3)

# creating first model for living room
livingroom1 = LivingRoom()
livingroom1.setName("LR 1")
livingroom1.setTypeOfRoom("Living Room")
livingroom1.setColor("Light salmon")
livingroom1.setTypeOfFloor("Marble")
livingroom1.setNumOfWindows("2")
livingroom1.setNumOfLights("4")
livingroom1.setNumOfFans("1")
livingroom1.setNumOfDoors("1")
livingroom1.setNumOfSofas("3")
livingroom1.setNumOfCarpets("1")
livingroom1.setTypeOfTV("Plasma")
livingroom1.setTypeOfTable("End Table")
# done creating first model

print("``````````````````````````````````````````````````````````````````````````````````````````````")
createandupdate(livingroom1)

# creating second model for living room
livingroom2 = LivingRoom()
livingroom2.setName("LR 2")
livingroom2.setTypeOfRoom("Living Room")
livingroom2.setColor("Light pink")
livingroom2.setTypeOfFloor("wood")
livingroom2.setNumOfWindows("3")
livingroom2.setNumOfLights("5")
livingroom2.setNumOfFans("2")
livingroom2.setNumOfDoors("1")
livingroom2.setNumOfSofas("4")
livingroom2.setNumOfCarpets("none")
livingroom2.setTypeOfTV("LG")
livingroom2.setTypeOfTable("Coffee Table")
#done creating second model

print("``````````````````````````````````````````````````````````````````````````````````````````````")
createandupdate(livingroom2)

#creating last model for kitchen
livingroom3 = LivingRoom()
livingroom3.setName("LR 3")
livingroom3.setTypeOfRoom("Living Room")
livingroom3.setColor("Light blue")
livingroom3.setTypeOfFloor("Carpet")
livingroom3.setNumOfWindows("3")
livingroom3.setNumOfLights("4")
livingroom3.setNumOfFans("1")
livingroom3.setNumOfDoors("3")
livingroom3.setNumOfSofas("2")
livingroom3.setNumOfCarpets("1")
livingroom3.setTypeOfTV("Sony")
livingroom3.setTypeOfTable("Ottoman Table")
#done creating last model

print("``````````````````````````````````````````````````````````````````````````````````````````````")
createandupdate(livingroom3)

# creating first model for guest room
guestroom1 = GuestRoom()
guestroom1.setName("GR 1")
guestroom1.setTypeOfRoom("Guest Room")
guestroom1.setColor("white")
guestroom1.setTypeOfFloor("carpet")
guestroom1.setNumOfWindows("2")
guestroom1.setNumOfLights("4")
guestroom1.setNumOfFans("1")
guestroom1.setNumOfDoors("2")
guestroom1.setNumOfLamps("1")
guestroom1.setTypeOfDesk("Corner Desk")
guestroom1.setTypeOfComputer("Macbook Air")
guestroom1.setTypeOfMattress("Memory Foam")
# done creating first model
print("``````````````````````````````````````````````````````````````````````````````````````````````")
createandupdate(guestroom1)

# creating second model for guest room
guestroom2 = GuestRoom()
guestroom2.setName("GR 2")
guestroom2.setTypeOfRoom("Guest Room")
guestroom2.setColor("light green")
guestroom2.setTypeOfFloor("tile")
guestroom2.setNumOfWindows("3")
guestroom2.setNumOfLights("5")
guestroom2.setNumOfFans("2")
guestroom2.setNumOfDoors("1")
guestroom2.setNumOfLamps("2")
guestroom2.setTypeOfDesk("Executive Desk")
guestroom2.setTypeOfComputer("Windows")
guestroom2.setTypeOfMattress("Gel-Infused Foam")
# done creating second model

print("``````````````````````````````````````````````````````````````````````````````````````````````")
createandupdate(guestroom2)

# creating last model for guest room
guestroom3 = GuestRoom()
guestroom3.setName("GR 3")
guestroom3.setTypeOfRoom("Guest Room")
guestroom3.setColor("light brown")
guestroom3.setTypeOfFloor("wood")
guestroom3.setNumOfWindows("2")
guestroom3.setNumOfLights("2")
guestroom3.setNumOfFans("1")
guestroom3.setNumOfDoors("2")
guestroom3.setNumOfLamps("1")
guestroom3.setTypeOfDesk("Corner Desk")
guestroom3.setTypeOfComputer("Macbook Air")
guestroom3.setTypeOfMattress("Memory Foam")
# done creating last model

print("``````````````````````````````````````````````````````````````````````````````````````````````")
createandupdate(guestroom3)

# creating first model for loft
loft1 = Loft()
loft1.setName("Loft 1")
loft1.setTypeOfRoom("Loft")
loft1.setColor("white")
loft1.setTypeOfFloor("wood")
loft1.setNumOfWindows("3")
loft1.setNumOfLights("5")
loft1.setNumOfFans("1")
loft1.setNumOfDoors("0")
loft1.setNumOfSofas("2")
loft1.setNumOfWorkAreas("1")
loft1.setProjectorPresent("does")
# done creating first model

print("``````````````````````````````````````````````````````````````````````````````````````````````")
createandupdate(loft1)

# creating second model for loft
loft2 = Loft()
loft2.setName("Loft 2")
loft2.setTypeOfRoom("Loft")
loft2.setColor("blue")
loft2.setTypeOfFloor("wood")
loft2.setNumOfWindows("4")
loft2.setNumOfLights("4")
loft2.setNumOfFans("2")
loft2.setNumOfDoors("2")
loft2.setNumOfSofas("4")
loft2.setNumOfWorkAreas("2")
loft2.setProjectorPresent("doesn't")
# done creating second model
print("``````````````````````````````````````````````````````````````````````````````````````````````")
createandupdate(loft2)

# creating last model for loft
loft3 = Loft()
loft3.setName("Loft 3")
loft3.setTypeOfRoom("Loft")
loft3.setColor("Light pink")
loft3.setTypeOfFloor("Marble")
loft3.setNumOfWindows("2")
loft3.setNumOfLights("6")
loft3.setNumOfFans("1")
loft3.setNumOfDoors("2")
loft3.setNumOfSofas("2 long, 1 loveseat")
loft3.setNumOfWorkAreas("1")
loft3.setProjectorPresent("does")
# done creating last mode
print("``````````````````````````````````````````````````````````````````````````````````````````````")
createandupdate(loft3)