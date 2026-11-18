from smarthouse.domain import SmartHouse

DEMO_HOUSE = SmartHouse()

# Building house structure
ground_floor = DEMO_HOUSE.register_floor(1)

entrance1 = DEMO_HOUSE.register_room(ground_floor, 10.5, "Entrance1")

entrance2 = DEMO_HOUSE.register_room(ground_floor, 10.5, "Entrance2")
entrance3 = DEMO_HOUSE.register_room(ground_floor, 10.5, "Entrance3")
bedroom1 = DEMO_HOUSE.register_room(ground_floor, 10.05, "Bedroom1")


second_floor = DEMO_HOUSE.register_floor(2)


livingroom1 = DEMO_HOUSE.register_room(second_floor, 10.5, "livingroom1")
livingroom2  = DEMO_HOUSE.register_room(second_floor, 10.5, "livingroom2")
livingroom3  = DEMO_HOUSE.register_room(second_floor, 10.5, "livingroom3")
livingroom4  = DEMO_HOUSE.register_room(second_floor, 10.05, "livingroom4")


third_floor = DEMO_HOUSE.register_floor(3)

livingroom5 = DEMO_HOUSE.register_room(third_floor, 10.5, "livingroom1")
livingroom6  = DEMO_HOUSE.register_room(third_floor, 10.5, "livingroom2")
livingroom7  = DEMO_HOUSE.register_room(third_floor, 10.5, "livingroom3")
livingroom8  = DEMO_HOUSE.register_room(third_floor, 10.05, "livingroom4")