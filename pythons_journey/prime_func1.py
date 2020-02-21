def is_prime(num):
  if num <  2:
      return False
  if num==2:
      return True
  elif num%2==0:
      return False

  for i in range(3,int(num//2),2):
      if num%i==0:
          return False
  return True