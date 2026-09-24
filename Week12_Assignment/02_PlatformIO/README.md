# Arduino PlatformIO บน ESP32

ตัวอย่างใช้ ESP32 Dev Module แบบ ESP32 รุ่นดั้งเดิม ไม่ใช่ ESP32-C3/S3
ติดตั้ง VS Code และส่วนขยาย PlatformIO IDE แล้วเปิดโฟลเดอร์ `02_PlatformIO`
ต่อ LED ภายนอก: GPIO2 → ตัวต้านทาน 220–330 Ω → ขา Anode ของ LED และ Cathode → GND
บางบอร์ดมี LED ที่ GPIO2 อยู่แล้ว หากบอร์ดใช้ขาอื่นให้แก้ LED_PIN ตามวงจรบอร์ด

## Build / Upload / Monitor

เปิด PlatformIO Core CLI จาก VS Code แล้วรันในโฟลเดอร์นี้:

```sh
pio run
pio run --target upload
pio device monitor --baud 115200
```

หากอัปโหลดไม่ได้ ตรวจสาย USB ที่รับส่งข้อมูลได้ พอร์ตและไดรเวอร์ของบอร์ด
ผลที่คาดหวังสำหรับโค้ดปัจจุบัน: LED สลับ ON/OFF ทุก 0.5 วินาที หนึ่งรอบติดและดับรวม 1 วินาที
ใช้ millis() เพื่อตรวจเวลาโดยไม่หยุด loop() ด้วย delay()

## เปิดงานจาก repository นี้

โปรเจกต์อยู่ที่ https://github.com/pitchakornming53/mtet03-w1/tree/main/Week12_Assignment/02_PlatformIO

```sh
git clone https://github.com/pitchakornming53/mtet03-w1.git
cd mtet03-w1
```

เปิดโฟลเดอร์ Week12_Assignment/02_PlatformIO ใน VS Code เพื่อ Build / Upload

## แสดงวิธีแก้ Code ผ่าน branch และ Pull Request

จากราก repository mtet03-w1:

```sh
git switch -c feature/faster-blink
```

แก้ `02_PlatformIO/src/main.cpp` จาก:

```cpp
constexpr unsigned long BLINK_INTERVAL_MS = 1000;
```

เป็น:

```cpp
constexpr unsigned long BLINK_INTERVAL_MS = 500;
```

ทดสอบ build และ upload จากโฟลเดอร์ PlatformIO แล้วกลับโฟลเดอร์หลัก:

```sh
git diff
git add Week12_Assignment/02_PlatformIO/src/main.cpp
git commit -m "Change LED toggle interval from 1000 to 500 ms"
git push -u origin feature/faster-blink
```

บน GitHub เลือก Compare & pull request → ตรวจ Files changed → Create pull request → Merge pull request
จากนั้นที่เครื่องรัน `git switch main` และ `git pull origin main`
ผลที่คาดหวังหลังแก้: LED เปลี่ยนสถานะทุก 0.5 วินาที หนึ่งรอบติดและดับรวม 1 วินาที
เก็บภาพ repository, diff, commit/PR และ Serial Monitor เป็นหลักฐานจริง

อ้างอิง: https://docs.platformio.org/en/latest/boards/espressif32/esp32dev.html

## ประวัติการแก้โค้ดที่ทำไว้จริง

commit แรกเพิ่มโค้ด BLINK_INTERVAL_MS = 1000 จากนั้น commit ถัดมาเปลี่ยนเป็น 500 พร้อมปรับเอกสารนี้ เปิด History ของ src/main.cpp เพื่อดู diff จริงได้
ตัวอย่างคำสั่ง branch/PR ด้านบนเป็นขั้นตอนสำหรับฝึกเพิ่มเติม การแก้ครั้งนี้บันทึกเป็น commit บน main ไม่ได้สร้าง PR และยังไม่ได้ทดสอบกับบอร์ดจริง
