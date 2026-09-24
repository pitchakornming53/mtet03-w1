# Lecture Note — สัปดาห์ที่ 12

วิชา 030143375 อินเตอร์เน็ตของสรรพสิ่งสำหรับงานอุตสาหกรรม
เรื่อง การใช้งาน GitHub, Docker และ n8n
ชื่อ–นามสกุล: ____________________ รหัสนักศึกษา: ____________________
แหล่งบทเรียน: https://minrobots.com/IoTMtET/Contents/Week12.html

## 1. วัตถุประสงค์

เรียนรู้การจัดการเวอร์ชันและทำงานร่วมกันด้วย GitHub การบรรจุโปรแกรมพร้อม dependency ด้วย Docker และการเชื่อมงานอัตโนมัติผ่าน n8n รวมทั้งประยุกต์กับ ESP32, OpenCV และ AI
บทเรียนกำหนดบรรยาย 120 นาทีและปฏิบัติ 120 นาที

## 2. Git และ GitHub

Git เป็นระบบควบคุมเวอร์ชันแบบกระจาย เก็บประวัติการเปลี่ยนแปลง ย้อนดูและเปรียบเทียบโค้ดได้
GitHub เป็นบริการโฮสต์ Git repository และสนับสนุนการร่วมพัฒนา เช่น Pull Request และการตรวจโค้ด
Repository คือพื้นที่โปรเจกต์; commit คือจุดบันทึกการเปลี่ยนแปลง; branch คือสายการพัฒนาที่แยกจากกัน
README อธิบายวัตถุประสงค์ การติดตั้งและการใช้งานให้ผู้เปิดโปรเจกต์เข้าใจ

### ขั้นตอนบนเว็บไซต์ตามบทเรียน

สมัคร GitHub → สร้าง repository → สร้าง branch → แก้ README.md → commit
จากนั้นสร้าง Pull Request เปรียบเทียบ branch ตรวจ diff และ merge เมื่อพร้อม
หลัง merge สามารถลบ branch ที่ใช้เสร็จแล้ว หรือ restore branch บน GitHub ในกรณีที่ระบบรองรับ
ตรวจหน้า main อีกครั้งว่าการแก้ไขถูกนำมารวมแล้ว

### ใช้ Git บนเครื่องผ่าน VS Code

ติดตั้ง Git จาก https://git-scm.com/downloads แล้วเปิดโฟลเดอร์งานใน VS Code
สร้าง test.py ที่มี `print("Hi")` และสร้าง remote repository ว่างก่อนเชื่อมต่อ

