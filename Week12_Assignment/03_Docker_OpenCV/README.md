# Docker + Python + OpenCV: ตรวจนับวัตถุในภาพ

โปรแกรมสร้างภาพสังเคราะห์ 3 วัตถุเมื่อไม่ระบุ input หรืออ่านภาพจากไฟล์ที่กำหนด
ขั้นตอน: BGR → Grayscale → Gaussian Blur → Canny สำหรับแสดงขอบ
และ Otsu Threshold → External Contours → กรองพื้นที่ ≥ 500 px² → วาดกรอบและนับวัตถุ
การนับใช้ mask ไม่ได้นับเส้นขอบ Canny เพื่อลดปัญหาขอบซ้ำ
ตัวอย่างเหมาะกับวัตถุสว่างแยกกันบนพื้นหลังมืด วัตถุแตะกันอาจถูกนับรวม
ไม่ใช่โมเดล AI สำหรับจำแนกชนิดวัตถุ

## รันด้วย Docker (PowerShell)

ติดตั้งและเปิด Docker Desktop ให้พร้อมใช้งาน Linux containers
เปิด Terminal ในโฟลเดอร์ `03_Docker_OpenCV`:

```powershell
docker build -t week12-opencv .
New-Item -ItemType Directory -Force results | Out-Null
docker run --rm --mount "type=bind,source=$($PWD.Path)/results,target=/app/results" week12-opencv
```

ผลอยู่ใน `results`: original.png, gray.png, edges.png, mask.png, annotated.png และ report.json
ตัวอย่างสังเคราะห์ควรได้ object_count เท่ากับ 3
Bind mount ทำให้ผลลัพธ์ยังอยู่หลัง container ถูกลบด้วย --rm
ใช้ opencv-python-headless เพราะ container นี้ไม่ต้องเปิดหน้าต่าง cv2.imshow()

## ใช้ภาพของตนเอง

สร้างโฟลเดอร์ input แล้วใส่ sample.jpg ก่อนรัน:

```powershell
docker run --rm --mount "type=bind,source=$($PWD.Path)/input,target=/data,readonly" --mount "type=bind,source=$($PWD.Path)/results,target=/app/results" week12-opencv --input /data/sample.jpg --output /app/results
```

## รัน Python โดยตรงเพื่อเปรียบเทียบ

```sh
python -m pip install -r requirements.txt
python app.py --output results
```

เก็บภาพ docker build สำเร็จ, console แสดง object_count และ annotated.png
ผล Python ที่แนบเป็นการรันจริงบนเครื่องนี้ ไม่ใช่หลักฐานการรัน Docker
อ้างอิง: https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html
