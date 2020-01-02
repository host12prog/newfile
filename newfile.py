import click

@click.command()
@click.argument("file_name")
def addFile(file_name):
  """A simple program made in Python designed to simplify making files in a Command Prompt."""
  f = open(file_name, "x")
  f.close()
	
if __name__ == "__main__":
  addFile()
