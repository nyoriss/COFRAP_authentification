import qrcode

def generateQRCodeFor(password, name):
    generatedQrcode = qrcode.make(password)
    generatedQrcode.save('assets\QRCode\QRcode_'+name+'.png')