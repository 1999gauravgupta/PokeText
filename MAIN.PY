import random
import pickle
import string 
################################           FUNCTIONS             ##################################
def home():
    print"""
                                              PARK

                  
        POKEMART                                                            GYMS


                                         POKE LEAGUE"""
    move=raw_input("Enter your preffered direction of moving:")
    if move=="w":
        park()
    if move=="a":
        pokemart()
    if move=="s":
        pokeleague()
    if move=="d":
        gyms()
    else:
            home()
###################################################################################################
def gyms():
    print"""

                                          FIRE GYM


       AQUA GYM                                                          EARTH GYM


                                        AERIAL GYM"""
    move=raw_input("Enter your preffered direction of moving:")
    if move=="w":
        if getattr(fire,'value')==0:
                print'                        Welcome to Fire Gym'
                print'You will fight 2 pokemons to win a fire badge but be prepared the fight will not be easy'
                print'                      A  Magmar appeared'
                for i in range(len(getattr(pokeindex,'value'))):
                               print'You have: ',getattr(pokeindex,'value')
                               choose=raw_input('Choose your pokemon:')
                               poke=pokeselect(choose)
                               if getattr(poke,'hp')==0:
                                        print'Selected pokemon has no health'
                                        continue

                               else:
                                opp=magmar
                                ymulti2=1
                                omulti2=1
                                if (getattr(poke,'cat')=='Electric'):
                                    ymulti2=ymulti2*2
                                if (getattr(poke,'cat')=='Fire' or getattr(poke,'cat')=='Rock'):
                                    omulti2=omulti2*2
                                b=battle(getattr(poke,'move1'),getattr(poke,'move2'),getattr(opp,'move1'),getattr(opp,'move2'),getattr(poke,'multi')*ymulti2,getattr(opp,'multi')*omulti2,getattr(poke,'hp'),getattr(opp,'hp'))          
                                if b==1:
                                        setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                        evolve(choose,poke)
                                        print"A Flareon appeared"
                                        for i in range(len(getattr(pokeindex,'value'))):
                                               print'You have: ',getattr(pokeindex,'value')
                                               choose=raw_input('Choose your pokemon:')
                                               poke=pokeselect(choose)
                                               if getattr(poke,'hp')==0:
                                                   print'Selected pokemon has no health'
                                                   continue
                                               else:
                                                opp=flareon
                                                ymulti2=1
                                                omulti2=1
                                                if (getattr(poke,'cat')=='Electric'):
                                                     ymulti2=ymulti2*2
                                                if (getattr(poke,'cat')=='Fire' or getattr(poke,'cat')=='Rock'):
                                                    omulti2=omulti2*2
                                                b=battle(getattr(poke,'move1'),getattr(poke,'move2'),getattr(opp,'move1'),getattr(opp,'move2'),getattr(poke,'multi')*ymulti2,getattr(opp,'multi')*omulti2,getattr(poke,'hp'),getattr(opp,'hp'))          
                                                if b==1:
                                                            setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                                            evolve(choose,poke)
                                                            setattr(pokecoins,'value',(getattr(pokecoins,'value')+500))
                                                            setattr(fire,'value',1)
                                                            print'You have won the fire badge.Congratulations!!'
                                                            home()
                                                else:
                                                        setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                                        evolve(choose,poke)
                                                        setattr(poke,'hp',0)
                                                        continue

                                        home()
                                else:
                                                        setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                                        evolve(choose,poke)
                                                        setattr(poke,'hp',0)
                                                        continue

                home()                             
        else:
                print"You have already got the badge"
                home()
    if move=="a":
        if getattr(aqua,'value')==0:
                print'                        Welcome to Aqua Gym'
                print'You will fight 2 pokemons to win a aqua badge but be prepared the fight will not be easy'
                print'                      A  Polywrath appeared'
                for i in range(len(getattr(pokeindex,'value'))):
                               print'You have: ',getattr(pokeindex,'value')
                               choose=raw_input('Choose your pokemon:')
                               poke=pokeselect(choose)
                               if getattr(poke,'hp')==0:
                                        print'Selected pokemon has no health'
                                        continue

                               else:
                                opp=polywrath
                                ymulti2=1
                                omulti2=1
                                if (getattr(poke,'cat')=='Electric'):
                                    ymulti2=ymulti2*2
                                if (getattr(poke,'cat')=='Fire' or getattr(poke,'cat')=='Rock'):
                                    omulti2=omulti2*2
                                b=battle(getattr(poke,'move1'),getattr(poke,'move2'),getattr(opp,'move1'),getattr(opp,'move2'),getattr(poke,'multi')*ymulti2,getattr(opp,'multi')*omulti2,getattr(poke,'hp'),getattr(opp,'hp'))          
                                if b==1:
                                        setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                        evolve(choose,poke)
                                        print"A Golduck appeared"
                                        for i in range(len(getattr(pokeindex,'value'))):
                                               print'You have: ',getattr(pokeindex,'value')
                                               choose=raw_input('Choose your pokemon:')
                                               poke=pokeselect(choose)
                                               if getattr(poke,'hp')==0:
                                                   print'Selected pokemon has no health'
                                                   continue
                                               else:
                                                opp=golduck
                                                ymulti2=1
                                                omulti2=1
                                                if (getattr(poke,'cat')=='Electric'):
                                                    ymulti2=ymulti2*2
                                                if (getattr(poke,'cat')=='Fire' or getattr(poke,'cat')=='Rock'):
                                                    omulti2=omulti2*2
                                                b=battle(getattr(poke,'move1'),getattr(poke,'move2'),getattr(opp,'move1'),getattr(opp,'move2'),getattr(poke,'multi')*ymulti2,getattr(opp,'multi')*omulti2,getattr(poke,'hp'),getattr(opp,'hp'))          
                                                if b==1:
                                                            setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                                            evolve(choose,poke)
                                                            setattr(pokecoins,'value',(getattr(pokecoins,'value')+500))
                                                            setattr(aqua,'value',1)
                                                            print'You have won the aqua badge.Congratulations!!'
                                                            home()
                                                else:
                                                        setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                                        evolve(choose,poke)
                                                        setattr(poke,'hp',0)
                                                        continue

                                        home()
                                else:
                                                        setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                                        evolve(choose,poke)
                                                        setattr(poke,'hp',0)
                                                        continue

                home()                             
        else:
                print"You have already got the badge"
                home()
    if move=="s":
        if getattr(aerial,'value')==0:
                print'                        Welcome to Aerial Gym'
                print'You will fight 2 pokemons to win a aerial badge but be prepared the fight will not be easy'
                print'                      A  Fearow appeared'
                for i in range(len(getattr(pokeindex,'value'))):
                               print'You have: ',getattr(pokeindex,'value')
                               choose=raw_input('Choose your pokemon:')
                               poke=pokeselect(choose)
                               if getattr(poke,'hp')==0:
                                        print'Selected pokemon has no health'
                                        continue

                               else:
                                opp=fearow
                                ymulti2=1
                                omulti2=1
                                if (getattr(poke,'cat')=='Electric'):
                                   ymulti2=ymulti2*2
                                if (getattr(poke,'cat')=='Grass' or getattr(poke,'cat')=='Fighting'):
                                        omulti2=omulti2*2
                                b=battle(getattr(poke,'move1'),getattr(poke,'move2'),getattr(opp,'move1'),getattr(opp,'move2'),getattr(poke,'multi')*ymulti2,getattr(opp,'multi')*omulti2,getattr(poke,'hp'),getattr(opp,'hp'))          
                                if b==1:
                                        setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                        evolve(choose,poke)
                                        print"A Farfetch'd appeared"
                                        for i in range(len(getattr(pokeindex,'value'))):
                                               print'You have: ',getattr(pokeindex,'value')
                                               choose=raw_input('Choose your pokemon:')
                                               poke=pokeselect(choose)
                                               if getattr(poke,'hp')==0:
                                                   print'Selected pokemon has no health'
                                                   continue
                                               else:
                                                opp=farfetch
                                                ymulti2=1
                                                omulti2=1
                                                if (getattr(poke,'cat')=='Electric'):
                                                   ymulti2=ymulti2*2
                                                if (getattr(poke,'cat')=='Grass' or getattr(poke,'cat')=='Fighting'):
                                                   omulti2=omulti2*2
                                                b=battle(getattr(poke,'move1'),getattr(poke,'move2'),getattr(opp,'move1'),getattr(opp,'move2'),getattr(poke,'multi')*ymulti2,getattr(opp,'multi')*omulti2,getattr(poke,'hp'),getattr(opp,'hp'))          
                                                if b==1:
                                                            setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                                            evolve(choose,poke)
                                                            setattr(pokecoins,'value',(getattr(pokecoins,'value')+500))
                                                            setattr(aerial,'value',1)
                                                            print'You have won the aerial badge.Congratulations!!'
                                                            home()
                                                else:
                                                        setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                                        evolve(choose,poke)
                                                        setattr(poke,'hp',0)
                                                        continue

                                        home()
                                else:
                                                        setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                                        evolve(choose,poke)
                                                        setattr(poke,'hp',0)
                                                        continue

                home()                             
        else:
                print"You have already got the badge"
                home()
    if move=="d":
        if getattr(earth,'value')==0:
                print'                        Welcome to Earth Gym'
                print'You will fight 2 pokemons to win a earth badge but be prepared the fight will not be easy'
                print'                      A  Taurus appeared'
                for i in range(len(getattr(pokeindex,'value'))):
                               print'You have: ',getattr(pokeindex,'value')
                               choose=raw_input('Choose your pokemon:')
                               poke=pokeselect(choose)
                               if getattr(poke,'hp')==0:
                                        print'Selected pokemon has no health'
                                        continue

                               else:
                                opp=taurus
                                ymulti2=1
                                omulti2=1
                                if (getattr(poke,'cat')=='Ghost'):
                                   ymulti2=ymulti2*2
                                if (getattr(poke,'cat')=='Rock' or getattr(poke,'cat')=='Grass'):
                                   omulti2=omulti2*2
                                b=battle(getattr(poke,'move1'),getattr(poke,'move2'),getattr(opp,'move1'),getattr(opp,'move2'),getattr(poke,'multi')*ymulti2,getattr(opp,'multi')*omulti2,getattr(poke,'hp'),getattr(opp,'hp'))          
                                if b==1:
                                        setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                        evolve(choose,poke)
                                        print"A Onix appeared"
                                        for i in range(len(getattr(pokeindex,'value'))):
                                               print'You have: ',getattr(pokeindex,'value')
                                               choose=raw_input('Choose your pokemon:')
                                               poke=pokeselect(choose)
                                               if getattr(poke,'hp')==0:
                                                   print'Selected pokemon has no health'
                                                   continue
                                               else:
                                                opp=onix
                                                ymulti2=1
                                                omulti2=1
                                                if (getattr(poke,'cat')=='Ghost'):
                                                   ymulti2=ymulti2*2
                                                if (getattr(poke,'cat')=='Rock' or getattr(poke,'cat')=='Grass'):
                                                   omulti2=omulti2*2
                                                b=battle(getattr(poke,'move1'),getattr(poke,'move2'),getattr(opp,'move1'),getattr(opp,'move2'),getattr(poke,'multi')*ymulti2,getattr(opp,'multi')*omulti2,getattr(poke,'hp'),getattr(opp,'hp'))          
                                                if b==1:
                                                            setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                                            evolve(choose,poke)
                                                            setattr(pokecoins,'value',(getattr(pokecoins,'value')+500))
                                                            setattr(earth,'value',1)
                                                            print'You have won the earth badge.Congratulations!!'
                                                            home()
                                                else:
                                                        setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                                        evolve(choose,poke)
                                                        setattr(poke,'hp',0)
                                                        continue

                                        home()
                                else:
                                                        setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                                        evolve(choose,poke)
                                                        setattr(poke,'hp',0)
                                                        continue

                home()                             
        else:
                print"You have already got the badge"
                home()
    else:
            home()
