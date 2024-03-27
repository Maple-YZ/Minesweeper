# 导入pygame和sys
import pygame
import random
import sys

# 初始化数值
screensize = scwidth, scheight = 375, 375
cellsize = 9, 9
Lclicked = False
Rclicked = False
mines = []
defeat = False
victory = False
# 0=未开 1-8=数字 9=插旗 10=空白 11=炸弹
cellstates = []
cellcount = 0
openedcount = 0
minecount = 0
ischosen = False
for i in mines:
    minecount += sum(i)

# 初始化窗体
pygame.init()
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("minesweeperV1.0")

# 初始化素材
boom = pygame.image.load("resource/boom.png")
pygame.display.set_icon(boom)

flag = pygame.image.load("resource/flag.png")
opened = pygame.image.load("resource/opened.png")
chosen = pygame.image.load("resource/chosen.png")
nonopened = pygame.image.load("resource/nonopened.png")
# victoryp = pygame.image.load("resource/victory.png")
defeatp = pygame.image.load("resource/defeat.png")
num1 = pygame.image.load("resource/1.png")
num2 = pygame.image.load("resource/2.png")
num3 = pygame.image.load("resource/3.png")
num4 = pygame.image.load("resource/4.png")
num5 = pygame.image.load("resource/5.png")
num6 = pygame.image.load("resource/6.png")
num7 = pygame.image.load("resource/7.png")
num8 = pygame.image.load("resource/8.png")

font = pygame.font.SysFont('SimHei', 20)
vicstr = '恭喜获胜!'
tipstr = '数字按键1-3可以选择难度'
defstr = '你输啦，菜鸡!'
vicword = font.render(vicstr, True, (255, 255, 255))
tipword = font.render(tipstr, True, (255, 255, 255))
defword = font.render(defstr, True, (255, 255, 255))


# 建立坐标系
def posis(pos):
    x = pos[0] // 25 - 3
    y = pos[1] // 25 - 3
    return x, y


# 绘制图像函数
def draw(pos, type):
    # print(pos, type)
    screen.blit(type, ((pos[0] + 3) * 25, (pos[1] + 3) * 25))


# 左键单击
def Lclick(pos):
    global openedcount, defeat, victory
    # 判断是否在可点击空间
    if 0 <= pos[0] < len(mines[0]) and 0 <= pos[1] < len(mines):
        # print("在游玩区域中，位置为：{}，游戏地区为{}行{}列".format(pos, len(booms[0]), len(booms[1])))
        # 判断是否尚未点击
        if cellstates[pos[1]][pos[0]] == 0:
            # 判断是否为炸弹
            if mines[pos[1]][pos[0]]:
                if openedcount == 0:
                    fresh((len(mines[0]), len(mines)), minecount)
                    Lclick(pos)
                else:
                    draw(pos, boom)
                    # print('{}处是地雷，你输了'.format(pos))
                    screen.blit(defword, (75, 25))
                    screen.blit(tipword, (75, 50))
                    defeat = True
            else:
                openedcount += 1
                count = 0
                for boomrow in mines[max(0, pos[1] - 1):min(len(mines), pos[1] + 2)]:
                    for boomcheck in boomrow[max(0, pos[0] - 1):min(len(boomrow), pos[0] + 2)]:
                        count += boomcheck
                        # print(count)
                if count:
                    # print('count:', count)
                    exec('draw(pos,num{})'.format(count))
                    cellstates[pos[1]][pos[0]] = count
                else:
                    draw(pos, opened)
                    # print('pos', pos, 'opened')
                    cellstates[pos[1]][pos[0]] = 10
                    for y in range(max(0, pos[1] - 1), min(len(cellstates), pos[1] + 2)):
                        for x in range(max(0, pos[0] - 1), min(len(cellstates[0]), pos[0] + 2)):
                            # print('x,y =', x, y)
                            Lclick((x, y))
                if openedcount == cellcount - minecount:
                    # print('恭喜你，赢啦')
                    # screen.blit(victoryp, (75, 0))
                    screen.blit(vicword, (75, 25))
                    screen.blit(tipword, (75, 50))
                    victory = True
                    return
        # print('Lclick')


