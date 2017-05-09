# Justin Mo
# Dieter, Koller
# CPE 202
import unittest

# a StrList is one of
# ~ "mt", or
# ~ Pair(first, rest) 
class Pair:
   def __init__(self, first, rest):
      self.first = first # a Str
      self.rest = rest # a strlist

   def __repr__(self):
      return "Pair({!r}, {!r})".format(self.first, self.rest)

   def __eq__(self, other):
      return type(other) == Pair and self.first == other.first and self.rest == other.rest

# ClassShape is one of
# ~ "mt", or
# ~ strlist
class ClassShape:
   def __init__(self, name, strlist):
      self.name = name # a Str
      self.strlist = strlist # a strlist of fieldnames

   def __repr__(self):
      return "ClassShape({!r}, {!r})".format(self.name, self.strlist)

   def __eq__(self, other):
      return type(other) == ClassShape and self.name == other.name and self.strlist == other.strlist

# StrList -> Str
# takes in a strlist and returns a single string with all of the lines of code conjoined
def join_lines(strlist):
   if strlist == "mt":
      return ""
   return strlist.first + "\n" + join_lines(strlist.rest)

# StrList -> StrList
# takes in a strlist of fieldnames and maps it to a strlist of lines
def fields_to_assignments(strlist):
   if strlist == "mt":
      return "mt"
   return Pair("        self.{:s} = {:s}".format(str(strlist.first), str(strlist.first)), fields_to_assignments(strlist.rest))

#print(fields_to_assignments(Pair("a", Pair("b", Pair("c", "mt")))))

# StrList -> StrList
# takes in a strlist of fieldnames and returns a list where all the elements are joined by a comma preceding each element
def commasep(strlist):
   if strlist == "mt":
      return ""
   return ", " + strlist.first + commasep(strlist.rest)

# StrList -> StrList
# takes in a strlist of fieldnames and returns a strlist representing the lines of a __init__ method   
def init_method(strlist):
   if strlist == "mt":
      return Pair(\
      "    def __init__(self):",\
 Pair('        pass', 'mt'))
   return Pair("    def __init__(self{:s}):".format(str(commasep(strlist))), fields_to_assignments(strlist))

print(init_method("mt"))

# StrList -> string
# takes in a strlist of fieldnames and maps it to a strlist of lines
def equal_helper(strlist):
   if strlist == "mt":
      return Pair("                )", "mt")
   return Pair("                and self.{:s} == other.{:s}".format(str(strlist.first), str(strlist.first)), equal_helper(strlist.rest))

# ClassShape -> StrList
# takes in ClassShape that contains the class name and fieldnames and returns a strlist representing the lines of a __eq__ method
def eq_method(ClassShape):
   return Pair("    def __eq__(self, other):", Pair("        return (type(other) == {:s}".format(str(ClassShape.name)), equal_helper(ClassShape.strlist)))

# StrList -> string
# takes in a strlist and returns a string containing the number of {!r}'s that are needed to represent the amount of fieldnames
def r_helper(strlist):
   if strlist == "mt":
      return ""
   if strlist.rest == "mt":
      return "{!r}"
   return "{!r}, " + r_helper(strlist.rest)

# StrList -> string
# takes in a strlist and returns a string in the format of self.fieldname
def self_helper(strlist):
   if strlist == "mt":
      return ""
   if strlist.rest == "mt":
      return "self." + strlist.first
   return "self.{:s}, ".format(strlist.first) + self_helper(strlist.rest)

# ClassShape -> StrList
# takes in a ClassShape and returns a StrList of the lines of a repr function
def repr_method(ClassShape):
   return Pair("    def __repr__(self):", Pair('        return "{:s}'.format(ClassShape.name) + "(" + r_helper(ClassShape.strlist) + ')"' + ".format(" + self_helper(ClassShape.strlist) + ")", "mt"))

# ClassShape -> string
# takes in a ClassShape and returns a string of the entire class definition
def render_class(ClassShape):
   return "class {:s}:\n".format(ClassShape.name) + join_lines(init_method(ClassShape.strlist)) + '\n' + join_lines(eq_method(ClassShape)) + '\n' + join_lines(repr_method(ClassShape))

#print(render_class(ClassShape("MyName", Pair("hi", Pair("im", Pair("jmo", "mt"))))))

