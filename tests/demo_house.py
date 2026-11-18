from smarthouse.domain import SmartHouse

DEMO_HOUSE = SmartHouse()

# Building house structure
ground_floor = DEMO_HOUSE.register_floor(1)

entrance = DEMO_HOUSE.register_room(ground_floor, 13, "Entrance")
livingRoomKitchen = DEMO_HOUSE.register_room(ground_floor, 39.75, "LivingRoomKitchen")
bathroom1 = DEMO_HOUSE.register_room(ground_floor, 6.3, "Bathroom1")
guestRoom1 = DEMO_HOUSE.register_room(ground_floor, 8, "GuestRoom1")
Garage = DEMO_HOUSE.register_room(ground_floor, 29, "Garage")


second_floor = DEMO_HOUSE.register_floor(2)

office = DEMO_HOUSE.register_room(second_floor, 11.75, "Office")
bathroom2 = DEMO_HOUSE.register_room(second_floor, 9.25, "Bathroom2")
hallway = DEMO_HOUSE.register_room(second_floor, 10, "Hallway")
GuestRoom2 = DEMO_HOUSE.register_room(second_floor, 8, "GuestRoom2")
GuestRoom3 = DEMO_HOUSE.register_room(second_floor, 10, "GuestRoom3")
DressingRoom = DEMO_HOUSE.register_room(second_floor, 4, "DressingRoom")
MasterBedroom = DEMO_HOUSE.register_room(second_floor, 17, "MasterBedroom")
