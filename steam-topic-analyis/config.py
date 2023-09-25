# Special paths and variables that are used across the project
def file_directory(TYPE):
  """Returns file directory given file status"""
  if TYPE == 'raw':
      return 'C:/Users/billy/OneDrive/Documents/Python Scripts/1. Portfolio/steam-topic-analysis/data/raw/'
  elif TYPE == 'cleaned':
      return 'C:/Users/billy/OneDrive/Documents/Python Scripts/1. Portfolio/steam-topic-analysis/data/cleaned/'
  elif TYPE == 'processed':
      return 'C:/Users/billy/OneDrive/Documents/Python Scripts/1. Portfolio/steam-topic-analysis/data/processed/'