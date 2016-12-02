# -*- coding: utf-8 -*-
import random
from PIL import Image, ImageDraw

mode = int(input('mode:'))
image = Image.open("test.jpg")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

# градации серого
if (mode == 0):
	for i in range(width):
		for j in range(height):
			r = pix[i, j][0]
			g = pix[i, j][1]
			b = pix[i, j][2]
			S = (r + g + b) // 3
			draw.point((i, j), (S, S, S))

# сепия
if (mode == 1):
	depth = int(input('depth:'))
	for i in range(width):
		for j in range(height):
			r = pix[i, j][0]
			g = pix[i, j][1]
			b = pix[i, j][2]
			S = (r + g + b) // 3
			r = S + depth * 2
			g = S + depth
			b = S
			if (r > 255):
				r = 255
			if (g > 255):
				g = 255
			if (b > 255):
				b = 255
			draw.point((i, j), (r, g, b))

# негатив
if (mode == 2):
	for i in range(width):
		for j in range(height):
			r = pix[i, j][0]
			g = pix[i, j][1]
			b = pix[i, j][2]
			draw.point((i, j), (255 - r, 255 - g, 255 - b))

# добавление шумов
if (mode == 3):
	factor = int(input('factor:'))
	for i in range(width):
		for j in range(height):
			rand = random.randint(-factor, factor)
			r = pix[i, j][0] + rand
			g = pix[i, j][1] + rand
			b = pix[i, j][2] + rand
			if (r < 0):
				r = 0
			if (g < 0):
				g = 0
			if (b < 0):
				b = 0
			if (r > 255):
				r = 255
			if (g > 255):
				g = 255
			if (b > 255):
				b = 255
			draw.point((i, j), (r, g, b))

# яркость
if (mode == 4):
	factor = int(input('factor:'))
	for i in range(width):
		for j in range(height):
			r = pix[i, j][0] + factor
			g = pix[i, j][1] + factor
			b = pix[i, j][2] + factor
			if (r < 0):
				r = 0
			if (g < 0):
				g = 0
			if (b < 0):
				b = 0
			if (r > 255):
				r = 255
			if (g > 255):
				g = 255
			if (b > 255):
				b = 255
			draw.point((i, j), (r, g, b))

# черно-белое
if (mode == 5):
	factor = int(input('factor:'))
	for i in range(width):
		for j in range(height):
			r = pix[i, j][0]
			g = pix[i, j][1]
			b = pix[i, j][2]
			S = r + g + b
			if (S > (((255 + factor) // 2) * 3)):
				r, g, b = 255, 255, 255
			else:
				r, g, b = 0, 0, 0
			draw.point((i, j), (r, g, b))

# сохранение изображения
image.save("postprocessing.jpg", "JPEG")
del draw
