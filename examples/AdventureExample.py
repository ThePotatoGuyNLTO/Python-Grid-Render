import extra.grid as grid

import random

key = ""

playerx = 1
playery = 1

player_attack = 2

enemy_alive = True

in_battle = False
current_enemy_health = 10

enemy_position = [3,2]

gold = 0

room = 0

while True:
    
    if key == "d" and not grid.get_grid_spot(playerx+1,playery)== "7":
        playerx += 1
    if key == "a" and not grid.get_grid_spot(playerx-1,playery) == "7":
        playerx -= 1
    if key == "s" and not grid.get_grid_spot(playerx,playery+1) == "7":
        playery += 1
    if key == "w" and not grid.get_grid_spot(playerx,playery-1) == "7":
        playery -= 1

    grid.set_bkg_image("examples/extra/background.txt")
    grid.create_spr(playerx,playery,1,0)

    if grid.check_spr_pos(0,2,0):
        enemy_position = [round(random.random()*2)+1,round(random.random()*2)]
        enemy_alive = True
        playerx = 2
        playery = 3
        current_enemy_health = 10
        room += 1
    if grid.check_spr_pos(0,2,4):
        if room > 0:
            enemy_position = [round(random.random()*2)+1,round(random.random()*2)]
            enemy_alive = True
            playerx = 2
            playery = 1
            current_enemy_health = 10
            room -= 1
        else:
            playerx = 2
            playery = 3
    
    if grid.collide_spr(0,1):
        if key == "attack":
            if not in_battle and enemy_alive:
                in_battle = True
            else:
                damage = round(round(random.random()*10)/5)*player_attack
                current_enemy_health -= damage
                if damage == 0:
                    print("MISS")
    if in_battle:
        if current_enemy_health < 1:
            in_battle = False
            enemy_alive = False
            gold += round(random.random()*4)+1
    
    grid.create_spr(playerx,playery,1,0)
    
    grid.create_spr(enemy_position[0],enemy_position[1],5,1)
    
    if enemy_alive:
        grid.show_spr(1)

    grid.show_spr(0)
    grid.render_grid()

    if in_battle:
        print("BATTLE",current_enemy_health)
    
    if key == "upgrade":
        if gold > ((player_attack-1)*10)-1:
            gold -= ((player_attack-1)*10)
            player_attack += 1
        
    gold_display = f"${gold}"
    
    print(gold_display,",ATTACK :",player_attack, ",ROOM",room)
    
    past_key = key
    
    key = grid.get_input()
    
    grid.clear_grid()