import pygame
import time
#Imports the keys
from pygame.locals import(
  KEYUP,
  KEYDOWN,
  K_RIGHT,
  K_LEFT,
  K_UP,
  K_o,
  K_p,
  K_i,
  K_w,
  K_a,
  K_d,
  K_c,
  K_z,
  K_x
)


#Checks to see if you are inputting the keys 
IgnoreInputs = True

#Checks if a projectile is to be activated
P1Projectile = False
P2Projectile = False

#Checks if Player1 hits player2
Player1Hits = False

#Checks if Player2 hits Player1
Player2Hits = False
#Checks the screen
#Title is Title Screen.
#P1Sel is Player 1 select screen
#P2Sel is Player 2 select screen
#Stages is the stage select screen
#Game is the actual game (Ky)
Page = "Title"


#Checks what character each player selects
Character1 = "Mario"
Character2 = "Mario"

#Checks the background
#MarioLand, 
Background = "None"

#Maintains gravity
Gravity = 0.1

#Clock
Clock = pygame.time.Clock()

pygame.init()


#Fonts
  #Title
TitleFont = pygame.font.SysFont("Comic Sans MS",40)
TitleFontShadow  = pygame.font.SysFont("Comic Sans MS",40)
  #CHOOSE YOUR FIGHTERS
ChooseYourFighterFont = pygame.font.SysFont("Comic Sans MS",30)
#Choose Your stage
ChooseStage = pygame.font.SysFont("Comic Sans MS",30)
#WINNERS
Winner = pygame.font.SysFont("Comic Sans MS",40)
#Other Fonts
PHPF = pygame.font.SysFont("Comic Sans MS",20)

#Texts
  #Title
Title = TitleFont.render("Super Smash Bros by Kyan Hsu",False,(0,0,0))
TitleShadow = TitleFontShadow.render("Super Smash Bros by Kyan Hsu",False,(255,255,255))
  #CHOOSE YOUR FIGHTERS
ChooseYourFighterP1 = ChooseYourFighterFont.render("Choose your fighter P1",False,(0,0,0))
ChooseYourFighterP1Shadow = ChooseYourFighterFont.render("Choose your fighter P1",False,(255,255,255))
  #ChooseYourStage
YourStage = ChooseStage.render("Choose your stage",False,(0,0,0))
#WINNERS
Player1Wins = Winner.render("Player 1 wins!", False,(0,255,0))
Player2Wins = Winner.render("Player 2 wins!", False,(0,0,255))
#Other Texts
P1HP = PHPF.render("Player 1", False,(255,255,255))
P2HP = PHPF.render("Player 2", False,(255,255,255))

  

ChooseYourFighterP2 = ChooseYourFighterFont.render("Choose your fighter P2",False,(0,0,0))
ChooseYourFighterP2Shadow = ChooseYourFighterFont.render("Choose your fighter P2",False,(255,255,255))

#Screen
screen = pygame.display.set_mode([1000,600])

#The class that manages all objects in the game
class GameObject:

  def __init__(self,x,y,width,height,image):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.image = image
    self.vx = 0
    self.vy = 0
    self.hitwidth = self.width
    self.hitheight = self.height
    
    self.img = pygame.image.load(image)
    self.img = pygame.transform.scale(self.img,(self.hitwidth,self.hitheight))

    self.img_flip = pygame.transform.flip(self.img, True, False)
    self.FacingRight = True
    
    self.hitbox = pygame.Rect(x,y,width,height)
    self.collision = [False] * 9    
    self.InAir = False

  # set center
  def set_center(self, screen):
    self.rect.center = screen.get_rect().center

  # recreates this GameObject's hitbox so that it aligns with the GameObject's position
  def UpdateHitbox(self):
    self.hitbox = pygame.Rect(self.x,self.y,self.width,self.height)


  # handle collisions
  def check_collision(self, rect):
    self.collision[0] = rect.collidepoint(self.hitbox.topleft)
    self.collision[1] = rect.collidepoint(self.hitbox.topright)
    self.collision[2] = rect.collidepoint(self.hitbox.bottomleft)
    self.collision[3] = rect.collidepoint(self.hitbox.bottomright)
    self.collision[4] = rect.collidepoint(self.hitbox.midleft)
    self.collision[5] = rect.collidepoint(self.hitbox.midright)
    self.collision[6] = rect.collidepoint(self.hitbox.midtop)
    self.collision[7] = rect.collidepoint(self.hitbox.midbottom)
    self.collision[8] = rect.collidepoint(self.hitbox.center)

  #If something is clicked
  def Clicked(self):
    mouse = pygame.mouse.get_pos()
    if mouse[0] >= self.x and mouse[0] <= self.x + self.width and mouse[1] >= self.y and mouse[1] <= self.y + self.height:
      return True


#Gravity mechanics
def CollisionGround(Object,Ground):
  Object.check_collision(Ground.hitbox)
  if Object.collision[7]:
    Object.vy = 0
    Object.InAir = False
    Object.y = Ground.y - (Object.height)

  if Object.collision[4] or Object.collision[0]:
    Object.x += 1.5
  if Object.collision[5] or Object.collision[1]:
    Object.x -=1.5

def get_time():
  return time.time() * 1000

#First attack
def Attack1(Player,Character):
  
  if Character == "Mario":
        Player.img = pygame.image.load("Assets/Characters/Mario/MarioPunch.png")
        Player.img = pygame.transform.scale(Player.img,(48,90))
        Player.width = 48
        Player.height = 90

  if Character == "DK":
        Player.img = pygame.image.load("Assets/Characters/DK/DKPunch.png")
        Player.img = pygame.transform.scale(Player.img,(81,103))
        Player.width = 81
        Player.height = 103

  if Character == "Link":
        Player.img = pygame.image.load("Assets/Characters/Link/LinkSword.png")
        Player.img = pygame.transform.scale(Player.img,(54,96))
        Player.width = 54
        Player.height = 96

  if Character == "Samus":
        Player.img = pygame.image.load("Assets/Characters/Samus/SamusFire.png")
        Player.img = pygame.transform.scale(Player.img,(57,96))
        Player.width = 57
        Player.height = 96

  if Character == "Yoshi":
        Player.img = pygame.image.load("Assets/Characters/Yoshi/YoshiTounge.png")
        Player.img = pygame.transform.scale(Player.img,(60,90))
        Player.width = 60
        Player.height = 90

  if Character == "Kirby":
        Player.img = pygame.image.load("Assets/Characters/Kirby/KirbyHammer.png")
        Player.img = pygame.transform.scale(Player.img,(60,70))
        Player.width = 60
        Player.height = 70

  if Character == "Fox":
        Player.img = pygame.image.load("Assets/Characters/Fox/FoxKick.png")
        Player.img = pygame.transform.scale(Player.img,(46,87))
        Player.width = 46
        Player.height = 87

  if Character == "Pikachu":
        Player.img = pygame.image.load("Assets/Characters/Pikachu/PikachuCharge.png")
        Player.img = pygame.transform.scale(Player.img,(65,73))
        Player.width = 65
        Player.height = 73

  if Character == "Luigi":
      Player.img = pygame.image.load("Assets/Characters/Luigi/LuigiPunch.png")
      Player.img = pygame.transform.scale(Player.img,(42,93))
      Player.width = 42
      Player.height = 93

  if Character == "CaptainFalcon":
      Player.img = pygame.image.load("Assets/Characters/CaptainFalcon/CaptainFalconPunch.png")
      Player.img = pygame.transform.scale(Player.img,(65,98))
      Player.width = 65
      Player.height = 98

  if Character == "Peach":
      Player.img = pygame.image.load("Assets/Characters/Peach/PeachHeart.png")
      Player.img = pygame.transform.scale(Player.img,(55,97))
      Player.width = 55
      Player.height = 97

  if Character == "Bowser":
      Player.img = pygame.image.load("Assets/Characters/Bowser/BowserClaw.png")
      Player.img = pygame.transform.scale(Player.img,(140,140))
      Player.width = 140
      Player.height = 140

  if Character == "Ganon":
      Player.img = pygame.image.load("Assets/Characters/Ganon/GanonPower.png")
      Player.img = pygame.transform.scale(Player.img,(107,120))
      Player.width = 107
      Player.height = 120

  if Character == "Mewtwo":
      Player.img = pygame.image.load("Assets/Characters/Mewtwo/Mewtwopunch.png")
      Player.img = pygame.transform.scale(Player.img,(84,105))
      Player.width = 84
      Player.height = 105

  if Character == "MetaKnight":
      Player.img = pygame.image.load("Assets/Characters/MetaKnight/MetaKnightSword.png")
      Player.img = pygame.transform.scale(Player.img,(70,75))
      Player.width = 70
      Player.height = 75

  if Character == "Wario":
      Player.img = pygame.image.load("Assets/Characters/Wario/WarioPunch.png")
      Player.img = pygame.transform.scale(Player.img,(48,90))
      Player.width = 48
      Player.height = 90

  if Character == "Charizard":
      Player.img = pygame.image.load("Assets/Characters/Charizard/CharizardClaw.png")
      Player.img = pygame.transform.scale(Player.img,(108,108))
      Player.width = 108
      Player.height = 108

  if Character == "DiddyKong":
      Player.img = pygame.image.load("Assets/Characters/DiddyKong/DiddyKongKick.png")
      Player.img = pygame.transform.scale(Player.img,(72,80))
      Player.width = 72
      Player.height = 80

  if Character == "Sonic":
      Player.img = pygame.image.load("Assets/Characters/Sonic/SonicPunch.png")
      Player.img = pygame.transform.scale(Player.img,(60,88))
      Player.width = 60
      Player.height = 88

  if Character == "KingDedede":
      Player.img = pygame.image.load("Assets/Characters/KingDedede/KingDededeMouth.png")
      Player.img = pygame.transform.scale(Player.img,(108,108))
      Player.width = 108
      Player.height = 108

  if Character == "MegaMan":
      Player.img = pygame.image.load("Assets/Characters/MegaMan/MegaManPunch.png")
      Player.img = pygame.transform.scale(Player.img,(96,90))
      Player.width = 96
      Player.height = 90

  if Character == "Greninja":
      Player.img = pygame.image.load("Assets/Characters/Greninja/GreninjaKick.png")
      Player.img = pygame.transform.scale(Player.img,(70,70))
      Player.width = 70
      Player.height = 70

  if Character == "PacMan":
      Player.img = pygame.image.load("Assets/Characters/PacMan/PacManPunch.png")
      Player.img = pygame.transform.scale(Player.img,(60,81))
      Player.width = 60
      Player.height = 81

  if Character == "Inkling":
      Player.img = pygame.image.load("Assets/Characters/Inkling/InklingSquirt.png")
      Player.img = pygame.transform.scale(Player.img,(80,80))
      Player.width = 80
      Player.height = 80

  if Character == "Ridley":
      Player.img = pygame.image.load("Assets/Characters/Ridley/RidleyTail.png")
      Player.img = pygame.transform.scale(Player.img,(169,120))
      Player.width = 169
      Player.height = 120

  if Character == "KingKRool":
      Player.img = pygame.image.load("Assets/Characters/KingKRool/KingKRoolArmor.png")
      Player.img = pygame.transform.scale(Player.img,(105,120))
      Player.width = 105
      Player.height = 120

  if Character == "Banjo":
      Player.img = pygame.image.load("Assets/Characters/Banjo/BanjoJump.png")
      Player.img = pygame.transform.scale(Player.img,(96,96))
      Player.width = 96
      Player.height = 96
      if Player.InAir == False:
          Player.y -= 1
          Player.UpdateHitbox()
          Player.vy = -4

  if Character == "Steve":
      Player.img = pygame.image.load("Assets/Characters/Steve/SteveBlock.png")
      Player.img = pygame.transform.scale(Player.img,(63,85))
      Player.width = 63
      Player.height = 85

  if Character == "Kazuya":
      Player.img = pygame.image.load("Assets/Characters/Kazuya/KazuyaKick.png")
      Player.img = pygame.transform.scale(Player.img,(80,100))
      Player.width = 80
      Player.height = 100

  if Character == "Waluigi":
      Player.img = pygame.image.load("Assets/Characters/Waluigi/WaluigiKick.png")
      Player.img = pygame.transform.scale(Player.img,(42,108))
      Player.width = 42
      Player.height = 108


  if Character == "Tails":
      Player.img = pygame.image.load("Assets/Characters/Tails/TailsClap.png")
      Player.img = pygame.transform.scale(Player.img,(75,82))
      Player.width = 75
      Player.height = 82

  
  if Character == "Knuckles":
      Player.img = pygame.image.load("Assets/Characters/Knuckles/KnucklesPunch.png")
      Player.img = pygame.transform.scale(Player.img,(94,94))
      Player.width = 94
      Player.height = 94

  if Character == "Eggman":
      Player.img = pygame.image.load("Assets/Characters/Eggman/EggmanDrill.png")
      Player.img = pygame.transform.scale(Player.img,(99,117))
      Player.width = 99
      Player.height = 117

  if Character == "Roblox":
      Player.img = pygame.image.load("Assets/Characters/Roblox/RobloxSword.png")
      Player.img = pygame.transform.scale(Player.img,(70,90))
      Player.width = 70
      Player.height = 90

  if Character == "Sans":
      Player.img = pygame.image.load("Assets/Characters/Sans/SansAttack.png")
      Player.img = pygame.transform.scale(Player.img,(85,85))
      Player.width = 85
      Player.height = 85

  if Character == "Decidueye":
      Player.img = pygame.image.load("Assets/Characters/Decidueye/DecidueyeWing.png")
      Player.img = pygame.transform.scale(Player.img,(90,96))
      Player.width = 90
      Player.height = 96

      

