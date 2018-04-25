#Author: Ivan Yurkin
#to run type py Monster_Arena.py or python3 Monster_Arena.py
import random
import tkinter
#set up gui
tk = tkinter.Tk()
name = tkinter.StringVar()
monster_hp_str = tkinter.StringVar()
hero_hp_str = tkinter.StringVar()
#display main screen
def start_game():
    title.place_forget()
    button_start.place_forget()
    play_again.place_forget()
    name_label.place(x=150,y=50, width=300, height=100)
    name_ask.place(x=250,y=200, width=100, height=20)
    continue_game.place(x=250, y=300, width=100, height=50)

def continue_start():
    name_label.place_forget()
    name_ask.place_forget()
    continue_game.place_forget()
    play_again.place_forget()
    win_mes.place_forget()
    lose_mes.place_forget()
    name_hero = name_ask.get()
    welcome_message = tkinter.Label(text='Welcome ' + name_hero,font = 16)
    welcome_message.place(x=225,y=50, width=150, height=50)
    question_character.place(x=150,y=100, width=300, height=100)
    hero_1.place(x=175 , y=200 , width=50 , height= 50)
    hero_2.place(x=225 , y=200 , width=50 , height= 50)
    hero_3.place(x=275 , y=200 , width=50 , height= 50)
    hero_4.place(x=325 , y=200 , width=50 , height= 50)
    hero_5.place(x=375 , y=200 , width=50 , height= 50)

def continue_hero_stats(hero_level):
    global hero_attack
    global hero_hp
    global hero_max_hp
    global hero_defense
    global hero_healing
    question_character.place_forget()
    hero_1.place_forget()
    hero_2.place_forget()
    hero_3.place_forget()
    hero_4.place_forget()
    hero_5.place_forget()
    hero_hp = 100 + (hero_level * 20)
    hero_max_hp = hero_hp
    hero_attack = hero_level
    hero_defense = hero_level
    hero_healing = hero_level
    hero_health = tkinter.Label(text='Hero Health',font = 14)
    hero_health.place(x=30,y=50, width=120, height=50)
    hero_hp_str.set(str(hero_hp))
    hero_hp_current = tkinter.Label(text=str(hero_hp),font = 14)
    hero_hp_current.place(x=30,y=100, width=120, height=50)
    question_monster.place(x=150,y=100, width=300, height=100)
    monster_1.place(x=175 , y=200 , width=50 , height= 50)
    monster_2.place(x=225 , y=200 , width=50 , height= 50)
    monster_3.place(x=275 , y=200 , width=50 , height= 50)
    monster_4.place(x=325 , y=200 , width=50 , height= 50)
    monster_5.place(x=375 , y=200 , width=50 , height= 50)

def continue_monster_stats(monster_level):
    global monster_attack
    global monster_hp
    global monster_max_hp
    global monster_defense
    global monster_healing
    question_monster.place_forget()
    monster_1.place_forget()
    monster_2.place_forget()
    monster_3.place_forget()
    monster_4.place_forget()
    monster_5.place_forget()
    monster_hp = 100 + (monster_level * 40)
    monster_max_hp = monster_hp
    monster_attack = monster_level
    monster_defense = monster_level
    monster_healing = monster_level
    monster_health = tkinter.Label(text='Monster Health',font = 14)
    monster_health.place(x=420,y=50, width=150, height=50)
    choice.place(x=150,y=150, width=300, height=50)
    monster_hp_str.set(str(monster_hp))
    monster_hp_current = tkinter.Label(text=str(monster_hp),font = 14)
    monster_hp_current.place(x=420,y=100, width=150, height=50)
    hero_attack_now.place(x=250, y=200, width=100, height=50)
    hero_heal_now.place(x=250, y=275, width=100, height=50)

def hero_attacks():
    global monster_hp
    hero_hit = ((random.randint(5,15) + hero_attack * 2) - (random.randint(1,5) + monster_defense))
    monster_hp -= hero_hit
    monster_hp_current = tkinter.Label(text=str(monster_hp),font = 14)
    monster_hp_current.place(x=420,y=100, width=150, height=50)
    if monster_hp <= 0:
        win_screen()
    monster_action()
def hero_heals():
    global hero_hp
    hero_heal = random.randint(1,5) + hero_healing
    hero_hp += hero_heal
    if hero_hp > hero_max_hp:
        hero_hp = hero_max_hp
    hero_hp_current = tkinter.Label(text=str(hero_hp),font = 14)
    hero_hp_current.place(x=30,y=100, width=120, height=50)
    monster_action()

def monster_action():
    global monster_attack
    global monster_hp
    global monster_max_hp
    global monster_defense
    global monster_healing
    global hero_attack
    global hero_hp
    global hero_max_hp
    global hero_defense
    global hero_healing
    if monster_hp == monster_max_hp:
        monster_choice = 'attack'
    elif monster_hp <= 0:
        win_screen()
    else:
        monster_chance = random.randint(0,monster_hp)
        if monster_chance < monster_hp / 2:
            monster_choice = 'heal'
        else:
            monster_choice = 'attack'
            if monster_choice == 'attack':
                monster_hit =  ((random.randint(5,15) + monster_attack * 2) - (random.randint(1,5) + hero_defense))
                hero_hp -= monster_hit
    hero_hp_current = tkinter.Label(text=str(hero_hp),font = 14)
    hero_hp_current.place(x=30,y=100, width=120, height=50)
    monster_hp_current = tkinter.Label(text=str(monster_hp),font = 14)
    monster_hp_current.place(x=420,y=100, width=150, height=50)
    if hero_hp <= 0:
        lose_screen()

