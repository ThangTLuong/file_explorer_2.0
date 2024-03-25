import sys
import os

root_dir: str = os.path.abspath(
  os.path.join(
    os.path.dirname(__file__), '..'
    )
  )

sys.path.append(root_dir)

from gui import GUI

def main(*args) -> None:
  app = GUI()
  app.run()
  
if __name__ == '__main__':
  main()