#include <Arduino.h>

#define GREEN_PIN 9  // Define o Verde no pino 9
#define RED_PIN 10   // Define o Vermelho no pino 10
#define BLUE_PIN 11  // Define o Azul no pino 11

void setup() {
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(RED_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);
}

void loop() {
  // Acende o Verde
  analogWrite(GREEN_PIN, 255);
  analogWrite(RED_PIN, 0);
  analogWrite(BLUE_PIN, 0);
  delay(2000);  // Espera 1 segundo

  // Acende o Vermelho
  analogWrite(GREEN_PIN, 0);
  analogWrite(RED_PIN, 255);
  analogWrite(BLUE_PIN, 0);
  delay(2000);

  // Acende o Azul
  analogWrite(GREEN_PIN, 0);
  analogWrite(RED_PIN, 0);
  analogWrite(BLUE_PIN, 255);
  delay(2000);

  // Acende o Azul
  analogWrite(GREEN_PIN, 0);
  analogWrite(RED_PIN, 255);
  analogWrite(BLUE_PIN, 255);
  delay(2000);
}
