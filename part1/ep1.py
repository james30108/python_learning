# Python สามารถแสดงตัวแกรได้โดยไม่ต้องประกาศชนิดของข้อมูล เช่น
a = "500"
b = 10
c = 10.5 
d = True
e,f,g = 5,7,9

print(str(10))  # str คือคำสั่งแปลงค่าให้เป็น String
print(type(a))  # type คือคำสั่งแสดงชนิดข้อมูล
print(int(a))   # int คือแปลงชนิดข้อมูลให้เป็น integer
print(float(a)) # float คือแปลงชนิดข้อมูลให้เป็น float (ให้มีทศนิยม)

# ---------------------
"""
กฏการตั้งชื่อ
1. ใส่ตัวเลข ตัวอักษร เครื่องหมายได้
2. ห้ามขึ้นต้นด้วยตัวเลขและสัญลักษณ์พิเศษ (ยกเว้น Under Score)
3. ห้ามซ้ำกับ Keyword ของระบบ (เช่น fase, class, and)
4. case sensitive (พิมพ์เล็กพิมพ์ใหญ่)
"""

# ---------------------
name = input("ป้อนชื่อของท่าน = ") # input คือคำสั่งสำหรับรับค่าจากแป้นพิมพ์
print("ชื่อของท่านคือ = " + name)

# ตัวอย่างการป้อนข้อมูลชนิดตัวเลข
e = int(input("ป้อนตัวเลขที่ 1 : "))
f = int(input("ป้อนตัวเลขที่ 2 : "))
g = e + f
"""
สามารถทำแบบนี้ก็ได้
g = int(e) + int(f)
"""
print(g)

# ---------------------
"""
Oparetor

+ บวก
- ลบ
* คูณ
/ หาร
// หารปัดเศษ
** ยกกำลัง
% หารเอาเศษ
"""

# ---------------------
# ตัวดำเนินการทางตรรกศาสตร์
# and , or, not

a = (5 > 10) # ค่า a = bool
b = (10 == 5) # ค่า b = bool

c = x and y
d = x or y
e = x not y

print (c)
print (d)
print (e)

# ---------------------
# Compound Assiment
# ตัวอย่าง
a = 10
a+=5 # นำ A มาเพิ่มอีก 5
a-=5
a*=5
a**=5
a/=5
a//=5
a%=5

# ---------------------