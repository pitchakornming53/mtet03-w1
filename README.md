# mtet03-w1 — Calculator

เครื่องคิดเลข (Calculator) ธีมสีแดงเข้ม รองรับการใช้งาน 2 รูปแบบ:

- **Desktop app** — เขียนด้วย Python (Tkinter) — `test.py`
- **Web version** — เขียนด้วย HTML/CSS/JavaScript ล้วน (ไม่ต้องพึ่ง library ภายนอก) — `webpage.html`

ทั้งสองเวอร์ชันมีหน้าตาและฟังก์ชันการทำงานเหมือนกัน

## ฟีเจอร์

- บวก ลบ คูณ หาร (`+ − × ÷`)
- ปุ่มพิเศษ: `C` (ล้างค่า), `±` (สลับเครื่องหมาย), `%` (เปอร์เซ็นต์)
- แสดงนิพจน์ย่อย (sub-display) ด้านบนตอนกด `=`
- ป้องกันการใส่จุดทศนิยมซ้ำในตัวเลขเดียวกัน
- คำนวณแบบปลอดภัย โดยกรองอักขระที่อนุญาตก่อนประมวลผล (ไม่ eval string ที่ผู้ใช้พิมพ์ตรง ๆ)
- จัดรูปแบบผลลัพธ์อัตโนมัติ (ตัดเลข 0 ท้ายทศนิยมที่ไม่จำเป็นออก)

## วิธีใช้งาน

### Desktop (Python)

ต้องติดตั้ง Python 3 (มี Tkinter ติดตั้งมาให้อยู่แล้วในไลบรารีมาตรฐาน)

```bash
python test.py
```

หรือดับเบิลคลิกไฟล์ `run1.bat` (หรือชอร์ตคัต `run1 - ทางลัด.lnk`) เพื่อรันโปรแกรมได้ทันทีบน Windows

### Web (HTML)

เปิดไฟล์ `webpage.html` ด้วยเว็บเบราว์เซอร์ได้โดยตรง ไม่ต้องมีเซิร์ฟเวอร์หรือการติดตั้งเพิ่มเติม

## หน้าเว็บข้อมูลส่วนตัว (Personal Profile)

ในโฟลเดอร์ `profile/` มีหน้าเว็บข้อมูลส่วนตัว (ธีมขาวดำ) พร้อมรูปโปรไฟล์ (ลบพื้นหลังแล้ว คงสีจริงของรูป) และลิงก์อีเมล/เบอร์โทร และสคริปต์สำหรับรัน private server (เข้าถึงได้เฉพาะเครื่องนี้ ไม่เปิดสู่สาธารณะ)

```
profile/
├── index.html                # หน้าเว็บข้อมูลส่วนตัว
├── assets/avatar.png          # รูปโปรไฟล์ (สีจริง, ลบพื้นหลังแล้ว — พื้นหลังโปร่งใส)
├── assets/avatar_source.png   # รูปต้นฉบับก่อนลบพื้นหลัง (เก็บไว้สำรอง)
├── server.py                  # private server (Python http.server, bind เฉพาะ 127.0.0.1)
└── run_server.bat             # สคริปต์รัน server.py บน Windows
```

**แก้ไขข้อมูลก่อนใช้งาน:**
- เปิด `profile/index.html` แล้วแก้ไขชื่อ, อีเมล, เบอร์โทรให้เป็นของคุณเอง
- แทนที่ `profile/assets/avatar.png` ด้วยรูปอื่นได้ตามต้องการ (แนะนำให้ใช้รูปพื้นหลังโปร่งใส/PNG)

**รัน private server:**

```bash
cd profile
python server.py
```

หรือดับเบิลคลิก `profile/run_server.bat` — เบราว์เซอร์จะเปิดไปที่ `http://127.0.0.1:8000/` โดยอัตโนมัติ เซิร์ฟเวอร์นี้ผูกกับ `127.0.0.1` เท่านั้น จึงเข้าถึงได้จากเครื่องนี้เครื่องเดียว (private) กด `Ctrl+C` เพื่อหยุดเซิร์ฟเวอร์

## โครงสร้างไฟล์

```
├── test.py               # แอปเครื่องคิดเลข (Python + Tkinter)
├── webpage.html           # แอปเครื่องคิดเลขเวอร์ชันเว็บ (HTML/CSS/JS)
├── run1.bat               # สคริปต์รัน test.py บน Windows
├── run1 - ทางลัด.lnk      # ชอร์ตคัตสำหรับรัน run1.bat
├── run.bat.txt            # สำเนาสคริปต์รัน (text)
└── profile/               # หน้าเว็บข้อมูลส่วนตัว + private server
    ├── index.html
    ├── assets/avatar.png
    ├── assets/avatar_source.png
    ├── server.py
    └── run_server.bat
```

## Arduino Teamwork

เริ่มทำงาน Arduino เป็นทีมได้จาก [คู่มือ Arduino Teamwork](ARDUINO_TEAMWORK.md) พร้อมตัวอย่าง [Blink](Blink/Blink.ino) และแบบฟอร์ม Issues / Pull Requests สำหรับแบ่งงานและตรวจโค้ด


## Week 12 — GitHub, Docker และ n8n

เปิด [ชุด Assignment สัปดาห์ที่ 12](Week12_Assignment/README.md) รวม Lecture Note, ESP32 PlatformIO, Docker OpenCV และ n8n AI → Telegram พร้อมคู่มือภาษาไทยและผลทดสอบที่ระบุขอบเขตไว้
