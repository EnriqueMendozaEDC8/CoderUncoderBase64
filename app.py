import base64,os,fnmatch
from io import BytesIO
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from PIL import Image

class main():
    def __init__(self,root):
        #Declaracion de variables de clase
        self.wind = root
        self.wind.title('Base 64 PJ')
        self.direccionImagen = ''
        self.direccionKik = ''
        self.direccionDestino = ''
        
        #Declaracion del Primer frame Buscar Imagen
        frame1 = LabelFrame(self.wind,text = 'Buscar imagen:')
        frame1.grid(row = 0,column = 0,columnspan = 3,pady=20)
        #textBox y Boton de busqueda de Buscar Imagen
        Label(frame1,text= 'Buscar Imagen:').grid(row = 1,column = 0,columnspan = 4)
        self.lbDireccionImagen = Entry(frame1,textvariable=self.direccionImagen,width=40)
        self.lbDireccionImagen.grid(row = 1,column = 1)
        self.btBuscarImagen = ttk.Button(frame1,text = 'Buscar',command = self.findImage )
        self.btBuscarImagen.grid(row = 1,column = 2)

        #Declaracion del Segundo frame Buscar Imagen Encriptadao
        frame2 = LabelFrame(self.wind,text = 'Buscar Imagen Encriptada:')
        frame2.grid(row = 2,column = 0,columnspan = 3,pady=20)
        #textBox y Boton de busqueda de Buscar Imagen Encriptada
        Label(frame2,text= 'Buscar Kik:').grid(row = 3,column = 0,columnspan = 4)
        self.lbDireccionKik = Entry(frame2,textvariable=self.direccionKik,width=40)
        self.lbDireccionKik.grid(row = 3,column = 1)
        self.btBuscarKik = ttk.Button(frame2,text = 'Buscar',command = self.findKik )
        self.btBuscarKik.grid(row = 3,column = 2)

        #Declaracion del tercer frame Ubicacion Destino
        frameDestiono = LabelFrame(self.wind,text = 'Ubicacion Destino:')
        frameDestiono.grid(row = 4,column = 0,columnspan = 3,pady=20)
        #textBox y Boton de busqueda de Ubicacion Destino
        Label(frameDestiono,text= 'Buscar Destino:').grid(row = 5,column = 0,columnspan = 4)
        self.lbDireccionDestino = Entry(frameDestiono,textvariable=self.direccionDestino,width=40 )
        self.lbDireccionDestino.grid(row = 5,column = 1)
        self.btBuscarDestino = ttk.Button(frameDestiono,text = 'Buscar',command = self.findDestino )
        self.btBuscarDestino.grid(row = 5,column = 2)

        #Botones de Codificar,Decodificar y Ver imagen
        self.btBuscarDestino = ttk.Button(text = 'Codificar',command = self.base64Encoder )
        self.btBuscarDestino.grid(row = 6,column = 0)
        self.btBuscarDestino = ttk.Button(text = 'Descodificar',command = self.base64Decoder )
        self.btBuscarDestino.grid(row = 6,column = 1)
        self.btBuscarDestino = ttk.Button(text = 'Ver Imagen',command = self.base64Show )
        self.btBuscarDestino.grid(row = 6,column = 2)
    
    def findKik(self):
        self.direccionKik = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("kik files","*.kik"),("all files","*.*")))
        self.lbDireccionKik.delete(0,END)
        self.lbDireccionKik.insert(0,self.direccionKik)

    def findImage(self):
        self.direccionImagen = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("PNG files","*.png"),("all files","*.*")))
        self.lbDireccionImagen.delete(0,END)
        self.lbDireccionImagen.insert(0,self.direccionImagen)

    def findDestino(self):
        self.direccionDestino = filedialog.askdirectory()
        self.lbDireccionDestino.delete(0,END)
        self.lbDireccionDestino.insert(0,self.direccionDestino)

    def base64Encoder(self):
        try:
            with open(self.direccionImagen, "rb") as image_file:
                fileOrigin = self.direccionImagen.split('/')
                f = open(self.direccionDestino+'/'+fileOrigin[len(fileOrigin)-1][:-4]+".kik","w+")
                image64 = base64.encodestring(image_file.read())
                f.write(image64.decode("utf-8"))
                f.close
            return True    
        except:
            return False

    def base64Decoder(self):
        try:
            with open(self.direccionKik, 'rb') as file64:
                data = file64.read()
                imageDecod = Image.open(BytesIO(base64.decodestring(data)))
                fileDestination = self.direccionKik.split('/')
                imageDecod.save(self.direccionDestino+'/'+fileDestination[len(fileDestination)-1][:-4]+".png", 'PNG')
                file64.close
            return True    
        except:
            return False

    def base64Show(self):
        try:
            with open(self.direccionKik, 'rb') as file64:
                data = file64.read()
                imageDecod = Image.open(BytesIO(base64.decodestring(data)))
                imageDecod.show()
                file64.close
            return True
        except:
            return False

if __name__ == "__main__":
    root = Tk()
    app = main(root)
    root.mainloop()
    
