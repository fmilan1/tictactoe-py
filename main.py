import pygame, time

bgColor = [240, 240, 240]
t = time.time()
running = True
screenWidth = 400
screenHeight = screenWidth
tableLineSize = 5
slotWidth = screenWidth / 3
slotHeight = screenHeight / 3
slots = [["", "", ""], ["", "", ""], ["", "", ""]]
letterWeight = 15
players = ["x", "o"]
currentPlayer = players[0]
canmove = True
honnan, hova = [-10, -10], [-10, -10]
window = pygame.display.set_mode([screenWidth, screenHeight])
pygame.display.set_caption("Tic Tac Toe")
xColors, oColors = [[0, 255, 0], [200, 255, 0]], [[255, 100, 0], [255, 200, 0]]
xColor, oColor = xColors[0], oColors[0]


def drawTable():
    pygame.draw.rect(window, [0, 0, 0], [0 - tableLineSize / 2, 0, tableLineSize, screenHeight])
    pygame.draw.rect(window, [0, 0, 0], [screenWidth / 3 - tableLineSize / 2, 0, tableLineSize, screenHeight])
    pygame.draw.rect(window, [0, 0, 0], [screenWidth * (2 / 3) - tableLineSize / 2, 0, tableLineSize, screenHeight])
    pygame.draw.rect(window, [0, 0, 0], [screenWidth - tableLineSize / 2, 0, tableLineSize, screenHeight])

    pygame.draw.rect(window, [0, 0, 0], [0, 0 - tableLineSize / 2, screenWidth, tableLineSize])
    pygame.draw.rect(window, [0, 0, 0], [0, screenHeight / 3 - tableLineSize / 2, screenWidth, tableLineSize])
    pygame.draw.rect(window, [0, 0, 0], [0, screenHeight * (2 / 3) - tableLineSize / 2, screenWidth, tableLineSize])
    pygame.draw.rect(window, [0, 0, 0], [0, screenHeight - tableLineSize / 2, screenWidth, tableLineSize])

def drawLetters():
    for i, item in enumerate(slots):
        for j, jItem in enumerate(slots[i]):
            if (jItem == "x"):
                pygame.draw.line(window, xColor, [j * slotWidth + tableLineSize / 2 + letterWeight / 2, i * slotHeight + tableLineSize / 2], [j * slotWidth + slotWidth - tableLineSize / 2 - 1 - letterWeight / 2, i * slotHeight + slotHeight - tableLineSize / 2 - 1], letterWeight + int(letterWeight / 3))
                pygame.draw.line(window, xColor, [j * slotWidth + slotWidth - tableLineSize / 2 - 1 - letterWeight / 2, i * slotHeight + tableLineSize / 2], [j * slotWidth + tableLineSize / 2 + letterWeight / 2, i * slotHeight + slotHeight - tableLineSize / 2 - 1], letterWeight + int(letterWeight / 3))
            elif (jItem == "o"):
                pygame.draw.circle(window, oColor, [j * slotWidth + slotWidth / 2, i * slotHeight + slotHeight / 2], screenWidth / letterWeight * 2.4)
                pygame.draw.circle(window, bgColor, [j * slotWidth + slotWidth / 2, i * slotHeight + slotHeight / 2], screenWidth / letterWeight * 2.4 - letterWeight)



def draw():
    window.fill(bgColor)
    drawLetters()
    drawTable()



while running:
    draw()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        if (canmove and event.type == pygame.MOUSEBUTTONUP):
            x, y = pygame.mouse.get_pos()
            for i, item in enumerate(slots):
                for j, jItem in enumerate(slots[i]):
                    if (slots[i][j] == "" and x >= j * slotWidth and x <= j * slotWidth + slotWidth and y >= i * slotHeight and y <= i * slotHeight + slotHeight):
                        slots[i][j] = currentPlayer
                        currentPlayer = players[len(players) - players.index(currentPlayer) - 1]

            for i, item in enumerate(slots[0]):
                if (slots[0][i] != "" and slots[0][i] == slots[1][i] and slots[0][i] == slots[2][i]):
                    canmove = False
            for i, item in enumerate(slots):
                if (slots[i][0] != "" and slots[i][0] == slots[i][1] and slots[i][0] == slots[i][2]):
                    canmove = False
            if (slots[0][0] != "" and slots[1][1] == slots[0][0] and slots[2][2] == slots[0][0]):
                canmove = False
            elif (slots[0][2] != "" and slots[1][1] == slots[0][2] and slots[2][0] == slots[0][2]):
                canmove = False
    if (not canmove):
        if (time.time() - t >= 0.5):
            if (players[len(players) - players.index(currentPlayer) - 1] == "x"):
                xColor = xColors[len(xColors) - xColors.index(xColor) - 1]
            elif (players[len(players) - players.index(currentPlayer) - 1] == "o"):
                oColor = oColors[len(oColors) - oColors.index(oColor) - 1]
            t = time.time()
    pygame.display.flip()
