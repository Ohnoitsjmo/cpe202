# Justin Mo
# Dieter, Koller
# CPE 103 

#* Section 1 (Git)

# 1) persnickety

#* Section 2 (Data Definitions)

#* 1)
# celsius is a float
# return value (farenheit) is a float

class Farenheit:

      def __init__(self, celsius):
         self.celsius = celsius
         self.farenheit = (self.celsius*1.8) + 32

      def __repr__(self):
         return ("Farenheit: {:f}".format(self.farenheit))

      def __eq__(self, other):
         return type(other) == Farenheit and self.farenheit == other.farenheit


#* 2) 
# price is a float
# return value (price in cents) is an integer

class Price:

      def __init__(self, price):
         self.price = price*100

      def __repr__(self):
         return ("Price: {:f}".format(self.price))

      def __eq__(self, other):
         return type(other) == Price and self.price == other.price

#* 3) 
# price (in cents) is an integer
# name is a string 

class PriceName:

      def __init__(self, price, name):
         self.price = price*100
         self.name = name

      def __repr__(self):
         return ("Name: {:s}, Price: {:f}".format(self.name, self.price))

      def __eq__(self, other):
         return type(other) == PriceName and self.price == other.price and self.name == other.name

#* 4) 
# url is a string
# date is an integer (number of second since unix epoch)

class OpenTab:

      def __init__(self, url, date):
         self.url = url
         self.date = date

      def __repr__(self):
         return ("URL: {:s}, Date: {:d}".format(self.url, self.date))

      def __eq__(self, other):
         return type(other) == OpenTab and self.url == other.url and self.date == other.date


#* Section 3 (Signature, Purpose Statements, Headers)

#* 1)
# signature: add_tax int int -> int
# purpose: return the price of an item after adding sales tax
def add_tax(price):
   pass

#* 2)
# signature:find_price str -> int
# purpose: return the price of a given item by finding it in a price database
def find_price(item_name):
   pass

#* 3)
# signature: median_income str list -> int 
# purpose: return the average income given a geographical region by sorting through a database
def median_income(region, database):
   pass

#* 4)
# signature: city_overlap str list -> str
# purpose: return a string of cities that overlap given a geographical region and database
def city_overlap(region, database):
   pass

#* Section 4 (Test Cases)

#* 1) 
# contract: second_largest int int int -> int 
# purpose: return the second largest number out of the three given numbers
def second_largest(number_one, number_two, number_three):
   pass

#import unittest
#class test_second_largest(unittest.TestCase):
   #def test_1(self):
      #self.assertEqual(second_largest(1, 2, 3), 2)
   #def test_2(self):
      #self.assertEqual(second_largest(2, 4, 6), 4)
#if __name__ == '__main__':
   #unittest.main()

#* 2)
# contract: no_capitals str -> boolean
# purpose: return a boolean showing whether the given string contains any capital letters
def no_capitals(string):
   pass

#import unittest
#class no_capitals(unittest.TestCase):
   #def test_1(self):
      #self.assertTrue(no_capitals(HELLO))
   #def test_2(self):
      #self.assertFalse(no_capitals(hello))
#if __name__ == '__main__':
   #unittest.main()

#* 3)
# contract: most_north str str -> str
# purpose: return a string that is the northern most state given two strings (states)
def most_north(state_1, state_2):
   pass

#import unittest
#class most_north(unittest.TestCase):
   #def test_1(self):
      #self.assertEqual(most_north(Texas, California), California)
   #def test_2(self):
      #self.assertEqual(most_north(Illinois, Michigan), Michigan)
#if __name__ == '__main__':
   #unittest.main()

#* Section 5 (Whole Functions)

#* 1)
# signature: f2m int -> float
# purpose: return the length in meters given the length in feet
def f2m(feet):
      meters = feet*0.3048
      return meters 

#import unittest
#class f2m(unittest.TestCase):
   #def test_1(self):
      #self.assertEqual(f2m(30), 9.144)
   #def test_2(self):
      #self.assertEqual(f2m(10), 3.048)
#if __name__ == '__main__':
   #unittest.main()

#* 2) 
# frequency is an integer
# duration is an integer
# signature: MusicalNote int int -> int int
# purpose: return pitch in hz and duration in seconds 
class MusicalNote:
   def __init__(self, frequency, duration):
      self.frequency = frequency
      self.duration = duration

   def __repr__(self):
      return ("Pitch: {:d}, Duration: {:d}".format(self.frequency, self.duration))

   def __eq__(self, other):
      return type(other) == MusicalNote and self.frequency == other.frequency and self.duration == other.duration
	   
#import unittest
#class TestCases(unittest.TestCase):
   #def test_1(self):
      #self.assertEqual(MusicalNote(3500, 10), "Pitch: 3500, Duration: 10")
   #def test_2(self):
      #self.assertEqual(MusicalNote(4000, 20), "Pitch: 4000, Duration: 20")
#if __name__ == '__main__':
   #unittest.main()

#* 3) 
# signature: up_one_octave int -> int
# purpose: return a note that is one octave higher by doubling the frequency
def up_one_octave(note2):
   if type(note2) == MusicalNote:
      return MusicalNote(note2.frequency*2, note2.duration)
   return None

#import unittest
#class up_one_octave(unittest.TestCase):
   #def test_1(self):
      #self.assertEqual(up_one_octave(2500), 5000)
   #def test_2(self):
      #self.assertEqual(up_one_octave(3000), 6000)
#if __name__ == '__main__':
   #unittest.main()
         
#* 4)
# signature: up_one_octave_m int -> None
# purpose: return None when given frequency because the function mutates the object itself
def up_one_octave_m(note1):
   if type(note1) == MusicalNote:
      note1.frequency = note1.frequency*2
   return None
   
#import unittest
#class up_one_octave_m(unittest.TestCase):
   #def test_1(self):
      #self.assertEqual(up_one_octave_m(2500), None)
   #def test_2(self):
      #self.assertEqual(up_one_octave_m(3000), None)
#if __name__ == '__main__':
   #unittest.main()   
      