# 右键单击
def Rclick(pos):
    if 0 <= pos[0] < len(mines[0]) and 0 <= pos[1] < len(mines):
        if cellstates[pos[1]][pos[0]] == 0:
            draw(pos, flag)
            cellstates[pos[1]][pos[0]] = 9
        elif cellstates[pos[1]][pos[0]] == 9:
            draw(pos, nonopened)
            cellstates[pos[1]][pos[0]] = 0
        # print('Rclick')


# 同时点击
def Bclick(pos):
    if 0 <= pos[0] < len(mines[0]) and 0 <= pos[1] < len(mines):
        count = 0
        for y in range(max(0, pos[1] - 1), min(len(cellstates), pos[1] + 2)):
            for x in range(max(0, pos[0] - 1), min(len(cellstates[0]), pos[0] + 2)):
                if cellstates[y][x] == 9:
                    count += 1
        if count == cellstates[pos[1]][pos[0]]:
            for y in range(max(0, pos[1] - 1), min(len(cellstates), pos[1] + 2)):
                if victory:
                    return
                for x in range(max(0, pos[0] - 1), min(len(cellstates[0]), pos[0] + 2)):
                    if victory:
                        return
                    Lclick((x, y))
        # print('Bclick')


# 刷新
def fresh(size=(10, 10), boomnum=5):
    global Lclicked, Rclicked, cellstates, cellcount, openedcount, mines, minecount, defeat, victory, cellsize
    # print(Lclicked,Rclicked)
    screensize = size[0] * 25 + 150, size[1] * 25 + 150
    screen = pygame.display.set_mode(screensize)
    Lclicked = False
    Rclicked = False
    defeat = False
    victory = False
    cellsize = size
    ls = [[0 for i in range(size[0])] for i in range(size[1])]
    screen.fill((50, 50, 50))
    mines = [[0 for i in range(size[0])] for i in range(size[1])]
    for id in random.sample(range(cellsize[0] * cellsize[1]), boomnum):
        x = id % cellsize[0]
        y = id // cellsize[0]
        mines[y][x] = 1
    # 0=未开 1-8=数字 9=插旗 10=空白 11=炸弹
    cellstates = [[0 for i in range(size[0])] for i in range(size[1])]

    cellcount = len(mines) * len(mines[0])
    openedcount = 0
    minecount = boomnum
    for x in range(size[0]):
        for y in range(size[1]):
            draw((x, y), nonopened)


# 初次刷新
fresh()
# 游戏主循环
while True:
    # 事件处理
    for event in pygame.event.get():
        # 退出事件
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 鼠标按下事件
            if defeat == True or victory == True:
                pass
            elif event.button == 1:
                Lpos = posis(event.pos)
                if 0 <= Lpos[0] < len(mines[0]) and 0 <= Lpos[1] < len(mines):
                    if cellstates[Lpos[1]][Lpos[0]] == 0:
                        draw(Lpos, chosen)
                        ischosen = True
                Lclicked = True
            elif event.button == 3:
                Rpos = posis(event.pos)
                Rclicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            # print(event.button)
            # 鼠标抬起事件
            Nowpos = posis(event.pos)
            if defeat == True or victory == True:
                pass
            elif event.button == 1:
                if Rclicked and Lclicked:
                    if Lpos == Rpos and Lpos == Nowpos:
                        Bclick(Nowpos)
                    Lclicked = False
                    Rclicked = False
                elif Lclicked:
                    if Nowpos == Lpos:
                        Lclick(Nowpos)
                    elif ischosen:
                        draw(Lpos, nonopened)
                        ischosen = False
                    Lclicked = False
            elif event.button == 3:
                if Rclicked and Lclicked:
                    if Lpos == Rpos and Lpos == Nowpos:
                        Bclick(Nowpos)
                    Lclicked = False
                    Rclicked = False
                elif Rclicked:
                    if Nowpos == Rpos:
                        Rclick(Nowpos)
                    Rclicked = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                fresh((9, 9), 10)
            elif event.key == pygame.K_2:
                fresh((16, 16), 40)
            elif event.key == pygame.K_3:
                fresh((30, 16), 99)
    # 窗口刷新
    pygame.display.update()
