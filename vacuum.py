# Vacuum is assumed to be in the first room listed below.
ROOMS = [["A", False], ["B", True], ["C", False], ["E", True]]

lastRoom = ROOMS[-1]
travelCost = 1
workCost = 1
totalCost = 0

# Loop through every room in the array of rooms
for index, room in enumerate(ROOMS):
    # Fetch data of the current room
    roomName = room[0]
    isClean = room[1]

    # If room is not clean, then clean the room and add cost
    if not isClean:
        print("Clean room " + roomName + " (Cost : " + str(workCost) + ").")
        totalCost += workCost
        room[1] = True

    # If current room isn't the last room then travel to the next room(regardless of cleanliness) and add cost
    if not room == lastRoom:
        print("Travel from room " + roomName + " to room " + ROOMS[index + 1][0] + " (Cost : " + str(travelCost) + ").")
        totalCost += travelCost

# Print total cost
print("Total cost : " + str(totalCost))
