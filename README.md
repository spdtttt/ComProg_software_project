# Detective Game

เกมนักสืบแบบสุ่มคดีด้วยภาษา Python โดยเน้นการออกแบบโปรแกรมด้วยแนวคิด **Object-Oriented Programming (OOP)** เป็นหลัก ผู้เล่นจะรับบทเป็นนักสืบ ทำการสำรวจสถานที่ สอบสวนผู้ต้องสงสัย เก็บหลักฐาน และตัดสินใจว่าใครคือฆาตกร

---

## 1. Project Concept

ในแต่ละรอบ เกมจะสร้างคดีใหม่แบบสุ่ม โดยกำหนดข้อมูลสำคัญ เช่น

- ฆาตกร
- ผู้ต้องสงสัย 4-5 คน
- สถานที่ 4 แห่ง
- เวลาที่เกิดเหตุ
- แรงจูงใจ
- อาวุธ
- สถานที่เกิดเหตุ
- หลักฐานที่เกี่ยวข้องกับฆาตกร

ผู้เล่นจะ **ไม่เห็นข้อมูลเฉลยโดยตรง** แต่จะต้องค้นหาความจริงผ่านระบบ Investigation(สืบสวน) และ Interrogation(สอบสวน)

จุดสำคัญคือ หลักฐานไม่ได้ถูกสุ่มแบบอิสระจากคดี แต่ถูกสร้างขึ้น **หลังจากสุ่มฆาตกรแล้ว** ทำให้ Evidence ทุกชิ้นสามารถเชื่อมโยงกลับไปยังคนร้ายได้จริง

---

## 2. Main Requirements

โปรเจ็กต์นี้รองรับ Requirement หลักดังนี้

- Random murderer
- 4-5 suspects
- 4 locations
- Random crime time
- Random motive
- Random weapon
- Physical Evidence
- Digital Evidence
- Testimony
- Investigation
- Interrogation
- Evidence Inventory
- Accusation
- Win / Lose

---

## 3. Gameplay
	
เมื่อเริ่มเกม ระบบจะสุ่มคดีใหม่ จากนั้นแสดงข้อมูลเบื้องต้นให้ผู้เล่นทราบ เช่น รายชื่อผู้ต้องสงสัยและสถานที่ที่สามารถตรวจสอบได้

ผู้เล่นสามารถเลือก Action ได้ดังนี้

```text
1. Investigate Location
2. Interrogate Suspect
3. View Evidence Inventory
4. Accuse Suspect
5. Exit Game
```

### 3.1 Investigate Location

ผู้เล่นสามารถเลือกสถานที่เพื่อค้นหาหลักฐาน

ตัวอย่างสถานที่:

```text
1. Office
2. Lobby
3. Parking Lot
4. Security Room
```

เมื่อสำรวจสถานที่ อาจพบหลักฐาน เช่น

```text
[Physical Evidence]
Knife with fingerprints

A knife was discovered at the crime scene.
Fingerprints matching Bob Wilson were found on it.
```

หลักฐานที่พบจะถูกเพิ่มเข้าไปใน `Evidence Inventory` ของนักสืบโดยอัตโนมัติ

---

### 3.2 Interrogate Suspect

ผู้เล่นสามารถเลือกสอบสวนผู้ต้องสงสัยแต่ละคนได้

ตัวอย่าง:

```text
Interrogating: Bob Banana
Occupation: Business Partner

"I was at the Parking Lot around 22:15.
I never went near the Office."
```

คำให้การของฆาตกรจะถูกสร้างให้ขัดแย้งกับหลักฐานบางส่วน เพื่อให้ผู้เล่นสามารถจับพิรุธได้

ตัวอย่าง:

```text
Statement:
Bob says he was at the Parking Lot.

CCTV:
Bob entered the Office shortly before 22:15.
```

---

### 3.3 Evidence Inventory

หลักฐานที่เก็บได้จะถูกบันทึกไว้ในตัวนักสืบ

ตัวอย่าง:

```text
========== EVIDENCE ==========

Evidence #1
[Physical Evidence]
Knife with fingerprints

Evidence #2
[Digital Evidence]
Security Camera Footage

Evidence #3
[Testimony]
Witness Statement
```

ผู้เล่นสามารถย้อนกลับมาดู Evidence ทั้งหมดก่อนตัดสินใจกล่าวหาได้

---

### 3.4 Accuse Suspect

เมื่อผู้เล่นคิดว่าทราบตัวฆาตกรแล้ว สามารถเลือกกล่าวหาผู้ต้องสงสัยได้

