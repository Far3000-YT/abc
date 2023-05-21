import random
import time
import colorama
from characters import *
#Importing what we defined from the characters.py file

colorama.init() #I initialize the module or it will not work

class waves:
    def __init__(self):
        #Im gonan use colors in the terminal to see more easily the actions done in the party
        self.blue = colorama.Fore.BLUE
        self.red = colorama.Fore.RED
        self.yellow = colorama.Fore.YELLOW
        self.green = colorama.Fore.GREEN
        self.white = colorama.Fore.WHITE

    def wave1(self):
        self.villain1, self.villain2, self.villain3 = characters.troll1, characters.troll2, characters.troll3
        self.villains = [self.villain1, self.villain2, self.villain3]
        self.warrior, self.hunter, self.mage, self.healer = characters.warrior, characters.hunter, characters.mage, characters.healer
        self.heroes = [self.warrior, self.hunter, self.mage, self.healer]
        self.arrows_num = 5

        print(self.white + "\nFight Start - Wave Number 1")
        
        while self.villains:
            #WARRIOR ATTACK ON RANDOM TROLL
            if self.warrior not in self.heroes:
                pass
            else:
                self.villain_choice = random.choice(self.villains)
                self.warrior_ad = random.randint(0,5)
                self.villain_choice['lp'] -= self.warrior_ad
                print(self.blue + f"The Warrior attacked a troll and dealt {self.warrior_ad} damages. The troll is now {self.villain_choice['lp']} HP")
                time.sleep(0.2)

                if self.villain_choice['lp'] <= 0:
                    self.villains.remove(self.villain_choice)
                    print(self.yellow + "A troll died !")
                    time.sleep(0.2)
                    if len(self.villains) == 0:
                        print(self.yellow + "All the trolls died !")
                        break
            
                #TROLL ATTACK ON WARRIOR  / REVERSE 1
                self.villain_ad = random.randint(0,4)
                self.warrior["lp"] -= self.villain_ad
                print(self.red + f"A Troll attacked the Warrior and dealt {self.villain_ad} damages. The Warrior is now {self.warrior['lp']} HP")
                time.sleep(0.2)

                if self.warrior["lp"] <= 0:
                    self.heroes.remove(self.warrior)
                    print(self.yellow + "The warrior died !")
                    time.sleep(0.2)
                    if len(self.heroes) == 0:
                        print(self.yellow + "All the heroes are down !")
                        break

            #HUNTER ATTACK ON RANDOM TROLL
            if self.hunter not in self.heroes:
                pass
            else:
                self.arrows_num -= 1
                self.villain_choice = random.choice(self.villains)
                if self.arrows_num >= 1:
                    self.hunter_ad = random.randint(0,3)
                else:
                    self.arrows_num = 1
                    self.hunter_ad = random.randint(0,1)

                self.villain_choice["lp"] -= self.hunter_ad
                print(self.blue + f"The Hunter attacked a troll and dealt {self.hunter_ad} damages. The troll is now {self.villain_choice['lp']} HP")
                time.sleep(0.2)

                if self.villain_choice["lp"] <= 0:
                    print(self.yellow + "A troll died !")
                    time.sleep(0.2)
                    self.villains.remove(self.villain_choice)
                    if len(self.villains) == 0:
                        print(self.yellow + "All the trolls died !")
                        break
                
                #TROLL ATTACK ON HUNTER / REVERSE 2
                self.villain_ad = random.randint(0,2)
                self.hunter["lp"] -= self.villain_ad
                print(self.red + f"A Troll attacked the Hunter and dealt {self.villain_ad} damages. The Hunter is now {self.hunter['lp']} HP")
                time.sleep(0.2)

                if self.hunter["lp"] <= 0:
                    self.heroes.remove(self.hunter)
                    print(self.yellow + "The hunter died !")
                    time.sleep(0.2)
                    if len(self.heroes) == 0:
                        print(self.yellow + "All the heroes are down !")
                        break
            
            #HEALER HEAL ON RANDOM ALLY
            if self.healer not in self.heroes:
                pass
            else:
                self.hero_choice = random.choice(self.heroes)
                self.hero_choice["lp"] += self.healer["hp"]
                print(self.green + f"The healer healed the {self.hero_choice['name']} for {self.healer['hp']} HP")
                time.sleep(0.2)

                #HEALER DAMAGE ON RANDOM TROLL
                self.villain_choice = random.choice(self.villains)
                self.healer_ad = random.randint(0,1)
                self.villain_choice['lp'] -= self.healer_ad
                print(self.blue + f"The Healer attacked a troll and dealt {self.healer_ad} damages. The troll is now {self.villain_choice['lp']} HP")
                time.sleep(0.2)

                if self.villain_choice["lp"] <= 0:
                    print(self.yellow + "A troll died !")
                    time.sleep(0.2)
                    self.villains.remove(self.villain_choice)
                    if len(self.villains) == 0:
                        print(self.yellow + "All the trolls died !")
                        break

                #TROLL ATTACK ON HEALER / REVERSE 3
                self.villain_ad = random.randint(0,4)
                self.healer["lp"] -= self.villain_ad
                print(self.red + f"A Troll attacked the Healer and dealt {self.villain_ad} damages. The Healer is now {self.healer['lp']} HP")
                time.sleep(0.2)

                if self.healer["lp"] <= 0:
                    self.heroes.remove(self.healer)
                    print(self.yellow + "The healer died !")
                    time.sleep(0.2)
                    if len(self.heroes) == 0:
                        print(self.yellow + "All the heroes are down !")
                        break

            #MAGE DAMAGE ON RANDOM TROLL THEN ALL THE OTHER TROLLS FOR AT MAX 2 DAMAGES
            if self.mage not in self.heroes:
                pass
            else:
                self.villain_choice = random.choice(self.villains)
                self.mage_ad = random.randint(0,4)
                self.mage_ad_2 = random.randint(0,2)

                choice2 = 0
                choice = random.randint(0, len(self.villains))

                for villain in self.villains:
                    choice2 += 1
                    if choice2 == choice:
                        villain["lp"] -= self.mage_ad
                        print(self.blue + f"The Mage attacked a troll and dealt {self.mage_ad} damages. The troll is now {self.villain_choice['lp']} HP")
                        time.sleep(0.2)
                    else:
                        villain["lp"] -= self.mage_ad_2
                        print(self.blue + f"The Mage attacked a troll and dealt {self.mage_ad_2} damages. The troll is now {self.villain_choice['lp']} HP")
                        time.sleep(0.2)

                if self.villain_choice["lp"] <= 0:
                    self.villains.remove(self.villain_choice)
                    print(self.yellow + "A troll died !")
                    time.sleep(0.2)
                    if len(self.villains) == 0:
                        print(self.yellow + "All the trolls died !")
                        break
                
                #TROLL ATTACK ON MAGE / REVERSE 4
                self.villain_ad = random.randint(0,4)
                self.mage["lp"] -= self.villain_ad
                print(self.red + f"A Troll attacked the Mage and dealt {self.villain_ad} damages. The Mage is now {self.healer['lp']} HP")
                time.sleep(0.2)

                if self.mage["lp"] <= 0:
                    self.heroes.remove(self.mage)
                    print("The mage died !")
                    time.sleep(0.2)
                    if len(self.heroes) == 0:
                        print("All the heroes are down !")
                        break

    def wave2(self):
        self.villain1, self.villain2, self.villain3, self.villain4 = characters.troll1, characters.troll2, characters.troll3, characters.troll4
        self.villains = [self.villain1, self.villain2, self.villain3, self.villain4]
        self.warrior, self.hunter, self.mage, self.healer = self.warrior, self.hunter, self.mage, self.healer
        self.heroes = self.heroes
        self.arrows_num = 5

        print(self.white + "\nFight Start - Wave Number 2")
        
        while self.villains:
            #WARRIOR ATTACK ON RANDOM TROLL
            if self.warrior not in self.heroes:
                pass
            else:
                self.villain_choice = random.choice(self.villains)
                self.warrior_ad = random.randint(0,5)
                self.villain_choice['lp'] -= self.warrior_ad
                print(self.blue + f"The Warrior attacked a troll and dealt {self.warrior_ad} damages. The troll is now {self.villain_choice['lp']} HP")
                time.sleep(0.2)

                if self.villain_choice['lp'] <= 0:
                    self.villains.remove(self.villain_choice)
                    print(self.yellow + "A troll died !")
                    time.sleep(0.2)
                    if len(self.villains) == 0:
                        print(self.yellow + "All the trolls died !")
                        break
            
                #TROLL ATTACK ON WARRIOR  / REVERSE 1
                self.villain_ad = random.randint(0,4)
                self.warrior["lp"] -= self.villain_ad
                print(self.red + f"A Troll attacked the Warrior and dealt {self.villain_ad} damages. The Warrior is now {self.warrior['lp']} HP")
                time.sleep(0.2)

                if self.warrior["lp"] <= 0:
                    self.heroes.remove(self.warrior)
                    print(self.yellow + "The warrior died !")
                    time.sleep(0.2)
                    if len(self.heroes) == 0:
                        print(self.yellow + "All the heroes are down !")
                        break

            #HUNTER ATTACK ON RANDOM TROLL
            if self.hunter not in self.heroes:
                pass
            else:
                self.arrows_num -= 1
                self.villain_choice = random.choice(self.villains)
                if self.arrows_num >= 1:
                    self.hunter_ad = random.randint(0,3)
                else:
                    self.arrows_num = 1
                    self.hunter_ad = random.randint(0,1)

                self.villain_choice["lp"] -= self.hunter_ad
                print(self.blue + f"The Hunter attacked a troll and dealt {self.hunter_ad} damages. The troll is now {self.villain_choice['lp']} HP")
                time.sleep(0.2)

                if self.villain_choice["lp"] <= 0:
                    print(self.yellow + "A troll died !")
                    time.sleep(0.2)
                    self.villains.remove(self.villain_choice)
                    if len(self.villains) == 0:
                        print(self.yellow + "All the trolls died !")
                        break
                
                #TROLL ATTACK ON HUNTER / REVERSE 2
                self.villain_ad = random.randint(0,2)
                self.hunter["lp"] -= self.villain_ad
                print(self.red + f"A Troll attacked the Hunter and dealt {self.villain_ad} damages. The Hunter is now {self.hunter['lp']} HP")
                time.sleep(0.2)

                if self.hunter["lp"] <= 0:
                    self.heroes.remove(self.hunter)
                    print(self.yellow + "The hunter died !")
                    time.sleep(0.2)
                    if len(self.heroes) == 0:
                        print(self.yellow + "All the heroes are down !")
                        break
            
            #HEALER HEAL ON RANDOM ALLY
            if self.healer not in self.heroes:
                pass
            else:
                self.hero_choice = random.choice(self.heroes)
                self.hero_choice["lp"] += self.healer["hp"]
                print(self.green + f"The healer healed the {self.hero_choice['name']} for {self.healer['hp']} HP")
                time.sleep(0.2)

                #HEALER DAMAGE ON RANDOM TROLL
                self.villain_choice = random.choice(self.villains)
                self.healer_ad = random.randint(0,1)
                self.villain_choice['lp'] -= self.healer_ad
                print(self.blue + f"The Healer attacked a troll and dealt {self.healer_ad} damages. The troll is now {self.villain_choice['lp']} HP")
                time.sleep(0.2)

                if self.villain_choice["lp"] <= 0:
                    print(self.yellow + "A troll died !")
                    time.sleep(0.2)
                    self.villains.remove(self.villain_choice)
                    if len(self.villains) == 0:
                        print(self.yellow + "All the trolls died !")
                        break

                #TROLL ATTACK ON HEALER / REVERSE 3
                self.villain_ad = random.randint(0,4)
                self.healer["lp"] -= self.villain_ad
                print(self.red + f"A Troll attacked the Healer and dealt {self.villain_ad} damages. The Healer is now {self.healer['lp']} HP")
                time.sleep(0.2)

                if self.healer["lp"] <= 0:
                    self.heroes.remove(self.healer)
                    print(self.yellow + "The healer died !")
                    time.sleep(0.2)
                    if len(self.heroes) == 0:
                        print(self.yellow + "All the heroes are down !")
                        break

            #MAGE DAMAGE ON RANDOM TROLL THEN ALL THE OTHER TROLLS FOR AT MAX 2 DAMAGES
            if self.mage not in self.heroes:
                pass
            else:
                self.villain_choice = random.choice(self.villains)
                self.mage_ad = random.randint(0,4)
                self.mage_ad_2 = random.randint(0,2)

                choice2 = 0
                choice = random.randint(0, len(self.villains))

                for villain in self.villains:
                    choice2 += 1
                    if choice2 == choice:
                        villain["lp"] -= self.mage_ad
                        print(self.blue + f"The Mage attacked a troll and dealt {self.mage_ad} damages. The troll is now {self.villain_choice['lp']} HP")
                        time.sleep(0.2)
                    else:
                        villain["lp"] -= self.mage_ad_2
                        print(self.blue + f"The Mage attacked a troll and dealt {self.mage_ad_2} damages. The troll is now {self.villain_choice['lp']} HP")
                        time.sleep(0.2)

                if self.villain_choice["lp"] <= 0:
                    self.villains.remove(self.villain_choice)
                    print(self.yellow + "A troll died !")
                    time.sleep(0.2)
                    if len(self.villains) == 0:
                        print(self.yellow + "All the trolls died !")
                        break
                
                #TROLL ATTACK ON MAGE / REVERSE 4
                self.villain_ad = random.randint(0,4)
                self.mage["lp"] -= self.villain_ad
                print(self.red + f"A Troll attacked the Mage and dealt {self.villain_ad} damages. The Mage is now {self.healer['lp']} HP")
                time.sleep(0.2)

                if self.mage["lp"] <= 0:
                    self.heroes.remove(self.mage)
                    print("The mage died !")
                    time.sleep(0.2)
                    if len(self.heroes) == 0:
                        print("All the heroes are down !")
                        break
    
    def wave3(self):
        self.villain1, self.villain2, self.villain3, self.villain4, self.villain5 = characters.troll1, characters.troll2, characters.troll3, characters.troll4, characters.troll5
        self.villains = [self.villain1, self.villain2, self.villain3, self.villain4, self.villain5]
        self.warrior, self.hunter, self.mage, self.healer = self.warrior, self.hunter, self.mage, self.healer
        self.heroes = self.heroes
        self.arrows_num = 5

        print(self.white + "\nFight Start - Wave Number 3")
        
        while self.villains:
            #WARRIOR ATTACK ON RANDOM TROLL
            if self.warrior not in self.heroes:
                pass
            else:
                self.villain_choice = random.choice(self.villains)
                self.warrior_ad = random.randint(0,5)
                self.villain_choice['lp'] -= self.warrior_ad
                print(self.blue + f"The Warrior attacked a troll and dealt {self.warrior_ad} damages. The troll is now {self.villain_choice['lp']} HP")
                time.sleep(0.2)

                if self.villain_choice['lp'] <= 0:
                    self.villains.remove(self.villain_choice)
                    print(self.yellow + "A troll died !")
                    time.sleep(0.2)
                    if len(self.villains) == 0:
                        print(self.yellow + "All the trolls died !")
                        break
            
                #TROLL ATTACK ON WARRIOR  / REVERSE 1
                self.villain_ad = random.randint(0,4)
                self.warrior["lp"] -= self.villain_ad
                print(self.red + f"A Troll attacked the Warrior and dealt {self.villain_ad} damages. The Warrior is now {self.warrior['lp']} HP")
                time.sleep(0.2)

                if self.warrior["lp"] <= 0:
                    self.heroes.remove(self.warrior)
                    print(self.yellow + "The warrior died !")
                    time.sleep(0.2)
                    if len(self.heroes) == 0:
                        print(self.yellow + "All the heroes are down !")
                        break

            #HUNTER ATTACK ON RANDOM TROLL
            if self.hunter not in self.heroes:
                pass
            else:
                self.arrows_num -= 1
                self.villain_choice = random.choice(self.villains)
                if self.arrows_num >= 1:
                    self.hunter_ad = random.randint(0,3)
                else:
                    self.arrows_num = 1
                    self.hunter_ad = random.randint(0,1)

                self.villain_choice["lp"] -= self.hunter_ad
                print(self.blue + f"The Hunter attacked a troll and dealt {self.hunter_ad} damages. The troll is now {self.villain_choice['lp']} HP")
                time.sleep(0.2)

                if self.villain_choice["lp"] <= 0:
                    print(self.yellow + "A troll died !")
                    time.sleep(0.2)
                    self.villains.remove(self.villain_choice)
                    if len(self.villains) == 0:
                        print(self.yellow + "All the trolls died !")
                        break
                
                #TROLL ATTACK ON HUNTER / REVERSE 2
                self.villain_ad = random.randint(0,2)
                self.hunter["lp"] -= self.villain_ad
                print(self.red + f"A Troll attacked the Hunter and dealt {self.villain_ad} damages. The Hunter is now {self.hunter['lp']} HP")
                time.sleep(0.2)

                if self.hunter["lp"] <= 0:
                    self.heroes.remove(self.hunter)
                    print(self.yellow + "The hunter died !")
                    time.sleep(0.2)
                    if len(self.heroes) == 0:
                        print(self.yellow + "All the heroes are down !")
                        break
            
            #HEALER HEAL ON RANDOM ALLY
            if self.healer not in self.heroes:
                pass
            else:
                self.hero_choice = random.choice(self.heroes)
                self.hero_choice["lp"] += self.healer["hp"]
                print(self.green + f"The healer healed the {self.hero_choice['name']} for {self.healer['hp']} HP")
                time.sleep(0.2)

                #HEALER DAMAGE ON RANDOM TROLL
                self.villain_choice = random.choice(self.villains)
                self.healer_ad = random.randint(0,1)
                self.villain_choice['lp'] -= self.healer_ad
                print(self.blue + f"The Healer attacked a troll and dealt {self.healer_ad} damages. The troll is now {self.villain_choice['lp']} HP")
                time.sleep(0.2)

                if self.villain_choice["lp"] <= 0:
                    print(self.yellow + "A troll died !")
                    time.sleep(0.2)
                    self.villains.remove(self.villain_choice)
                    if len(self.villains) == 0:
                        print(self.yellow + "All the trolls died !")
                        break

                #TROLL ATTACK ON HEALER / REVERSE 3
                self.villain_ad = random.randint(0,4)
                self.healer["lp"] -= self.villain_ad
                print(self.red + f"A Troll attacked the Healer and dealt {self.villain_ad} damages. The Healer is now {self.healer['lp']} HP")
                time.sleep(0.2)

                if self.healer["lp"] <= 0:
                    self.heroes.remove(self.healer)
                    print(self.yellow + "The healer died !")
                    time.sleep(0.2)
                    if len(self.heroes) == 0:
                        print(self.yellow + "All the heroes are down !")
                        break

            #MAGE DAMAGE ON RANDOM TROLL THEN ALL THE OTHER TROLLS FOR AT MAX 2 DAMAGES
            if self.mage not in self.heroes:
                pass
            else:
                self.villain_choice = random.choice(self.villains)
                self.mage_ad = random.randint(0,4)
                self.mage_ad_2 = random.randint(0,2)

                choice2 = 0
                choice = random.randint(0, len(self.villains))

                for villain in self.villains:
                    choice2 += 1
                    if choice2 == choice:
                        villain["lp"] -= self.mage_ad
                        print(self.blue + f"The Mage attacked a troll and dealt {self.mage_ad} damages. The troll is now {self.villain_choice['lp']} HP")
                        time.sleep(0.2)
                    else:
                        villain["lp"] -= self.mage_ad_2
                        print(self.blue + f"The Mage attacked a troll and dealt {self.mage_ad_2} damages. The troll is now {self.villain_choice['lp']} HP")
                        time.sleep(0.2)

                if self.villain_choice["lp"] <= 0:
                    self.villains.remove(self.villain_choice)
                    print(self.yellow + "A troll died !")
                    time.sleep(0.2)
                    if len(self.villains) == 0:
                        print(self.yellow + "All the trolls died !")
                        break
                
                #TROLL ATTACK ON MAGE / REVERSE 4
                self.villain_ad = random.randint(0,4)
                self.mage["lp"] -= self.villain_ad
                print(self.red + f"A Troll attacked the Mage and dealt {self.villain_ad} damages. The Mage is now {self.healer['lp']} HP")
                time.sleep(0.2)

                if self.mage["lp"] <= 0:
                    self.heroes.remove(self.mage)
                    print("The mage died !")
                    time.sleep(0.2)
                    if len(self.heroes) == 0:
                        print("All the heroes are down !")
                        break

    def wave_drag(self):
        self.dragon = characters.dragon
        print(self.white + "\nFinal Wave - The Dragon")

        #A RANDOM HERO ATTACKS THE DRAGON, THEN THE DRAGON DEALS DAMAGES TO THE ENNEMIES (up to 6 to the one that attacked the dragon, and up to 2 to all the other ones)
        while self.heroes:
            self.dragon_ad1 = random.randint(0,6)
            if len(self.heroes) == 1:
                self.hero_choice = self.heroes[0]
            else:
                self.hero_choice = random.choice(self.heroes)

            for hero in self.heroes:
                if hero == self.hero_choice:
                    if hero["name"] == "Warrior":
                        self.hero_ad = random.randint(0,5)
                        self.dragon["lp"] -= self.hero_ad
                        print(self.blue + f"The Warrior attacked The Dragon and dealt {self.hero_ad} damages. The Dragon is now {self.dragon['lp']} HP")
                        time.sleep(0.2)

                        if self.dragon['lp'] <= 0:
                            print(self.yellow + "The Dragon Died !")
                            time.sleep(0.2)
                            break

                        hero["lp"] -= self.dragon_ad1
                        print(self.red + f"The Dragon attacked The Warrior and dealt {self.dragon_ad1} damages. The Warrior is now {self.warrior['lp']} HP")
                        time.sleep(0.2)

                        if len(self.heroes) == 0:
                            print(self.yellow + "All the heroes died ! END OF THE GAME")
                            break
                        else:
                            if hero['lp'] <= 0:
                                print(self.yellow + f"The {hero['name']} died !")
                                self.heroes.remove(hero)
                                time.sleep(0.2)

                    elif hero["name"] == "Hunter":
                        self.hero_ad = random.randint(0,3)
                        self.dragon["lp"] -= self.hero_ad
                        print(self.blue + f"The Hunter attacked The Dragon and dealt {self.hero_ad} damages. The Dragon is now {self.dragon['lp']} HP")
                        time.sleep(0.2)

                        if self.dragon['lp'] <= 0:
                            print(self.yellow + "The Dragon Died !")
                            time.sleep(0.2)
                            break

                        hero["lp"] -= self.dragon_ad1
                        print(self.red + f"The Dragon attacked The Hunter and dealt {self.dragon_ad1} damages. The Hunter is now {self.hunter['lp']} HP")
                        time.sleep(0.2)

                        if len(self.heroes) == 0:
                            print(self.yellow + "All the heroes died ! END OF THE GAME")
                            break
                        else:
                            if hero['lp'] <= 0:
                                print(self.yellow + f"The {hero['name']} died !")
                                self.heroes.remove(hero)
                                time.sleep(0.2)

                    elif hero["name"] == "Healer":
                        self.hero_ad = random.randint(0,1)
                        self.dragon["lp"] -= self.hero_ad
                        print(self.blue + f"The Healer attacked The Dragon and dealt {self.hero_ad} damages. The Dragon is now {self.dragon['lp']} HP")
                        time.sleep(0.2)

                        if self.dragon['lp'] <= 0:
                            print(self.yellow + "The Dragon Died !")
                            time.sleep(0.2)
                            break

                        hero["lp"] -= self.dragon_ad1
                        print(self.red + f"The Dragon attacked The Healer and dealt {self.dragon_ad1} damages. The Healer is now {self.healer['lp']} HP")
                        time.sleep(0.2)

                        if len(self.heroes) == 0:
                            print(self.yellow + "All the heroes died ! END OF THE GAME")
                            break
                        else:
                            if hero['lp'] <= 0:
                                print(self.yellow + f"The {hero['name']} died !")
                                self.heroes.remove(hero)
                                time.sleep(0.2)

                    elif hero["name"] == "Mage":
                        self.hero_ad = random.randint(0,4)
                        self.dragon["lp"] -= self.hero_ad
                        print(self.blue + f"The Mage attacked The Dragon and dealt {self.hero_ad} damages. The Dragon is now {self.dragon['lp']} HP")
                        time.sleep(0.2)

                        if self.dragon['lp'] <= 0:
                            print(self.yellow + "The Dragon Died !")
                            time.sleep(0.2)
                            break

                        hero["lp"] -= self.dragon_ad1
                        print(self.red + f"The Dragon attacked The Mage and dealt {self.dragon_ad1} damages. The Mage is now {self.mage['lp']} HP")
                        time.sleep(0.2)

                        if len(self.heroes) == 0:
                            print(self.yellow + "All the heroes died ! END OF THE GAME")
                            break
                        else:
                            if hero['lp'] <= 0:
                                print(self.yellow + f"The {hero['name']} died !")
                                self.heroes.remove(hero)
                                time.sleep(0.2)

                else:
                    self.dragon_ad2 = random.randint(0,2)
                    hero["lp"] -= self.dragon_ad2
                    print(self.red + f"The Dragon attacked the {hero['name']} and dealt {self.dragon_ad2} damages. The {hero['name']} is now {hero['lp']} HP")
                    time.sleep(0.2)

                    if len(self.heroes) == 0:
                            print(self.yellow + "All the heroes died ! END OF THE GAME")
                            break
                    else:
                        if hero['lp'] <= 0:
                            print(self.yellow + f"The {hero['name']} died !")
                            self.heroes.remove(hero)
                            time.sleep(0.2)
        if len(self.heroes) == 0:
            print(self.yellow + "All the heroes died ! END OF THE GAME")
        else:
            pass


run = waves()
run.wave1()
run.wave2()
run.wave3()
run.wave_drag()