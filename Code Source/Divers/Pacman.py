# Ce code n'est pas tellement fait pour tourner, mais juste pour s'en inspirer
# Code de Innohvateur

import pygame, math, random

pygame.init()
screen = pygame.display.set_mode((23 * 24, 23 * 24))
clock = pygame.time.Clock()
running = True
dt = clock.tick(60) / 1000

tiles = {0: "tiles/0.png", 3: "tiles/3.png", 4: "tiles/4.png", 5: "tiles/5.png", 6: "tiles/6.png", 7: "tiles/7.png",
         8: "tiles/8.png", 9: "tiles/9.png", 10: "tiles/10.png", 11: "tiles/11.png", 12: "tiles/12.png",
         13: "tiles/13.png", 14: "tiles/14.png", 15: "tiles/15.png", 16: "tiles/16.png", 17: "tiles/17.png"}
array_map = [[3, 8, 8, 8, 16, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 16, 8, 8, 8, 4],
             [7, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 7],
             [7, 0, 17, 0, 9, 0, 12, 8, 16, 8, 11, 0, 12, 8, 16, 8, 11, 0, 9, 0, 17, 0, 7],
             [7, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 7],
             [13, 8, 11, 0, 10, 0, 10, 0, 7, 0, 3, 8, 4, 0, 7, 0, 10, 0, 10, 0, 12, 8, 15],
             [7, 0, 0, 0, 7, 0, 7, 0, 7, 0, 7, 18, 7, 0, 7, 0, 7, 0, 7, 0, 0, 0, 7],
             [7, 0, 17, 0, 7, 0, 7, 0, 9, 0, 5, 8, 6, 0, 9, 0, 7, 0, 7, 0, 17, 0, 7],
             [7, 0, 0, 0, 7, 0, 7, 0, 18, 0, 18, 0, 18, 0, 18, 0, 7, 0, 7, 0, 0, 0, 7],
             [13, 8, 8, 8, 6, 0, 7, 0, 12, 8, 8, 8, 8, 8, 11, 0, 7, 0, 5, 8, 8, 8, 15],
             [7, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 7],
             [9, 18, 12, 8, 8, 8, 6, 0, 3, 8, 11, 18, 12, 8, 4, 0, 5, 8, 8, 8, 11, 18, 9],
             [0, 0, 0, 0, 0, 0, 0, 0, 7, 18, 18, 18, 18, 18, 7, 0, 0, 0, 0, 0, 0, 0, 0],
             [10, 18, 12, 8, 8, 8, 4, 0, 5, 8, 8, 8, 8, 8, 6, 0, 3, 8, 8, 8, 11, 18, 10],
             [7, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 7],
             [13, 8, 8, 8, 4, 0, 7, 0, 12, 8, 8, 8, 8, 8, 11, 0, 7, 0, 3, 8, 8, 8, 15],
             [7, 0, 0, 0, 7, 0, 7, 0, 18, 0, 18, 0, 18, 0, 18, 0, 7, 0, 7, 0, 0, 0, 7],
             [7, 0, 17, 0, 7, 0, 7, 0, 10, 0, 3, 8, 4, 0, 10, 0, 7, 0, 7, 0, 17, 0, 7],
             [7, 0, 0, 0, 7, 0, 7, 0, 7, 0, 7, 18, 7, 0, 7, 0, 7, 0, 7, 0, 0, 0, 7],
             [13, 8, 11, 0, 9, 0, 9, 0, 7, 0, 5, 8, 6, 0, 7, 0, 9, 0, 9, 0, 12, 8, 15],
             [7, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 7],
             [7, 0, 17, 0, 10, 0, 12, 8, 14, 8, 11, 0, 12, 8, 14, 8, 11, 0, 10, 0, 17, 0, 7],
             [7, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 7],
             [5, 8, 8, 8, 14, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 14, 8, 8, 8, 6]]


def affiche():
    for y in range(len(array_map)):
        for x in range(len(array_map[y])):
            if (array_map[y][x] != 18 and array_map[y][x] != 19):
                img = pygame.image.load(tiles[array_map[y][x]])
                screen.blit(img, (x * 24, y * 24))


def affiche_single(x, y):
    if (array_map[y][x] != 18 and array_map[y][x] != 19):
        img = pygame.image.load(tiles[array_map[y][x]])
        print(f"I have printed ${tiles[array_map[y][x]]}")
        screen.blit(img, (x * 24, y * 24))


