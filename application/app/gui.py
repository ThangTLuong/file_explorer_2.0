import customtkinter as ctk
from styles import config as css
from modules import decorators

from typing import (
  Any,
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
    self._base_width: int = 900
    self._base_height: int = 500
    
    self.title('File Explorer 2.0')
    self.geometry(f'{self._base_width}x{self._base_height}')
    self.minsize(width=self._min_width, height=self._min_height)
  
  
  # Public methods
  def run(self) -> None:
    '''
    Run the mainloop of the GUI
    '''
    self._default_settings()
    self._gui()
    self.mainloop()
    
    
  @decorators.Private
  def _default_settings(self) -> None:
    self.configure(
      font = css.DEFAULT_FONT,
      background = css.DEFAULT_BACKGROUND_COLOR)
  
  @decorators.Private
  def _gui(self) -> None:
    body_container = ctk.CTkScrollableFrame(
      self, 
      width = self._base_width,
      height = self._base_height,
      fg_color = css.DEFAULT_BACKGROUND_COLOR)
    body_container.pack(side = 'top', fill = 'both', expand = True)
  
  @decorators.Private
  def _new_container(self, **kwargs: Dict[str, Any]) -> ctk.CTkFrame:
    '''
    Attributes
    ----------
    master, width, height, border_width, fg_color, border_color
    
    Methods
    ----------
    .configure(attributes = value, ...) \n
    .cget(attribute_name) \n
    .bind(sequence = None, command = None, add = None)
    '''
    container = ctk.CTkFrame(kwargs)
    return container
    
  
def main(*args) -> None:
  app = GUI()
  app.run()

if __name__ == '__main__':
  main()