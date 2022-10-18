def room_checker(num_of_rooms):
    free_chairs = 0
    needed_chairs = 0
    for room in range(1, num_of_rooms + 1):
        chairs, people = input().split()
        diff = len(chairs) - int(people)
        if diff >= 0:
            free_chairs += diff
        else:
            needed_chairs += abs(diff)
            print(f"{abs(diff)} more chairs needed in room {room}")
    return free_chairs, needed_chairs


rooms = int(input())
available_chairs, not_enougt_chairs = room_checker(rooms)
if available_chairs >= not_enougt_chairs:
    print(f"Game On, {available_chairs} free chairs left")
