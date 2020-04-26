import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("gayam.software@gmail.com", "manikant123")
server.sendmail(
  "gayam.software@gmail.com",
  "gayam.software@gmail.com",
  "this message is from python")

server.quit()