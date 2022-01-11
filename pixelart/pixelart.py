from PIL import Image
import matplotlib.pyplot as plt



def photo2pixelart(image, i_size, o_size):

    img=Image.open(image)

    simg=img.resize(i_size,Image.BILINEAR)

    res=simg.resize(img.size, Image.NEAREST)

    fname=f'mario_{i_size[0]}x{i_size[1]}.png'
    res.save(fname)


    plt.figure(figsize=(16,10))

    plt.subplot(1,2,1)
    plt.title('Original image', size=18)
    plt.imshow(img)
    plt.axis('off')
    plt.subplot(1,2,2)
    plt.title(f'Pixel Art {i_size[0]}x{i_size[1]}', size=18)
    plt.imshow(res)
    plt.axis('on')
    plt.show()



print("======PIXEL ART GENERATOR======")
print()
imag = input("Enter image path: ")
img=Image.open(imag)
photo2pixelart(image=imag, i_size=(32,32), o_size=img.size)