#Second attack
def Attack2(Player,Character):
  
  if Character == "Mario":
        Player.img = pygame.image.load("Assets/Characters/Mario/MarioKick.png")
        Player.img = pygame.transform.scale(Player.img,(48,90))
        Player.width = 48
        Player.height = 90

  if Character == "DK":
        Player.img = pygame.image.load("Assets/Characters/DK/DKSmash.png")
        Player.img = pygame.transform.scale(Player.img,(81,103))
        Player.width = 81
        Player.height = 103

  if Character == "Link":
        Player.img = pygame.image.load("Assets/Characters/Link/LinkSword.png")
        Player.img = pygame.transform.scale(Player.img,(54,96))
        Player.width = 54
        Player.height = 96

  if Character == "Samus":
        Player.img = pygame.image.load("Assets/Characters/Samus/SamusBullet.png")
        Player.img = pygame.transform.scale(Player.img,(57,96))
        Player.width = 57
        Player.height = 96

  if Character == "Yoshi":
        Player.img = pygame.image.load("Assets/Characters/Yoshi/YoshiPunch.png")
        Player.img = pygame.transform.scale(Player.img,(60,90))
        Player.width = 60
        Player.height = 90

  if Character == "Kirby":
        Player.img = pygame.image.load("Assets/Characters/Kirby/KirbyMouth.png")
        Player.img = pygame.transform.scale(Player.img,(60,70))
        Player.width = 60
        Player.height = 70


  if Character == "Fox":
        Player.img = pygame.image.load("Assets/Characters/Fox/FoxDash.png")
        Player.img = pygame.transform.scale(Player.img,(46,87))
        Player.width = 46
        Player.height = 87

  if Character == "Pikachu":
        Player.img = pygame.image.load("Assets/Characters/Pikachu/PikachuElectric.png")
        Player.img = pygame.transform.scale(Player.img,(65,73))
        Player.width = 65
        Player.height = 73

  if Character == "Luigi":
      Player.img = pygame.image.load("Assets/Characters/Luigi/LuigiKick.png")
      Player.img = pygame.transform.scale(Player.img,(42,93))
      Player.width = 42
      Player.height = 93

  if Character == "CaptainFalcon":
      Player.img = pygame.image.load("Assets/Characters/CaptainFalcon/FalconGrab.png")
      Player.img = pygame.transform.scale(Player.img,(65,98))
      Player.width = 65
      Player.height = 98

  if Character == "Peach":
      Player.img = pygame.image.load("Assets/Characters/Peach/PeachPunch.png")
      Player.img = pygame.transform.scale(Player.img,(55,97))
      Player.width = 55
      Player.height = 97

  if Character == "Bowser":
      Player.img = pygame.image.load("Assets/Characters/Bowser/BowserFire.png")
      Player.img = pygame.transform.scale(Player.img,(140,140))
      Player.width = 140
      Player.height = 140

  if Character == "Ganon":
      Player.img = pygame.image.load("Assets/Characters/Ganon/GanonPunch.png")
      Player.img = pygame.transform.scale(Player.img,(107,120))
      Player.width = 107
      Player.height = 120

  if Character == "Mewtwo":
      Player.img = pygame.image.load("Assets/Characters/Mewtwo/MewtwoThrow.png")
      Player.img = pygame.transform.scale(Player.img,(84,105))
      Player.width = 84
      Player.height = 105

  if Character == "MetaKnight":
      Player.img = pygame.image.load("Assets/Characters/MetaKnight/MetaKnightTornado.png")
      Player.img = pygame.transform.scale(Player.img,(70,75))
      Player.width = 70
      Player.height = 75

  if Character == "Wario":
      Player.img = pygame.image.load("Assets/Characters/Wario/WarioFart.png")
      Player.img = pygame.transform.scale(Player.img,(48,90))
      Player.width = 48
      Player.height = 90

  if Character == "Charizard":
      Player.img = pygame.image.load("Assets/Characters/Charizard/CharizardFire.png")
      Player.img = pygame.transform.scale(Player.img,(108,108))
      Player.width = 108
      Player.height = 108

  if Character == "DiddyKong":
      Player.img = pygame.image.load("Assets/Characters/DiddyKong/DiddyKongSlap.png")
      Player.img = pygame.transform.scale(Player.img,(72,80))
      Player.width = 72
      Player.height = 80

  if Character == "Sonic":
      Player.img = pygame.image.load("Assets/Characters/Sonic/SonicOrb.png")
      Player.img = pygame.transform.scale(Player.img,(60,88))
      Player.width = 60
      Player.height = 88
      if Player.InAir == False:
          Player.y -= 1
          Player.UpdateHitbox()
          Player.vy = -4

  if Character == "KingDedede":
      Player.img = pygame.image.load("Assets/Characters/KingDedede/KingDededeHammer.png")
      Player.img = pygame.transform.scale(Player.img,(108,108))
      Player.width = 108
      Player.height = 108

  if Character == "MegaMan":
      Player.img = pygame.image.load("Assets/Characters/MegaMan/MegaManProjectile.png")
      Player.img = pygame.transform.scale(Player.img,(96,90))
      Player.width = 96
      Player.height = 90

  if Character == "Greninja":
      Player.img = pygame.image.load("Assets/Characters/Greninja/GreninjaWater.png")
      Player.img = pygame.transform.scale(Player.img,(70,70))
      Player.width = 70
      Player.height = 70

  if Character == "PacMan":
      Player.img = pygame.image.load("Assets/Characters/PacMan/PacManEat.png")
      Player.img = pygame.transform.scale(Player.img,(60,81))
      Player.width = 60
      Player.height = 81

  if Character == "Inkling":
      Player.img = pygame.image.load("Assets/Characters/Inkling/InklingInk.png")
      Player.img = pygame.transform.scale(Player.img,(80,80))
      Player.width = 80
      Player.height = 80

  if Character == "Ridley":
      Player.img = pygame.image.load("Assets/Characters/Ridley/RidleyClaw.png")
      Player.img = pygame.transform.scale(Player.img,(169,120))
      Player.width = 169
      Player.height = 120

  if Character == "KingKRool":
      Player.img = pygame.image.load("Assets/Characters/KingKRool/KingKRoolClaw.png")
      Player.img = pygame.transform.scale(Player.img,(105,120))
      Player.width = 105
      Player.height = 120

  if Character == "Banjo":
      Player.img = pygame.image.load("Assets/Characters/Banjo/BanjoInstrument.png")
      Player.img = pygame.transform.scale(Player.img,(96,96))
      Player.width = 96
      Player.height = 96


  if Character == "Steve":
      Player.img = pygame.image.load("Assets/Characters/Steve/SteveSword.png")
      Player.img = pygame.transform.scale(Player.img,(63,85))
      Player.width = 63
      Player.height = 85

  if Character == "Kazuya":
      Player.img = pygame.image.load("Assets/Characters/Kazuya/KazuyaPunch.png")
      Player.img = pygame.transform.scale(Player.img,(80,100))
      Player.width = 80
      Player.height = 100

  if Character == "Waluigi":
      Player.img = pygame.image.load("Assets/Characters/Waluigi/WaluigiRacket.png")
      Player.img = pygame.transform.scale(Player.img,(42,108))
      Player.width = 42
      Player.height = 108


  if Character == "Tails":
      Player.img = pygame.image.load("Assets/Characters/Tails/TailsHelicopter.png")
      Player.img = pygame.transform.scale(Player.img,(75,82))
      Player.width = 75
      Player.height = 82
      if Player.InAir == False:
          Player.y -= 1
          Player.UpdateHitbox()
          Player.vy = -4

  if Character == "Knuckles":
      Player.img = pygame.image.load("Assets/Characters/Knuckles/KnucklesJump.png")
      Player.img = pygame.transform.scale(Player.img,(94,94))
      Player.width = 94
      Player.height = 94
      if Player.InAir == False:
          Player.y -= 1
          Player.UpdateHitbox()
          Player.vy = -4

  if Character == "Eggman":
      Player.img = pygame.image.load("Assets/Characters/Eggman/EggmanWreckingBall.png")
      Player.img = pygame.transform.scale(Player.img,(99,165))
      Player.width = 99
      Player.height = 165

  if Character == "Roblox":
      Player.img = pygame.image.load("Assets/Characters/Roblox/RobloxProjectile.png")
      Player.img = pygame.transform.scale(Player.img,(70,90))
      Player.width = 70
      Player.height = 90

  if Character == "Sans":
      Player.img = pygame.image.load("Assets/Characters/Sans/SansProjectile.png")
      Player.img = pygame.transform.scale(Player.img,(85,85))
      Player.width = 85
      Player.height = 85

  if Character == "Decidueye":
      Player.img = pygame.image.load("Assets/Characters/Decidueye/DecidueyeFeather.png")
      Player.img = pygame.transform.scale(Player.img,(90,96))
      Player.width = 90
      Player.height = 96

  
