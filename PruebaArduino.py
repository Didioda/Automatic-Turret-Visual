import cv2
from cv2 import LINE_AA
import numpy as np
import serial
COM = "COM3"
BAUD = 9600
ser = serial.Serial(COM, BAUD)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
width = 1280
height = 720
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


#redBajo1 = np.array([0, 100, 20], np.uint8)
#redAlto1 = np.array([8, 255, 255], np.uint8)
#redBajo2 = np.array([175, 100, 20], np.uint8)
#redAlto2 = np.array([179, 255, 255], np.uint8)
verdeBajo = np.array([31, 100, 20], np.uint8)
verdeAlto = np.array([43, 255, 255], np.uint8)
while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
        #maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
        #mascara = cv2.add(maskRed1, maskRed2)
        mascara = cv2.inRange(frameHSV, verdeBajo, verdeAlto)

        contornos, _ = cv2.findContours(
            mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame, contornos, -1, (255, 0, 0))

        for c in contornos:
            area = cv2.contourArea(c)
            if area > 200:

                M = cv2.moments(c)
                if M["m00"] == 0:
                    M["m00"] == 1
                x = int(M['m10'] / M['m00'])
                y = int(M['m01'] / M['m00'])
                cv2.circle(frame, (x, y), 7, (0, 0, 255), -1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, '{},{}'.format(x, y), (x+10, y),
                            font, 1.2, (0, 0, 255), 2, cv2.LINE_AA)
                nuevoContorno = cv2.convexHull(c)
                cv2.drawContours(frame, [nuevoContorno], 0, (255, 0, 0), 3)
                print(x)
                if (0 > x >= -7):
                    ser.write(b'izq1\n')
                elif (7 > x >= 0):
                    ser.write(b'izq2\n')
                elif (14 > x >= 7):
                    ser.write(b'izq3\n')
                elif (21 > x >= 14):
                    ser.write(b'izq4\n')
                elif (28 > x >= 21):
                    ser.write(b'izq5\n')
                elif (36 > x >= 28):
                    ser.write(b'izq6\n')
                elif (43 > x >= 36):
                    ser.write(b'izq7\n')
                elif (50 > x >= 43):
                    ser.write(b'izq8\n')
                elif (57 > x >= 50):
                    ser.write(b'izq9\n')
                elif (64 > x >= 57):
                    ser.write(b'izq10\n')
                elif (71 > x >= 64):
                    ser.write(b'izq11\n')
                elif (78 > x >= 71):
                    ser.write(b'izq12\n')
                elif (85 > x >= 78):
                    ser.write(b'izq13\n')
                elif (92 > x >= 85):
                    ser.write(b'izq14\n')
                elif (100 > x >= 92):
                    ser.write(b'izq15\n')
                elif (107 > x >= 100):
                    ser.write(b'izq16\n')
                elif (114 > x >= 107):
                    ser.write(b'izq17\n')
                elif (121 > x >= 114):
                    ser.write(b'izq18\n')
                elif (128 > x >= 121):
                    ser.write(b'izq19\n')
                elif (135 > x >= 128):
                    ser.write(b'izq20\n')
                elif (142 > x >= 135):
                    ser.write(b'izq21\n')
                elif (149 > x >= 142):
                    ser.write(b'izq22\n')
                elif (156 > x >= 149):
                    ser.write(b'izq23\n')
                elif (164 > x >= 156):
                    ser.write(b'izq24\n')
                elif (171 > x >= 164):
                    ser.write(b'izq25\n')
                elif (178 > x >= 171):
                    ser.write(b'izq26\n')
                elif (185 > x >= 178):
                    ser.write(b'izq27\n')
                elif (192 > x >= 185):
                    ser.write(b'izq28\n')
                elif (199 > x >= 192):
                    ser.write(b'izq29\n')
                elif (206 > x >= 199):
                    ser.write(b'izq30\n')
                elif (213 > x >= 206):
                    ser.write(b'izq31\n')
                elif (220 > x >= 213):
                    ser.write(b'izq32\n')
                elif (228 > x >= 220):
                    ser.write(b'izq33\n')
                elif (235 > x >= 228):
                    ser.write(b'izq34\n')
                elif (242 > x >= 235):
                    ser.write(b'izq35\n')
                elif (249 > x >= 242):
                    ser.write(b'izq36\n')
                elif (256 > x >= 249):
                    ser.write(b'izq37\n')
                elif (263 > x >= 256):
                    ser.write(b'izq38\n')
                elif (270 > x >= 263):
                    ser.write(b'izq39\n')
                elif (277 > x >= 270):
                    ser.write(b'izq40\n')
                elif (284 > x >= 277):
                    ser.write(b'izq41\n')
                elif (292 > x >= 284):
                    ser.write(b'izq42\n')
                elif (299 > x >= 292):
                    ser.write(b'izq43\n')
                elif (306 > x >= 299):
                    ser.write(b'izq44\n')
                elif (313 > x >= 306):
                    ser.write(b'izq45\n')
                elif (320 > x >= 313):
                    ser.write(b'izq46\n')
                elif (327 > x >= 320):
                    ser.write(b'izq47\n')
                elif (334 > x >= 327):
                    ser.write(b'izq48\n')
                elif (341 > x >= 334):
                    ser.write(b'izq49\n')
                elif (348 > x >= 341):
                    ser.write(b'izq50\n')
                elif (356 > x >= 348):
                    ser.write(b'izq51\n')
                elif (363 > x >= 356):
                    ser.write(b'izq52\n')
                elif (370 > x >= 363):
                    ser.write(b'izq53\n')
                elif (377 > x >= 370):
                    ser.write(b'izq54\n')
                elif (384 > x >= 377):
                    ser.write(b'izq55\n')
                elif (391 > x >= 384):
                    ser.write(b'izq56\n')
                elif (398 > x >= 391):
                    ser.write(b'izq57\n')
                elif (405 > x >= 398):
                    ser.write(b'izq58\n')
                elif (412 > x >= 405):
                    ser.write(b'izq59\n')
                elif (420 > x >= 412):
                    ser.write(b'izq60\n')
                elif (427 > x >= 420):
                    ser.write(b'izq61\n')
                elif (434 > x >= 427):
                    ser.write(b'izq62\n')
                elif (441 > x >= 434):
                    ser.write(b'izq63\n')
                elif (448 > x >= 441):
                    ser.write(b'izq64\n')
                elif (455 > x >= 448):
                    ser.write(b'izq65\n')
                elif (462 > x >= 455):
                    ser.write(b'izq66\n')
                elif (469 > x >= 462):
                    ser.write(b'izq67\n')
                elif (476 > x >= 469):
                    ser.write(b'izq68\n')
                elif (484 > x >= 476):
                    ser.write(b'izq69\n')
                elif (491 > x >= 484):
                    ser.write(b'izq70\n')
                elif (498 > x >= 491):
                    ser.write(b'izq71\n')
                elif (505 > x >= 498):
                    ser.write(b'izq72\n')
                elif (512 > x >= 505):
                    ser.write(b'izq73\n')
                elif (519 > x >= 512):
                    ser.write(b'izq74\n')
                elif (526 > x >= 519):
                    ser.write(b'izq75\n')
                elif (533 > x >= 526):
                    ser.write(b'izq76\n')
                elif (540 > x >= 533):
                    ser.write(b'izq77\n')
                elif (548 > x >= 540):
                    ser.write(b'izq78\n')
                elif (555 > x >= 548):
                    ser.write(b'izq79\n')
                elif (562 > x >= 555):
                    ser.write(b'izq80\n')
                elif (569 > x >= 562):
                    ser.write(b'izq81\n')
                elif (576 > x >= 569):
                    ser.write(b'izq82\n')
                elif (583 > x >= 576):
                    ser.write(b'izq83\n')
                elif (590 > x >= 583):
                    ser.write(b'izq84\n')
                elif (597 > x >= 590):
                    ser.write(b'izq85\n')
                elif (604 > x >= 597):
                    ser.write(b'izq86\n')
                elif (612 > x >= 604):
                    ser.write(b'izq87\n')
                elif (619 > x >= 612):
                    ser.write(b'izq88\n')
                elif (626 > x >= 619):
                    ser.write(b'izq89\n')
                elif (633 > x >= 626):
                    ser.write(b'izq90\n')
                elif (640 > x >= 633):
                    ser.write(b'ctr\n')
                elif (647 > x >= 640):
                    ser.write(b'der1\n')
                elif (654 > x >= 647):
                    ser.write(b'der2\n')
                elif (661 > x >= 654):
                    ser.write(b'der3\n')
                elif (668 > x >= 661):
                    ser.write(b'der4\n')
                elif (676 > x >= 668):
                    ser.write(b'der5\n')
                elif (683 > x >= 676):
                    ser.write(b'der6\n')
                elif (690 > x >= 683):
                    ser.write(b'der7\n')
                elif (697 > x >= 690):
                    ser.write(b'der8\n')
                elif (704 > x >= 697):
                    ser.write(b'der9\n')
                elif (711 > x >= 704):
                    ser.write(b'der10\n')
                elif (718 > x >= 711):
                    ser.write(b'der11\n')
                elif (725 > x >= 718):
                    ser.write(b'der12\n')
                elif (732 > x >= 725):
                    ser.write(b'der13\n')
                elif (740 > x >= 732):
                    ser.write(b'der14\n')
                elif (747 > x >= 740):
                    ser.write(b'der15\n')
                elif (754 > x >= 747):
                    ser.write(b'der16\n')
                elif (761 > x >= 754):
                    ser.write(b'der17\n')
                elif (768 > x >= 761):
                    ser.write(b'der18\n')
                elif (775 > x >= 768):
                    ser.write(b'der19\n')
                elif (782 > x >= 775):
                    ser.write(b'der20\n')
                elif (789 > x >= 782):
                    ser.write(b'der21\n')
                elif (796 > x >= 789):
                    ser.write(b'der22\n')
                elif (804 > x >= 796):
                    ser.write(b'der23\n')
                elif (811 > x >= 804):
                    ser.write(b'der24\n')
                elif (818 > x >= 811):
                    ser.write(b'der25\n')
                elif (825 > x >= 818):
                    ser.write(b'der26\n')
                elif (832 > x >= 825):
                    ser.write(b'der27\n')
                elif (839 > x >= 832):
                    ser.write(b'der28\n')
                elif (846 > x >= 839):
                    ser.write(b'der29\n')
                elif (853 > x >= 846):
                    ser.write(b'der30\n')
                elif (860 > x >= 853):
                    ser.write(b'der31\n')
                elif (868 > x >= 860):
                    ser.write(b'der32\n')
                elif (875 > x >= 868):
                    ser.write(b'der33\n')
                elif (882 > x >= 875):
                    ser.write(b'der34\n')
                elif (889 > x >= 882):
                    ser.write(b'der35\n')
                elif (896 > x >= 889):
                    ser.write(b'der36\n')
                elif (903 > x >= 896):
                    ser.write(b'der37\n')
                elif (910 > x >= 903):
                    ser.write(b'der38\n')
                elif (917 > x >= 910):
                    ser.write(b'der39\n')
                elif (924 > x >= 917):
                    ser.write(b'der40\n')
                elif (932 > x >= 924):
                    ser.write(b'der41\n')
                elif (939 > x >= 932):
                    ser.write(b'der42\n')
                elif (946 > x >= 939):
                    ser.write(b'der43\n')
                elif (953 > x >= 946):
                    ser.write(b'der44\n')
                elif (960 > x >= 953):
                    ser.write(b'der45\n')
                elif (967 > x >= 960):
                    ser.write(b'der46\n')
                elif (974 > x >= 967):
                    ser.write(b'der47\n')
                elif (981 > x >= 974):
                    ser.write(b'der48\n')
                elif (988 > x >= 981):
                    ser.write(b'der49\n')
                elif (996 > x >= 988):
                    ser.write(b'der50\n')
                elif (1003 > x >= 996):
                    ser.write(b'der51\n')
                elif (1010 > x >= 1003):
                    ser.write(b'der52\n')
                elif (1017 > x >= 1010):
                    ser.write(b'der53\n')
                elif (1024 > x >= 1017):
                    ser.write(b'der54\n')
                elif (1031 > x >= 1024):
                    ser.write(b'der55\n')
                elif (1038 > x >= 1031):
                    ser.write(b'der56\n')
                elif (1045 > x >= 1038):
                    ser.write(b'der57\n')
                elif (1052 > x >= 1045):
                    ser.write(b'der58\n')
                elif (1060 > x >= 1052):
                    ser.write(b'der59\n')
                elif (1067 > x >= 1060):
                    ser.write(b'der60\n')
                elif (1074 > x >= 1067):
                    ser.write(b'der61\n')
                elif (1081 > x >= 1074):
                    ser.write(b'der62\n')
                elif (1088 > x >= 1081):
                    ser.write(b'der63\n')
                elif (1095 > x >= 1088):
                    ser.write(b'der64\n')
                elif (1102 > x >= 1095):
                    ser.write(b'der65\n')
                elif (1109 > x >= 1102):
                    ser.write(b'der66\n')
                elif (1116 > x >= 1109):
                    ser.write(b'der67\n')
                elif (1124 > x >= 1116):
                    ser.write(b'der68\n')
                elif (1131 > x >= 1124):
                    ser.write(b'der69\n')
                elif (1138 > x >= 1131):
                    ser.write(b'der70\n')
                elif (1145 > x >= 1138):
                    ser.write(b'der71\n')
                elif (1152 > x >= 1145):
                    ser.write(b'der72\n')
                elif (1159 > x >= 1152):
                    ser.write(b'der73\n')
                elif (1166 > x >= 1159):
                    ser.write(b'der74\n')
                elif (1173 > x >= 1166):
                    ser.write(b'der75\n')
                elif (1180 > x >= 1173):
                    ser.write(b'der76\n')
                elif (1188 > x >= 1180):
                    ser.write(b'der77\n')
                elif (1195 > x >= 1188):
                    ser.write(b'der78\n')
                elif (1202 > x >= 1195):
                    ser.write(b'der79\n')
                elif (1209 > x >= 1202):
                    ser.write(b'der80\n')
                elif (1216 > x >= 1209):
                    ser.write(b'der81\n')
                elif (1223 > x >= 1216):
                    ser.write(b'der82\n')
                elif (1230 > x >= 1223):
                    ser.write(b'der83\n')
                elif (1237 > x >= 1230):
                    ser.write(b'der84\n')
                elif (1244 > x >= 1237):
                    ser.write(b'der85\n')
                elif (1252 > x >= 1244):
                    ser.write(b'der86\n')
                elif (1259 > x >= 1252):
                    ser.write(b'der87\n')
                elif (1266 > x >= 1259):
                    ser.write(b'der88\n')
                elif (1273 > x >= 1266):
                    ser.write(b'der89\n')
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            ser.close()
            break

cap.release()
cv2.destroyAllWindows()
