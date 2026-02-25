import sys, pygame, os

def resource_path(relative_path):
    """获取资源的绝对路径，适用于开发环境和 PyInstaller 打包后的 exe"""
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller 会创建临时文件夹，将资源文件放在 _MEIPASS 中
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

pygame.init()
pygame.mixer.init()

size = width, height = 1920, 1080
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

# 播放音频
pygame.mixer.music.load(resource_path('qier.mp3'))
pygame.mixer.music.play(-1)  # -1表示无限循环播放

shit = pygame.image.load(resource_path("couqier.gif"))
shitrect = shit.get_rect()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    shitrect = shitrect.move(speed)
    if shitrect.left < 0 or shitrect.right > width:
        speed[0] = -speed[0]
    if shitrect.top < 0 or shitrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(shit, shitrect)
    pygame.display.flip()
