from irover  import *
from time import sleep
w=IROVER()
w.OK() #กดปุ่มสีเหลือง เพื่อทำงาน
w.led(1) #ไฟสีแดงเปิด
refL=1350 #ค่าที่ได้จากการวัดค่าแสง ด้าน L port32
refR=1150 #ค่าที่ได้จากการวัดค่าแสง ด้าน R port33

#Lightning Mcqueeen Sectionnnnnnnnnn
speed_forward = 30  # ความเร็วเดินหน้า
speed_left = 30     # ความเร็วหมุนซ้าย
speed_right = 30    # ความเร็วหมุนขวา
speed_back = 30     # ความเร็วถอยหลัง

def Start_Robot():  # ฟังก์ชัน Start_robot
    w.fd2(speed_forward, speed_forward)  # เดินหน้า
    w.sound(2000, 0.5)  # เสียงเตือน

def Follow_Line():  # ฟังก์ชัน Follow_line
    while True:
        L = w.analog(32)  # เก็บค่าตัวแปร port32 ไว้ที่ L
        R = w.analog(33)  # เก็บค่าตัวแปร port33 ไว้ที่ R
        if L > refL and R > refR:  # L เจอสีขาว R เจอสีขาว
            w.fd2(speed_forward, speed_forward)  # เดินหน้า
        elif L < refL and R > refR:  # L เจอสีดำ R เจอสีขาว
            w.sl(speed_left)  # หมุนซ้าย
        elif L > refL and R < refR:  # L เจอสีขาว R เจอสีดำ
            w.sr(speed_right)  # หมุนขวา
        if L < refL and R < refR:  # L เจอสีดำ R เจอสีดำ
            break  # หยุดการทำงาน

def Stop_Robot():  # ฟังก์ชัน Stop_robot
    while True:
        w.fill(0)  # เคลียร์หน้าจอ
        Follow_Line()  # เรียกฟังก์ชัน Follow_line
        w.stop()  # หยุดเคลื่อนที่
        w.sound(2000, 0.5)  # เสียงเตือน
        break  # หยุดการทำงาน

def Cross_Over():  # ฟังก์ชัน Cross_Over
    while True:  # ทําซ้ําถ้าเป็นจริง
        w.fill(0)  # เคลียร์หน้าจอ
        w.text("Move Over", 0, 10)  # ข้อความ Move Over ตำแหน่ง (0,10)
        w.show()  # แสดงข้อความ
        Follow_Line()  # เรียกฟังก์ชัน Follow Line
        w.fd2(speed_forward, speed_forward)  # เดินหน้า
        sleep(0.2)  # เวลา 0.3
        w.sound(2000, 0.1)  # เสียงเตือน
        break  # หยุดการทํางาน

def Turn_Back():  # ฟังก์ชัน Turn_Back
    while True:
        w.fill(0)  # เคลียร์หน้าจอ
        w.text("Back", 0, 40)  # ข้อความ Back ตำแหน่ง (0,40)
        w.show()  # แสดงข้อความ
        w.bk2(speed_back, speed_back)  # ถอยหลัง
        sleep(0.2)  # เวลา 0.2
        w.sl(speed_left)  # หมุนซ้าย
        sleep(0.2)  # เวลา 0.2
        while w.analog(32) > refL:  # port 32 เจอสีขาว
            w.sl(speed_left)  # หมุนซ้าย
        while w.analog(32) < refL:  # port 32 เจอสีดำ
            w.sl(speed_left)  # หมุนหมุนซ้าย
        break  # หยุดการทำงาน

def Hit_Item():  # ฟังก์ชัน Hit_Item
    w.fill(0)  # เคลียร์หน้าจอ
    w.text("Hit", 0, 30)  # ข้อความ Back ตำแหน่ง (0,30)
    w.show()  # แสดงข้อความ
    Follow_Line()  # เรียกฟังก์ชัน Follow_line
    w.stop()  # หยุดเคลื่อนที่
    w.sound(2000, 0.1)  # เสียงเตือน
    w.servo(10, 0)  # เซอร์โว port10 ค่า 0 องศา
    sleep(1)  # เวลา 1
    w.servo(10, 180)  # เซอร์โว port10 ค่า 180 องศา
    sleep(1)  # เวลา 1
    w.servo(10, 0)  # เซอร์โว port10 ค่า 0 องศา
    sleep(1)  # เวลา 1

def Cross_Left():  # ฟังก์ชัน Cross_Left
    while True:  # ทําซ้ําถ้าเป็นจริง
        w.fill(0)  # เคลียร์หน้าจอ
        w.text("Left", 0, 20)  # ข้อความ Left ตำแหน่ง (0,20)
        w.show()  # แสดงข้อความ
        Follow_Line()  # เรียกฟังก์ชัน Follow_line
        w.fd2(speed_forward, speed_forward)  # เดินหน้า
        sleep(0.3)  # เวลา 0.3
        w.sound(2000, 0.1)  # เสียงเตือน
        while w.analog(32) > refL:  # port 32 เจอสีขาว
            w.sl(speed_left)  # หมุนซ้าย
        while w.analog(32) < refL:  # port 32 เจอสีดำ
            w.sl(speed_left)  # หมุนหมุนซ้าย
        break  # หยุดการทำงาน

def Cross_Right():  # ฟังก์ชัน Cross_Right
    while True:  # ทําซ้ําถ้าเป็นจริง
        w.fill(0)  # เคลียร์หน้าจอ
        w.text("Right", 0, 20)  # ข้อความ Right ตำแหน่ง (0,20)
        w.show()  # แสดงข้อความ
        Follow_Line()  # เรียกฟังก์ชัน Follow_line
        w.fd2(speed_forward, speed_forward)  # เดินหน้า
        sleep(0.3)  # รอเวลา 0.3 วินาที
        w.sound(2000, 0.1)  # ส่งเสียงเตือน
        while w.analog(33) > refL:  # port 33 เจอสีขาว
            w.sr(speed_right)  # หมุนขวา
        while w.analog(33) < refL:  # port 33 เจอสีดำ
            w.sr(speed_right)  # หมุนขวา
        break  # หยุดการทำงาน

def Follow_Crossover(n):
    crossovered = 0
    while crossovered < n:
        Follow_Line()
        Cross_Over()
        crossovered += 1