def draw_rect(x, y, direction):
    rect = pygame.Rect(x * 24, y * 24, 30, 30)
    #     match direction:
    #         case "up":
    #             rect = pygame.Rect(x*24, y*24, 30, 51)
    #         case "left":
    #             rect = pygame.Rect(x*24, y*24, 51, 30)
    if direction == "up":
        rect = pygame.Rect(x * 24, y * 24, 30, 51)
    if direction == "left":
        rect = pygame.Rect(x * 24, y * 24, 51, 30)
    pygame.draw.rect(screen, "black", rect)


def gen_man(dest):
    mans = [[-1 for i in range(23)] for i in range(23)]
    for x in range(23):
        for y in range(23):
            if not (array_map[y][x] in list(range(3, 18))):
                mans[y][x] = abs(x - dest.x) + abs(y - dest.y)
    return mans


class Monster:
    def __init__(self, color):
        self.x = 11.0
        self.y = 11.0
        self.man = -1
        self.color = color
        self.state = None
        self.sprite = None

    def setState(self, newstate):
        self.state = newstate

    def getState(self):
        return self.state

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def shiftX(self, dx):
        self.x += dx

    def shiftY(self, dy):
        self.y += dy

    def draw(self):
        # img = pygame.image.load("sprites/" + self.sprite)
        # screen.blit(img, (self.x * 24, self.y * 24))
        rect = pygame.Rect(self.x * 24, self.y * 24, 30, 30)
        pygame.draw.rect(screen, self.color, rect)

    def update_man(self, dest):
        self.man = abs(self.x - dest.x) + abs(self.y - dest.y)


class PacMan:
    def __init__(self):
        self.x = 11.0
        self.y = 13.0
        self.state = None
        self.powered = False;
        self.lives = 3
        self.sprite = "pacman_r.png"

    def setState(self, newstate):
        if newstate == "up":
            if self.sprite == "pacman_l.png":
                self.sprite = "pacman_u_prev_l.png"
            elif self.sprite == "pacman_r.png":
                self.sprite = "pacman_u_prev_r.png"
            elif self.sprite == "pacman_d_prev_l.png":
                self.sprite = "pacman_u_prev_r.png"
            elif self.sprite == "pacman_d_prev_r.png":
                self.sprite = "pacman_u_prev_l.png"
        elif newstate == "down":
            if self.sprite == "pacman_l.png":
                self.sprite = "pacman_d_prev_l.png"
            elif self.sprite == "pacman_r.png":
                self.sprite = "pacman_d_prev_r.png"
            elif self.sprite == "pacman_u_prev_l.png":
                self.sprite = "pacman_d_prev_r.png"
            elif self.sprite == "pacman_u_prev_r.png":
                self.sprite = "pacman_d_prev_l.png"
        elif newstate == "right":
            self.sprite = "pacman_r.png"
        elif newstate == "left":
            self.sprite = "pacman_l.png"
        self.state = newstate

    def getState(self):
        return self.state

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def power(self):
        self.powered = True

    def unpower(self):
        self.powered = False

    def die(self):
        self.lives -= 1

    def heal(self):
        self.lives += 1

    def shiftX(self, dx):
        self.x += dx

    def shiftY(self, dy):
        self.y += dy

    def draw(self):
        img = pygame.image.load("sprites/" + self.sprite)
        screen.blit(img, (self.x * 24, self.y * 24))


