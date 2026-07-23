#if defined(ESP8266)
  #include <ESP8266WiFi.h>
#elif defined(ESP32)
  #include <WiFi.h>
#endif

// ตั้งค่า WiFi
const char* ssid     = "Ming";     // <--- ชื่อ WiFi ของคุณ
const char* password = "12345678"; // <--- รหัสผ่าน WiFi

// ตั้งค่า ThingSpeak
const char* host = "api.thingspeak.com";
const int httpPort = 80;
String writeAPIKey = "HFQWDLUEXB8W3KU3";   // <--- เปลี่ยนเป็น API Key ของคุณ

void setup() {
  Serial.begin(115200);
  delay(10);

  // เชื่อมต่อ WiFi
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected");
}

void loop() {
  // สุ่มข้อมูลจำลอง (หรืออ่านค่าจากเซนเซอร์จริงตรงนี้)
  int sensorValue = random(10, 100); 

  Serial.print("Connecting to ");
  Serial.println(host);

  // ใช้ WiFiClient เป็น TCP Client
  WiFiClient client;
  if (!client.connect(host, httpPort)) {
    Serial.println("Connection failed, retrying in 20s");
    // เว้น 20 วิเหมือน path ปกติ กัน ThingSpeak ปฏิเสธเพราะส่งถี่เกินไป
    delay(20000);
    return;
  }

  // สร้าง URL สำหรับส่งข้อมูล
  String url = "/update?api_key=" + writeAPIKey + "&field1=" + String(sensorValue);

  Serial.print("Requesting URL: ");
  Serial.println(url);

  // ส่ง HTTP Request ผ่าน TCP Connection
  client.print(String("GET ") + url + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" + 
               "Connection: close\r\n\r\n");
               
  unsigned long timeout = millis();
  while (client.available() == 0) {
    if (millis() - timeout > 8000) {
      Serial.println(">>> Client Timeout !");
      client.stop();
      // request อาจไปถึง ThingSpeak แล้วแม้ฝั่งเราจะ timeout รอ response
      // เว้น 20 วิก่อน retry กันโดนปฏิเสธเพราะส่งถี่กว่า 15 วิ/ครั้ง
      delay(20000);
      return;
    }
  }

  // อ่าน response ทั้งหมด บรรทัดสุดท้ายคือ body ซึ่งเป็น ThingSpeak entry ID
  // (ถ้าได้ "0" แปลว่า ThingSpeak ปฏิเสธ เช่น ส่งถี่กว่า 15 วินาที หรือ API key ผิด)
  String line;
  String lastLine;
  while (client.connected() || client.available()) {
    if (client.available()) {
      line = client.readStringUntil('\n');
      line.trim();
      if (line.length() > 0) lastLine = line;
    }
  }
  Serial.print("ThingSpeak entry ID: ");
  Serial.println(lastLine);

  Serial.println("Closing connection");
  
  // ThingSpeak บัญชีฟรี ต้องเว้นระยะห่างอย่างน้อย 15 วินาทีต่อการส่ง 1 ครั้ง
  delay(20000); 
}