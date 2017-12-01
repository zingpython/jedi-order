


class CreditCard:

	card_number=str()
	card_type=str()
	valid=str()

	def __init__(self,card_number):
		self.card_number=card_number
		self.Determine_Card_type()
		self.Validate()

	def Determine_Card_type(self):		

		if len(self.card_number)==15 or len(self.card_number)==16:
			VISA=["4"]
			MAST=["51","52","53","54","55"]
			AMEX=["34","37"]
			DISC=["6"]

			if self.card_number[0] in VISA and len(self.card_number)==16 :
				self.card_type = "Visa Card"                

			elif self.card_number[0:2] in MAST and len(self.card_number)==16:
				self.card_type = "Mastercard"

			elif self.card_number[0:2] in AMEX and len(self.card_number)==15:
				self.card_type = "American Express"

			elif self.card_number[0] in DISC and len(self.card_number)==16:
				self.card_type = "Discover"	

			else:
				self.card_type="Unknown"

		else:
			self.card_type="Unknown"



	def getCard_Type(self):
		return self.card_type

	def Validate(self):
		integer_list=[]

		for digits in self.card_number:			
			integer_list.append(int(digits))
		#print(integer_list)

		string_list1=integer_list[-2::-2]
		#print(string_list1)
		for x in range(len(string_list1)):
			string_list1[x]=string_list1[x]*2
		#print(string_list1)
		string_list2=integer_list[-1::-2]
		#print(string_list2)
		for x in range(len(string_list1)):
			if string_list1[x] > 9:
				string_list1[x]=string_list1[x]+1-10
		#print(string_list1)	

		total=sum(string_list1)+sum(string_list2)
		#print(total)

		if total%10==0:
			self.valid="Valid"
		else:
			self.valid="Not Valid"
		#print(self.valid)

		#adding up all the numbers








user_input = input("Master Yoda, please give me your credit card number")
yodas_card=CreditCard(user_input)
print(yodas_card.card_number)
print(yodas_card.card_type)
print("Yodas card number is",yodas_card.valid)




#yodas_card=CreditCard("341221121212")
#print(CreditCard.card_number)


			#card_type="not recognized"
			#valid="invalid"
