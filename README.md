# Python-Grid-Render

![screenshot](https://github.com/ThePotatoGuyNLTO/Python-Grid-Render/blob/main/Screenshot.png?raw=true)

Renders a grid with a bkg and collision system.
Always add <br>
```import (dict).grid as grid```
<br>
## Basics
Renders in a bkg image
<br>
```grid.set_bkg_image("dict")```<br>
Try setting the dict as a string, as good practice. <br>
<br>
```dict = "examples/extra/background.txt"``` 
<br>
```grid.set_bkg_image(dict)```
<br>
<br>
Then render your grid using this line of code
<br>
```grid.render_grid()``` <br> <br>
Your full code should be this <br>
```import extra.grid as grid``` <br>
```dict = "examples/extra/background.txt"``` <br>
```grid.set_bkg_image(dict)``` <br>
```grid.render_grid()``` <br> <br>
When making a new project try duplicating "Template.py" as your project and rename it to what you want.