##################################################################################################         
def pokemart():
        print"""
                                        Welcome to Pokemart"""
        print'''
Where would you like to go:
1-Pokeshop(place to buy pokeballs and potions)
2-Pokecentre(place to heal injured pokemons)
3-Savecentre(place to save your progress)'''
        check=input('Enter your decision:')
        if check==1:
                    pokeshop()
        elif check==2:
                    pokecentre()
        elif check==3:
                savecentre()
        else:
                home()
###################################################################################################
def savecentre():
        file1=open('pokemon.bat','wb')
        file2=open('variable.bat','wb')
        pickle.dump(pikachu,file1)
        pickle.dump(raichu,file1)
        pickle.dump(squirtle,file1)
        pickle.dump(wartortle,file1)
        pickle.dump(blastoise,file1)
        pickle.dump(charmender,file1)
        pickle.dump(charmeleon,file1)
        pickle.dump(charizard,file1)
        pickle.dump(bulbasaur,file1)
        pickle.dump(ivysaur,file1)
        pickle.dump(venasaur,file1)
        pickle.dump(pidgey,file1)
        pickle.dump(pidgeotto,file1)
        pickle.dump(pidgeot,file1)
        pickle.dump(gastly,file1)
        pickle.dump(haunter,file1)
        pickle.dump(gengar,file1)
        pickle.dump(abra,file1)
        pickle.dump(kadabra,file1)
        pickle.dump(alakazam,file1)
        pickle.dump(machop,file1)
        pickle.dump(machoke,file1)
        pickle.dump(machamp,file1)
        pickle.dump(geodude,file1)
        pickle.dump(gravelar,file1)
        pickle.dump(golem,file1)
        pickle.dump(magmar,file1)
        pickle.dump(flareon,file1)
        pickle.dump(polywrath,file1)
        pickle.dump(golduck,file1)
        pickle.dump(taurus,file1)
        pickle.dump(onix,file1)
        pickle.dump(fearow,file1)
        pickle.dump(farfetch,file1)
        pickle.dump(dragonite,file1)
        pickle.dump(zapdos,file1)
        pickle.dump(vaporeon,file1)
        pickle.dump(pokeballs,file2)
        pickle.dump(potion,file2)
        pickle.dump(pokecoins,file2)
        pickle.dump(earth,file2)
        pickle.dump(fire,file2)
        pickle.dump(aqua,file2)
        pickle.dump(aerial,file2)
        pickle.dump(sector0,file2)
        pickle.dump(sector1,file2)
        pickle.dump(sector2,file2)
        pickle.dump(sector4,file2)
        pickle.dump(sector5,file2)
        pickle.dump(sector6,file2)
        pickle.dump(sector8,file2)
        pickle.dump(sector9,file2)
        pickle.dump(pokeindex,file2)
        file1.close()
        file2.close()
        print"Your progress has been saved"
        home()
