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
    
    self.title('File Explorer 2.0')
    self.geometry(f'{css.BASE_WIDTH}x{css.BASE_HEIGHT}')
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
    
    self.grid_columnconfigure(2, weight = 1)
    self.grid_rowconfigure(2, weight = 1)
  
  @decorators.Private
  def _gui(self) -> None:
    body_container: ctk.CTkFrame = ctk.CTkFrame(
      master = self, 
      width = css.BASE_WIDTH,
      height = css.BASE_HEIGHT,
      fg_color = css.DEFAULT_BACKGROUND_COLOR)
    body_container.pack(side = 'top', fill = 'both', expand = True)
    
    top_view: ctk.CTkFrame = self._top_view(body_container)
    left_view: ctk.CTkScrollableFrame = self._left_view(body_container)
    main_view: ctk.CTkScrollableFrame = self._main_view(body_container)
    
  @decorators.Private
  def _top_view(self, master) -> ctk.CTkFrame:
    container: ctk.CTkFrame = ctk.CTkFrame(
      master = master,
      fg_color = css.TOP_VIEW_COLOR,
      width = css.BASE_WIDTH,
      height = 125,
      corner_radius = 0
    )
    
    container.grid(
      row = 0, 
      column = 0, 
      columnspan = 2, 
      sticky = 'n'
    )
    
    return container
  
  @decorators.Private
  def _left_view(self, master) -> ctk.CTkFrame:
    container: ctk.CTkFrame = ctk.CTkFrame(
      master = master,
      fg_color = css.LEFT_VIEW_COLOR,
      width = 180,
      height = css.BASE_HEIGHT - 124,
      corner_radius = 0
    )
    
    container.grid(
      row = 1, 
      column = 0, 
      sticky = 'nsw'
    )
    
    return container
  
  @decorators.Private
  def _main_view(self, master) -> ctk.CTkFrame:
    container: ctk.CTkFrame = ctk.CTkFrame(
      master = master,
      fg_color = css.MAIN_VIEW_COLOR,
      width = css.BASE_WIDTH - 180,
      height = css.BASE_HEIGHT - 124,
      corner_radius = 0
    )
    
    container.grid(
      row = 1, 
      column = 1, 
      sticky = 'nsew'
    )
  
    return container
  
def main(*args) -> None:
  app = GUI()
  app.run()

if __name__ == '__main__':
  main()