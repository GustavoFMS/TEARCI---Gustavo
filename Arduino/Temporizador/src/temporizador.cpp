#include "Arduino.h"

unsigned long previous_time = millis();
unsigned long interval = 5000;


void setup () {
  Serial.begin(9600);
}

void loop () {
  // Objetivo: Implementar um temporizador 
  // Testar condição de tempo do intervalo

  Serial.println(millis());
  Serial.println(previous_time);
  Serial.println("");

  if (millis() - previous_time > interval){
    
    previous_time = millis();
  }
  
}