##################################################################################################        
def pokeshop():
    print"""
                                        Welcome to Pokeshop

What would you like to buy?
1)Pokeballs-200coins
2)Potion-200coins:"""
    choice=input("Enter the product you want to buy:")
    quantity=input("Enter the Quantity you require:")
    if choice==1:
        check=getattr(pokecoins,'value')-(quantity*200)
        if check<0:
            print"You do not have sufficient funds"
            choice=input("Enter 1 to go back or 2 to reduce quantity:")
            if choice==1:
                home()
            else:
                pokemart()
        else:
            setattr(pokeballs,'value',(getattr(pokeballs,'value'))+quantity)
            setattr(pokecoins,'value',(getattr(pokecoins,'value')-(quantity*200)))
            print "Thanks for Visiting"
            print "You now have",getattr(pokeballs,'value')," pokeballs and ",getattr(pokecoins,'value'),"pokecoins"
            home()
    else:
        check=getattr(pokecoins,'value')-(quantity*200)
        if check<0:
            print"You do not have sufficient funds"
            choice=input("Enter 1 to go back or 2 to reduce quantity:")
            if choice==1:
                home()
            else:
                pokemart()
        else:
            setattr(potion,'value',(getattr(potion,'value'))+quantity)
            setattr(pokecoins,'value',(getattr(pokecoins,'value')-(quantity*200)))
            print"Thanks for Visiting"
            print"You now have",getattr(potion,'value')," potion and ",getattr(pokecoins,'value'),"pokecoins"
            home()
###################################################################################################
def battle(move1,move2,move3,move4,ymulti,omulti,yhp,ohp):
        play_again = True
        while play_again:
            winner = None
            player_health =yhp
            computer_health =ohp
            turn = random.randint(1,2) 
            if turn == 1:
                player_turn = True
                computer_turn = False
                print("Player will go first.")
            else:
                player_turn = False
                computer_turn = True
                print("Computer will go first.")
                print("Player health: ", player_health, "Computer health: ", computer_health)
            while (player_health != 0 or computer_health != 0):
                heal_up = False 
                miss = False 
                moves = {move1: random.randint(18*ymulti, 25*ymulti),
                         move2: random.randint(10*ymulti, 35*ymulti),
                         "Heal": random.randint(20, 25),
                         move3: random.randint(18*omulti,25*omulti),
                         move4: random.randint(10*omulti,25*omulti)}
                if player_turn:
                    print"Please select a move:" 
                    print "1 ",move1,'(Deal damage between ',18*ymulti,'-',25*ymulti,")"
                    print "2 ",move2,"(Deal damage between ",10*ymulti,'-',35*ymulti,')'
                    print'3 Heal (Restore between 20-25 health)'
                    player_move = input("> ")
                    move_miss = random.randint(1,5) 
                    if move_miss == 1:
                        miss = True
                    else:
                        miss = False
                    if miss:
                        player_move = 0 
                        print("You missed!")
                    else:
                        if player_move in (1, move1):
                            player_move = moves[move1]
                            print("You used ",move1,". It dealt ", player_move, " damage.")
                        elif player_move in (2, move2):
                            player_move = moves[move2]
                            print("You used ",move2,". It dealt ", player_move, " damage.")
                        elif player_move in (3, "heal"):
                            heal_up = True # heal activated
                            player_move = moves["Heal"]
                            print("You used Heal. It healed for ", player_move, " health.")
                        else:
                            print("That is not a valid move. Please try again.")
                            continue
                else: 
                    move_miss = random.randint(1,5)
                    if move_miss == 1:
                        miss = True
                    else:
                        miss = False
                    if miss:
                        computer_move = 0 
                        print("The computer missed!")
                    else:
                        if computer_health > 30: 
                            if player_health > 75:
                                computer_move = moves[move3]
                                print("The computer used ",move3,". It dealt ", computer_move, " damage.")
                            elif player_health > 35 and player_health <= 75: 
                                imoves = [move3, move4]
                                imoves = random.choice(imoves)
                                computer_move = moves[imoves]
                                print("The computer used ", imoves, ". It dealt ", computer_move, " damage.")
                            elif player_health <= 35:
                                computer_move = moves[move4] 
                                print("The computer used ",move4,". It dealt ", computer_move, " damage.")                       
                        else: 
                            heal_or_fight = random.randint(1,2) 
                            if heal_or_fight == 1:
                                heal_up = True
                                computer_move = moves["Heal"]
                                print("The computer used Heal. It healed for ", computer_move, " health.")
                            else:
                                if player_health > 75:
                                    computer_move = moves[move3]
                                    print("The computer used ",move3,". It dealt ", computer_move, " damage.")
                                elif player_health > 35 and player_health <= 75:
                                    imoves = [move3, move4]
                                    imoves = random.choice(imoves)
                                    computer_move = moves[imoves]
                                    print("The computer used ", imoves, ". It dealt ", computer_move, " damage.")
                                elif player_health <= 35:
                                    computer_move = moves[move4] 
                                    print("The computer used ",move4,". It dealt ", computer_move, " damage.")
                if heal_up:
                    if player_turn:
                        player_health += player_move
                        if player_health > 100:
                            player_health = 100 # cap max health at 100. No over healing!
                    else:
                        computer_health += computer_move
                        if computer_health > 100:
                            computer_health = 100
                else:
                    if player_turn:
                        computer_health -= player_move
                        if computer_health < 0:
                            computer_health = 0 # cap minimum health at 0
                            winner = "Player"
                            break
                    else:
                        player_health -= computer_move
                        if player_health < 0:
                            player_health = 0
                            winner = "Computer"
                            break
                print("Player health: ", player_health, "Computer health: ", computer_health)
                player_turn = not player_turn
                computer_turn = not computer_turn
            if winner == "Player":
                print("Player health: ", player_health, "Computer health: ", computer_health)
                print("Congratulations! You have won. You're a good Trainer!!")
                return 1
            else:
                print("Player health: ", player_health, "Computer health: ", computer_health)
                print("Sorry, but your opponent wiped the floor with you. Better luck next time.")
                return 2