#When not attacking
def Idle(Player,Character):
  
  if Character == "Mario":
        Player.img = pygame.image.load("Assets/Characters/Mario/Mario.png")
        Player.img = pygame.transform.scale(Player.img,(48,90))
        Player.width = 48
        Player.height = 90
  if Character == "DK":
        Player.img = pygame.image.load("Assets/Characters/DK/DK.png")
        Player.img = pygame.transform.scale(Player.img,(81,103))
        Player.width = 81
        Player.height = 103

  if Character == "Link":
        Player.img = pygame.image.load("Assets/Characters/Link/Link.png")
        Player.img = pygame.transform.scale(Player.img,(54,96))
        Player.width = 54
        Player.height = 96

  if Character == "Samus":
        Player.img = pygame.image.load("Assets/Characters/Samus/Samus.png")
        Player.img = pygame.transform.scale(Player.img,(57,96))
        Player.width = 57
        Player.height = 96

  if Character == "Yoshi":
        Player.img = pygame.image.load("Assets/Characters/Yoshi/Yoshi.png")
        Player.img = pygame.transform.scale(Player.img,(60,90))
        Player.width = 60
        Player.height = 90

  if Character == "Kirby":
        Player.img = pygame.image.load("Assets/Characters/Kirby/Kirby.png")
        Player.img = pygame.transform.scale(Player.img,(60,70))
        Player.width = 60
        Player.height = 70

  if Character == "Fox":
        Player.img = pygame.image.load("Assets/Characters/Fox/Fox.png")
        Player.img = pygame.transform.scale(Player.img,(46,87))
        Player.width = 46
        Player.height = 87

  if Character == "Pikachu":
        Player.img = pygame.image.load("Assets/Characters/Pikachu/Pikachu.png")
        Player.img = pygame.transform.scale(Player.img,(65,73))
        Player.width = 65
        Player.height = 73

  if Character == "Luigi":
      Player.img = pygame.image.load("Assets/Characters/Luigi/Luigi.png")
      Player.img = pygame.transform.scale(Player.img,(42,93))
      Player.width = 42
      Player.height = 93

  if Character == "CaptainFalcon":
      Player.img = pygame.image.load("Assets/Characters/CaptainFalcon/CaptainFalcon.png")
      Player.img = pygame.transform.scale(Player.img,(65,98))
      Player.width = 65
      Player.height = 98

  if Character == "Peach":
      Player.img = pygame.image.load("Assets/Characters/Peach/Peach.png")
      Player.img = pygame.transform.scale(Player.img,(55,97))
      Player.width = 55
      Player.height = 97

  if Character == "Bowser":
      Player.img = pygame.image.load("Assets/Characters/Bowser/Bowser.png")
      Player.img = pygame.transform.scale(Player.img,(140,140))
      Player.width = 140
      Player.height = 140

  if Character == "Ganon":
      Player.img = pygame.image.load("Assets/Characters/Ganon/Ganon.png")
      Player.img = pygame.transform.scale(Player.img,(107,120))
      Player.width = 107
      Player.height = 120

  if Character == "Mewtwo":
      Player.img = pygame.image.load("Assets/Characters/Mewtwo/Mewtwo.png")
      Player.img = pygame.transform.scale(Player.img,(84,105))
      Player.width = 84
      Player.height = 105

  if Character == "MetaKnight":
      Player.img = pygame.image.load("Assets/Characters/MetaKnight/MetaKnight.png")
      Player.img = pygame.transform.scale(Player.img,(70,75))
      Player.width = 70
      Player.height = 75

  if Character == "Wario":
      Player.img = pygame.image.load("Assets/Characters/Wario/Wario.png")
      Player.img = pygame.transform.scale(Player.img,(48,90))
      Player.width = 48
      Player.height = 90

  if Character == "Charizard":
      Player.img = pygame.image.load("Assets/Characters/Charizard/Charizard.png")
      Player.img = pygame.transform.scale(Player.img,(108,108))
      Player.width = 108
      Player.height = 108

  if Character == "DiddyKong":
      Player.img = pygame.image.load("Assets/Characters/DiddyKong/DiddyKong.png")
      Player.img = pygame.transform.scale(Player.img,(72,80))
      Player.width = 72
      Player.height = 80

  if Character == "Sonic":
      Player.img = pygame.image.load("Assets/Characters/Sonic/Sonic.png")
      Player.img = pygame.transform.scale(Player.img,(60,88))
      Player.width = 60
      Player.height = 88

  if Character == "KingDedede":
      Player.img = pygame.image.load("Assets/Characters/KingDedede/KingDedede.png")
      Player.img = pygame.transform.scale(Player.img,(108,108))
      Player.width = 108
      Player.height = 108

  if Character == "MegaMan":
      Player.img = pygame.image.load("Assets/Characters/MegaMan/MegaMan.png")
      Player.img = pygame.transform.scale(Player.img,(96,90))
      Player.width = 96
      Player.height = 90

  if Character == "Greninja":
      Player.img = pygame.image.load("Assets/Characters/Greninja/Greninja.png")
      Player.img = pygame.transform.scale(Player.img,(70,70))
      Player.width = 70
      Player.height = 70

  if Character == "PacMan":
      Player.img = pygame.image.load("Assets/Characters/PacMan/PacMan.png")
      Player.img = pygame.transform.scale(Player.img,(60,81))
      Player.width = 60
      Player.height = 81

  if Character == "Inkling":
      Player.img = pygame.image.load("Assets/Characters/Inkling/Inkling.png")
      Player.img = pygame.transform.scale(Player.img,(80,80))
      Player.width = 80
      Player.height = 80

  if Character == "Ridley":
      Player.img = pygame.image.load("Assets/Characters/Ridley/Ridley.png")
      Player.img = pygame.transform.scale(Player.img,(169,120))
      Player.width = 169
      Player.height = 120

  if Character == "KingKRool":
      Player.img = pygame.image.load("Assets/Characters/KingKRool/KingKRool.png")
      Player.img = pygame.transform.scale(Player.img,(105,120))
      Player.width = 105
      Player.height = 120

  if Character == "Banjo":
      Player.img = pygame.image.load("Assets/Characters/Banjo/Banjo.png")
      Player.img = pygame.transform.scale(Player.img,(96,96))
      Player.width = 96
      Player.height = 96

  if Character == "Steve":
      Player.img = pygame.image.load("Assets/Characters/Steve/Steve.png")
      Player.img = pygame.transform.scale(Player.img,(63,85))
      Player.width = 63
      Player.height = 85

  if Character == "Kazuya":
      Player.img = pygame.image.load("Assets/Characters/Kazuya/Kazuya.png")
      Player.img = pygame.transform.scale(Player.img,(80,100))
      Player.width = 80
      Player.height = 100

  if Character == "Waluigi":
      Player.img = pygame.image.load("Assets/Characters/Waluigi/Waluigi.png")
      Player.img = pygame.transform.scale(Player.img,(42,108))
      Player.width = 42
      Player.height = 108


  if Character == "Tails":
      Player.img = pygame.image.load("Assets/Characters/Tails/Tails.png")
      Player.img = pygame.transform.scale(Player.img,(75,82))
      Player.width = 75
      Player.height = 82

  if Character == "Knuckles":
      Player.img = pygame.image.load("Assets/Characters/Knuckles/Knuckles.png")
      Player.img = pygame.transform.scale(Player.img,(94,94))
      Player.width = 94
      Player.height = 94

  if Character == "Eggman":
      Player.img = pygame.image.load("Assets/Characters/Eggman/Eggman.png")
      Player.img = pygame.transform.scale(Player.img,(99,117))
      Player.width = 99
      Player.height = 117

  if Character == "Roblox":
      Player.img = pygame.image.load("Assets/Characters/Roblox/Roblox.png")
      Player.img = pygame.transform.scale(Player.img,(70,90))
      Player.width = 70
      Player.height = 90

  if Character == "Sans":
      Player.img = pygame.image.load("Assets/Characters/Sans/Sans.png")
      Player.img = pygame.transform.scale(Player.img,(85,85))
      Player.width = 85
      Player.height = 85

  if Character == "Decidueye":
      Player.img = pygame.image.load("Assets/Characters/Decidueye/Decidueye.png")
      Player.img = pygame.transform.scale(Player.img,(90,96))
      Player.width = 90
      Player.height = 96






  if Character == "Mario":
        Player.img = pygame.transform.scale(Player.img,(48,90))
        Player.width = 48
        Player.height = 90
  if Character == "DK":
        Player.img = pygame.transform.scale(Player.img,(81,103))
        Player.width = 81
        Player.height = 103

  if Character == "Link":
        Player.img = pygame.transform.scale(Player.img,(54,96))
        Player.width = 54
        Player.height = 96

  if Character == "Samus":
        Player.img = pygame.transform.scale(Player.img,(57,96))
        Player.width = 57
        Player.height = 96

  if Character == "Yoshi":
        Player.img = pygame.transform.scale(Player.img,(60,90))
        Player.width = 60
        Player.height = 90

  if Character == "Kirby":
        Player.img = pygame.transform.scale(Player.img,(60,70))
        Player.width = 60
        Player.height = 70

  if Character == "Fox":
        Player.img = pygame.transform.scale(Player.img,(46,87))
        Player.width = 46
        Player.height = 87

  if Character == "Pikachu":
        Player.img = pygame.transform.scale(Player.img,(65,73))
        Player.width = 65
        Player.height = 73

  if Character == "Luigi":
      Player.img = pygame.transform.scale(Player.img,(42,93))
      Player.width = 42
      Player.height = 93

  if Character == "CaptainFalcon":
      Player.img = pygame.transform.scale(Player.img,(65,98))
      Player.width = 65
      Player.height = 98

  if Character == "Peach":
      Player.img = pygame.transform.scale(Player.img,(55,97))
      Player.width = 55
      Player.height = 97

  if Character == "Bowser":
      Player.img = pygame.transform.scale(Player.img,(140,140))
      Player.width = 140
      Player.height = 140

  if Character == "Ganon":
      Player.img = pygame.transform.scale(Player.img,(107,120))
      Player.width = 107
      Player.height = 120

  if Character == "Mewtwo":
      Player.img = pygame.transform.scale(Player.img,(84,105))
      Player.width = 84
      Player.height = 105

  if Character == "MetaKnight":
      Player.img = pygame.transform.scale(Player.img,(70,75))
      Player.width = 70
      Player.height = 75

  if Character == "Wario":
      Player.img = pygame.transform.scale(Player.img,(48,90))
      Player.width = 48
      Player.height = 90

  if Character == "Charizard":
      Player.img = pygame.transform.scale(Player.img,(108,108))
      Player.width = 108
      Player.height = 108

  if Character == "DiddyKong":
      Player.img = pygame.transform.scale(Player.img,(72,80))
      Player.width = 72
      Player.height = 80

  if Character == "Sonic":
      Player.img = pygame.transform.scale(Player.img,(60,88))
      Player.width = 60
      Player.height = 88

  if Character == "KingDedede":
      Player.img = pygame.transform.scale(Player.img,(108,108))
      Player.width = 108
      Player.height = 108

  if Character == "MegaMan":
      Player.img = pygame.transform.scale(Player.img,(96,90))
      Player.width = 96
      Player.height = 90

  if Character == "Greninja":
      Player.img = pygame.transform.scale(Player.img,(70,70))
      Player.width = 70
      Player.height = 70

  if Character == "PacMan":
      Player.img = pygame.transform.scale(Player.img,(60,81))
      Player.width = 60
      Player.height = 81

  if Character == "Inkling":
      Player.img = pygame.transform.scale(Player.img,(80,80))
      Player.width = 80
      Player.height = 80

  if Character == "Ridley":
      Player.img = pygame.transform.scale(Player.img,(169,120))
      Player.width = 169
      Player.height = 120

  if Character == "KingKRool":
      Player.img = pygame.transform.scale(Player.img,(105,120))
      Player.width = 105
      Player.height = 120

  if Character == "Banjo":
      Player.img = pygame.transform.scale(Player.img,(96,96))
      Player.width = 96
      Player.height = 96

  if Character == "Steve":
      Player.img = pygame.transform.scale(Player.img,(63,85))
      Player.width = 63
      Player.height = 85

  if Character == "Kazuya":
      Player.img = pygame.transform.scale(Player.img,(80,100))
      Player.width = 80
      Player.height = 100

  if Character == "Waluigi":
      Player.img = pygame.transform.scale(Player.img,(42,108))
      Player.width = 42
      Player.height = 108


  if Character == "Tails":
      Player.img = pygame.transform.scale(Player.img,(75,82))
      Player.width = 75
      Player.height = 82

  if Character == "Knuckles":
      Player.img = pygame.transform.scale(Player.img,(94,94))
      Player.width = 94
      Player.height = 94

  if Character == "Eggman":
      Player.img = pygame.transform.scale(Player.img,(99,117))
      Player.width = 99
      Player.height = 117

  if Character == "Roblox":
      Player.img = pygame.transform.scale(Player.img,(70,90))
      Player.width = 70
      Player.height = 90

  if Character == "Sans":
      Player.img = pygame.transform.scale(Player.img,(85,85))
      Player.width = 85
      Player.height = 85

  if Character == "Decidueye":
      Player.img = pygame.transform.scale(Player.img,(90,96))
      Player.width = 90
      Player.height = 96

    
  Player.img_flip = pygame.transform.flip(Player.img, True, False)

