import pygame
import player


class DefaultTeam:
    def __init__ (self, name, offense, defense, goalie, scorebug, selectImage, overall):
        self.name = name
        self.offense = offense
        self.defense = defense
        self.goalie = goalie
        self.scorebug = scorebug
        self.selectImage = selectImage
        self.overall = overall #will be calculated by players later

def createAll():
    ala = DefaultTeam("Alaskan Thunder",player.andyLevyFF,"andy",player.rickyNoviaFG, pygame.image.load("assets/images/alaSB.png"), pygame.image.load("assets/images/alaPN.png"), 6)
    ame = DefaultTeam("American Revolution",player.mikeyPapaOF,"andy",player.mikeMarottaOG, pygame.image.load("assets/images/ameSB.png"), pygame.image.load("assets/images/amePN.png"), 7)
    bbw = DefaultTeam("Boondock Beluga Whales","bob","andy","ricky", pygame.image.load("assets/images/bbwSB.png"), pygame.image.load("assets/images/bbwPN.png"), 6)
    flo = DefaultTeam("Florida Tropics","bob","andy","ricky", pygame.image.load("assets/images/floSB.png"), pygame.image.load("assets/images/floPN.png"), 7)
    smc = DefaultTeam("Smashville Chippewas","bob","andy","ricky", pygame.image.load("assets/images/smcSB.png"), pygame.image.load("assets/images/smcPN.png"), 7)
    sss = DefaultTeam("Southside Spartans","bob","andy","ricky", pygame.image.load("assets/images/sssSB.png"), pygame.image.load("assets/images/sssPN.png"), 7)
    teams = [ala, ame, bbw, flo, smc, sss]
    return teams