###################################################################################################
def pokecentre():
      print 'You have ',getattr(potion,'value'),' potions'
      if getattr(potion,'value')>0:
          print'You have: ',getattr(pokeindex,'value')
          choose=raw_input('Choose your pokemon:')
          poke=pokeselect(choose)
          setattr (poke,'hp',(getattr(poke,'hpmax')))
          setattr(potion,'value',(getattr(potion,'value')-(1)))
          check=raw_input('Want to heal more pokemon:y/n')
          if check=='y':
                 pokecentre()
          else:
              home()
             
      elif getattr(potion,'value')==0:
                        print"You don't have potion to heal your pokemon"
                        check=raw_input('Want to purchase: y/n')
                        if check=='y':
                          pokeshop()
                        else:
                           home()
##################################################################################################                 
def pokeselect(choose):
        if choose=='pikachu':
            return pikachu
        elif choose=='raichu':
            return raichu
        elif choose=='squirtle':
            return squirtle
        elif choose=='wartortle':
            return wartortle
        elif choose=='blastoise':
            return blastoise
        elif choose=='charmender':
            return charmender
        elif choose=='charmeleon':
            return charmeleon
        elif choose=='charizard':
            return charizard
        elif choose=='bulbasaur':
            return bulbasaur
        elif choose=='ivysaur':
            return ivysaur
        elif choose=='venasaur':
            return venasaur
        elif choose=='pidgey':
            return pidgey
        elif choose=='pidgeotto':
            return pidgeotto
        elif choose=='pidgeot':
            return pidgeot
        elif choose=='gastly':
            return gastly
        elif choose=='haunter':
            return haunter
        elif choose=='gengar':
            return gengar
        elif choose=='abra':
            return abra
        elif choose=='kadabra':
            return kadabra
        elif choose=='alakazam':
            return alakazam
        elif choose=='machop':
            return machop
        elif choose=='machoke':
            return machoke
        elif choose=='machamp':
            return machamp
        elif choose=='geodude':
                return geodude
        elif choose=='gravelar':
                return gravelar
        elif choose=='golem':
                return golem
        else:
                choose=raw_input('Invalid Input,Try Again:')
                poke=pokeselect(choose)
                return poke
###################################################################################################
def evolve(choose,poke):
        efight=getattr(poke,'fight')
        list1=getattr(pokeindex,'value')
        if efight>2:
                if poke==pikachu:
                       list1.remove('pikachu')
                       list1.append('raichu')
                       setattr(pokeindex,'value',list1)
                if poke==squirtle:
                       list1.remove('squirtle')
                       list1.append('wartortle')
                       setattr(pokeindex,'value',list1)
                if poke==wartortle:
                       list1.remove('wartortle')
                       list1.append('blastoise')
                       setattr(pokeindex,'value',list1)
                if poke==bulbasaur:
                       list1.remove('bulbasaur')
                       list1.append('ivysaur')
                       setattr(pokeindex,'value',list1)
                if poke==ivysaur:
                       list1.remove('ivysaur')
                       list1.append('venasaur')
                       setattr(pokeindex,'value',list1)
                if poke==charmender:
                       list1.remove('charmender')
                       list1.append('charmeleon')
                       setattr(pokeindex,'value',list1)
                if poke==charmeleon:
                       list1.remove('charmeleonr')
                       list1.append('charizard')
                       setattr(pokeindex,'value',list1)
                if poke==pidgey:
                       list1.remove('pidgey')
                       list1.append('pidgeotto')
                       setattr(pokeindex,'value',list1)
                if poke==pidgeotto:
                       list1.remove('pidgeotto')
                       list1.append('pidgeot')
                       setattr(pokeindex,'value',list1)
                if poke==gastly:
                       list1.remove('gastly')
                       list1.append('haunter')
                       setattr(pokeindex,'value',list1)
                if poke==haunter:
                       list1.remove('haunter')
                       list1.append('gengar')
                       setattr(pokeindex,'value',list1)
                if poke==abra:
                       list1.remove('abra')
                       list1.append('kadabra')
                       setattr(pokeindex,'value',list1)
                if poke==kadabra:
                       list1.remove('kadabra')
                       list1.append('alakazam')
                       setattr(pokeindex,'value',list1)
                if poke==machop:
                       list1.remove('machop')
                       list1.append('machoke')
                       setattr(pokeindex,'value',list1)
                if poke==machoke:
                       list1.remove('machoke')
                       list1.append('machamp')
                       setattr(pokeindex,'value',list1)
                if poke==geodude:
                       list1.remove('geodude')
                       list1.append('gravelar')
                       setattr(pokeindex,'value',list1)
                if poke==gravelar:
                       list1.remove('gravelar')
                       list1.append('golem')
                       setattr(pokeindex,'value',list1)
