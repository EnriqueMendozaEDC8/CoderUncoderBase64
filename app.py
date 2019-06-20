import base64,os,fnmatch
from PIL import Image
from io import BytesIO

path = 'C:\\VisorBase64\\images\\'
pathkik = 'C:\\VisorBase64\\kikfiles\\'
path2 = 'C:\\VisorBase64\\'

def main():
    for r, d,f in os.walk(path):
        for file in f:
            with open(path+file, "rb") as image_file:
                f = open(pathkik+file[:-4]+".kik","w+")
                image64 = base64.encodestring(image_file.read())
                f.write(image64.decode("utf-8"))
                f.close

                file64 = open(pathkik+file[:-4]+".kik", 'rb')
                data = file64.read()
                imageDecod = Image.open(BytesIO(base64.decodestring(data)))
                imageDecod.save(path2+file, 'PNG')
                file64.close
                
                print("suscefull")
    return

if __name__ == "__main__":
    main()