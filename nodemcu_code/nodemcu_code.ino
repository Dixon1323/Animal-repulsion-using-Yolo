

#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

#define BLYNK_TEMPLATE_ID "TMPL3KcdhUdWq"
#define BLYNK_TEMPLATE_NAME "Animal"
#define BLYNK_AUTH_TOKEN "Lzcua_B_NLgI5pY16-3MW2xTLBMPFMR1"
#define BLYNK_PRINT Serial

char auth[] = BLYNK_AUTH_TOKEN;
char ssid[] = "iQOO";
char pass[] = "iqoo123456";

int data = 0;

BLYNK_WRITE(V0) {
  data = param.asInt();
}

void setup() {
  pinMode(D0, OUTPUT);
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, OUTPUT);
  pinMode(D4, OUTPUT);
  Blynk.begin(auth, ssid, pass, "blynk.cloud", 80);
  digitalWrite(D0, HIGH);
  digitalWrite(D1, HIGH);
  digitalWrite(D2, HIGH);
  digitalWrite(D3, HIGH);
  digitalWrite(D4, HIGH);
}

void loop() {
  Blynk.run();
  switch (data){
    case 0:
      digitalWrite(D0,LOW);
      digitalWrite(D1, HIGH);
      digitalWrite(D2, HIGH);
      digitalWrite(D3, HIGH);
      digitalWrite(D4, HIGH);
      break;
    case 1:
      digitalWrite(D0,HIGH);
      digitalWrite(D1, LOW);
      digitalWrite(D2, HIGH);
      digitalWrite(D3, HIGH);
      digitalWrite(D4, HIGH);
      break;
    case 2:
      digitalWrite(D0,HIGH);
      digitalWrite(D1, HIGH);
      digitalWrite(D2, LOW);
      digitalWrite(D3, HIGH);
      digitalWrite(D4, HIGH);
      break;
    case 3:
      digitalWrite(D0,HIGH);
      digitalWrite(D1, HIGH);
      digitalWrite(D2, HIGH);
      digitalWrite(D3, LOW);
      digitalWrite(D4, HIGH);
      break;
    case 4:
      digitalWrite(D0,HIGH);
      digitalWrite(D1, HIGH);
      digitalWrite(D2, HIGH);
      digitalWrite(D3, HIGH);
      digitalWrite(D4, LOW);
      break;
    default:
      digitalWrite(D0,HIGH);
      digitalWrite(D1, HIGH);
      digitalWrite(D2, HIGH);
      digitalWrite(D3, HIGH);
      digitalWrite(D4, HIGH);
}
}