เกมกำหนดให้มีโอกาสกล่าวหาเพียง **1 ครั้ง**

ถ้าถูกต้อง:

```text
========================================
                YOU WIN!
========================================

Correct! Bob Banana is the murderer.
```

ถ้าผิด:

```text
========================================
               YOU LOSE!
========================================

Alice Wang was innocent.
```

หลังจากนั้นเกมจะแสดงเฉลยของคดี

---

## 4. Game Flow

```text
START
  |
  v
Create Game
  |
  +--> Create Detective
  |
  +--> Generate Case
          |
          +--> Random 4-5 Suspects
          |
          +--> Random Murderer
          |
          +--> Random Crime Time
          |
          +--> Random Motive
          |
          +--> Random Weapon
          |
          +--> Random Crime Location
          |
          +--> Generate Statements
          |
          +--> Generate Evidence
                  |
                  +--> Physical Evidence
                  +--> Digital Evidence
                  +--> Testimony
  |
  v
Show Case Information
  |
  v
GAME LOOP
  |
  +--> Investigate Location
  |
  +--> Interrogate Suspect
  |
  +--> View Evidence
  |
  +--> Accuse Suspect
  |       |
  |       +--> Correct --> WIN
  |       |
  |       +--> Wrong --> LOSE
  |
  +--> Exit
```

---

## 5. OOP Design

โปรเจ็กต์นี้ถูกออกแบบให้ใช้ OOP เป็นส่วนหลัก ไม่ใช่เพียงสร้าง Class เพื่อเก็บข้อมูล

### 5.1 Class Hierarchy: Character

```text
              Character
                  |
       +----------+----------+
       |          |          |
       v          v          v
   Detective   Suspect     Victim
```

`Character` เป็น Parent Class ที่เก็บข้อมูลพื้นฐานของตัวละคร เช่น

- `name`
- `role`

จากนั้น Class อื่นจะ Inherit คุณสมบัติจาก `Character`

---

### 5.2 Class Hierarchy: Evidence

```text
                 Evidence
                    |
       +------------+------------+
       |            |            |
       v            v            v
   Physical      Digital      Testimony
   Evidence      Evidence      Evidence
```

`Evidence` เป็น Abstract Class และมี Abstract Method ชื่อ

```python
examine()
```

Evidence แต่ละชนิดจะ Override Method นี้ให้แสดงผลแตกต่างกัน

ตัวอย่าง:

```python
class PhysicalEvidence(Evidence):
    def examine(self):
        print("[Physical Evidence]")
```

```python
class DigitalEvidence(Evidence):
    def examine(self):
        print("[Digital Evidence]")
```

จึงเป็นตัวอย่างของ **Polymorphism**

---

## 6. OOP Concepts Used

### 6.1 Encapsulation

ข้อมูลสำคัญของคดีถูกซ่อนไว้ภายใน Object เช่น

```python
self.__murderer
self.__crime_time
self.__motive
self.__weapon
self.__crime_location
```

ผู้เล่นจึงไม่สามารถเข้าถึงเฉลยผ่าน Gameplay ปกติได้

ใน `Suspect` มีการซ่อนคำให้การไว้เช่นกัน

```python
self.__statement
```

---

### 6.2 Inheritance

ตัวอย่าง:

```python
class Suspect(Character):
    ...
```

```python
class Detective(Character):
    ...
```

```python
class PhysicalEvidence(Evidence):
    ...
```

ทำให้สามารถนำ Attribute และ Method พื้นฐานกลับมาใช้ซ้ำได้

---

### 6.3 Abstraction

`Evidence` ถูกกำหนดเป็น Abstract Class

```python
class Evidence(ABC):

    @abstractmethod
    def examine(self):
        pass
```

หมายความว่า Evidence ทุกประเภทต้องมี Method `examine()` ของตัวเอง

---

### 6.4 Polymorphism

Evidence ทั้งหมดสามารถเรียก Method เดียวกันได้

```python
evidence.examine()
```

แต่ผลลัพธ์ขึ้นอยู่กับชนิดของ Object

เช่น

- `PhysicalEvidence`
- `DigitalEvidence`
- `TestimonyEvidence`


---

## 7. Important Classes

### Character

เป็น Base Class ของตัวละครทั้งหมด

```python
class Character:
    def __init__(self, name, role):
        self.name = name
        self.role = role
```

---

### Suspect

ใช้แทนผู้ต้องสงสัยแต่ละคน

