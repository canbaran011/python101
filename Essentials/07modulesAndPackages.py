## Folder Structure
# mygame/
# mygame/game.py
# mygame/draw.py


# game.py
# import the draw module
# import draw

# def play_game():
#     ...

# def main():
#     result = play_game()
#     draw.draw_game(result)

# # this means that if this script is executed, then 
# # main() will be executed
# if __name__ == '__main__':
#     main()


# The draw module may look something like this:

# # draw.py

# def draw_game():
#     ...

# def clear_screen(screen):
#     ...

# Importing module objects to the current namespace

# # game.py
# # import the draw module
# from draw import draw_game

# def main():
#     result = play_game()
#     draw_game(result)


# Custom import name

# # game.py
# # import the draw module
# if visual_mode:
#     # in visual mode, we draw using graphics
#     import draw_visual as draw
# else:
#     # in textual mode, we print out text
#     import draw_textual as draw

# def main():
#     result = play_game()
#     # this can either be visual or textual depending on visual_mode
#     draw.draw_game(result)

# Module initialization


# # draw.py

# def draw_game():
#     # when clearing the screen we can use the main screen object initialized in this module
#     clear_screen(main_screen)
#     ...

# def clear_screen(screen):
#     ...

# class Screen():
#     ...

# # initialize main_screen as a singleton
# main_screen = Screen()


## There is more // org


