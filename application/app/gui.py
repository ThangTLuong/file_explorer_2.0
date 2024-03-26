import customtkinter as ctk
from styles import config

from typing import (
  Dict
)

class GUI(ctk.CTk):
  def __init__(self) -> None:
    super().__init__()
    # The minimum size the application can shrink to
    # No maximum size, since the maximum size is full screen
    self._min_width: int = 200
    self._min_height: int = 250
    
    # When the application is opened, this is the size it will take
    # For now, we're using a set number. Later on, I want to cache the size
    self._base_width: int = 600
    self._base_height: int = 300
    
    self.geometry(f'{self._base_width}x{self._base_height}')
    self.minsize(width=self._min_width, height=self._min_height)
  
  def run(self) -> None:
    '''
    Run the mainloop of the GUI
    '''
    self.mainloop()
    
  
def main(args=None) -> None:
  app = GUI()
  app.run()

if __name__ == '__main__':
  main()