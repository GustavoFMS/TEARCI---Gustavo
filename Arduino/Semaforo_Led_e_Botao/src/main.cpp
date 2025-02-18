#include <Arduino.h>  // Inclui a biblioteca do Arduino para uso das funções básicas

// Definição dos pinos onde os LEDs RGB estão conectados e o Botão
#define GREEN_PIN 9   // Canal verde no pino 9
#define RED_PIN   10  // Canal vermelho no pino 10
#define BLUE_PIN  11  // Canal azul no pino 11
#define BUTTON_PIN 12 // Botão no pino 12

// Função para acender a cor verde no LED RGB
void setGreen() {
  analogWrite(RED_PIN, 0);   
  analogWrite(GREEN_PIN, 255); 
  analogWrite(BLUE_PIN, 0);   
}

// Função para acender a cor amarela no LED RGB
void setYellow() {
  // O amarelo é formado pela combinação de vermelho e verde
  analogWrite(RED_PIN, 255); 
  analogWrite(GREEN_PIN, 75); 
  analogWrite(BLUE_PIN, 0);   
}

// Função para acender a cor vermelha no LED RGB
void setRed() {
  analogWrite(RED_PIN, 255); 
  analogWrite(GREEN_PIN, 0); 
  analogWrite(BLUE_PIN, 0); 
}

void setup() {
  Serial.begin(9600); // Inicializa a comunicação serial com o monitor serial

  // Define os pinos dos LEDs RGB como saída
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(RED_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);

  // Configura o pino do botão como entrada com resistor pull-up interno
  // Isso significa que, quando não pressionado, o pino estará em HIGH (5V)
  // e quando pressionado, ficará em LOW (0V)
  pinMode(BUTTON_PIN, INPUT_PULLUP);
}

void loop() {
  // Se o botão não estiver pressionado (estado HIGH), o LED fica verde
  if (digitalRead(BUTTON_PIN) == HIGH) {
    setGreen();  // Ativa a cor verde
    delay(500);  // Aguarda 500ms
  }

 // Se o botão for pressionado (estado LOW), altera a cor do LED RGB
  if (digitalRead(BUTTON_PIN) == LOW) {
    setYellow();  // Ativa a cor amarela
    delay(7000);  // Aguarda 7 segundos

    setRed();     // Ativa a cor vermelha
    delay(10000); // Aguarda 10 segundos
  }
}