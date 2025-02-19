import grid

bkg_image = "background.txt"
grid.set_bkg_image(bkg_image)

while True:
    key = grid.get_input()
    grid.clear_grid()
    grid.render_grid()