#Title screen
Play = GameObject(450,130,75,75,"Assets/TitleScreen/Play.png")

#P1Selects(Spaces 20 in the X)
P1Mario = GameObject(255,100,50,50,"Assets/CharacterSelects/MarioSel.png")

P1DK = GameObject(305,100,50,50,"Assets/CharacterSelects/DKSel.png")

P1Link = GameObject(355,100,50,50,"Assets/CharacterSelects/LinkSel.png")

P1Samus = GameObject(405,100,50,50,"Assets/CharacterSelects/SamusSel.png")

P1Yoshi = GameObject(455,100,50,50,"Assets/CharacterSelects/YoshiSel.png")

P1Kirby = GameObject(505,100,50,50,"Assets/CharacterSelects/KirbySel.png")

P1Fox = GameObject(555,100,50,50,"Assets/CharacterSelects/FoxSel.png")

P1Pikachu = GameObject(605,100,50,50,"Assets/CharacterSelects/PikachuSel.png")

P1Luigi = GameObject(655,100,50,50,"Assets/CharacterSelects/LuigiSel.png")

P1CaptainFalcon = GameObject(255,150,50,50,"Assets/CharacterSelects/CaptainFalconSel.png")

P1Peach = GameObject(305,150,50,50,"Assets/CharacterSelects/PeachSel.png")

P1Bowser = GameObject(355,150,50,50,"Assets/CharacterSelects/BowserSel.png")

P1Ganon = GameObject(405,150,50,50,"Assets/CharacterSelects/GanonSel.png")

P1Mewtwo = GameObject(455,150,50,50,"Assets/CharacterSelects/MewtwoSel.png")

P1MetaKnight = GameObject(505,150,50,50,"Assets/CharacterSelects/MetaKnightSel.png")

P1Wario = GameObject(555,150,50,50,"Assets/CharacterSelects/WarioSel.png")

P1Charizard = GameObject(605,150,50,50,"Assets/CharacterSelects/CharizardSel.png")

P1DiddyKong = GameObject(655,150,50,50,"Assets/CharacterSelects/DiddyKongSel.png")

P1Sonic = GameObject(255,200,50,50,"Assets/CharacterSelects/SonicSel.png")

P1KingDedede = GameObject(305,200,50,50,"Assets/CharacterSelects/KingDededeSel.png")

P1MegaMan= GameObject(355,200,50,50,"Assets/CharacterSelects/MegaManSel.png")

P1Greninja= GameObject(405,200,50,50,"Assets/CharacterSelects/GreninjaSel.png")

P1PacMan= GameObject(455,200,50,50,"Assets/CharacterSelects/PacManSel.png")

P1Inkling= GameObject(505,200,50,50,"Assets/CharacterSelects/InklingSel.png")

P1Ridley= GameObject(555,200,50,50,"Assets/CharacterSelects/RidleySel.png")

P1KingKRool= GameObject(605,200,50,50,"Assets/CharacterSelects/KingKRoolSel.png")

P1Banjo = GameObject(655,200,50,50,"Assets/CharacterSelects/BanjoSel.png")

P1Steve = GameObject(255,250,50,50,"Assets/CharacterSelects/SteveSel.png")

P1Kazuya = GameObject(305,250,50,50,"Assets/CharacterSelects/KazuyaSel.png")

P1Waluigi = GameObject(355,250,50,50,"Assets/CharacterSelects/WaluigiSel.png")

P1Tails = GameObject(405,250,50,50,"Assets/CharacterSelects/TailsSel.png")

P1Knuckles = GameObject(455,250,50,50,"Assets/CharacterSelects/KnucklesSel.png")

P1Eggman = GameObject(505,250,50,50,"Assets/CharacterSelects/EggmanSel.png")

P1Roblox = GameObject(555,250,50,50,"Assets/CharacterSelects/RobloxSel.png")

P1Sans = GameObject(605,250,50,50,"Assets/CharacterSelects/SansSel.png")

P1Decidueye = GameObject(655,250,50,50,"Assets/CharacterSelects/DecidueyeSel.png")


#P2Selects
P2Mario = GameObject(255,100,50,50,"Assets/CharacterSelects/MarioSel.png")

P2DK = GameObject(305,100,50,50,"Assets/CharacterSelects/DKSel.png")

P2Link = GameObject(355,100,50,50,"Assets/CharacterSelects/LinkSel.png")

P2Samus = GameObject(405,100,50,50,"Assets/CharacterSelects/SamusSel.png")

P2Yoshi = GameObject(455,100,50,50,"Assets/CharacterSelects/YoshiSel.png")

P2Kirby = GameObject(505,100,50,50,"Assets/CharacterSelects/KirbySel.png")

P2Fox = GameObject(555,100,50,50,"Assets/CharacterSelects/FoxSel.png")

P2Pikachu = GameObject(605,100,50,50,"Assets/CharacterSelects/PikachuSel.png")

P2Luigi = GameObject(655,100,50,50,"Assets/CharacterSelects/LuigiSel.png")

P2CaptainFalcon = GameObject(255,150,50,50,"Assets/CharacterSelects/CaptainFalconSel.png")

P2Peach = GameObject(305,150,50,50,"Assets/CharacterSelects/PeachSel.png")

P2Bowser = GameObject(355,150,50,50,"Assets/CharacterSelects/BowserSel.png")

P2Ganon = GameObject(405,150,50,50,"Assets/CharacterSelects/GanonSel.png")

P2Mewtwo = GameObject(455,150,50,50,"Assets/CharacterSelects/MewtwoSel.png")

P2MetaKnight = GameObject(505,150,50,50,"Assets/CharacterSelects/MetaKnightSel.png")

P2Wario = GameObject(555,150,50,50,"Assets/CharacterSelects/WarioSel.png")

P2Charizard = GameObject(605,150,50,50,"Assets/CharacterSelects/CharizardSel.png")

P2DiddyKong = GameObject(655,150,50,50,"Assets/CharacterSelects/DiddyKongSel.png")

P2Sonic = GameObject(255,200,50,50,"Assets/CharacterSelects/SonicSel.png")

P2KingDedede = GameObject(305,200,50,50,"Assets/CharacterSelects/KingDededeSel.png")

P2MegaMan= GameObject(355,200,50,50,"Assets/CharacterSelects/MegaManSel.png")

P2Greninja= GameObject(405,200,50,50,"Assets/CharacterSelects/GreninjaSel.png")

P2PacMan= GameObject(455,200,50,50,"Assets/CharacterSelects/PacManSel.png")

P2Inkling= GameObject(505,200,50,50,"Assets/CharacterSelects/InklingSel.png")

P2Ridley= GameObject(555,200,50,50,"Assets/CharacterSelects/RidleySel.png")

P2KingKRool= GameObject(605,200,50,50,"Assets/CharacterSelects/KingKRoolSel.png")

P2Banjo = GameObject(655,200,50,50,"Assets/CharacterSelects/BanjoSel.png")

P2Steve = GameObject(255,250,50,50,"Assets/CharacterSelects/SteveSel.png")

P2Kazuya = GameObject(305,250,50,50,"Assets/CharacterSelects/KazuyaSel.png")

P2Waluigi = GameObject(355,250,50,50,"Assets/CharacterSelects/WaluigiSel.png")

P2Tails = GameObject(405,250,50,50,"Assets/CharacterSelects/TailsSel.png")

P2Knuckles = GameObject(455,250,50,50,"Assets/CharacterSelects/KnucklesSel.png")

P2Eggman = GameObject(505,250,50,50,"Assets/CharacterSelects/EggmanSel.png")

P2Roblox = GameObject(555,250,50,50,"Assets/CharacterSelects/RobloxSel.png")

P2Sans = GameObject(605,250,50,50,"Assets/CharacterSelects/SansSel.png")

P2Decidueye = GameObject(655,250,50,50,"Assets/CharacterSelects/DecidueyeSel.png")



#BackgroundSelects
MarioLand = GameObject(225,90,250,100,"Assets/BackGroundSelects/MarioBackground.png")
FinalDestinationSel = GameObject(225,180,250,100,"Assets/BackGroundSelects/FinalDestinationSel.png")
Brinstar = GameObject(475,90,250,100,"Assets/BackGroundSelects/BrinstarSel.png")
GreenHillZoneSel = GameObject(475,180,250,100,"Assets/BackGroundSelects/GreenHillZoneSel.png")

#Backgrounds
FinalDestination = GameObject(0,0,1000,5000,"Assets/Backgrounds/FinalDestination.PNG")
#PalmTrees = GameObject(25,0,500,255,"Assets/Backgrounds/PalmTrees.png")

#Ground
Ground = GameObject(120,200,750,150,"Assets/Grounds/MarioGround.png")

#Players
Player1 = GameObject(125,20,10,10,"Assets/Characters/Mario/Mario.png")
Player2 = GameObject(700,20,10,10,"Assets/Characters/Mario/Mario.png")


#EndScreen
Replay = GameObject(435,200,75,75,"Assets/Winners/Restart.png")

#Projectiles
ProjectilePlayer1 = GameObject(Player1.x,Player1.y,30,36,"Assets/Projectile/Arrow.png")
ProjectilePlayer2 = GameObject(Player2.x,Player2.y,30,36,"Assets/Projectile/Arrow.png")



#Manages Health
Player2HealthWidth = 70
Player1HealthWidth = 70

#Main game loop
running = True
while running:
  Clock.tick(200)

  #Moves the players
  Player1.x = Player1.x + Player1.vx
  Player1.hitbox = pygame.Rect(Player1.x,Player1.y,Player1.width,Player1.height)
  
  Player2.x = Player2.x + Player2.vx
  Player2.hitbox = pygame.Rect(Player2.x,Player2.y,Player2.width,Player2.height)
