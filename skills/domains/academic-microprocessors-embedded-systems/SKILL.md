---
name: academic-microprocessors-embedded-systems
description: "Especialista em Arquitetura de Microprocessadores, Sistemas Embarcados, RTOS e Linux Embarcado baseado em Patterson & Hennessy (Computer Organization and Design), Rodolfo Giometti (Yocto Project) e Andrew Eliasz (Zephyr RTOS). Cobre microcontroladores ARM Cortex-M/A/R, RISC-V (RV32I/RV64G), Assembly, pipelines de 5 estágios com Data Forwarding e Previsão de Desvio, hierarquia de caches L1/L2/L3, barramentos (UART, SPI, I2C, CAN, USB), DMA, FreeRTOS, Zephyr RTOS, Yocto Project (BitBake, recipes .bb, meta-layers), Device Trees e bootloaders U-Boot."
---

# Arquitetura de Microprocessadores, RTOS e Linux Embarcado (Yocto & Zephyr)

Esta skill estabelece os princípios de arquitetura de computadores, projeto de microprocessadores (ARM e RISC-V), controle de periféricos por hardware, programação determinística em tempo real com **FreeRTOS / Zephyr RTOS** e compilação de sistemas operacionais customizados com **Yocto Project**.

---

## 💻 1. Pipeline Clássico de 5 Estágios (IF, ID, EX, MEM, WB)

```
[ IF: Busca de Instrução ] ──> [ ID: Decodificação & Registradores ]
                            ──> [ EX: Execução na ULA / Cálculo de Branch ]
                            ──> [ MEM: Acesso à Memória de Dados ]
                            ──> [ WB: Escrita de Retorno no Registrador ]
```

### 1.1 Resolução de Hazards
- **Hazard Estrutural**: Caches separadas de Instrução e Dados (Arquitetura Harvard / L1 Split).
- **Hazard de Dados**: Encaminhamento direto (*Data Forwarding / Bypassing*) da saída da ULA/MEM diretamente para as entradas da ULA do ciclo seguinte sem bolhas de stall.
- **Hazard de Controle**: Preditor de desvios (*Branch Predictor*) dinâmico de 2 bits (bimodal / gshare) e slots de atraso (*branch delay slot*).

---

## 🔌 2. Barramentos e Periféricos de Hardware

| Barramento | Topologia | Fios / Sinais | Taxa Típica | Aplicações |
| :--- | :--- | :--- | :--- | :--- |
| **UART** | Ponto-a-ponto, assíncrono, Full-Duplex | TX, RX, GND | 9.6 kbps – 921.6 kbps | Logs de debug, módulos GPS/Bluetooth |
| **SPI** | Mestre-Escravo, síncrono, Full-Duplex | MOSI, MISO, SCK, CS | 10 MHz – 80 MHz | Displays OLED, memória Flash NOR, cartões SD |
| **I2C** | Barramento multimestre, síncrono, Half-Duplex | SDA, SCL (Pull-up) | 100 kHz, 400 kHz, 3.4 MHz | Sensores MEMS (IMU, temperatura), RTC, EEPROM |
| **CAN / CAN-FD** | Barramento diferencial imune a ruído | CAN_H, CAN_L (120 $\Omega$) | 1 Mbps (CAN) / 5-8 Mbps (FD) | Indústria automotiva, aeroespacial, automação |

---

## ⏱️ 3. Programação em Tempo Real: Zephyr RTOS & FreeRTOS

```c
#include <zephyr/kernel.h>
#include <zephyr/sys/printk.h>

#define STACK_SIZE 1024
#define PRIORITY 7

K_THREAD_STACK_DEFINE(sensor_stack, STACK_SIZE);
struct k_thread sensor_thread_data;
K_SEM_DEFINE(data_ready_sem, 0, 1);

void sensor_worker(void *p1, void *p2, void *p3) {
    while (1) {
        k_sem_take(&data_ready_sem, K_FOREVER);
        printk("Processando telemetria determinística no Zephyr RTOS\n");
        k_msleep(100);
    }
}

int main(void) {
    k_thread_create(&sensor_thread_data, sensor_stack,
                    K_THREAD_STACK_SIZEOF(sensor_stack),
                    sensor_worker, NULL, NULL, NULL,
                    PRIORITY, 0, K_NO_WAIT);
    
    while (1) {
        k_msleep(1000);
        k_sem_give(&data_ready_sem);
    }
    return 0;
}
```

---

## 🐧 4. Linux Embarcado: Yocto Project, BitBake e Device Trees

### 4.1 Estrutura de Camadas (Layers) e Recipes BitBake
```
meta-custom-bsp/
├── conf/layer.conf
├── recipes-bsp/
│   ├── u-boot/u-boot-custom_%.bbappend
│   └── device-tree/custom-board.dts
└── recipes-kernel/
    └── linux/linux-yocto-custom_6.6.bb
```

### 4.2 Exemplo de Device Tree Source (`.dts`) para Mapeamento de Periférico I2C
```dts
&i2c1 {
    status = "okay";
    clock-frequency = <400000>;

    sensor_imu: mpu6050@68 {
        compatible = "invensense,mpu6050";
        reg = <0x68>;
        interrupt-parent = <&gpio1>;
        interrupts = <15 IRQ_TYPE_EDGE_RISING>;
    };
};
```
