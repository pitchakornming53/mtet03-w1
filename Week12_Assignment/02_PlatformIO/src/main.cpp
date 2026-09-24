#include <Arduino.h>

// External LED: GPIO2 -> 220-330 ohm resistor -> LED anode; cathode -> GND.
constexpr uint8_t LED_PIN = 2;
constexpr unsigned long BLINK_INTERVAL_MS = 500;
unsigned long lastToggle = 0;
bool ledOn = false;

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);
  Serial.println("Week12: ESP32 Blink");
}

void loop() {
  const unsigned long now = millis();
  if (now - lastToggle >= BLINK_INTERVAL_MS) {
    lastToggle = now;
    ledOn = !ledOn;
    digitalWrite(LED_PIN, ledOn ? HIGH : LOW);
    Serial.println(ledOn ? "LED ON" : "LED OFF");
  }
}
