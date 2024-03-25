import customtkinter as ctk

class GUI(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.mainloop()
  
def main(args=None) -> None:
  app = GUI()

if __name__ == '__main__':
  main()