#include <Arduino.h>
// O objetivo deste codigo é simular um semaforo

void setup() {
  pinMode(10, OUTPUT); // Configura o pino digital 10 como saida
  pinMode(9, OUTPUT); // Configura o pino digital 9 como saida
  pinMode(8, OUTPUT); // Configura o pino digital 8 como saida
}

// A função loop() é executa a instrução repetidamente
void loop() {
  digitalWrite(10, HIGH); // Liga o Led conectado ao pino 10
  delay(2000); // Aguarda 2s antes de executar a proxima instrução
  digitalWrite(10, LOW); // Após 2s desliga o Led conectado ao pino 10

  digitalWrite(9, HIGH);// Liga o Led conectado ao pino 10
  delay(2000);// Aguarda 2s antes de executar a proxima instrução
  digitalWrite(9, LOW);  // Após 2s desliga o Led conectado ao pino 10
  
  digitalWrite(8, HIGH); // Liga o Led conectado ao pino 10
  delay(2000);// Aguarda 2s antes de executar a proxima instrução
  digitalWrite(8, LOW);  // Após 2s desliga o Led conectado ao pino 10
}
