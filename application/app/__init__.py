import sys
import os

root_dir: str = os.path.abspath(
  os.path.join(
    os.path.dirname(__file__), '..'
    )
  )

sys.path.append(root_dir)