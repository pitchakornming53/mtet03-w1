# n8n เรียก AI วิเคราะห์ข้อมูลและส่ง Telegram

Flow: Manual Trigger → Sample Data → AI Analysis (DeepSeek) → Format Message → Send Telegram
ข้อมูลจำลอง: Motor-A01 อุณหภูมิ 78°C (เกณฑ์ 70°C) และความสั่น 6.2 mm/s (เกณฑ์ 4.5 mm/s)
เกณฑ์นี้ตั้งขึ้นเพื่อสาธิต ไม่ใช่มาตรฐานความปลอดภัยของเครื่องจักร

## ติดตั้งและนำเข้า

1. เปิด Docker Desktop จากโฟลเดอร์นี้รัน `docker compose up -d`
2. เปิด http://localhost:5678 และสร้างบัญชีเจ้าของระบบในเครื่อง
3. สร้าง workflow แล้วเลือก Import from File เลือก workflow.json
4. สร้างบัญชี DeepSeek API ที่ https://platform.deepseek.com/ และเตรียม API key ที่ใช้งานได้ มี quota/เครดิตตามบริการ
5. ใน AI Analysis สร้าง Header Auth credential: Name = Authorization, Value = Bearer ตามด้วยช่องว่างและ API key จริง แล้วเลือก credential นี้
6. ใช้ Telegram คุยกับ @BotFather สั่ง /newbot รับ token แล้วเปิดแชตกับ bot ของตนเอง กด Start
7. สร้าง Telegram credential ใน Send Telegram แล้วใส่ bot token
8. หา chat ID ด้วย Telegram Trigger ชั่วคราวใน n8n ที่มี HTTPS webhook หรือเรียก getUpdates จาก Telegram Bot API ภายในเครื่องหลังส่งข้อความหา bot และอ่าน message.chat.id หากไม่ได้ตั้ง webhook ไว้
9. แทน REPLACE_WITH_YOUR_CHAT_ID ด้วย ID แชตของตนเอง ตรวจปลายทางให้ถูกต้อง
10. กด Execute workflow เพื่อเรียก AI และส่งข้อความจริงถึงแชตที่ตั้งไว้ การเรียก AI อาจมีค่าใช้จ่ายตามบัญชี

เก็บ key/token ใน Credentials ของ n8n เท่านั้น ไม่ใส่ใน workflow JSON หรือ GitHub
workflow ใช้การกดรันเอง จึงไม่ต้องใช้ ngrok หรือรับ webhook เพื่อส่งข้อความ
หากใช้ Telegram Trigger รับข้อความเข้า ระบบภายนอกต้องเข้าถึง HTTPS webhook ได้ เช่นผ่าน ngrok ที่ตั้งค่า WEBHOOK_URL ถูกต้อง

## ตรวจผล

- Sample Data ต้องแสดงข้อมูล 78, 6.2 และเกณฑ์ทั้งสอง
- AI Analysis ต้องมี choices[0].message.content เป็นข้อความ
- คำตอบควรระบุว่าอุณหภูมิเกิน 8°C และความสั่นเกิน 1.7 mm/s (คำตอบจริงอาจใช้ถ้อยคำต่างกัน)
- Send Telegram สำเร็จและมีข้อความในแชตจริง จึงถือว่าทดสอบครบวงจร
- API 401: ตรวจ credential; 429: ตรวจ quota/rate limit; chat not found: ตรวจ ID และกด Start ที่ bot
- หากชื่อ model ใช้ไม่ได้ ให้เลือกชื่อโมเดลที่บัญชี DeepSeek รองรับปัจจุบันแล้วแก้ model ใน AI Analysis

ยังไม่ได้เชื่อม credential หรือทดสอบส่งจริง ไฟล์นี้เป็น workflow ที่เตรียมไว้ให้นำเข้าและตั้งค่า
ห้ามนำข้อความตัวอย่างไปอ้างว่าเป็นผลทดสอบจริง เก็บภาพ workflow, execution และข้อความ Telegram หลังรันด้วยบัญชีตนเอง

อ้างอิง:
- https://docs.n8n.io/hosting/installation/docker/
- https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/
- https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations/
- https://api-docs.deepseek.com/
- https://core.telegram.org/bots/api#getupdates
