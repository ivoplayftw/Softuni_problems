a_team = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
b_team = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
carded_players = input().split()
game_stopped = False

for player in carded_players:
    if player in a_team:
        a_team.remove(player)
    elif player in b_team:
        b_team.remove(player)
    if len(b_team) < 7 or len(a_team) < 7:
        game_stopped = True
        break
print(f"Team A - {len(a_team)}; Team B - {len(b_team)}")
if game_stopped:
    print("Game was terminated")
