#qrcode generte = pip install qrcode
#for show output=pip install pillow
import qrcode

#taking upI id as a input
upi_id=input("Enter your UPI ID =")


#   QR CODE Formate given below
#    upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# defining the payment URL based on th UPI ID and the payment app
#you can modify these URLS based on the payment apps you want to supports

phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create QR CODE for each payment app
phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
google_pay_qr=qrcode.make(google_pay_url)

#save the QR code to image file (optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')



#display qr code
#PIL pillow libarry viewer use for display QR code
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
