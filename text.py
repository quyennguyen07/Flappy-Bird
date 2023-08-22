class Text:
    score = 0

    def __init__(self):
        pass

    def create_text(self, txt, font, color):
        return font.render(txt, True, color)

    def draw(self, screen, text, x, y):
        return screen.blit(text, (x, y))


