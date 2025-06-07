#include <Arduino.h>

// Definição de pinos
#define LED_VERMELHO 2
#define LED_VERDE 4
#define LED_AMARELO 5
#define SENSOR_FLUXO 34
#define SENSOR_VAZAMENTO 35
#define VALVULA 18

// Capacidade de cada filtro (em litros)
#define CAPACIDADE_FILTRO1 1500
#define CAPACIDADE_FILTRO2 1500
#define CAPACIDADE_FILTRO3 3000
#define CAPACIDADE_FILTRO4 3000

// Alertas de 100L antes da capacidade total
#define FALTA_100L_FILTRO1 (CAPACIDADE_FILTRO1 - 100)
#define FALTA_100L_FILTRO2 (CAPACIDADE_FILTRO2 - 100)
#define FALTA_100L_FILTRO3 (CAPACIDADE_FILTRO3 - 100)
#define FALTA_100L_FILTRO4 (CAPACIDADE_FILTRO4 - 100)

// Contadores para cada filtro
float litrosFiltrados1 = 0.0;
float litrosFiltrados2 = 0.0;
float litrosFiltrados3 = 0.0;
float litrosFiltrados4 = 0.0;

volatile int contagemPulsos = 0;
const float FATOR_CONVERSAO = 1.0 / 450.0;  // 1 litro = 450 pulsos (ajuste conforme o sensor)

// Estados da máquina de estados
enum Estado {
    E1_TESTAR_SENSORES,
    E2_AGUARDANDO,
    E3_TORNEIRA_ABERTA,
    E4_MONITORAMENTO_VAZAMENTOS,
    E5_CAPACIDADE_MAXIMA,
    E6_FALTA_100L
};

Estado estadoAtual = E1_TESTAR_SENSORES;

// Interrupção para contar pulsos do sensor de fluxo
void contarPulso() {
    contagemPulsos++;
}

void setup() {
    pinMode(LED_VERMELHO, OUTPUT);
    pinMode(LED_VERDE, OUTPUT);
    pinMode(LED_AMARELO, OUTPUT);
    pinMode(SENSOR_FLUXO, INPUT);
    pinMode(SENSOR_VAZAMENTO, INPUT);
    pinMode(VALVULA, OUTPUT);
    
    Serial.begin(115200);
    
    // Configurar interrupção no sensor de fluxo
    attachInterrupt(digitalPinToInterrupt(SENSOR_FLUXO), contarPulso, RISING);
}

void loop() {
    // Atualiza a quantidade de litros filtrados
    float litrosFiltrados = (contagemPulsos * FATOR_CONVERSAO);
    contagemPulsos = 0;  // Zera a contagem para a próxima medição

    // Distribuir a água filtrada entre os 4 filtros (exemplo: uso uniforme)
    litrosFiltrados1 += litrosFiltrados * (CAPACIDADE_FILTRO1 / 9000.0);
    litrosFiltrados2 += litrosFiltrados * (CAPACIDADE_FILTRO2 / 9000.0);
    litrosFiltrados3 += litrosFiltrados * (CAPACIDADE_FILTRO3 / 9000.0);
    litrosFiltrados4 += litrosFiltrados * (CAPACIDADE_FILTRO4 / 9000.0);

    switch (estadoAtual) {
        case E1_TESTAR_SENSORES:
            Serial.println("Testando Sensores...");
            if (digitalRead(SENSOR_FLUXO) == LOW && digitalRead(SENSOR_VAZAMENTO) == LOW) {
                digitalWrite(LED_VERDE, HIGH);
                estadoAtual = E2_AGUARDANDO;
            } else {
                digitalWrite(LED_VERMELHO, HIGH);
                Serial.println("Erro nos sensores! Notificação enviada.");
            }
            break;

        case E2_AGUARDANDO:
            Serial.println("Aguardando (Torneira Fechada)...");
            if (digitalRead(SENSOR_FLUXO) > 0) {
                estadoAtual = E3_TORNEIRA_ABERTA;
            }
            break;

        case E3_TORNEIRA_ABERTA:
            Serial.println("Torneira Aberta. Filtrando Água...");
            if (digitalRead(SENSOR_VAZAMENTO) == HIGH) {
                estadoAtual = E4_MONITORAMENTO_VAZAMENTOS;
            } else if (litrosFiltrados1 >= CAPACIDADE_FILTRO1 || 
                       litrosFiltrados2 >= CAPACIDADE_FILTRO2 ||
                       litrosFiltrados3 >= CAPACIDADE_FILTRO3 ||
                       litrosFiltrados4 >= CAPACIDADE_FILTRO4) {
                estadoAtual = E5_CAPACIDADE_MAXIMA;
            } else if (litrosFiltrados1 >= FALTA_100L_FILTRO1 || 
                       litrosFiltrados2 >= FALTA_100L_FILTRO2 ||
                       litrosFiltrados3 >= FALTA_100L_FILTRO3 ||
                       litrosFiltrados4 >= FALTA_100L_FILTRO4) {
                estadoAtual = E6_FALTA_100L;
            }
            break;

        case E4_MONITORAMENTO_VAZAMENTOS:
            Serial.println("Monitorando Vazamentos...");
            digitalWrite(LED_VERMELHO, HIGH);
            Serial.println("Vazamento detectado! Notificação enviada.");
            estadoAtual = E2_AGUARDANDO;
            break;

        case E5_CAPACIDADE_MAXIMA:
            Serial.println("Capacidade Máxima de um dos filtros atingida!");
            digitalWrite(LED_VERMELHO, HIGH);
            Serial.println("Notificação enviada.");
            estadoAtual = E2_AGUARDANDO;
            break;

        case E6_FALTA_100L:
            Serial.println("Faltam 100L para a capacidade máxima de um dos filtros...");
            digitalWrite(LED_AMARELO, HIGH);
            Serial.println("Notificação enviada.");
            estadoAtual = E3_TORNEIRA_ABERTA;
            break;
    }
    delay(1000);
}
