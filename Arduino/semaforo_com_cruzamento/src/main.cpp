#include <Arduino.h> // Inclui a biblioteca padrão do Arduino

/* Simular um cruzamento com dois semáforos usando máquina de estados */

enum States {    // Define um tipo de enumeração (enum) com dois estados
  state1,        // estado 1
  state2,        // estado 2
};

int states = state1; // A variável 'states' é inicializada com o estado 'state1'

void setup() {
  /* Semáforo 1 */
  pinMode(13, OUTPUT); // Define o pino 13 como saída (Vermelho Semáforo 1)
  pinMode(12, OUTPUT); // Define o pino 12 como saída (Amarelo Semáforo 1)
  pinMode(11, OUTPUT); // Define o pino 11 como saída (Verde Semáforo 1)

  pinMode(10, OUTPUT); // Define o pino 10 como saída (Vermelho Semáforo 2)
  pinMode(9, OUTPUT);  // Define o pino 9 como saída (Amarelo Semáforo 2)
  pinMode(8, OUTPUT);  // Define o pino 8 como saída (Verde Semáforo 2)
}

void loop() {
  switch (states) {  // Verifica o valor da variável 'states' e executa o código dentro do case correspondente
    case state1:  // Se o estado for 'state1'
      digitalWrite(8, HIGH);   // Acende o LED verde no Semáforo 2 (pino 8)
      digitalWrite(13, HIGH);  // Acende o LED vermelho no Semáforo 1 (pino 13)
      delay(2000);             // Espera por 2 segundos (tempo de verde no Semáforo 2)

      digitalWrite(8, LOW);    // Desliga o LED verde do Semáforo 2 (pino 8)
      digitalWrite(9, HIGH);   // Acende o LED amarelo no Semáforo 2 (pino 9)
      delay(2000);             // Espera por 2 segundos (tempo de amarelo no Semáforo 2)

      digitalWrite(9, LOW);    // Desliga o LED amarelo do Semáforo 2 (pino 9)
      digitalWrite(10, HIGH);  // Acende o LED vermelho no Semáforo 2 (pino 10)
      states = state2;         // Muda para o estado 'state2'
      break;

    case state2:  // Se o estado for 'state2'
      delay(2000);             // Espera por 2 segundos (tempo de vermelho no Semáforo 1)

      digitalWrite(13, LOW);   // Desliga o LED vermelho do Semáforo 1 (pino 13)
      digitalWrite(11, HIGH);  // Acende o LED verde no Semáforo 1 (pino 11)
      delay(2000);             // Espera por 2 segundos (tempo de verde no Semáforo 1)

      digitalWrite(11, LOW);   // Desliga o LED verde do Semáforo 1 (pino 11)
      digitalWrite(12, HIGH);  // Acende o LED amarelo no Semáforo 1 (pino 12)
      delay(2000);             // Espera por 2 segundos (tempo de amarelo no Semáforo 1)

      digitalWrite(12, LOW);   // Desliga o LED amarelo do Semáforo 1 (pino 12)
      digitalWrite(13, HIGH);  // Acende o LED vermelho no Semáforo 1 (pino 13)
      delay(2000);             // Espera por 2 segundos (tempo de vermelho no Semáforo 1)

      digitalWrite(10, LOW);   // Desliga o LED vermelho do Semáforo 2 (pino 10)
      states = state1;         // Muda para o estado 'state1'
      break;
  }
}
