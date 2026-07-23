#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "Ming"; // <--- ชื่อ WiFi ของคุณ
const char* password = "12345678"; // <--- รหัสผ่าน WiFi
const char* mqtt_server = "broker.hivemq.com";
const int mqtt_port = 1883;

WiFiClient espClient;
PubSubClient client(espClient);

void connectWiFi() {
  Serial.println("Connecting to WiFi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

void reconnectMQTT() {
  while (!client.connected()) {
    Serial.println("Attempting MQTT connection...");
    String clientId = "esp32-client-" + String(random(0xffff), HEX);

    if (client.connect(clientId.c_str())) {
      Serial.println("MQTT connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  randomSeed(analogRead(0));

  connectWiFi();
  client.setServer(mqtt_server, mqtt_port);
}

void loop() {
  if (WiFi.status() != WL_CONNECTED) {
    connectWiFi();
  }

  if (!client.connected()) {
    reconnectMQTT();
  }

  client.loop();

  float temperature = 25.0 + random(0, 100) / 10.0;
  float humidity = 45.0 + random(0, 200) / 10.0;
  int counter = millis() / 1000;

  char tempBuf[10];
  char humBuf[10];
  char counterBuf[12];

  dtostrf(temperature, 4, 1, tempBuf);
  dtostrf(humidity, 4, 1, humBuf);
  itoa(counter, counterBuf, 10);

  client.publish("iot/week4/random1", tempBuf);
  client.publish("iot/week4/random2", humBuf);
  client.publish("iot/week4/random3", counterBuf);

  Serial.print("Published -> temp:");
  Serial.print(tempBuf);
  Serial.print(" humidity:");
  Serial.print(humBuf);
  Serial.print(" counter:");
  Serial.println(counterBuf);

  delay(3000);
}