def win_screen():
    hero_attack_now.place_forget()
    hero_heal_now.place_forget()
    choice.place_forget()
    win_mes.place(x=175,y=150, width=250, height=50)
    play_again.place(x=250, y=300, width=100, height=50)

def lose_screen():
    hero_attack_now.place_forget()
    hero_heal_now.place_forget()
    choice.place_forget()
    lose_mes.place(x=150,y=150, width=300, height=50)
    play_again.place(x=250, y=300, width=100, height=50)
#set up screen and global vars and buttons that will be used in various functions
monster_attack =''
monster_hp =''
monster_max_hp =''
monster_defense =''
monster_healing =''
hero_attack =''
hero_hp =''
hero_max_hp =''
hero_defense =''
hero_healing =''
tk.geometry("600x480+30+30")
title = tkinter.Label(text='Welcome to Monster Arena!',font=16 )
title.place(x=150,y=50, width=300, height=100)
button_start = tkinter.Button(text ='Start Game',command = start_game)
button_start.place(x=250, y=300, width=100, height=50)
button_quit = tkinter.Button(text='Quit',command = tk.quit)
button_quit.place(x=250, y=350, width=100, height=50)
name_label = tkinter.Label(text='What is your name hero?',font=16 )
name_ask = tkinter.Entry(tk,text='Name: ',command=print(name.get()))
continue_game = tkinter.Button(text ='Continue',command = continue_start)
question_character = tkinter.Label(text='What is your hero level?',font=12 )
question_monster = tkinter.Label(text='What is your monster level?',font=12 )
hero_1 = tkinter.Button(text ='1',command=lambda *args: continue_hero_stats(1))
hero_2 = tkinter.Button(text ='2',command=lambda *args: continue_hero_stats(2))
hero_3 = tkinter.Button(text ='3',command=lambda *args: continue_hero_stats(3))
hero_4 = tkinter.Button(text ='4',command=lambda *args: continue_hero_stats(4))
hero_5 = tkinter.Button(text ='5',command=lambda *args: continue_hero_stats(5))
monster_1 = tkinter.Button(text ='1',command=lambda *args: continue_monster_stats(1))
monster_2 = tkinter.Button(text ='2',command=lambda *args: continue_monster_stats(2))
monster_3 = tkinter.Button(text ='3',command=lambda *args: continue_monster_stats(3))
monster_4 = tkinter.Button(text ='4',command=lambda *args: continue_monster_stats(4))
monster_5 = tkinter.Button(text ='5',command=lambda *args: continue_monster_stats(5))
monster_hp_current = tkinter.Label(text=str(monster_hp),font = 14)
choice = tkinter.Label(text='Do you want to attack or heal?',font=16)
hero_attack_now =  tkinter.Button(text ='Attack',command=hero_attacks)
hero_heal_now =  tkinter.Button(text ='Heal',command=lambda *args: hero_heals())
win_mes = tkinter.Label(text='Congratulations you win!',font=16)
lose_mes = tkinter.Label(text='You lose, better luck next time',font=16)
play_again = tkinter.Button(text='Play Again',command=continue_start)
#show gui
tk.mainloop()
# while 1==1:
#
#     #Generate hero and monster stats from user input
#     print("Hello welcome to the monster arena ")
#     name = input("State your name hero: ")
#     print('Hello '+ name)
#     hero_level = int(input('What is your level hero(1-5): '))
#     hero_hp = 100 + (hero_level * 20)
#     hero_max_hp = hero_hp
#     hero_attack = hero_level
#     hero_defense = hero_level
#     hero_healing = hero_level
#     monster_level = int(input('What level of monster would you wish to fight(1-5): '))
#     monster_hp = 100 + (monster_level * 20)
#     monster_max_hp = monster_hp
#     monster_attack = monster_level
#     monster_defense = monster_level
#     monster_healing = monster_level
#     #runs while both of the characters are alive
#     while hero_hp > 0 and monster_hp > 0:
#         print('Your hp is: ' + str(hero_hp))
#         print('The monster\'s hp is: ' + str(monster_hp))
#         hero_choice = input('Would you like to attack or heal: ')
#         if hero_choice == 'attack':
#             hero_hit = ((random.randint(5,15) + hero_attack * 2) - (random.randint(1,5) + monster_defense))
#             monster_hp -= hero_hit
#             print('You hit the monster for ' + str(hero_hit) + ' damage')
#         else:
#             hero_heal = random.randint(1,5) + hero_healing
#             hero_hp += hero_heal
#             print('You healed for ' + str(hero_heal) + ' hp')
#             if hero_hp > hero_max_hp:
#                 hero_hp = hero_max_hp
#         if monster_hp > 0:
#             if monster_hp == monster_max_hp:
#                 monster_choice = 'attack'
#             else:
#                 monster_chance = random.randint(0,monster_hp)
#                 if monster_chance < monster_hp / 2:
#                     monster_choice = 'heal'
#                 else:
#                     monster_choice = 'attack'
#                     if monster_choice == 'attack':
#                         monster_hit =  ((random.randint(5,15) + monster_attack * 2) - (random.randint(1,5) + hero_defense))
#                         hero_hp -= monster_hit
#                         print('Monster hit you for ' + str(monster_hit) + ' damage')
#                     else:
#                         monster_heal = random.randint(1,5) + monster_healing
#                         monster_hp += monster_heal
#                         print('Monster healed for ' + str(monster_heal) + ' hp')
#                         if monster_hp > monster_max_hp:
#                             monster_hp = monster_max_hp
#     #determine who won
#     if hero_hp < 0:
#         print('You lose!')
#     elif monster_hp < 0:
#         print('You win!')
#     #asks user if they want to play again
#     play_again = input('Would you like to play again?(y/n): ')
#     if play_again == 'y':
#         continue
#     else:
#         break
