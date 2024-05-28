class Colors:
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)
    pink = (255, 192, 203)
    brown = (165, 42, 42)
    grey = (128, 128, 128)
    black = (0, 0, 0)
    light_grey = (211, 211, 211)
    dark_green = (0, 100, 0)
    light_green = (144, 238, 144)
    dark_red = (139, 0, 0)
    light_red = (255, 106, 106)
    dark_orange = (191, 96, 0)
    light_orange = (255, 165, 0)
    dark_yellow = (184, 134, 11)
    light_yellow = (255, 255, 0)
    dark_purple = (75, 0, 130)
    light_purple = (238, 130, 238)
    dark_cyan = (0, 139, 139)
    light_cyan = (224, 255, 255)
    light_pink = (255, 182, 193)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue, 
                cls.pink, cls.brown, cls.grey, cls.black, cls.light_grey, cls.dark_green, cls.light_green, 
                cls.dark_red, cls.light_red, cls.dark_orange, cls.light_orange, cls.dark_yellow, cls.light_yellow, 
                cls.dark_purple, cls.light_purple, cls.dark_cyan, cls.light_cyan, cls.light_pink, cls.dark_blue,
                cls.light_blue]