def sleep_in(weekday, vacation):
  return (not weekday or vacation)

def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

def sum_double(a, b):
  sum = a + b
  if a == b:
    sum = sum * 2
  return sum

def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

def makes10(a, b):
  return (a == 10) or (b == 10) or (a + b == 10)

def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return (a > 0 and b < 0) or (a < 0 and b > 0)

def not_string(str):
  if str[:3] == 'not':
    return str 
  return 'not ' + str

def missing_char(str, n):
  return str[:n] + str[n+1:]

def front_back(str):
  if len(str) <= 1:
    return str
  return str[-1:] + str[1:-1] + str[:1]

def front3(str):
  return str[:3] * 3

# String 1

def hello_name(name):
  return "Hello " + name + "!"

def make_abba(a, b):
  return a + b + b + a
  
def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"
  
def make_out_word(out, word):
  return out[:len(out)/2] + word + out[len(out)/2:]

def extra_end(str):
  return str[-2:]*3

def first_two(str):
  if len(str) >= 2:
    return str[:2]
  return str

def first_half(str):
  return str[:len(str)/2]

def without_end(str):
  return str[1:len(str)-1]



