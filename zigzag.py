import time
def l1():
    print("    ********")
def l2():
    print("   ********")
def l3():
    print("  ********")
def l4():
    print(" ********")
def l5():
    print("********")
def l6():
    print(" ********")
def l7():
    print("  ********")
def l8():
    print("  ********")
def l9():
    print("   ********")
def l10():
    print("    ********")

try:
     time.sleep(0.1)
     while True:
      l1()
      l2()
      l3()
      l4()
      l5()
      l6()
      l7()
      l8()
      l9()
      l10()
except KeyboardInterrupt:
    sys.exit()
