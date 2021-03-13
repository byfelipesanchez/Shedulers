import smtplib, ssl


class Start:
	def __init__(self, start, val):
		self.start = start
		self.val = val
		self.val = input("Welcome to the URL saving system! Press a for the tutorial or m to access the menu   ")


class Menu:
	def menu(self, val):
		if self.val == "a":
			#tutorial function
		elif self.val == "m":
			print("""
			f - Save Links
			e - Email Current Links
			l - Check Links Library
			""")

		menuu = input("How would you like to continue?")
		if menuu == "f":
			print("open and add links to library.json ")
			#open and add links to library.json
		elif menuu == "e":
			email()
		elif menuu == "l":
			#oepn library.json

	def email(self, menuu):
		print("email test")
		port = 465
		sender, password = 'senderemailfs@gmail.com', 'FelipeSanchezsSenderEmail'
		recieve = '2018.felipe.sanchez@gmail.com'
		message = '''\
		Subject: Testing Python Email

		test!

		Felipe

		'''
		context = ssl.create_default_context()
		print("test.py")
		with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)as server:
		   server.login(sender, password)
		   server.sendmail(sender, recieve, message)
		print("Email Sent!")



# class Main:
# 	def intro(self):
# 		print("test" + self.test)

# testing = Main()
# testing.test = "testing classes"
# testing.intro()
