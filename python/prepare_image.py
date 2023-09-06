import sys
from PIL import Image
import numpy as np

param=100
def prepare_real_photo(path):
    img = Image.open(path)
    img = img.convert("L")
    img=img.resize((28,28),Image.BOX)
    pix = img.load()
    lis=[]
    width, height = img.size
    for y in range(height):
        for x in range(width):
            # print(pix[x,y],end=" ")
            if(pix[x,y]>158):pix[x,y]=(255)
            else :pix[x,y]=(0)
    for i in range(height):
        for j in range(width):
            # print(pix[i,j])
            if(0 == pix[j,i]) :lis.append(1)
            else: 
                lis.append(0)

    numpy_arr=np.array(lis)
    img=numpy_arr
    img.shape += (1,)
    img=img.reshape(784, 1)
    img=(img*param).astype('int')
    return numpy_arr

def convert_to_list_1D(arr):
    lista=[]
    lista_listi=arr.tolist()
    for i in lista_listi:
        lista.append(i[0])
    return lista
def prep(path):
    img=prepare_real_photo(path)
    img.shape += (1,)
    img=img.reshape(784, 1)
    img=(img*param).astype('int')

    img_list=convert_to_list_1D(img)
    return img_list


def prepare_img_for_verilog():
    print("reg signed [31:0] img [0:783] = '{",end="")
    count=0
    img_list=prep(sys.argv[1])
    for i in img_list:
        count+=1
        if(count==len(img_list)):print(i,end="")
        else:print(i,end=',')
    print("};")

prepare_img_for_verilog()