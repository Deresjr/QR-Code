# install all the libraries needed
# create a function that collects a text and converts it to a qrcode
# save the qrcode as a image
# run the function

import qrcode


def generate_qrcode(text):

  qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
  )

  qr.add_data(text)
  qr.make(fit=True)
  img = qr.make_image(fill_color="black", back_color="white")
  img.save("qrimg.png")


generate_qrcode("https://www.linkedin.com/in/deres-benn-jr-145564141?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BrFBqpuj9ScKKsYXiCMOgOQ%3D%3D")