class Test(unittest.TestCase):
   def test_eq(self):
      self.assertTrue(ClassShape(3, "mt") == ClassShape(3, "mt"))
   def test_repr1(self):
      self.assertEqual(repr(ClassShape("hello", "mt")), str(ClassShape("hello", "mt")))
   def test_repr2(self):
      self.assertEqual(repr(Pair(3, "mt")), str(Pair(3, "mt")))
   def test_join_lines(self):
      self.assertEqual(join_lines("mt"), "")
      self.assertEqual(join_lines(Pair("hello", Pair("im", Pair("jmo", "mt")))), "hello\nim\njmo\n")
   def test_fields_to_assignments(self):
      self.assertEqual(fields_to_assignments("mt"), "mt")
      self.assertEqual(fields_to_assignments(Pair("hi", Pair("im", Pair("jmo", "mt")))), Pair("        self.hi = hi", Pair("        self.im = im", Pair("        self.jmo = jmo", "mt"))))   
   def test_comma_sep(self):
      self.assertEqual(commasep("mt"), "")
      self.assertEqual(commasep(Pair("hi", Pair("i'm", Pair("jmo", "mt")))), ", hi, i'm, jmo")
   def test_init_method(self):
      self.assertEqual(init_method("mt"), Pair('    def __init__(self):', Pair('        pass', 'mt')))
      self.assertEqual(init_method(Pair("hi", Pair("im", Pair("jmo", "mt")))), Pair("    def __init__(self, hi, im, jmo):", Pair("        self.hi = hi", Pair("        self.im = im", Pair("        self.jmo = jmo", "mt")))))
   def test_equal_helper(self):
      self.assertEqual(equal_helper("mt"), Pair("                )", "mt"))
      self.assertEqual(equal_helper(Pair("hi", Pair("im", Pair("jmo", "mt")))), Pair("                and self.hi == other.hi", Pair("                and self.im == other.im", Pair("                and self.jmo == other.jmo", Pair("                )", "mt")))))
   def test_eq_method(self):
      self.assertEqual(eq_method(ClassShape("MyName", Pair("hi", Pair("im", Pair("jmo", "mt"))))), Pair("    def __eq__(self, other):", Pair("        return (type(other) == MyName", Pair("                and self.hi == other.hi", Pair("                and self.im == other.im", Pair("                and self.jmo == other.jmo", Pair("                )", "mt")))))))  
   def test_r_helper(self):
      self.assertEqual(r_helper("mt"), "")
      self.assertEqual(r_helper(Pair("hi", Pair("im", Pair("jmo", "mt")))), "{!r}, {!r}, {!r}")
   def test_self_helper(self):
      self.assertEqual(self_helper("mt"), "")
      self.assertEqual(self_helper(Pair("hi", Pair("im", Pair("jmo", "mt")))), "self.hi, self.im, self.jmo")
   def test_repr_method(self):
      self.assertEqual(repr_method(ClassShape("MyName", Pair("hi", Pair("im", Pair("jmo", "mt"))))), Pair("    def __repr__(self):", Pair('        return "MyName({!r}, {!r}, {!r})".format(self.hi, self.im, self.jmo)', "mt")))
   def test_render_class(self):
      self.assertEqual(render_class(ClassShape("MyName", "mt")), \
'class MyName:\n\
    def __init__(self):\n\
        pass\n\n\
    def __eq__(self, other):\n\
        return (type(other) == MyName\n\
                )\n\n\
    def __repr__(self):\n\
        return "MyName()".format()\n')
      self.assertEqual(render_class(ClassShape("MyName", Pair("hi", Pair("im", Pair("jmo", "mt"))))), \
'class MyName:\n\
    def __init__(self, hi, im, jmo):\n\
        self.hi = hi\n\
        self.im = im\n\
        self.jmo = jmo\n\n\
    def __eq__(self, other):\n\
        return (type(other) == MyName\n\
                and self.hi == other.hi\n\
                and self.im == other.im\n\
                and self.jmo == other.jmo\n\
                )\n\n\
    def __repr__(self):\n\
        return "MyName({!r}, {!r}, {!r})".format(self.hi, self.im, self.jmo)\n')
if __name__ == '__main__':
   unittest.main()   
