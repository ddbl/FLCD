import os

from console import Console

if __name__ == '__main__':
    print(os.listdir())
    ui = Console()
    ui.run()
