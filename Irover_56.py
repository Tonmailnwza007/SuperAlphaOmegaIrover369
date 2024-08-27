from irover  import *
from time import sleep
w=IROVER()
w.OK() #กดปุ่มสีเหลือง เพื่อทำงาน
w.led(1) #ไฟสีแดงเปิด
refL=1350 #ค่าที่ได้จากการวัดค่าแสง ด้าน L port32
refR=1150 #ค่าที่ได้จากการวัดค่าแสง ด้าน R port33

# while 1:
#   valKnob=int(i.knob(0,255))
#   w.fill(0)
#   w.text("KNOB=%d " % w.knob(),0,0*8)
#   w.text("IO34=%d " % w.analog(34),0,(1*8)+1)
#   w.text("iKB_pin1=%d " % w.analog(i1,-100,100),0,(2*8)+1)
#   w.text("iKB_pin0=%d " % w.input(i0),0,(3*8)+1)
#   w.show()
#   w.sled(1,(valKnob,valKnob,valKnob))
#   w.output(w6,w.sw1())
  
def Start_Robot(): #ฟังก์ชัน Start_robot
    w.fd2(30,30) #เดินหน้า 30,30
    w.sound(2000,0.5) #เสียงเตือน

def Follow_Line(): #ฟังก์ชัน Follow_line
    whwle True:
        L=w.analog(32) #เก็บค่าตัวแปร port32 ไว้ที่ L
        R=w.analog(33) #เก็บค่าตัวแปร port33 ไว้ที่ R
        if(L > refL and R > refR): #L เจอสีขาว R เจอสีขาว
            w.fd2(30,30) #เดินหน้า 30,30
        elif(L < refL and R > refR): #L เจอสีดำ R เจอสีขาว
            w.sl(30) #หมุนซ้าย 30
        elif(L > refL and R < refR): #L เจอสีขาว R เจอสีดำ
            w.sr(30) #หมุนขวา 30
        if(L < refL and R < refR): #L เจอสีดำ R เจอสีดำ
            break #หยุดการทำงาน

def Stop_Robot(): #ฟังก์ชัน Stop_robot
    while True:
        w.fill(0) #เคลียร์หน้าจอ
        Follow_line() #เรียกฟังก์ชัน Follow_line
        w.stop() #หยุดเคลื่อนที่
        w.sound(2000,0.5) #เสียงเตือน
        break #หยุดการทำงาน

def Cross_Over(): #ฟังก์ชัน Cross_Over
    while True: #ทําซ้ําถ้าเป็นจริง 
        w.fill(0) #เคลียร์หน้าจอ
        w.text("Move Over",0,10) # ข้อความ Move Over ตำแหน่ง (0,10)
        w.show() #แสดงข้อความ
        Follow_line() #เรียกฟังก์ชัน Follow Line 
        w.fd2(30,30) #เดินหน้า (30,30)
        sleep(0.2) #เวลา 0.3
        w.sound(2000,0.1) #เสียงเตือน
        break #หยุดการทํางาน

def Turn_Back(): #ฟังก์ชัน Turn_Back
    while True:
        w.fill(0) #เคลียร์หน้าจอ
        w.text("Back",0,40) #ข้อความ Back ตำแหน่ง (0,40)
        w.show() #แสดงข้อความ
        w.bk2(3,30) #ถอยหลัง(30,30)
        sleep(0.2) #เวลา 0.2
        w.sl(50) #หมุนซ้าย
        sleep(0.2) #เวลา 0.2
        while (w.analog(32) > refL): #port 32 เจอสีขาว
            w.sl(30) #หมุนซ้าย
        while (w.analog(32) < refL): #port 32 เจอสีดำ
            w.sl(30) #หมุนหมุนซ้าย
        break #หยุดการทำงาน
    
def Hit_Item(): #ฟังก์ชัน Hit_Item
    w.fill(0) #เคลียร์หน้าจอ
    w.text("Hit",0,30) #ข้อความ Back ตำแหน่ง (0,30)
    w.show() #แสดงข้อความ
    Follow_line() #เรียกฟังก์ชัน Follow_line
    w.stop() #หยุดเคลื่อนที่
    w.sound(2000,0.1) #เสียงเตือน
    w.servo(10,0) #เซอร์โว port10 ค่า 0 องศา
    sleep(1) #เวลา 1                                          
    w.servo(10,180) #เซอร์โว port10 ค่า 180 องศา
    sleep(1) #เวลา 1
    w.servo(10,0) #เซอร์โว port10 ค่า 0 องศา
    sleep(1) #เวลา 1

def Cross_Left(): #ฟังก์ชัน Cross_Left
    while True: #ทําซ้ําถ้าเป็นจริง
        w.fill(0) #เคลียร์หน้าจอ
        w.text("Left",0,20) #ข้อความ Left ตำแหน่ง (0,20)
        w.show() #แสดงข้อความ
        Follow_line() #เรียกฟังก์ชัน Follow_line
        w.fd2(30,30) #เดินหน้า 30,30
        sleep(0.3) #เวลา 0.3
        w.sound(2000,0.1) #เสียงเตือน
        while (w.analog(32) > refL): #port 32 เจอสีขาว
            w.sl(30) #หมุนซ้าย
        while (w.analog(32) < refL): #port 32 เจอสีดำ
            w.sl(30) #หมุนหมุนซ้าย
        break #หยุดการทำงาน
    
def Follow_Crossover(n):
    crossovered = 0
    while crossovered < n:
        Follow_Line()
        Cross_Over()
        crossovered += 1