player = PacMan()
monsters = [Monster("purple")]
screen.fill("black")
affiche()
prevPlayer = (11, 13, "right")
prevMonsters = [(11, 11, "right") for i in range(len(monsters))]
while running:
    draw_rect(int(player.getX()), int(player.getY()), player.getState())
    draw_rect(prevPlayer[0], prevPlayer[1], prevPlayer[2])
    player.draw()

    prevPlayer = (int(player.getX()), int(player.getY()), player.getState())

    for i in range(len(monsters)):
        draw_rect(int(monsters[i].getX()), int(monsters[i].getY()), monsters[i].getState())
        draw_rect(prevMonsters[i][0], prevMonsters[i][1], prevMonsters[i][2])
        monsters[i].draw()

        prevMonsters[i] = (int(monsters[i].getX()), int(monsters[i].getY()), monsters[i].getState())

    # affiche_single(int(player.getY() % 4), int(player.getX() % 4))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    keys = pygame.key.get_pressed()
    if ((player.getX()).is_integer() and (player.getY()).is_integer()):
        if array_map[int(player.getY())][int(player.getX())] == 0:
            array_map[int(player.getY())][int(player.getX())] = 18
    if keys[pygame.K_UP] and (player.getX()).is_integer():
        if [0, 1, 2, 18, 19].__contains__(array_map[(int)(player.getY()) - 1][(int)(player.getX())]):
            player.setState("up")
    elif keys[pygame.K_RIGHT] and (player.getY()).is_integer():
        if (player.getX(), player.getY()) == (22, 11) or [0, 1, 2, 18, 19].__contains__(
                array_map[(int)(player.getY())][(int)(player.getX()) + 1]):
            player.setState("right")
    elif keys[pygame.K_DOWN] and (player.getX()).is_integer():
        if [0, 1, 2, 18, 19].__contains__(array_map[(int)(player.getY()) + 1][(int)(player.getX())]):
            player.setState("down")
    elif keys[pygame.K_LEFT] and (player.getY()).is_integer():
        if (player.getX(), player.getY()) == (0, 11) or [0, 1, 2, 18, 19].__contains__(
                array_map[(int)(player.getY())][(int)(player.getX()) - 1]):
            player.setState("left")

    if player.getState() == "left" and (player.getX(), player.getY()) == (0, 11):
        player.x = 22
    elif player.getState() == "right" and (player.getX(), player.getY()) == (22, 11):
        player.x = 0
    if player.getState() == "up" and (player.getX()).is_integer() and [0, 1, 2, 18, 19].__contains__(
            array_map[math.ceil(player.getY()) - 1][math.floor(player.getX())]):
        player.shiftY(-0.125)
    elif player.getState() == "right" and (player.getY()).is_integer() and [0, 1, 2, 18, 19].__contains__(
            array_map[math.floor(player.getY())][math.floor(player.getX()) + 1]):
        player.shiftX(0.125)
    elif player.getState() == "down" and (player.getX()).is_integer() and [0, 1, 2, 18, 19].__contains__(
            array_map[math.floor(player.getY()) + 1][math.floor(player.getX())]):
        player.shiftY(0.125)
    elif player.getState() == "left" and (player.getY()).is_integer() and [0, 1, 2, 18, 19].__contains__(
            array_map[math.floor(player.getY())][math.ceil(player.getX()) - 1]):
        player.shiftX(-0.125)

    mans = gen_man(player)
    for m in monsters:
        m.update_man(player)

        if mans[(int)(m.getY()) - 1][(int)(m.getX())] >= 0 and mans[(int)(m.getY()) - 1][(int)(m.getX())] < m.man and (
        m.getX()).is_integer() and array_map[(int)(m.getY()) - 1][(int)(m.getX())] in [0, 1, 2, 18, 19]:
            m.setState("up")
        elif mans[(int)(m.getY())][(int)(m.getX()) + 1] >= 0 and mans[(int)(m.getY())][
            (int)(m.getX()) + 1] < m.man and (m.getY()).is_integer() and array_map[(int)(m.getY())][
            (int)(m.getX()) + 1] in [0, 1, 2, 18, 19]:
            m.setState("right")
        elif mans[(int)(m.getY()) + 1][(int)(m.getX())] >= 0 and mans[(int)(m.getY()) + 1][
            (int)(m.getX())] < m.man and (m.getX()).is_integer() and array_map[(int)(m.getY()) + 1][
            (int)(m.getX())] in [0, 1, 2, 18, 19]:
            m.setState("down")
        elif mans[(int)(m.getY())][(int)(m.getX()) - 1] >= 0 and mans[(int)(m.getY())][
            (int)(m.getX()) - 1] < m.man and (m.getY()).is_integer() and array_map[(int)(m.getY())][
            (int)(m.getX()) - 1] in [0, 1, 2, 18, 19]:
            m.setState("left")
        elif (m.getY()).is_integer() and (m.getX()).is_integer():
            states = ["up", "right", "down", "left"]
            i = random.randint(0, 3)
            m.setState(states[i])

        if m.getState() == "left" and (m.getX(), m.getY()) == (0, 11):
            m.x = 22
        elif m.getState() == "right" and (m.getX(), m.getY()) == (22, 11):
            m.x = 0
        if m.getState() == "up" and (m.getX()).is_integer() and array_map[math.ceil(m.getY()) - 1][
            math.floor(m.getX())] in [0, 1, 2, 18, 19]:
            m.shiftY(-0.0625)
        elif m.getState() == "right" and (m.getY()).is_integer() and array_map[math.floor(m.getY())][
            math.floor(m.getX()) + 1] in [0, 1, 2, 18, 19]:
            m.shiftX(0.0625)
        elif m.getState() == "down" and (m.getX()).is_integer() and array_map[math.floor(m.getY()) + 1][
            math.floor(m.getX())] in [0, 1, 2, 18, 19]:
            m.shiftY(0.0625)
        elif m.getState() == "left" and (m.getY()).is_integer() and array_map[math.floor(m.getY())][
            math.ceil(m.getX()) - 1] in [0, 1, 2, 18, 19]:
            m.shiftX(-0.0625)
    dt = clock.tick(60) / 1000
pygame.quit()