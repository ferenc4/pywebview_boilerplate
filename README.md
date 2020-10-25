# Overview
This implementation of pywebview loads a sample webpage that can invoke py client functions to customise the window.

# Build binary as one file
```
pyinstaller __main__.py --onefile --noconsole
```

# Build binary as a folder
```
pyinstaller __main__.py --onedir --noconsole
```
This will be significantly faster to run than a single file as the contents don't need to be unpacked during runtime.