###################################################################################################
def park():
    print"""
                                         WELCOME TO PARK



                                            SECTOR 0
        SECTOR 1                                                             SECTOR 3
                                            SECTOR 2
        SECTOR 4                                                             SECTOR 6
                                            SECTOR 5
        SECTOR 7                                                             SECTOR 8
                                            SECTOR 9"""
    choice=input("Enter your preferred sector number:")
    if choice==0:
            if getattr(sector0,'value')==0:
                print'                      A wild Squirtle appeared'
                print'You have: ',getattr(pokeindex,'value')
                choose=raw_input('Choose your pokemon:')
                poke=pokeselect(choose)
                if getattr(poke,'hp')==0:
                        print'Selected pokemon has no health'
                        home()
                opp=squirtle
                ymulti2=1
                omulti2=1
                if (getattr(poke,'cat')=='Electric'):
                    ymulti2=ymulti2*2
                if (getattr(poke,'cat')=='Fire' or getattr(poke,'cat')=='Rock'):
                    omulti2=omulti2*2
                b=battle(getattr(poke,'move1'),getattr(poke,'move2'),getattr(opp,'move1'),getattr(opp,'move2'),getattr(poke,'multi')*ymulti2,getattr(opp,'multi')*omulti2,getattr(poke,'hp'),getattr(opp,'hp'))          
                if b==1:
                    setattr(poke,'fight',(getattr(poke,'fight'))+1)
                    check=getattr(pokeballs,'value')
                    if check<=0:
                            print"You are low on pokeballs"
                    else:
                            setattr(pokeballs,'value',(getattr(pokeballs,'value')-1))
                            setattr(pokeindex,'value',(getattr(pokeindex,'value')+['squirtle']))
                            setattr(pokecoins,'value',(getattr(pokecoins,'value')+200))
                            evolve(choose,poke)
                            setattr(sector0,'value',1)
                            home()
                else:
                    setattr(poke,'hp',0)
                    setattr(poke,'fight',(getattr(poke,'fight'))+1)
                    setattr(pokecoins,'value',(getattr(pokecoins,'value')+100))
                    evolve(choose,poke)   
                    home()
            else:
                print"You have already caught the Pokemon"
                home()
    if choice==1:
            if getattr(sector1,'value')==0:
                print'                      A wild Bulbasaur appeared'
                print'You have: ',getattr(pokeindex,'value')
                choose=raw_input('Choose your pokemon:')
                poke=pokeselect(choose)
                if getattr(poke,'hp')==0:
                        print'Selected pokemon has no health'
                        home()
                opp=bulbasaur
                ymulti2=1
                omulti2=1
                if (getattr(poke,'cat')=='Fire'):
                    ymulti2=ymulti2*2
                if (getattr(poke,'cat')=='Water' or getattr(poke,'cat')=='Rock'):
                    omulti2=omulti2*2
                b=battle(getattr(poke,'move1'),getattr(poke,'move2'),getattr(opp,'move1'),getattr(opp,'move2'),getattr(poke,'multi')*ymulti2,getattr(opp,'multi')*omulti2,getattr(poke,'hp'),getattr(opp,'hp'))          
                if b==1:
                    setattr(poke,'fight',(getattr(poke,'fight'))+1)
                    check=getattr(pokeballs,'value')
                    if check<=0:
                            print"You are low on pokeballs"
                    else:
                            setattr(pokeballs,'value',(getattr(pokeballs,'value')-1))
                            setattr(pokeindex,'value',(getattr(pokeindex,'value')+['bulbasaur']))
                            setattr(pokecoins,'value',(getattr(pokecoins,'value')+200))
                            evolve(choose,poke)
                            setattr(sector1,'value',1)
                            home()
                else:
                    setattr(poke,'hp',0)
                    setattr(poke,'fight',(getattr(poke,'fight'))+1)
                    setattr(pokecoins,'value',(getattr(pokecoins,'value')+100))
                    evolve(choose,poke)
                    home()
            else:
                print"You have already caught the Pokemon"
                home()

    if choice==2:
        if getattr(sector2,'value')==0:
            
            print'                      A wild Charmender appeared'
            print'You have: ',getattr(pokeindex,'value')
            choose=raw_input('Choose your pokemon:')
            poke=pokeselect(choose)
            if getattr(poke,'hp')==0:
                        print'Selected pokemon has no health'
                        home()
            opp=charmender
            ymulti2=1
            omulti2=1
            if (getattr(poke,'cat')=='Water'):
                ymulti2=ymulti2*2
            if (getattr(poke,'cat')=='Grass'):
                omulti2=omulti2*2
            b=battle(getattr(poke,'move1'),getattr(poke,'move2'),getattr(opp,'move1'),getattr(opp,'move2'),getattr(poke,'multi')*ymulti2,getattr(opp,'multi')*omulti2,getattr(poke,'hp'),getattr(opp,'hp'))          
            if b==1:
                setattr(poke,'fight',(getattr(poke,'fight'))+1)
                check=getattr(pokeballs,'value')
                if check<=0:
                        print"You are low on pokeballs"
                else:
                        
                        setattr(pokeballs,'value',(getattr(pokeballs,'value')-1))
                        setattr(pokeindex,'value',(getattr(pokeindex,'value')+['charmender']))
                        setattr(pokecoins,'value',(getattr(pokecoins,'value')+200))
                        evolve(choose,poke)
                        setattr(sector2,'value',1)
                        home()
                home()
            else:
                setattr(poke,'hp',0)
                setattr(poke,'fight',(getattr(poke,'fight'))+1)
                setattr(pokecoins,'value',(getattr(pokecoins,'value')+100))
                evolve(choose,poke)
                home()
        else:
                print"You have already caught the Pokemon"
                home()
    if choice==3:
         print'Aw! Its empty here'
         back=raw_input('Press B to go back:')
         if back=='b' or back=='B':
                 home()
    if choice==4:
         if getattr(sector4,'value')==0:
            print'                      A wild Gastly appeared'
            print'You have: ',getattr(pokeindex,'value')
            choose=raw_input('Choose your pokemon:')
            poke=pokeselect(choose)
            if getattr(poke,'hp')==0:
                        print'Selected pokemon has no health'
                        home()
            opp=gastly
            ymulti2=1
            omulti2=1
            if (getattr(poke,'cat')=='Fire'):
                ymulti2=ymulti2*2
            if (getattr(poke,'cat')=='Psychic'):
                omulti2=omulti2*2
            b=battle(getattr(poke,'move1'),getattr(poke,'move2'),getattr(opp,'move1'),getattr(opp,'move2'),getattr(poke,'multi')*ymulti2,getattr(opp,'multi')*omulti2,getattr(poke,'hp'),getattr(opp,'hp'))          
            if b==1:
                setattr(poke,'fight',(getattr(poke,'fight'))+1)
                check=getattr(pokeballs,'value')
                if check<=0:
                        print"You are low on pokeballs"
                else:
                        setattr(pokeballs,'value',(getattr(pokeballs,'value')-1))
                        setattr(pokeindex,'value',(getattr(pokeindex,'value')+['gastly']))
                        setattr(pokecoins,'value',(getattr(pokecoins,'value')+200))
                        evolve(choose,poke)
                        setattr(sector4,'value',1)
                        home()
                home()
            else:
                setattr(poke,'hp',0)
                setattr(poke,'fight',(getattr(poke,'fight'))+1)
                setattr(pokecoins,'value',(getattr(pokecoins,'value')+100))
                evolve(choose,poke)
                home()
         else:
                print"You have already caught the Pokemon"
                home()
    if choice==5:
        if getattr(sector5,'value')==0:
            print'                      A wild Abra appeared'
            print'You have: ',getattr(pokeindex,'value')
            choose=raw_input('Choose your pokemon:')
            poke=pokeselect(choose)
            if getattr(poke,'hp')==0:
                        print'Selected pokemon has no health'
                        home()
            opp=abra
            ymulti2=1
            omulti2=1
            if (getattr(poke,'cat')=='Ghost'):
                ymulti2=ymulti2*2
            if (getattr(poke,'cat')=='Fighting'):
                omulti2=omulti2*2
            b=battle(getattr(poke,'move1'),getattr(poke,'move2'),getattr(opp,'move1'),getattr(opp,'move2'),getattr(poke,'multi')*ymulti2,getattr(opp,'multi')*omulti2,getattr(poke,'hp'),getattr(opp,'hp'))          
            if b==1:
                setattr(poke,'fight',(getattr(poke,'fight'))+1)
                check=getattr(pokeballs,'value')
                if check<=0:
                        print"You are low on pokeballs"
                else:
                        setattr(pokeballs,'value',(getattr(pokeballs,'value')-1))
                        setattr(pokeindex,'value',(getattr(pokeindex,'value')+['abra']))
                        setattr(pokecoins,'value',(getattr(pokecoins,'value')+200))
                        evolve(choose,poke)
                        setattr(sector5,'value',1)
                        home()
                home()
            else:
                setattr(poke,'hp',0)
                setattr(poke,'fight',(getattr(poke,'fight'))+1)
                setattr(pokecoins,'value',(getattr(pokecoins,'value')+100))
                evolve(choose,poke)
                home()
        else:
                print"You have already caught the Pokemon"
                home()
    if choice==6:
        if getattr(sector6,'value')==0:
            print'                      A wild Machop appeared'
            print'You have: ',getattr(pokeindex,'value')
            choose=raw_input('Choose your pokemon:')
            poke=pokeselect(choose)
            if getattr(poke,'hp')==0:
                        print'Selected pokemon has no health'
                        home()
            opp=machop
            ymulti2=1
            omulti2=1
            if (getattr(poke,'cat')=='Ghost'):
                ymulti2=ymulti2*2
            if (getattr(poke,'cat')=='Rock' or getattr(poke,'cat')=='Grass'):
                omulti2=omulti2*2
            b=battle(getattr(poke,'move1'),getattr(poke,'move2'),getattr(opp,'move1'),getattr(opp,'move2'),getattr(poke,'multi')*ymulti2,getattr(opp,'multi')*omulti2,getattr(poke,'hp'),getattr(opp,'hp'))          
            if b==1:
                setattr(poke,'fight',(getattr(poke,'fight'))+1)
                check=getattr(pokeballs,'value')
                if check<=0:
                        print"You are low on pokeballs"
                else:
                        setattr(pokeballs,'value',(getattr(pokeballs,'value')-1))
                        setattr(pokeindex,'value',(getattr(pokeindex,'value')+['machop']))
                        setattr(pokecoins,'value',(getattr(pokecoins,'value')+200))
                        evolve(choose,poke)
                        setattr(sector6,'value',1)
                        home()
                home()
            else:
                setattr(poke,'hp',0)
                setattr(poke,'fight',(getattr(poke,'fight'))+1)
                setattr(pokecoins,'value',(getattr(pokecoins,'value')+100))
                evolve(choose,poke)
                home()
        else:
                print"You have already caught the Pokemon"
                home()
    if choice==7:
        print'Aw! Its empty here'
        back=raw_input('Press B to go back:')
        if back=='b' or back=='B':
                 home()
    if choice==8:
        if getattr(sector8,'value')==0:
            print'                      A wild Pidgey appeared'
            print'You have: ',getattr(pokeindex,'value')
            choose=raw_input('Choose your pokemon:')
            poke=pokeselect(choose)
            if getattr(poke,'hp')==0:
                        print'Selected pokemon has no health'
                        home()
            opp=pidgey
            ymulti2=1
            omulti2=1
            if (getattr(poke,'cat')=='Electric'):
                ymulti2=ymulti2*2
            if (getattr(poke,'cat')=='Grass' or getattr(poke,'cat')=='Fighting'):
                omulti2=omulti2*2
            b=battle(getattr(poke,'move1'),getattr(poke,'move2'),getattr(opp,'move1'),getattr(opp,'move2'),getattr(poke,'multi')*ymulti2,getattr(opp,'multi')*omulti2,getattr(poke,'hp'),getattr(opp,'hp'))          
            if b==1:
                setattr(poke,'fight',(getattr(poke,'fight'))+1)
                check=getattr(pokeballs,'value')
                if check<=0:
                        print"You are low on pokeballs"
                else:
                        setattr(pokeballs,'value',(getattr(pokeballs,'value')-1))
                        setattr(pokeindex,'value',(getattr(pokeindex,'value')+['pidgey']))
                        setattr(pokecoins,'value',(getattr(pokecoins,'value')+200))
                        evolve(choose,poke)
                        setattr(sector8,'value',1)
                        home()
                home()
            else:
                setattr(poke,'hp',0)
                setattr(poke,'fight',(getattr(poke,'fight'))+1)
                setattr(pokecoins,'value',(getattr(pokecoins,'value')+100))
                evolve(choose,poke)
                home()
        else:
                print"You have already caught the Pokemon"
                home()
    if choice==9:
       if getattr(sector9,'value')==0:
            print'                      A wild Geodude appeared'
            print'You have: ',getattr(pokeindex,'value')
            choose=raw_input('Choose your pokemon:')
            poke=pokeselect(choose)
            if getattr(poke,'hp')==0:
                        print'Selected pokemon has no health'
                        home()
            opp=geodude
            ymulti2=1
            omulti2=1
            if (getattr(poke,'cat')=='Water'):
                ymulti2=ymulti2*2
            if (getattr(poke,'cat')=='Electric'):
                omulti2=omulti2*2
            b=battle(getattr(poke,'move1'),getattr(poke,'move2'),getattr(opp,'move1'),getattr(opp,'move2'),getattr(poke,'multi')*ymulti2,getattr(opp,'multi')*omulti2,getattr(poke,'hp'),getattr(opp,'hp'))          
            if b==1:
                setattr(poke,'fight',(getattr(poke,'fight'))+1)
                check=getattr(pokeballs,'value')
                if check<=0:
                        print"You are low on pokeballs"
                else:
                        setattr(pokeballs,'value',(getattr(pokeballs,'value')-1))
                        setattr(pokeindex,'value',(getattr(pokeindex,'value')+['geodude']))
                        setattr(pokecoins,'value',(getattr(pokecoins,'value')+200))
                        evolve(choose,poke)
                        setattr(sector9,'value',1)
                        home()
                home()
            else:
                setattr(poke,'hp',0)
                setattr(poke,'fight',(getattr(poke,'fight'))+1)
                setattr(pokecoins,'value',(getattr(pokecoins,'value')+100))
                evolve(choose,poke)
                home()
       else:
                print"You have already caught the Pokemon"
                home()
    else:
            home()
