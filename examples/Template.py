import extra.grid as grid

bkg_image = "examples/extra/background.txt"
grid.set_bkg_image(bkg_image)

running = True

while running:
    grid.clear_grid()
    grid.render_grid()
    key = grid.get_input()
    if key == "exit":
        running = False