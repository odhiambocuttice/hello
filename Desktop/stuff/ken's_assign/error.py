import sys

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(b / a)
except IndexError:
    print('enter two arguments')
except ValueError:
    print ('enter two integers arguments only')
except ZeroDivisionError:
	print("number divisible by 0")
except Exception:
    print('')

