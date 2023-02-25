# Online Multiplayer Game Server
import socket, threading, json, time

#------------------------------------------------------------------------------------------
# define socket constants to be used & ALTERED
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 54321

# define pygame constants to be used & ALTERED
ROOM_SIZE = 400
PLAYER_SIZE = 20
ROUND_TIME = 45
FPS = 15
TOTAL_PLAYERS = 4

# room must be divisible by player size for correct gameplay, adjust as needed
while ROOM_SIZE % PLAYER_SIZE != 0:
    PLAYER_SIZE += 1

# max num of players allowed is 4!
if TOTAL_PLAYERS > 4:
    TOTAL_PLAYERS = 4
#------------------------------------------------------------------------------------------
# define classes
class Connection():
    '''A socket connection class to be used as a server'''
    def __init__(self):
        "Initialization of the Connection class"
        # self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.server_socket.bind((HOST_IP, HOST_PORT))
        # self.server_socket.listen()
        pass


class Player():
    '''A class to store a connected client's player info'''
    def __init__(self, number):
    '''Initialization of the Player class'''
    pass

    def set_player_info(self, player_info):
        '''Set the player info to the given info from the client (coordinates & status flags)'''
        pass

    def reset_player(self):
        '''Reset player values for a new round on the server side'''
        pass


class Game():
    '''A class to handle all operations of gameplay'''
    def __init__(self, connection):
        '''Initialization of the Game class'''
        # client socket, client address = connection.accept()
        pass

    def connect_players(self):
        '''Connect ANY incoming player to the game'''
        pass

    def broadcast(self):
        '''Broadcast info to ALL players'''
        pass

    def ready_game(self, player, player_socket):
        '''Ready the game to be played for a SPECIFIC player'''
        pass

    def reset_game(self, player):
        '''Restart the game & wipe info for a SPECIFIC player'''
        pass

    def send_player_info(self, player, player_socket):
        '''Send specific info about THIS player to the given client'''
        pass

    def receive_pregame_player_info(self, player, player_socket):
        '''Receive specific info about THIS player pregame'''
        pass

    def receive_game_player_info(self, player, player_socket):
        '''Receive specific info about THIS player during the game'''
        pass

    def process_game_state(self, player, player_socket):
        '''Process the given player info & update the game's state'''
        pass

    def send_game_state(self, player_socket):
        '''Send the current game state of ALL players to THIS given player'''
        pass


# start the server
my_connection = Connection()
my_game = Game(my_connection) # passing in our 'Connection()' class obj 'my_connection' as the 'connection' attribute for our 'Game()' class obj 'my_game'

# listen for incoming connections
print("Server is listening for incoming connections...\n")
my_game.connect_players()