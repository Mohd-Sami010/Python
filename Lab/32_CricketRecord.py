players = {}

numOfPlayers = int(input("Enter the number of players: "))
for i in range(numOfPlayers):
    name = input("Enter the name of player: ")
    runs = int(input("Enter the runs scored by the player: "))
    players[name] = runs

playerToRetrieve = input("Enter the name of the player to retrieve runs: ")
print(f"Runs scored by {playerToRetrieve}: {players.get(playerToRetrieve, 'Player not found')}")