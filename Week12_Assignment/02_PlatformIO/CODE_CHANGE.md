# ตัวอย่างการแก้ Code

ไฟล์: src/main.cpp

```diff
-constexpr unsigned long BLINK_INTERVAL_MS = 1000;
+constexpr unsigned long BLINK_INTERVAL_MS = 500;
```

เปลี่ยนช่วงเวลาสลับสถานะ LED จาก 1000 ms เป็น 500 ms ทำให้ความถี่การกระพริบเพิ่มจาก 0.5 Hz เป็น 1 Hz เพราะหนึ่งรอบมีช่วงติดและดับ

ตรวจ diff จริงโดยเปิด [ประวัติไฟล์บน GitHub](https://github.com/pitchakornming53/mtet03-w1/commits/main/Week12_Assignment/02_PlatformIO/src/main.cpp) แล้วเลือก commit Change ESP32 LED toggle interval from 1000 to 500 ms

วิธีทดสอบ: เปิดโฟลเดอร์ 02_PlatformIO ใน VS Code → Build → Upload → Serial Monitor 115200 ควรแสดง LED ON/OFF สลับทุก 0.5 วินาที

สถานะ: แก้และบันทึกโค้ดจริงบน GitHub แล้ว ยังไม่ได้ build/upload ไปยังบอร์ดจริง
