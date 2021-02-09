# https://docs.python.org/3/tutorial/errors.html
# https://realpython.com/python-exceptions/
# https://www.datacamp.com/community/tutorials/exception-handling-python
# https://www.youtube.com/watch?v=NIWwJbo-9_8

# Error and Exception handling
# การจัดการ Error ช่วยเพิ่มความแข็งแกร่งให้กับโปรแกรมของเรา เมื่อเกิดความผิดพลาด โปรแกรมจะยังสามารถทำงานต่อไปได้
# ถ้าโปรแกรมไม่มีการจัดการข้อความพลาดที่ดี เมื่อเกิด Exception จะส่งผลให้โปรแกรมหยุดทำงานได้
# 
# ในแต่ละภาษาก็จะมีคำสั่งให้ใช้ในการจัดการข้อผิดพลาด
# ในภาษา python จะใช้ try,except,finally
# 
#  ในตัวอย่างนี้จะเป็นการจัดการข้อผิดพลาดเกี่ยวกับไฟล์

class NotAllowFileError(Exception): # สร้าง Exception เอง โดย inherite Exception class
    def __init__(self, filename):
        self.message = filename + '  is not allowed.'
        super().__init__(self.message)

try:
    # สั่งเปิดไฟล์ จะเกิด Error ถ้าไฟล์ไม่มีอยู่จริง ตอนทดสอบก็ให้แก้ชื่อไฟล์เป็นชื่ออื่น FileNotFoundError
    f1 = open('neis0736.txt')    

    # สั่งเปิดไฟล์และเขียนไฟล์ จะเกิด Error ถ้ามีไฟล์นี้อยู่แล้ว FileExistsError
    f2 = open('abc.txt','x')    
   
    # การใช้ Exception ที่เราประกาศเอง NotAllowFileError
    f3 = open('def.txt')
    if f3.name == 'def.txt': # ถ้าชื่อไฟล์ตรงกัน
        raise NotAllowFileError(f3.name) # สั่งให้ Error ไม่อนุญาตให้เปิดไฟล์นี้

    # จะเกิด Error เพราะ bad_var ยังไม่ได้ประกาศ Exception
    var = bad_var
except FileNotFoundError as e:
    print(e)
except FileExistsError as e:
    print(e)
except NotAllowFileError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f1.read())
    f1.close()
finally:
    print('End process')

# ลำดับการทำงานของ except จะทำจากบนลงล่าง
# จะทำคำสั่งใน else เมื่อไม่มีการเกิด Error เลย
# คำสั่งใน finally จะทำงานเสมอ ไม่ว่าจะเกิด Error หรือไม่ก็ตาม