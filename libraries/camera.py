from skimage import data
camera = data.camera()
print(type(camera))
print(camera.shape)
print(camera.size)
print(camera[10, 20])
mask = camera < 112
print(mask)
camera[mask] = 0
print(camera);
