def checkKeys(): 
    global player, lasers 
    if keyboard.space:        
        l = len(lasers)        
        lasers.append(Actor("laser2", (player.x, player.y-32)))
        [l].status = 0        
        lasers[l].type = 1


def drawLasers(): 
    for l in range(len(lasers)): 
        lasers[l].draw()


def updateLasers(): 
    global lasers, aliens 
    for l in range(len(lasers)): 
        if lasers[l].type == 0:            
            lasers[l].y += (2*DIFFICULTY)            
            checkLaserHit(l) 
            if lasers[l].y > 600: 
                lasers[l].status = 1 
            if lasers[l].type == 1:            
                lasers[l].y -= 5            
                checkPlayerLaserHit(l) 
            if lasers[l].y < 10: 
                lasers[l].status = 1    
    lasers = listCleanup(lasers)    
    aliens = listCleanup(aliens)