```sh
git init
git add test.py
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

git add นำการแก้ไขเข้าสู่ staging area; ใช้ git add . เพื่อ stage ทุกไฟล์ที่ไม่ถูก ignore
git commit บันทึกในเครื่อง; git push ส่ง commit ไป remote; git pull ดึงและรวมการเปลี่ยนแปลงจาก remote
เมื่อแก้โค้ดครั้งต่อไป ใช้ git diff ตรวจ แล้ว git add, git commit และ git push อีกครั้ง
สีเขียวใน VS Code อาจแสดงไฟล์ใหม่ที่ Git ยังไม่ได้ติดตาม แต่ควรใช้ git status ตรวจสถานะให้ชัดเจน

Fork คือสร้างสำเนา repository บนบัญชี GitHub ของตนเอง ส่วน clone คือดาวน์โหลด repository พร้อมประวัติมายังเครื่อง
บทเรียนยกตัวอย่าง Python-World/python-mini-projects ให้ fork ก่อนแล้วใช้ git clone URL ของ fork
เมื่อชนกันระหว่าง merge ต้องตรวจและแก้ conflict ให้ถูกต้องก่อน commit
ห้าม commit รหัสผ่าน API key หรือ token ให้ใช้ .gitignore และระบบ Credentials

## 3. Docker

Docker บรรจุแอปและ dependency เป็น image แล้วสร้าง container เพื่อรัน
Image เป็นแม่แบบแบบอ่านอย่างเดียว ส่วน container เป็น instance ที่มีสถานะขณะทำงาน
ช่วยลดความแตกต่างของสภาพแวดล้อม แต่ยังต้องพิจารณาระบบปฏิบัติการ สถาปัตยกรรมและอุปกรณ์ที่โปรแกรมต้องใช้
Dockerfile อธิบายการสร้าง image; registry เช่น Docker Hub ใช้เก็บและแจกจ่าย image

### ทดลองและจัดการ container

ติดตั้ง Docker Desktop จาก https://www.docker.com/ และเปิด engine ก่อนใช้งาน

```sh
docker --version
docker run hello-world
docker run -d -p 8080:80 --name my-web-server nginx
docker ps
docker ps -a
docker stop my-web-server
docker start my-web-server
docker rm my-web-server
docker images
docker rmi nginx
```

เปิด http://localhost:8080 เพื่อทดสอบ nginx ขณะ container ทำงาน
-d รันเบื้องหลัง; -p 8080:80 เชื่อมพอร์ต 8080 ของเครื่องกับพอร์ต 80 ใน container
docker ps แสดง container ที่กำลังทำงาน; -a รวมที่หยุดแล้ว
ต้อง stop container ก่อน rm ตามตัวอย่างปกติ และลบ container ที่อ้างอิง image ก่อน rmi
ข้อมูลใน writable layer ของ container หายเมื่อลบ container จึงใช้ volume หรือ bind mount สำหรับข้อมูลที่ต้องเก็บ

### สร้าง image ของ Python Flask ตามบทเรียน

requirements.txt ใส่ Flask; test.py สร้าง Flask app มี route / ตอบ Hello, World! และรัน host 0.0.0.0 port 5000
Dockerfile ใช้ FROM python:3.13-slim, WORKDIR /app, COPY requirements.txt ., RUN pip install -r requirements.txt, COPY . . และ CMD ["python", "test.py"]

```sh
docker build -t my-app1 .
docker images
docker run -d -p 5000:5000 my-app1
```

เปิด http://localhost:5000 เพื่อทดสอบ จุดท้ายคำสั่ง build คือ build context
0.0.0.0 ทำให้แอปรับการเชื่อมต่อจากภายนอก container ผ่านพอร์ตที่ publish ได้
Flask development server เหมาะกับการทดลอง ตัวอย่างนี้ไม่ได้ออกแบบสำหรับ production
Assignment เปลี่ยนงาน Python เป็นการประมวลผลภาพ OpenCV โดยใช้ headless และบันทึกไฟล์แทนหน้าต่าง GUI

## 4. n8n และการเชื่อม AI

n8n เป็นเครื่องมือสร้าง workflow ด้วย node และเส้นเชื่อม Trigger เริ่มงาน ส่วน node ถัดไปแปลงข้อมูล เรียก API และส่งผลลัพธ์
ข้อมูลระหว่าง node มักอยู่ในรูป items ที่มี json สามารถอ้างค่าด้วย expression เช่น {{ $json.text }}
Credentials เก็บข้อมูลยืนยันตัวตนแยกจากขั้นตอนประมวลผล

บทเรียนแนะนำติดตั้ง Node.js แบบ LTS พร้อม Add to PATH แล้วใช้ `npm install -g n8n` และรัน `n8n`
เปิด http://localhost:5678 เพื่อสร้าง workflow อย่างไรก็ตามเวอร์ชัน Node.js ที่รองรับเปลี่ยนตาม n8n จึงตรวจเอกสารก่อนติดตั้ง ไม่ยึดตัวอย่าง 20.x ในบทเรียนตลอดไป
ชุดงานนี้ใช้ Docker Compose เพื่อรัน n8n และเก็บข้อมูลใน volume โดยไม่ต้องติดตั้ง Node.js บนเครื่อง

การเรียก AI ต้องมีบัญชีผู้ให้บริการ เช่น OpenAI หรือ DeepSeek และ API key ที่ใช้ได้
ส่ง prompt พร้อมข้อมูลไปยัง API แล้วนำข้อความตอบกลับไปยัง Social Media หรือ Chat
ตรวจคำตอบกับข้อมูลต้นทางเสมอ เพราะ AI อาจสรุปผิดหรือเพิ่มข้อสันนิษฐาน
ngrok ใช้ทำ tunnel ให้บริการภายนอกเข้าถึงระบบ local สำหรับ webhook; flow ที่เริ่มด้วย Manual Trigger และส่งออกอย่างเดียวไม่จำเป็นต้องใช้

ตัวอย่าง Assignment: Manual Trigger → ข้อมูลเครื่องจักรจำลอง → HTTP Request เรียก DeepSeek → จัดข้อความ → ส่ง Telegram
ใช้ข้อมูลจำลองที่ระบุชัดเจน และตั้งปลายทางเป็นแชตของผู้ทดลอง
ตรวจ execution ของแต่ละ node รวมถึงข้อความที่ได้รับจริงก่อนรายงานความสำเร็จ

## 5. การประยุกต์กับ IoT อุตสาหกรรม

PlatformIO จัดการโปรเจกต์ Arduino และการ build/upload ไปยัง ESP32 ส่วน GitHub เก็บโค้ดและประวัติ
Docker ใช้บรรจุงานประมวลผลภาพบนคอมพิวเตอร์หรือเซิร์ฟเวอร์
n8n เชื่อมข้อมูลจากระบบกับ AI และแชตแจ้งผล ตัวอย่างทั้งสามส่วนในชุดนี้สาธิตแยกกัน ไม่ได้อ้างว่า ESP32 ส่งภาพหรือเชื่อมระบบทั้งหมดแล้ว
ข้อดีคือแบ่งหน้าที่ชัดเจนและนำไปพัฒนาต่อได้ โดยต้องทดสอบบนอุปกรณ์และสภาพแวดล้อมจริง

## 6. สิ่งที่จัดทำตาม Assignment

1. Lecture Note ฉบับนี้ครอบคลุม GitHub, Docker และ n8n ตามหัวข้อในหน้าเรียน
2. PlatformIO ESP32 Blink พร้อมขั้นตอนสร้าง repository และเปลี่ยนช่วงเวลา 1000 → 500 ms ผ่าน branch/PR
3. Python OpenCV และ Dockerfile สำหรับนับวัตถุจากภาพ พร้อมภาพก่อนและหลังประมวลผล
4. n8n workflow เรียก AI แล้วส่งข้อความเข้า Telegram พร้อมวิธีตั้ง credential

หัวข้อ Homework เรื่องตอบลูกค้าอัตโนมัติเป็นงานแยกจาก Assignment ที่ผู้ใช้ขอ จึงไม่ได้รวมในชุดนี้

## เอกสารประกอบ

- บทเรียน: https://minrobots.com/IoTMtET/Contents/Week12.html
- PlatformIO ESP32: https://docs.platformio.org/en/latest/boards/espressif32/esp32dev.html
- Docker: https://docs.docker.com/get-started/
- n8n Docker: https://docs.n8n.io/hosting/installation/docker/
- n8n HTTP Request: https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/