###################################################################################################
def pokeleague():
    if getattr(earth,'value')==1 and getattr(fire,'value')==1 and getattr(aqua,'value')==1 and getattr(aerial,'value')==1:
                print'                        Welcome to Pokeleague'
                print'You will fight 3 pokemons to win a pokeleague but be prepared the fight will not be easy'
                print'                      A  Dragonite appeared'
                for i in range(len(getattr(pokeindex,'value'))):
                               print'You have: ',getattr(pokeindex,'value')
                               choose=raw_input('Choose your pokemon:')
                               poke=pokeselect(choose)
                               if getattr(poke,'hp')==0:
                                        print'Selected pokemon has no health'
                                        continue

                               else:
                                opp=dragonite
                                ymulti2=1
                                omulti2=1
                                b=battle(getattr(poke,'move1'),getattr(poke,'move2'),getattr(opp,'move1'),getattr(opp,'move2'),getattr(poke,'multi')*ymulti2,getattr(opp,'multi')*omulti2,getattr(poke,'hp'),getattr(opp,'hp'))          
                                if b==1:
                                        setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                        evolve(choose,poke)
                                        print"A Vaporeon appeared"
                                        for i in range(len(getattr(pokeindex,'value'))):
                                               print'You have: ',getattr(pokeindex,'value')
                                               choose=raw_input('Choose your pokemon:')
                                               poke=pokeselect(choose)
                                               if getattr(poke,'hp')==0:
                                                   print'Selected pokemon has no health'
                                                   continue
                                               else:
                                                opp=vaporeon
                                                ymulti2=1
                                                omulti2=1
                                                if (getattr(poke,'cat')=='Electric'):
                                                    ymulti2=ymulti2*2
                                                if (getattr(poke,'cat')=='Fire' or getattr(poke,'cat')=='Rock'):
                                                    omulti2=omulti2*2
                                                b=battle(getattr(poke,'move1'),getattr(poke,'move2'),getattr(opp,'move1'),getattr(opp,'move2'),getattr(poke,'multi')*ymulti2,getattr(opp,'multi')*omulti2,getattr(poke,'hp'),getattr(opp,'hp'))          
                                                if b==1:
                                                            setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                                            evolve(choose,poke)
                                                            print"A Zapdos appeared"
                                                            for i in range(len(getattr(pokeindex,'value'))):
                                                              print'You have: ',getattr(pokeindex,'value')
                                                              choose=raw_input('Choose your pokemon:')
                                                              poke=pokeselect(choose)
                                                              if getattr(poke,'hp')==0:
                                                                 print'Selected pokemon has no health'
                                                                 continue
                                                              else:
                                                                 opp=zapdos
                                                                 ymulti2=1
                                                                 omulti2=1
                                                                 if (getattr(poke,'cat')=='Rock'):
                                                                    ymulti2=ymulti2*2
                                                                 if (getattr(poke,'cat')=='Water'):
                                                                         omulti2=omulti2*2                                           
                                                                 b=battle(getattr(poke,'move1'),getattr(poke,'move2'),getattr(opp,'move1'),getattr(opp,'move2'),getattr(poke,'multi')*ymulti2,getattr(opp,'multi')*omulti2,getattr(poke,'hp'),getattr(opp,'hp'))                                 
                                                                 if b==1:
                                                                         print'                   !!You won the Game!!'
                                                                         print"          Stay tuned with us for further updates"
                                                                         print"                   Thanks for Playing"
                                                                         quit()
                                                                 else:
                                                                        setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                                                        evolve(choose,poke)
                                                                        setattr(poke,'hp',0)
                                                                        continue
                                                            home()
                                                else:
                                                        setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                                        evolve(choose,poke)
                                                        setattr(poke,'hp',0)
                                                        

                                        home()
                                else:
                                                        setattr(poke,'fight',(getattr(poke,'fight'))+1)
                                                        evolve(choose,poke)
                                                        setattr(poke,'hp',0)
                                                        continue

                home()                             
    else:
        print"You have not reached sufficient level. Come back with more practice"
        home()
