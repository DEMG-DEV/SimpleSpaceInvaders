def init():
    global lasers, score, player, moveSequence, moveCounter, moveDelay
    initAliens()
    initBases()
    moveCounter = moveSequence = player.status = score = player.laserCountdown = 0
    lasers = []
    moveDelay = 30
    player.images = ["player", "explosion1", "explosion2",
                     "explosion3", "explosion4", "explosion5"]
    player.laserActive = 1