หน้าที่หลัก:

- เก็บชื่อ
- เก็บอาชีพ
- เก็บคำให้การ
- รองรับการสอบสวน

```python
suspect.interrogate()
```

---

### Detective

แทนผู้เล่น

หน้าที่หลัก:

- เก็บ Evidence Inventory
- รับหลักฐานใหม่
- แสดงหลักฐานทั้งหมด

```python
detective.collect_evidence(evidence)
```

---

### Evidence

เป็น Abstract Class สำหรับหลักฐาน

แบ่งออกเป็น

```text
PhysicalEvidence
DigitalEvidence
TestimonyEvidence
```

---

### Location

แทนสถานที่ในเกม

หน้าที่หลัก:

- เก็บ Evidence
- ตรวจสอบว่าสถานที่เคยถูกสำรวจหรือยัง
- ส่ง Evidence ให้ Detective เมื่อสำรวจ

---

### Case

ใช้เก็บข้อมูลทั้งหมดของคดี

ประกอบด้วย

```text
Victim
Suspects
Locations
Murderer
Crime Time
Motive
Weapon
Crime Location
```

รวมทั้งตรวจสอบผลการกล่าวหา

```python
case.accuse(suspect)
```

---

### CaseGenerator

เป็น Class ที่ใช้สร้างคดีแบบสุ่ม

หน้าที่หลัก:

```text
Random Suspects
      |
Random Murderer
      |
Random Crime Information
      |
Generate Statements
      |
Generate Evidence
      |
Create Case
```

การแยก `CaseGenerator` ออกจาก `Case` ทำให้แต่ละ Class มีหน้าที่ชัดเจนขึ้น

---

### Game

เป็นตัวควบคุม Gameplay หลัก

หน้าที่:

- เริ่มเกม
- แสดง Menu
- รับ Input
- ควบคุม Game Loop
- เรียก Investigation
- เรียก Interrogation
- ตรวจสอบ Accusation
- จบเกม

---

## 8. Evidence Generation

จุดสำคัญของเกมคือ Evidence จะถูกสร้างให้สัมพันธ์กับฆาตกร

สมมติสุ่มได้ว่า

```text
Murderer: Bob Banana
Crime Time: 22:15
Crime Location: Office
Weapon: Knife
```

ระบบจะสร้างหลักฐานประมาณนี้

### Physical Evidence

```text
Knife with fingerprints

Fingerprints matching Bob Banana
were found on the knife.
```

### Digital Evidence

```text
Security Camera Footage

Bob Banana entered the Office
shortly before 22:15.
```

### Testimony

```text
Witness Statement

A witness saw Bob Banana
leaving the Office around 22:15.
```

แต่ Bob อาจให้การว่า

```text
"I was at the Parking Lot around 22:15.
I never went near the Office."
```

ผู้เล่นจึงสามารถเชื่อมโยงข้อมูลและจับความขัดแย้งได้

---

## 9. Example Investigation Flow

```text
New Case Generated
        |
        v
Murderer = Diana
Time = 21:45
Weapon = Poison
Location = Office
        |
        v
Interrogate Diana
        |
        v
"I was at the Parking Lot."
        |
        v
Investigate Security Room
        |
        v
CCTV shows Diana entering Office
        |
        v
Investigate Office
        |
        v
Physical evidence links Diana
to the crime
        |
        v
Investigate Lobby
        |
        v
Witness saw Diana leaving Office
        |
        v
Accuse Diana
        |
        v
YOU WIN
```

---

## Conclusion

**AI Detective Game** เป็นโปรเจ็กต์เกมสืบสวนด้วย Python ที่ออกแบบมาเพื่อแสดงการประยุกต์ใช้แนวคิด Object-Oriented Programming อย่างชัดเจน

โปรเจ็กต์นี้ใช้แนวคิดสำคัญ ได้แก่

```text
Encapsulation
Inheritance
Abstraction
Polymorphism
Composition
```

ผู้เล่นต้องสำรวจสถานที่ สอบสวนผู้ต้องสงสัย วิเคราะห์หลักฐาน และเชื่อมโยงข้อมูลเพื่อหาฆาตกร

เนื่องจากคดีสามารถถูกสร้างใหม่แบบสุ่มในแต่ละรอบ จึงทำให้เกมสามารถเล่นซ้ำได้ และโครงสร้าง Class ยังรองรับการเพิ่มระบบใหม่ในอนาคตได้โดยไม่จำเป็นต้องแก้โปรแกรมทั้งหมด