#################################          CLASSES             ####################################
class variable():
    def __init__(self,value):
        self.value=value
###################################################################################################
class pokemon:
    def __init__(self,name,hp,move1,move2,hpmax,cat,multi,fight):
        self.name=name
        self.hp=hp
        self.move1=move1
        self.move2=move2
        self.hpmax=hpmax
        self.cat=cat
        self.multi=multi
        self.fight=fight
#################################         MAIN BLOCK           ####################################
print "\n"*40
print'                                    WELCOME TO POKEMON WORLD'
print""
print""
print"""
What do you want to do?:
1-Start a new journey
2-Continue your adventure"""
val=input('Take your decision:')
if val==1:
        pikachu=pokemon('Pikachu',100,'Thunder Shock','Electro Ball',100,'Electric',1,0)
        raichu=pokemon('Raichu',150,'Thunder Shock','Electro Ball',150,'Electric',2,0)
        squirtle=pokemon('Squirtle',100,'Psybeam','Hydro Pump',100,'Water',1,0)
        wartortle=pokemon('Wartortle',150,'Psybeam','Hydro Pump',150,'Water',2,0)
        blastoise=pokemon('Blastoise',200,'Psybeam','Hydro Pump',200,'Water',3,0)
        charmender=pokemon('Charmender',100,'Ember','Flame Thrower',100,'Fire',1,0)
        charmeleon=pokemon('Charmeleon',150,'Ember','Flame Thrower',150,'Fire',2,0)
        charizard=pokemon('Charizard',200,'Ember','Flame Thrower',200,'Fire',3,0)
        bulbasaur=pokemon('Bulbasaur',100,'Razor Leaf','Vine Whip',100,'Grass',1,0)
        ivysaur=pokemon('Ivysaur',150,'Razor Leaf','Vine Whip',150,'Grass',2,0)
        venasaur=pokemon('Venasaur',200,'Razor Leaf','Vine Whip',200,'Grass',3,0)
        pidgey=pokemon('Pidgey',100,'Gust','Steel Wing',100,'Air',1,0)
        pidgeotto=pokemon('Pidgeotto',150,'Gust','Steel Wing',150,'Air',2,0)
        pidgeot=pokemon('Pidgeot',200,'Gust','Steel Wing',200,'Air',3,0)
        gastly=pokemon('Gastly',100,'Sucker Pumch','Shadow Ball',100,'Ghost',1,0)
        haunter=pokemon('Haunter',150,'Sucker Pumch','Shadow Ball',150,'Ghost',2,0)
        gengar=pokemon('Gengar',200,'Sucker Pumch','Shadow Ball',200,'Ghost',3,0)
        abra=pokemon('Abra',100,'Confusion','Barrier',100,'Psychic',1,0)
        kadabra=pokemon('Kadabra',150,'Confusion','Barrier',150,'Psychic',2,0)
        alakazam=pokemon('Alakazam',200,'Confusion','Barrier',200,'Psychic',3,0)
        machop=pokemon('Machop',100,'Counter','Double Kick',100,'Fighting',1,0)
        machoke=pokemon('Machoke',150,'Counter','Double Kick',150,'Fighting',2,0)
        machamp=pokemon('Machamp',200,'Counter','Double Kick',200,'Fighting',3,0)
        geodude=pokemon('Geodude',100,'Quick Attack','Rock Throw',100,'Rock',1,0)
        gravelar=pokemon('Gravelar',150,'Quick Attack','Rock Throw',150,'Rock',2,0)
        golem=pokemon('Golem',200,'Quick Attack','Rock Throw',200,'Rock',3,0)
        magmar=pokemon('Magmar',100,'Ember','Flame Thrower',100,'Fire',2,0)
        flareon=pokemon('Flareon',100,'Ember','Flame Thrower',100,'Fire',2,0)
        polywrath=pokemon('Polywrath',100,'Psybeam','Hydro Pump',100,'Water',2,0)
        golduck=pokemon('Golduck',100,'Psybeam','Hydro Pump',100,'Water',2,0)
        taurus=pokemon('Taurus',100,'Counter','Double Kick',100,'Grass',2,0)
        onix=pokemon('Onix',100,'Quick Attack','Rock Throw',100,'Rock',2,0)
        fearow=pokemon('Fearow',100,'Gust','Steel Wing',100,'Air',2,0)
        farfetch=pokemon('Farfetch',100,'Gust','Steel Wing',100,'Air',2,0)
        dragonite=pokemon('Dragonite',150,'Flame Thrower','Hyper Beam',100,'Normal',3,0)
        zapdos=pokemon('Zapdos',150,'Thunder Shock','Electro Ball',150,'Electric',3,0)
        vaporeon=pokemon('Vaporeon',150,'Psybeam','Hydro Pump',150,'Water',3,0)
        pokeballs=variable(5)
        potion=variable(3)
        pokecoins=variable(1000)
        earth=variable(0)
        fire=variable(0)
        aqua=variable(0)
        aerial=variable(0)
        sector0=variable(0)
        sector1=variable(0)
        sector2=variable(0)
        sector4=variable(0)
        sector5=variable(0)
        sector6=variable(0)#Sector 3,7 empty
        sector8=variable(0)
        sector9=variable(0)
        pokeindex=variable(['pikachu'])
        home()
