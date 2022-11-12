 
from PIL import Image
import io
import numpy as np
import matplotlib.pyplot as plt
import seabonr as sns
def plottoByte(plt):
    with io.BytesIO() as buffer:  # use buffer memory
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image = buffer.getvalue()
    return image
def grafBar(data,location=""):
    fig = plt.figure(figsize = (10,5))
    plt.title(f"Inscription by {data.name}: {location}")
    sns.countplot(data)
    plt.xticks(rotation=90)
    plt.show()
    
    
    f =plottoByte(fig)
    return f

def mi_decorador(funcion):
    def nueva_funcion(a, b):
        print("Se va a llamar")
        c = funcion(a, b)
        print("Se ha llamado")#         
        a =grafBar(a)
        plt.subplot(1, 2, 2)
        b = grafBar(b)

        img1 = Image.open(io.BytesIO(a))
        img2 = Image.open(io.BytesIO(b))

        plt.figure(figsize=(10,8))
        plt.subplot(1, 2, 2)
        plt.imshow(img1,interpolation='nearest', aspect='auto')  
        plt.xticks([])
        plt.yticks([])
        plt.subplot(1, 2, 1)
        plt.imshow(img2,interpolation='nearest', aspect='auto')  
        plt.xticks([])
        plt.yticks([])
        
        return c
    return nueva_funcion

@mi_decorador
def graf2in1(a, b):
    print("Entra en funcion suma")
#     return a + b

graf2in1(df1.gender,df2.gender)
