class Colour:
    END = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    @classmethod
    def black(cls, string):
        return f"{cls.BLACK}{string}{cls.END}"

    @classmethod
    def yellow(cls, string):
        return f"{cls.YELLOW}{string}{cls.END}"

    @classmethod
    def blue(cls, string):
        return f"{cls.BLUE}{string}{cls.END}"

    @classmethod
    def magenta(cls, string):
        return f"{cls.MAGENTA}{string}{cls.END}"

    @classmethod
    def cyan(cls, string):
        return f"{cls.CYAN}{string}{cls.END}"

    @classmethod
    def white(cls, string):
        return f"{cls.WHITE}{string}{cls.END}"

    @classmethod
    def green(cls, string):
        return f"{cls.GREEN}{string}{cls.END}"

    @classmethod
    def red(cls, string):
        return f"{cls.RED}{string}{cls.END}"

    @staticmethod
    def exact_rgb(string, rgb):
        r, g, b = rgb
        return f"\033[38;2;{r};{g};{b}m{string} \033[38;2;255;255;255m"
