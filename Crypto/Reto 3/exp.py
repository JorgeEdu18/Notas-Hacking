from PIL import Image
import numpy as np 

imagen1 = np.asrray(Image.open(''))
imagen2 = np.asrray(Image.open(''))

data = imagen1 + imagen2	
nueva = Image.fromarray(data)
nueva.save('lachida', PNG)p