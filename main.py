class Numbers:
	num1 = 0
	num2 = 0

   def start(self):
    self.num1 = int(input("Input 1st number: "))
    self.num2 = int(input("Enter 2nd number: "))
    print("This is the result")
    return(self.Calculation(self))

  def Calculation(self):
    while (self.num2 != 0):
      carry = self.num1 & self.num2
      self.num1 = self.num1 ^ self.num2
      self.num2 = carry << 1
    return(self.num1)

toCalc = Numbers()
toCalc.start()
