from PIL import Image

black = Image.open('black.png')
black_size = black.size

white = Image.open('white.png')
white_size = white.size

white_pieces = [[], ["white-castle-on-black", "white-knight-on-white", "white-bishop-on-black", "white-queen-on-white", "white-king-on-black", "white-bishop-on-white", "white-knight-on-black", "white-castle-on-white"]]
black_pieces = [[], []]

for i in range(4):
    white_pieces[0].append("white-pawn-on-black")
    white_pieces[0].append("white-pawn-on-white")
    black_pieces[1].append("black-pawn-on-black")
    black_pieces[1].append("black-pawn-on-white")

print(white_pieces)
print(black_pieces)

bit = 54

for i, y in enumerate(range(0, black_size[1]-5, bit)):
    for j, x in enumerate(range(0, black_size[0], bit)):
        piece = black.crop((x + j, y + i, x + bit + j, y + bit + i))
        piece.save(f"black{x/bit}{y/bit}.png")

for i, y in enumerate(range(0, white_size[1]-5, bit)):
    for j, x in enumerate(range(0, white_size[0], bit)):
        piece = white.crop((x + j, y + i, x + bit + j, y + bit + i))
        piece.save(f"white{x/bit}{y/bit}.png")


