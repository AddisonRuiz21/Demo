TITLE = "Big Iron"
# screen dims
WIDTH = 900
HEIGHT = 800
# frames per second
FPS = 60
# colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
REDDISH = (240,55,66)
SKY_BLUE = (143, 185, 252)
VAULT_BLUE = (63, 66, 226)
WASTELAND_SKY = (178, 214, 111)
SCRAP_GRAY = (177, 186, 201)
FONT_NAME = 'comic sans'
SPRITESHEET = "spritesheet_jumper.png"
SPRITESHEET2 = "spritesheet.png"
# data files
HS_FILE = "highscore.txt"
# player settings
PLAYER_ACC = 0.4
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.7
PLAYER_JUMP = 25
# game settings
BOOST_POWER = 60
POW_SPAWN_PCT = 7
MOB_FREQ = 30
# layers - uses numerical value in layered sprites
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0

# platform settings
''' old platforms from drawing rectangles'''
'''
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (65, HEIGHT - 300, WIDTH-400, 40),
                 (20, HEIGHT - 350, WIDTH-300, 40),
                 (200, HEIGHT - 150, WIDTH-350, 40),
                 (200, HEIGHT - 450, WIDTH-350, 40)]
'''
PLATFORM_LIST = [(0, HEIGHT - 40),
                 (105, HEIGHT - 250),
                 (60, HEIGHT - 350),
                 (600, HEIGHT - 150),
                 (500, HEIGHT - 450)]