else:
        f1=open('pokemon.bat','rb')
        f2=open('variable.bat','rb')
        pikachu=pickle.load(f1)
        raichu=pickle.load(f1)
        squirtle=pickle.load(f1)
        wartortle=pickle.load(f1)
        blastoise=pickle.load(f1)
        charmender=pickle.load(f1)
        charmeleon=pickle.load(f1)
        charizard=pickle.load(f1)
        bulbasaur=pickle.load(f1)
        ivysaur=pickle.load(f1)
        venasaur=pickle.load(f1)
        pidgey=pickle.load(f1)
        pidgeotto=pickle.load(f1)
        pidgeot=pickle.load(f1)
        gastly=pickle.load(f1)
        haunter=pickle.load(f1)
        gengar=pickle.load(f1)
        abra=pickle.load(f1)
        kadabra=pickle.load(f1)
        alakazam=pickle.load(f1)
        machop=pickle.load(f1)
        machoke=pickle.load(f1)
        machamp=pickle.load(f1)
        geodude=pickle.load(f1)
        gravelar=pickle.load(f1)
        golem=pickle.load(f1)
        magmar=pickle.load(f1)
        flareon=pickle.load(f1)
        polywrath=pickle.load(f1)
        golduck=pickle.load(f1)
        taurus=pickle.load(f1)
        onix=pickle.load(f1)
        fearow=pickle.load(f1)
        farfetch=pickle.load(f1)
        dragonite=pickle.load(f1)
        zapdos=pickle.load(f1)
        vaporeon=pickle.load(f1)
        pokeballs=pickle.load(f2)
        potion=pickle.load(f2)
        pokecoins=pickle.load(f2)
        earth=pickle.load(f2)
        fire=pickle.load(f2)
        aqua=pickle.load(f2)
        aerial=pickle.load(f2)
        sector0=pickle.load(f2)
        sector1=pickle.load(f2)
        sector2=pickle.load(f2)
        sector4=pickle.load(f2)
        sector5=pickle.load(f2)
        sector6=pickle.load(f2)
        sector8=pickle.load(f2)
        sector9=pickle.load(f2)
        pokeindex=pickle.load(f2)
        f1.close()
        f2.close()
        home()
        
        


