// Starter example for a board with a built-in LED.
const unsigned long BLINK_INTERVAL_MS = 1000;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(BLINK_INTERVAL_MS);
  digitalWrite(LED_BUILTIN, LOW);
  delay(BLINK_INTERVAL_MS);
}