#Moves the projectiles
  ProjectilePlayer1.x = ProjectilePlayer1.x + ProjectilePlayer1.vx
  ProjectilePlayer1.hitbox = pygame.Rect(ProjectilePlayer1.x,ProjectilePlayer1.y, ProjectilePlayer1.width,ProjectilePlayer1.height)

  ProjectilePlayer2.x = ProjectilePlayer2.x + ProjectilePlayer2.vx
  ProjectilePlayer2.hitbox = pygame.Rect(ProjectilePlayer2.x,ProjectilePlayer2.y, ProjectilePlayer2.width,ProjectilePlayer2.height)
  
  #Event handler
  for event in pygame.event.get():


    if event.type == pygame.QUIT:
      running = False

 
    if event.type == KEYDOWN:
      
      #Player1Controls
      if event.key == K_w and Page == "Game":
 
        if Player1.InAir == False:          
          Player1.y -= 1
          Player1.UpdateHitbox()
          Player1.vy = -5.5

      if event.key == K_d and Page == "Game":
  
        Player1.vx = 2
        Player1.FacingRight = True

      if event.key == K_a and Page == "Game":

        Player1.vx = -2
        Player1.FacingRight = False


      if event.key == K_z and Page == "Game":
 
        Player1Hits = True
        Attack1(Player1,Character1)
        Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

      if event.key == K_x and Page == "Game":

        Player1Hits = True
        Attack2(Player1,Character1)
        Player1.img_flip = pygame.transform.flip(Player1.img, True, False)
        if (Character1 == "Link" or Character1 == "Samus" or Character1 == "Pikachu" or Character1 == "Mewtwo" or Character1 == "MegaMan" or Character1 == "Inkling" or Character1 == "Roblox" or Character1 == "Sans" or Character1 == "Decidueye")and P1Projectile == False:
          P1Projectile = True
          ProjectilePlayer1.FacingRight = Player1.FacingRight
          #ProjectilePlayer1.x = Player1.x
          #ProjectilePlayer1.y = ProjectilePlayer1.y

          

      #Player2Controls
      if event.key == K_o and Page == "Game":
     
        Player2Hits = True
        Attack1(Player2,Character2)
        Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

      if event.key == K_p and Page == "Game":
     
        Player2Hits = True
        Attack2(Player2,Character2)
        Player2.img_flip = pygame.transform.flip(Player2.img, True, False)
        
        if (Character2 == "Link" or Character2 == "Samus" or Character2 == "Pikachu" or Character2 == "Mewtwo" or Character2 == "MegaMan" or Character2 == "Inkling" or Character2 == "Roblox" or Character2 == "Sans" or Character2 == "Decidueye") and P2Projectile == False:
          P2Projectile = True
          ProjectilePlayer2.FacingRight = Player2.FacingRight


      if event.key == K_UP and Page == "Game":
  
        if Player2.InAir == False:
          Player2.y -= 1
          Player2.UpdateHitbox()
          Player2.vy = -5.5

      if event.key == K_RIGHT and Page == "Game":
  
        Player2.vx = 2
        Player2.FacingRight = True
        #if P2Projectile == False:
          #ProjectileDirectionP2 = "Right"
      if event.key == K_LEFT and Page == "Game":

        Player2.vx = -2
        Player2.FacingRight = False
        #if P2Projectile == False:
          #ProjectileDirectionP2 = "Left"
    if event.type == KEYUP:

      # IgnoreInputs = False

      #Player1Controls
      if event.key == K_d:
        Player1.vx = 0
 
      if event.key == K_a:
        Player1.vx = 0
    

     
      if event.key == K_z:
        #P1Projectile = False
        Player1Hits = False
        Idle(Player1,Character1)
        Player1.img_flip = pygame.transform.flip(Player1.img, True, False)
      if event.key == K_x:
        #P1Projectile = False
        Player1Hits = False
        Idle(Player1,Character1)
        Player1.img_flip = pygame.transform.flip(Player1.img, True, False)



      #Player2Controls
      if event.key == K_RIGHT:
        Player2.vx = 0
 
      if event.key == K_LEFT:
        Player2.vx = 0


      if event.key == K_o:
        #P2Projectile = False
        Player2Hits = False
        Idle(Player2,Character2)
        Player2.img_flip = pygame.transform.flip(Player2.img, True, False)
      if event.key == K_p:
        #P2Projectile = False
        Player2Hits = False
        Idle(Player2,Character2)
        Player2.img_flip = pygame.transform.flip(Player2.img, True, False)


 
    #Buttons
    if event.type == pygame.MOUSEBUTTONDOWN:

      #Title
      if Play.Clicked() == True and Page == "Title":
        Page = "P1Sel"

      #P1Selects
      elif Page == "P1Sel":
        if P1Mario.Clicked() == True:
          Character1 = "Mario"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Mario/Mario.png")
          Player1.img = pygame.transform.scale(Player1.img,(45,87))
          Player1.width = 48
          Player1.height = 90
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)
        
        if P1DK.Clicked() == True:
          Character1 = "DK"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/DK/DK.png")
          Player1.img = pygame.transform.scale(Player1.img,(78,100))
          Player1.width = 81
          Player1.height = 103
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)
 

        
        if P1Link.Clicked() == True:
          Character1 = "Link"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Link/Link.png")
          Player1.img = pygame.transform.scale(Player1.img,(51,93))
          Player1.width = 54
          Player1.height = 96
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)


        if P1Samus.Clicked() == True:
          Character1 = "Samus"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Samus/Samus.png")
          Player1.img = pygame.transform.scale(Player1.img,(54,93))
          Player1.width = 57
          Player1.height = 96
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)
    

        if P1Yoshi.Clicked() == True:
          Character1 = "Yoshi"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Yoshi/Yoshi.png")
          Player1.img = pygame.transform.scale(Player1.img,(57,87))
          Player1.width = 60
          Player1.height = 90
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1Kirby.Clicked() == True:
          Character1 = "Kirby"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Kirby/Kirby.png")
          Player1.img = pygame.transform.scale(Player1.img,(57,67))
          Player1.width = 60
          Player1.height = 70
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1Fox.Clicked() == True:
          Character1 = "Fox"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Fox/Fox.png")
          Player1.img = pygame.transform.scale(Player1.img,(43,84))
          Player1.width = 46
          Player1.height = 87
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1Pikachu.Clicked() == True:
          Character1 = "Pikachu"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Pikachu/Pikachu.png")
          Player1.img = pygame.transform.scale(Player1.img,(62,70))
          Player1.width = 65
          Player1.height = 73
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1Luigi.Clicked() == True:
          Character1 = "Luigi"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Luigi/Luigi.png")
          Player1.img = pygame.transform.scale(Player1.img,(39,90))
          Player1.width = 42
          Player1.height = 93
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1CaptainFalcon.Clicked() == True:
          Character1 = "CaptainFalcon"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/CaptainFalcon/CaptainFalcon.png")
          Player1.img = pygame.transform.scale(Player1.img,(62,95))
          Player1.width = 65
          Player1.height = 98
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1Peach.Clicked() == True:
          Character1 = "Peach"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Peach/Peach.png")
          Player1.img = pygame.transform.scale(Player1.img,(52,94))
          Player1.width = 55
          Player1.height = 97
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1Bowser.Clicked() == True:
          Character1 = "Bowser"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Bowser/Bowser.png")
          Player1.img = pygame.transform.scale(Player1.img,(137,137))
          Player1.width = 140
          Player1.height = 140
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1Ganon.Clicked() == True:
          Character1 = "Ganon"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Ganon/Ganon.png")
          Player1.img = pygame.transform.scale(Player1.img,(104,117))
          Player1.width = 107
          Player1.height = 120
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1Mewtwo.Clicked() == True:
          Character1 = "Mewtwo"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Mewtwo/Mewtwo.png")
          Player1.img = pygame.transform.scale(Player1.img,(81,102))
          Player1.width = 84
          Player1.height = 105
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1MetaKnight.Clicked() == True:
          Character1 = "MetaKnight"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/MetaKnight/MetaKnight.png")
          Player1.img = pygame.transform.scale(Player1.img,(67,72))
          Player1.width = 70
          Player1.height = 75
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1Wario.Clicked() == True:
          Character1 = "Wario"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Wario/Wario.png")
          Player1.img = pygame.transform.scale(Player1.img,(45,87))
          Player1.width = 48
          Player1.height = 90
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1Charizard.Clicked() == True:
          Character1 = "Charizard"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Charizard/Charizard.png")
          Player1.img = pygame.transform.scale(Player1.img,(105,105))
          Player1.width = 108
          Player1.height = 108
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1DiddyKong.Clicked() == True:
          Character1 = "DiddyKong"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/DiddyKong/DiddyKong.png")
          Player1.img = pygame.transform.scale(Player1.img,(69,77))
          Player1.width = 72
          Player1.height = 80
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1Sonic.Clicked() == True:
          Character1 = "Sonic"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Sonic/Sonic.png")
          Player1.img = pygame.transform.scale(Player1.img,(57,85))
          Player1.width = 60
          Player1.height = 88
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1KingDedede.Clicked() == True:
          Character1 = "KingDedede"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/KingDedede/KingDedede.png")
          Player1.img = pygame.transform.scale(Player1.img,(105,105))
          Player1.width = 108
          Player1.height = 108
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1MegaMan.Clicked() == True:
          Character1 = "MegaMan"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/MegaMan/MegaMan.png")
          Player1.img = pygame.transform.scale(Player1.img,(93,87))
          Player1.width = 96
          Player1.height = 90
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1Greninja.Clicked() == True:
          Character1 = "Greninja"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Greninja/Greninja.png")
          Player1.img = pygame.transform.scale(Player1.img,(67,67))
          Player1.width = 70
          Player1.height = 70
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1PacMan.Clicked() == True:
          Character1 = "PacMan"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/PacMan/PacMan.png")
          Player1.img = pygame.transform.scale(Player1.img,(57,78))
          Player1.width = 60
          Player1.height = 81
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1Inkling.Clicked() == True:
          Character1 = "Inkling"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Inkling/Inkling.png")
          Player1.img = pygame.transform.scale(Player1.img,(77,77))
          Player1.width = 80
          Player1.height = 80
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)


        
        if P1Ridley.Clicked() == True:
          Character1 = "Ridley"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Ridley/Ridley.png")
          Player1.img = pygame.transform.scale(Player1.img,(166,117))
          Player1.width = 169
          Player1.height = 120
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)


        
        if P1KingKRool.Clicked() == True:
          Character1 = "KingKRool"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/KingKRool/KingKRool.png")
          Player1.img = pygame.transform.scale(Player1.img,(132,117))
          Player1.width = 105
          Player1.height = 120
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)
      

        if P1Banjo.Clicked() == True:
          Character1 = "Banjo"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Banjo/Banjo.png")
          Player1.img = pygame.transform.scale(Player1.img,(93,93))
          Player1.width = 96
          Player1.height = 96
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)
  

        if P1Steve.Clicked() == True:
          Character1 = "Steve"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Steve/Steve.png")
          Player1.img = pygame.transform.scale(Player1.img,(60,82))
          Player1.width = 63
          Player1.height = 85
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)



        if P1Kazuya.Clicked() == True:
          Character1 = "Kazuya"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Kazuya/Kazuya.png")
          Player1.img = pygame.transform.scale(Player1.img,(77,97))
          Player1.width = 80
          Player1.height = 100
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)


        if P1Waluigi.Clicked() == True:
          Character1 = "Waluigi"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Waluigi/Waluigi.png")
          Player1.img = pygame.transform.scale(Player1.img,(39,105))
          Player1.width = 42
          Player1.height = 108
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1Tails.Clicked() == True:
          Character1 = "Tails"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Tails/Tails.png")
          Player1.img = pygame.transform.scale(Player1.img,(72,79))
          Player1.width = 75
          Player1.height = 82
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1Knuckles.Clicked() == True:
          Character1 = "Knuckles"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Knuckles/Knuckles.png")
          Player1.img = pygame.transform.scale(Player1.img,(91,91))
          Player1.width = 94
          Player1.height = 94
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1Eggman.Clicked() == True:
          Character1 = "Eggman"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Eggman/Eggman.png")
          Player1.img = pygame.transform.scale(Player1.img,(96,114))
          Player1.width = 99
          Player1.height = 117
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        
        if P1Roblox.Clicked() == True:
          Character1 = "Roblox"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Roblox/Roblox.png")
          Player1.img = pygame.transform.scale(Player1.img,(67,87))
          Player1.width = 70
          Player1.height = 90
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1Sans.Clicked() == True:
          Character1 = "Sans"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Sans/Sans.png")
          Player1.img = pygame.transform.scale(Player1.img,(82,82))
          Player1.width = 85
          Player1.height = 85
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)

        if P1Decidueye.Clicked() == True:
          Character1 = "Decidueye"
          Page = "P2Sel"      
          Player1.img = pygame.image.load("Assets/Characters/Decidueye/Decidueye.png")
          Player1.img = pygame.transform.scale(Player1.img,(87,93))
          Player1.width = 90
          Player1.height = 96
          Player1.img_flip = pygame.transform.flip(Player1.img, True, False)


      #P2Selects
      elif Page == "P2Sel":
        if P2Mario.Clicked() == True and Page == "P2Sel":
          Character2 = "Mario"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Mario/Mario.png")
          Player2.img = pygame.transform.scale(Player2.img,(45,87))
          Player2.width = 48
          Player2.height = 90
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2DK.Clicked() == True and Page == "P2Sel":
          Character2 = "DK"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/DK/DK.png")
          Player2.img = pygame.transform.scale(Player2.img,(81,103))
          Player2.width = 81
          Player2.height = 103
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2Link.Clicked() == True and Page == "P2Sel":
          Character2 = "Link"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Link/Link.png")
          Player2.img = pygame.transform.scale(Player2.img,(54,96))
          Player2.width = 54
          Player2.height = 96
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2Samus.Clicked() == True and Page == "P2Sel":
          Character2 = "Samus"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Samus/Samus.png")
          Player2.img = pygame.transform.scale(Player2.img,(57,96))
          Player2.width = 57
          Player2.height = 96
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2Yoshi.Clicked() == True and Page == "P2Sel":
          Character2 = "Yoshi"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Yoshi/Yoshi.png")
          Player2.img = pygame.transform.scale(Player2.img,(60,90))
          Player2.width = 60
          Player2.height = 90
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2Kirby.Clicked() == True and Page == "P2Sel":
          Character2 = "Kirby"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Kirby/Kirby.png")
          Player2.img = pygame.transform.scale(Player2.img,(60,70))
          Player2.width = 60
          Player2.height = 70
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)



        if P2Fox.Clicked() == True and Page == "P2Sel":
          Character2 = "Fox"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Fox/Fox.png")
          Player2.img = pygame.transform.scale(Player2.img,(46,87))
          Player2.width = 47
          Player2.height = 87
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2Pikachu.Clicked() == True and Page == "P2Sel":
          Character2 = "Pikachu"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Pikachu/Pikachu.png")
          Player2.img = pygame.transform.scale(Player2.img,(65,73))
          Player2.width = 65
          Player2.height = 73
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2Luigi.Clicked() == True and Page == "P2Sel":
          Character2 = "Luigi"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Luigi/Luigi.png")
          Player2.img = pygame.transform.scale(Player2.img,(42,93))
          Player2.width = 42
          Player2.height = 93
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2CaptainFalcon.Clicked() == True and Page == "P2Sel":
          Character2 = "CaptainFalcon"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/CaptainFalcon/CaptainFalcon.png")
          Player2.img = pygame.transform.scale(Player2.img,(60,96))
          Player2.width = 60
          Player2.height = 96
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2Peach.Clicked() == True and Page == "P2Sel":
          Character2 = "Peach"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Peach/Peach.png")
          Player2.img = pygame.transform.scale(Player2.img,(55,97))
          Player2.width = 55
          Player2.height = 97
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2Bowser.Clicked() == True and Page == "P2Sel":
          Character2 = "Bowser"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Bowser/Bowser.png")
          Player2.img = pygame.transform.scale(Player2.img,(140,140))
          Player2.width = 140
          Player2.height = 140
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2Ganon.Clicked() == True and Page == "P2Sel":
          Character2 = "Ganon"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Ganon/Ganon.png")
          Player2.img = pygame.transform.scale(Player2.img,(107,120))
          Player2.width = 107
          Player2.height = 120
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2Mewtwo.Clicked() == True and Page == "P2Sel":
          Character2 = "Mewtwo"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Mewtwo/Mewtwo.png")
          Player2.img = pygame.transform.scale(Player2.img,(84,105))
          Player2.width = 84
          Player2.height = 105
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2MetaKnight.Clicked() == True and Page == "P2Sel":
          Character2 = "MetaKnight"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/MetaKnight/MetaKnight.png")
          Player2.img = pygame.transform.scale(Player2.img,(70,75))
          Player2.width = 70
          Player2.height = 75
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2Wario.Clicked() == True and Page == "P2Sel":
          Character2 = "Wario"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Wario/Wario.png")
          Player2.img = pygame.transform.scale(Player2.img,(48,90))
          Player2.width = 48
          Player2.height = 90
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2Charizard.Clicked() == True and Page == "P2Sel":
          Character2 = "Charizard"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Charizard/Charizard.png")
          Player2.img = pygame.transform.scale(Player2.img,(108,108))
          Player2.width = 108
          Player2.height = 108
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2DiddyKong.Clicked() == True and Page == "P2Sel":
          Character2 = "DiddyKong"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/DiddyKong/DiddyKong.png")
          Player2.img = pygame.transform.scale(Player2.img,(72,80))
          Player2.width = 72
          Player2.height = 80
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2Sonic.Clicked() == True and Page == "P2Sel":
          Character2 = "Sonic"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Sonic/Sonic.png")
          Player2.img = pygame.transform.scale(Player2.img,(60,88))
          Player2.width = 60
          Player2.height = 88
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2KingDedede.Clicked() == True and Page == "P2Sel":
          Character2 = "KingDedede"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/KingDedede/KingDedede.png")
          Player2.img = pygame.transform.scale(Player2.img,(108,108))
          Player2.width = 108
          Player2.height = 108
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)


        if P2MegaMan.Clicked() == True and Page == "P2Sel":
          Character2 = "MegaMan"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/MegaMan/MegaMan.png")
          Player2.img = pygame.transform.scale(Player2.img,(96,90))
          Player2.width = 96
          Player2.height = 90
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2Greninja.Clicked() == True and Page == "P2Sel":
          Character2 = "Greninja"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Greninja/Greninja.png")
          Player2.img = pygame.transform.scale(Player2.img,(70,70))
          Player2.width = 70
          Player2.height = 70
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        
        if P2PacMan.Clicked() == True and Page == "P2Sel":
          Character2 = "PacMan"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/PacMan/PacMan.png")
          Player2.img = pygame.transform.scale(Player2.img,(60,81))
          Player2.width = 60
          Player2.height = 81
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2Inkling.Clicked() == True and Page == "P2Sel":
          Character2 = "Inkling"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Inkling/Inkling.png")
          Player2.img = pygame.transform.scale(Player2.img,(80,80))
          Player2.width = 80
          Player2.height = 80
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        
        if P2Ridley.Clicked() == True and Page == "P2Sel":
          Character2 = "Ridley"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Ridley/Ridley.png")
          Player2.img = pygame.transform.scale(Player2.img,(169,120))
          Player2.width = 169
          Player2.height = 120
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)


        if P2KingKRool.Clicked() == True and Page == "P2Sel":
          Character2 = "KingKRool"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/KingKRool/KingKRool.png")
          Player2.img = pygame.transform.scale(Player2.img,(105,120))
          Player2.width = 105
          Player2.height = 120
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)


        if P2Banjo.Clicked() == True and Page == "P2Sel":
          Character2 = "Banjo"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Banjo/Banjo.png")
          Player2.img = pygame.transform.scale(Player2.img,(96,96))
          Player2.width = 96
          Player2.height = 96
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        
        if P2Steve.Clicked() == True and Page == "P2Sel":
          Character2 = "Steve"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Steve/Steve.png")
          Player2.img = pygame.transform.scale(Player2.img,(63,85))
          Player2.width = 63
          Player2.height = 85
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)


        if P2Kazuya.Clicked() == True and Page == "P2Sel":
          Character2 = "Kazuya"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Kazuya/Kazuya.png")
          Player2.img = pygame.transform.scale(Player2.img,(80,100))
          Player2.width = 80
          Player2.height = 100
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)


        if P2Waluigi.Clicked() == True and Page == "P2Sel":
          Character2 = "Waluigi"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Waluigi/Waluigi.png")
          Player2.img = pygame.transform.scale(Player2.img,(42,108))
          Player2.width = 42
          Player2.height = 108
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2Tails.Clicked() == True and Page == "P2Sel":
          Character2 = "Tails"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Tails/Tails.png")
          Player2.img = pygame.transform.scale(Player2.img,(75,82))
          Player2.width = 75
          Player2.height = 82
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2Knuckles.Clicked() == True and Page == "P2Sel":
          Character2 = "Knuckles"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Knuckles/Knuckles.png")
          Player2.img = pygame.transform.scale(Player2.img,(94,94))
          Player2.width = 94
          Player2.height = 94
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)


        if P2Eggman.Clicked() == True and Page == "P2Sel":
          Character2 = "Eggman"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Eggman/Eggman.png")
          Player2.img = pygame.transform.scale(Player2.img,(99,117))
          Player2.width = 99
          Player2.height = 117
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)


        if P2Roblox.Clicked() == True and Page == "P2Sel":
          Character2 = "Roblox"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Roblox/Roblox.png")
          Player2.img = pygame.transform.scale(Player2.img,(70,90))
          Player2.width = 70
          Player2.height = 90
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2Sans.Clicked() == True and Page == "P2Sel":
          Character2 = "Sans"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Sans/Sans.png")
          Player2.img = pygame.transform.scale(Player2.img,(85,85))
          Player2.width = 85
          Player2.height = 85
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        if P2Decidueye.Clicked() == True and Page == "P2Sel":
          Character2 = "Decidueye"
          Page = "Stages"      
          Player2.img = pygame.image.load("Assets/Characters/Decidueye/Decidueye.png")
          Player2.img = pygame.transform.scale(Player2.img,(90,96))
          Player2.width = 90
          Player2.height = 96
          Player2.img_flip = pygame.transform.flip(Player2.img, True, False)

        
     #BackgroundSelects
      elif MarioLand.Clicked() == True and Page == "Stages":
        Background = "MarioLand"
        Page = "Game"

      elif Brinstar.Clicked() == True and Page == "Stages":
        Background = "Brinstar"
        Page = "Game"

      elif FinalDestinationSel.Clicked() == True and Page == "Stages":
        Background = "FinalDestination"
        Page = "Game"

      elif GreenHillZoneSel.Clicked() == True and Page == "Stages":
        Background = "GreenHillZone"
        Page = "Game"

    #Replay
      elif Replay.Clicked() == True and Page == "Player1Win" or Page == "Player2Win":
        Page = "P1Sel"
        
        
  #print(Player1.x,Player1.y)
  #print(Player2.x,Player2.y)
    #Title screen
  if Page == "Title":
    #Resets everything
    Player1Hits = False
    Player2Hits = False
    Player1.FacingRight = True
    Player2.FacingRight = True

    Player1.x = 125
    Player1.y = 20

    Player2.x = 700
    Player2.y = 10

    
    Player1HealthWidth = 70
    Player2HealthWidth = 70
    screen.fill((0,50,255))
      
    screen.blit(TitleShadow,(230,50))
    screen.blit(Title,(232,50))
    screen.blit(Play.img,(Play.x,Play.y))
    

    #Player1 Select Screen
  if Page == "P1Sel":
    #Resets everything
    Player1Hits = False
    Player2Hits = False
    Player1.FacingRight = True
    Player2.FacingRight = False

    
    Player1.x = 125
    Player1.y = 30

    Player2.x = 700
    Player2.y = 30
    
    Player1HealthWidth = 100
    Player2HealthWidth = 100



    #Draws stuff
    screen.fill((255,255,255))
    screen.blit(ChooseYourFighterP1Shadow,(330,8))
    screen.blit(ChooseYourFighterP1,(332,8))

    SelectPanel = pygame.Rect(0,75,2000,250)
    pygame.draw.rect(screen,[200,200,200],SelectPanel)

    #Character Selects
    screen.blit(P1Mario.img,(P1Mario.x,P1Mario.y))
    screen.blit(P1DK.img,(P1DK.x,P1DK.y))
    screen.blit(P1Link.img,(P1Link.x,P1Link.y))
    screen.blit(P1Samus.img,(P1Samus.x,P1Samus.y))
    screen.blit(P1Yoshi.img,(P1Yoshi.x,P1Yoshi.y))
    screen.blit(P1Kirby.img,(P1Kirby.x,P1Kirby.y))
    screen.blit(P1Fox.img,(P1Fox.x,P1Fox.y))
    screen.blit(P1Pikachu.img,(P1Pikachu.x,P1Pikachu.y))
    screen.blit(P1Luigi.img,(P1Luigi.x,P1Luigi.y))
    screen.blit(P1CaptainFalcon.img,(P1CaptainFalcon.x,P1CaptainFalcon.y))
    screen.blit(P1Peach.img,(P1Peach.x,P1Peach.y))
    screen.blit(P1Bowser.img,(P1Bowser.x,P1Bowser.y))
    screen.blit(P1Ganon.img,(P1Ganon.x,P1Ganon.y))
    screen.blit(P1Mewtwo.img,(P1Mewtwo.x,P1Mewtwo.y))
    screen.blit(P1MetaKnight.img,(P1MetaKnight.x,P1MetaKnight.y))
    screen.blit(P1Wario.img,(P1Wario.x,P1Wario.y))
    screen.blit(P1Charizard.img,(P1Charizard.x,P1Charizard.y))
    screen.blit(P1DiddyKong.img,(P1DiddyKong.x,P1DiddyKong.y))
    screen.blit(P1Sonic.img,(P1Sonic.x,P1Sonic.y))
    screen.blit(P1KingDedede.img,(P1KingDedede.x,P1KingDedede.y))
    screen.blit(P1MegaMan.img,(P1MegaMan.x,P1MegaMan.y))
    screen.blit(P1Greninja.img,(P1Greninja.x,P1Greninja.y))
    screen.blit(P1PacMan.img,(P1PacMan.x,P1PacMan.y))
    screen.blit(P1Inkling.img,(P1Inkling.x,P1Inkling.y))
    screen.blit(P1Ridley.img,(P1Ridley.x,P1Ridley.y))
    screen.blit(P1KingKRool.img,(P1KingKRool.x,P1KingKRool.y))
    screen.blit(P1Banjo.img,(P1Banjo.x,P1Banjo.y))
    screen.blit(P1Steve.img,(P1Steve.x,P1Steve.y))
    screen.blit(P1Kazuya.img,(P1Kazuya.x,P1Kazuya.y))
    screen.blit(P1Waluigi.img,(P1Waluigi.x,P1Waluigi.y))
    screen.blit(P1Tails.img,(P1Tails.x,P1Tails.y))
    screen.blit(P1Knuckles.img,(P1Knuckles.x,P1Knuckles.y))
    screen.blit(P1Eggman.img,(P1Eggman.x,P1Eggman.y))
    screen.blit(P1Roblox.img,(P1Roblox.x,P1Roblox.y))
    screen.blit(P1Sans.img,(P1Sans.x,P1Sans.y))
    screen.blit(P1Decidueye.img,(P1Decidueye.x,P1Decidueye.y))
      
    #Player2 Select screen
  if Page == "P2Sel":
    screen.fill((255,255,255))
    screen.blit(ChooseYourFighterP1Shadow,(330,8))
    screen.blit(ChooseYourFighterP2,(332,8))

    SelectPanel = pygame.Rect(0,75,2000,250)
    pygame.draw.rect(screen,[200,200,200],SelectPanel)

    SelectPanel = pygame.Rect(0,75,2000,250)
    pygame.draw.rect(screen,[200,200,200],SelectPanel)

      #Character Selects
    screen.blit(P2Mario.img,(P2Mario.x,P2Mario.y))
    screen.blit(P2DK.img,(P2DK.x,P2DK.y))
    screen.blit(P2Link.img,(P2Link.x,P2Link.y))
    screen.blit(P2Samus.img,(P2Samus.x,P2Samus.y))
    screen.blit(P2Yoshi.img,(P2Yoshi.x,P2Yoshi.y))
    screen.blit(P2Kirby.img,(P2Kirby.x,P2Kirby.y))
    screen.blit(P2Fox.img,(P2Fox.x,P2Fox.y))
    screen.blit(P2Pikachu.img,(P2Pikachu.x,P2Pikachu.y))
    screen.blit(P2Luigi.img,(P2Luigi.x,P2Luigi.y))
    screen.blit(P2CaptainFalcon.img,(P2CaptainFalcon.x,P2CaptainFalcon.y))
    screen.blit(P2Peach.img,(P2Peach.x,P2Peach.y))
    screen.blit(P2Bowser.img,(P2Bowser.x,P2Bowser.y))
    screen.blit(P2Ganon.img,(P2Ganon.x,P2Ganon.y))
    screen.blit(P2Mewtwo.img,(P2Mewtwo.x,P2Mewtwo.y))
    screen.blit(P2MetaKnight.img,(P2MetaKnight.x,P2MetaKnight.y))
    screen.blit(P2Wario.img,(P2Wario.x,P2Wario.y))
    screen.blit(P2Charizard.img,(P2Charizard.x,P2Charizard.y))
    screen.blit(P2DiddyKong.img,(P2DiddyKong.x,P2DiddyKong.y))
    screen.blit(P2Sonic.img,(P2Sonic.x,P2Sonic.y))
    screen.blit(P2KingDedede.img,(P2KingDedede.x,P2KingDedede.y))
    screen.blit(P2MegaMan.img,(P2MegaMan.x,P2MegaMan.y))
    screen.blit(P2Greninja.img,(P2Greninja.x,P2Greninja.y))
    screen.blit(P2PacMan.img,(P2PacMan.x,P2PacMan.y))
    screen.blit(P2Inkling.img,(P2Inkling.x,P2Inkling.y))
    screen.blit(P2Ridley.img,(P2Ridley.x,P2Ridley.y))
    screen.blit(P2KingKRool.img,(P2KingKRool.x,P2KingKRool.y))
    screen.blit(P2Banjo.img,(P2Banjo.x,P2Banjo.y))
    screen.blit(P2Steve.img,(P2Steve.x,P2Steve.y))
    screen.blit(P2Kazuya.img,(P2Kazuya.x,P2Kazuya.y))
    screen.blit(P2Waluigi.img,(P2Waluigi.x,P2Waluigi.y))
    screen.blit(P2Tails.img,(P2Tails.x,P2Tails.y))
    screen.blit(P2Knuckles.img,(P2Knuckles.x,P2Knuckles.y))
    screen.blit(P2Eggman.img,(P2Eggman.x,P2Eggman.y))
    screen.blit(P2Roblox.img,(P2Roblox.x,P2Roblox.y))
    screen.blit(P2Sans.img,(P2Sans.x,P2Sans.y))
    screen.blit(P2Decidueye.img,(P2Decidueye.x,P2Decidueye.y))

  if Page == "Stages":
    screen.fill((255,255,255))
    screen.blit(YourStage,(350,0))
      
    SelectPanel = pygame.Rect(0,70,2000,250)
    pygame.draw.rect(screen,[220,220,220],SelectPanel)

    #BackgroundSelects
    screen.blit(MarioLand.img,(MarioLand.x,MarioLand.y))
    screen.blit(Brinstar.img,(Brinstar.x,Brinstar.y))
    screen.blit(FinalDestinationSel.img,(FinalDestinationSel.x,FinalDestinationSel.y))
    screen.blit(GreenHillZoneSel.img,(GreenHillZoneSel.x,GreenHillZoneSel.y))


  if Page == "Game":
    screen.fill((0,0,0))
    Lava = pygame.Rect(0,290,1000,500)
    Water = pygame.Rect(0,290,1000,500)

      #BackgroundLogic(IncludesGround and background)
    if Background == "MarioLand":
      screen.fill((0,255,255))
      Ground.img = pygame.image.load("Assets/Grounds/MarioGround.png")
      Ground.img = pygame.transform.scale(Ground.img,(Ground.width,Ground.height))
      Ground.UpdateHitbox()

    if Background == "Brinstar":
      screen.fill((37,17,6))
      Ground.img = pygame.image.load("Assets/Grounds/BrinstarGround.png")
      Ground.img = pygame.transform.scale(Ground.img,(Ground.width,Ground.height))
      pygame.draw.rect(screen,[255,103,27],Lava)
      Ground.UpdateHitbox()

    if Background == "FinalDestination":
      screen.blit(FinalDestination.img,(FinalDestination.x,FinalDestination.y))
      Ground.img = pygame.image.load("Assets/Grounds/FinalDestinationGround.png")
      Ground.img = pygame.transform.scale(Ground.img,(Ground.width,Ground.height+50))
      Ground.UpdateHitbox()

    if Background == "GreenHillZone":
      screen.fill((0,255,255))
      #screen.blit(PalmTrees.img,(PalmTrees.x,PalmTrees.y))
      pygame.draw.rect(screen,[0,0,255],Water)
      Ground.img = pygame.image.load("Assets/Grounds/GreenHillZoneGround.png")
      Ground.img = pygame.transform.scale(Ground.img,(Ground.width,Ground.height+50))
      Ground.UpdateHitbox()

    #Ground display and draws the player(Image flips as well)
    screen.blit(Ground.img,(Ground.x,Ground.y))
    
    if Player1.FacingRight == True:     
      screen.blit(Player1.img,(Player1.x,Player1.y))
    else:
      screen.blit(Player1.img_flip,(Player1.x,Player1.y))

    if Player2.FacingRight == True:     
      screen.blit(Player2.img,(Player2.x,Player2.y))
    else:
      screen.blit(Player2.img_flip,(Player2.x,Player2.y))


    #Which projectile to display
    if Character1 == "Link":
      ProjectilePlayer1.img = pygame.image.load("Assets/Projectile/Arrow.png")
      ProjectilePlayer1.img = pygame.transform.scale(ProjectilePlayer1.img,(15,18))
      ProjectilePlayer1.img_flip = pygame.transform.flip(ProjectilePlayer1.img, True, False)

    if Character2 == "Link":
      ProjectilePlayer2.img = pygame.image.load("Assets/Projectile/Arrow.png")
      ProjectilePlayer2.img = pygame.transform.scale(ProjectilePlayer2.img,(15,18))
      ProjectilePlayer2.img_flip = pygame.transform.flip(ProjectilePlayer2.img, True, False)


    if Character1 == "Samus":
      ProjectilePlayer1.img = pygame.image.load("Assets/Projectile/Blast.png")
      ProjectilePlayer1.img = pygame.transform.scale(ProjectilePlayer1.img,(15,15))
      ProjectilePlayer1.img_flip = pygame.transform.flip(ProjectilePlayer1.img, True, False)

    if Character2 == "Samus":
      ProjectilePlayer2.img = pygame.image.load("Assets/Projectile/Blast.png")
      ProjectilePlayer2.img = pygame.transform.scale(ProjectilePlayer2.img,(15,15))
      ProjectilePlayer2.img_flip = pygame.transform.flip(ProjectilePlayer2.img, True, False)

    if Character1 == "Pikachu":
      ProjectilePlayer1.img = pygame.image.load("Assets/Projectile/Electricity.png")
      ProjectilePlayer1.img = pygame.transform.scale(ProjectilePlayer1.img,(20,10))
      ProjectilePlayer1.img_flip = pygame.transform.flip(ProjectilePlayer1.img, True, False)

    if Character2 == "Pikachu":
      ProjectilePlayer2.img = pygame.image.load("Assets/Projectile/Electricity.png")
      ProjectilePlayer2.img = pygame.transform.scale(ProjectilePlayer2.img,(20,10))
      ProjectilePlayer2.img_flip = pygame.transform.flip(ProjectilePlayer2.img, True, False)

    if Character1 == "Mewtwo":
      ProjectilePlayer1.img = pygame.image.load("Assets/Projectile/Psycic.png")
      ProjectilePlayer1.img = pygame.transform.scale(ProjectilePlayer1.img,(15,15))
      ProjectilePlayer1.img_flip = pygame.transform.flip(ProjectilePlayer1.img, True, False)

    if Character2 == "Mewtwo":
      ProjectilePlayer2.img = pygame.image.load("Assets/Projectile/Psycic.png")
      ProjectilePlayer2.img = pygame.transform.scale(ProjectilePlayer2.img,(15,15))
      ProjectilePlayer2.img_flip = pygame.transform.flip(ProjectilePlayer2.img, True, False)

    if Character1 == "MegaMan":
      ProjectilePlayer1.img = pygame.image.load("Assets/Projectile/Power.png")
      ProjectilePlayer1.img = pygame.transform.scale(ProjectilePlayer1.img,(25,25))
      ProjectilePlayer1.img_flip = pygame.transform.flip(ProjectilePlayer1.img, True, False)

    if Character2 == "MegaMan":
      ProjectilePlayer2.img = pygame.image.load("Assets/Projectile/Power.png")
      ProjectilePlayer2.img = pygame.transform.scale(ProjectilePlayer2.img,(25,25))
      ProjectilePlayer2.img_flip = pygame.transform.flip(ProjectilePlayer2.img, True, False)


    if Character1 == "Inkling":
      ProjectilePlayer1.img = pygame.image.load("Assets/Projectile/Ink.png")
      ProjectilePlayer1.img = pygame.transform.scale(ProjectilePlayer1.img,(25,25))
      ProjectilePlayer1.img_flip = pygame.transform.flip(ProjectilePlayer1.img, True, False)

    if Character2 == "Inkling":
      ProjectilePlayer2.img = pygame.image.load("Assets/Projectile/Ink.png")
      ProjectilePlayer2.img = pygame.transform.scale(ProjectilePlayer2.img,(25,25))
      ProjectilePlayer2.img_flip = pygame.transform.flip(ProjectilePlayer2.img, True, False)


    if Character1 == "Roblox":
      ProjectilePlayer1.img = pygame.image.load("Assets/Projectile/RobloxGreenProjectile.png")
      ProjectilePlayer1.img = pygame.transform.scale(ProjectilePlayer1.img,(25,25))
      ProjectilePlayer1.img_flip = pygame.transform.flip(ProjectilePlayer1.img, True, False)

    if Character2 == "Roblox":
      ProjectilePlayer2.img = pygame.image.load("Assets/Projectile/RobloxGreenProjectile.png")
      ProjectilePlayer2.img = pygame.transform.scale(ProjectilePlayer2.img,(25,25))
      ProjectilePlayer2.img_flip = pygame.transform.flip(ProjectilePlayer2.img, True, False)



    if Character1 == "Sans":
      ProjectilePlayer1.img = pygame.image.load("Assets/Projectile/Power.png")
      ProjectilePlayer1.img = pygame.transform.scale(ProjectilePlayer1.img,(25,25))
      ProjectilePlayer1.img_flip = pygame.transform.flip(ProjectilePlayer1.img, True, False)

    if Character2 == "Sans":
      ProjectilePlayer2.img = pygame.image.load("Assets/Projectile/Power.png")
      ProjectilePlayer2.img = pygame.transform.scale(ProjectilePlayer2.img,(25,25))
      ProjectilePlayer2.img_flip = pygame.transform.flip(ProjectilePlayer2.img, True, False)

    
    if Character1 == "Decidueye":
      ProjectilePlayer1.img = pygame.image.load("Assets/Projectile/Feather.png")
      ProjectilePlayer1.img = pygame.transform.scale(ProjectilePlayer1.img,(20,14))
      ProjectilePlayer1.img_flip = pygame.transform.flip(ProjectilePlayer1.img, True, False)

    if Character2 == "Decidueye":
      ProjectilePlayer2.img = pygame.image.load("Assets/Projectile/Feather.png")
      ProjectilePlayer2.img = pygame.transform.scale(ProjectilePlayer2.img,(20,14))
      ProjectilePlayer2.img_flip = pygame.transform.flip(ProjectilePlayer2.img, True, False)
      

    if P1Projectile == True:
      
      #Checks the direction the projectile should go
  
      if ProjectilePlayer1.FacingRight == True:
        ProjectilePlayer1.vx = 5
        screen.blit(ProjectilePlayer1.img,(ProjectilePlayer1.x,Player1.y+30))
      if ProjectilePlayer1.FacingRight == False:
        ProjectilePlayer1.vx = -5
        screen.blit(ProjectilePlayer1.img_flip,(ProjectilePlayer1.x,Player1.y+30))
    
        
      if ProjectilePlayer1.x > 700 or ProjectilePlayer1.x < 0:
        P1Projectile = False
    if P1Projectile == False:
      ProjectilePlayer1.x = Player1.x
      ProjectilePlayer1.y = Player1.y#+50

    if P2Projectile == True:

      if ProjectilePlayer2.FacingRight == True:
        ProjectilePlayer2.vx = 5
        screen.blit(ProjectilePlayer2.img,(ProjectilePlayer2.x,Player2.y+30))
      if ProjectilePlayer2.FacingRight == False:
        ProjectilePlayer2.vx = -5
        screen.blit(ProjectilePlayer2.img_flip,(ProjectilePlayer2.x,Player2.y+30))
      
      if ProjectilePlayer2.x > 700 or ProjectilePlayer2.x < 0:
        P2Projectile = False
    if P2Projectile == False:
      ProjectilePlayer2.x = Player2.x
      ProjectilePlayer2.y = Player2.y#+50
    

    #Gravity for player 1
    collide_platform = False
    CollisionGround(Player1,Ground)
    collide_platform = True in Player1.collision
  
    if collide_platform == False:
      Player1.InAir = True
  
    if Player1.InAir == True:
      Player1.vy = Player1.vy + Gravity
    Player1.y += Player1.vy

    #Gravity for player 2
    collide_platform = False
    CollisionGround(Player2,Ground)
    collide_platform = True in Player2.collision
  
    if collide_platform == False:
      Player2.InAir = True
  
    if Player2.InAir == True:
      Player2.vy = Player2.vy + Gravity
    Player2.y += Player2.vy

    
    #Health
    screen.blit(P1HP,(117,0))
    Player1Damage = pygame.Rect(100,25,100,15)
    Player1Health = pygame.Rect(100,25,Player1HealthWidth,15)
    pygame.draw.rect(screen,[255,0,0],Player1Damage)
    pygame.draw.rect(screen,[0,155,0],Player1Health)

    screen.blit(P2HP,(700,0))
    Player2Damage = pygame.Rect(680,25,100,15)
    Player2Health = pygame.Rect(680,25,Player2HealthWidth,15)
    pygame.draw.rect(screen,[255,0,0],Player2Damage)
    pygame.draw.rect(screen,[0,155,0],Player2Health)

    #Collisions with other players attacking
    Player1.check_collision(Player2.hitbox)
    for i in range(len(Player1.collision)):
      if Player1.collision[i] and Player1Hits == True:
        if Player1.FacingRight == True:
          Player2.x += 5
          Player2.y -=5
        elif Player1.FacingRight == False:
          Player2.x -= 5
          Player2.y -= 5
          
    Player2.check_collision(Player1.hitbox)
    for i in range(len(Player2.collision)):
      if Player2.collision[i] and Player2Hits == True:
        if Player2.FacingRight == True:
          Player1.x += 5
          Player1.y -=5
        elif Player2.FacingRight == False:
          Player1.x -= 5
          Player1.y -= 5

    #Collisions between players when not attacking
    Player1.check_collision(Player2.hitbox)
    if Player1.collision[8]:
      Player1.vx = 0
      if Player1.collision[5]:
        Player1.x -= 2
      if Player1.collision[4]:
        Player1.x += 2
    elif Player1.collision[7]:
      Player1.vy = -2
          
    Player2.check_collision(Player1.hitbox)
    if Player2.collision[8]:
      Player2.vx = 0
      if Player2.collision[5]:
        Player2.x -= 2
      if Player2.collision[4]:
        Player2.x += 2
    elif Player2.collision[7]:
      Player2.vy = -2

       

    #Collisions with projectiles
    Player1.check_collision(ProjectilePlayer2.hitbox)
    for i in range(len(Player1.collision)):
      if Player1.collision[i] and P2Projectile == True:
        Player1HealthWidth -= 1
        P2Projectile = False

    Player2.check_collision(ProjectilePlayer1.hitbox)
    for i in range(len(Player2.collision)):
      if Player2.collision[i] and P1Projectile == True:
        Player2HealthWidth -= 1
        P1Projectile = False
      
    #To tell which player is which
    #screen.blit(P1,(Player1.x,Player1.y - 20))
    #screen.blit(P2,(Player2.x,Player2.y - 20))
    #if a player falls down
    if Player1.y >= 250:
      Player1HealthWidth = 0
    elif Player2.y >= 250:
      Player2HealthWidth = 0
    #Checks who wins
    if Player2HealthWidth <= 0:
      Page = "Player1Win"
    elif Player1HealthWidth <= 0:
      Page = "Player2Win"

  if Page == "Player1Win":
    screen.fill((50,50,50))
    screen.blit(Player1Wins,(350,50))
    screen.blit(Replay.img,(Replay.x,Replay.y))

  if Page == "Player2Win":
    screen.fill((50,50,50))
    screen.blit(Player2Wins,(350,50))
    screen.blit(Replay.img,(Replay.x,Replay.y))

      
    #Renders everything
  pygame.display.flip()


#At the end of the loop, pygame will quit
pygame.quit()
