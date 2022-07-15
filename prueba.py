i = 0
contI = 1
contD = 51
'''
for i in range(180):
    if(i > 90):
        print(f"\t\telif (", round(7.111*i), "> x >= ", round(7.111 *
              (i-1)), f"): ser.write(b'der{contI}\\n')")
        contI += 1

    elif(i == 90):
        print(f"\t\telif (", round(7.111*i), "> x >= ", round(7.111 *
              (i-1)), f"): ser.write(b'ctr\\n')")
    else:
        print(f"\t\telif (", round(7.111*i), "> x >= ", round(7.111 *
              (i-1)), f"): ser.write(b'izq{contD}\\n')")

        contD += 1

'''

'''
restaD = 0
restaI = 0
for i in range(51, 102):

    if(i > 90):
        restaI += 0.1
        print(f'    if(entradaSerial == "der{contI}\\n")' +
              "\n    {\n         "+f'servo1.write({i-7});'+"\n    }")
        contI += 1
    elif(i == 90):
        print(f'    if(entradaSerial == "ctr{i}\\n")' +
              "\n    {\n         "+f'servo1.write({90});'+"\n    }")
    else:
        restaD += 0.1
        print(f'    if(entradaSerial == "izq{contD}\\n")' +
              "\n    {\n         "+f'servo1.write({i-7});'+"\n    }")
        contD += 1

'''
