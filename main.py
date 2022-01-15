import pyqrcode

link = input('Enter a link: ')
img = pyqrcode.create(link)
img.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
img.show()