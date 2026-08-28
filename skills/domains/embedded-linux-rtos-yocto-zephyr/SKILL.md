---
name: embedded-linux-rtos-yocto-zephyr
description: Especialista em Sistemas Operacionais Embarcados, Linux Embarcado (Yocto Project) e RTOS (Zephyr RTOS) baseado nas obras Yocto Project Customization (Rodolfo Giometti) e Zephyr RTOS Embedded C Programming (Andrew Eliasz). Cobre criação de Recipes/Layers no BitBake, Device Trees, U-Boot, POSIX API em microcontroladores (ARM Cortex-M/R, RISC-V), threads determinísticas em tempo real, semáforos, mutexes e drivers de dispositivos.
---

# Sistemas Operacionais Embarcados: Linux (Yocto) e Zephyr RTOS

Esta skill estabelece diretrizes para engenharia de software de sistemas de missão crítica, cobrindo desenvolvimento de distribuições Linux customizadas com **Yocto Project** e programação determinística em tempo real com **Zephyr RTOS**.

---

## 🐧 1. Yocto Project e BitBake Architecture

```
┌─────────────────────────────────────────────────────────────┐
│ Camadas de Configuração (meta-yocto, meta-oe, meta-custom)  │
└──────────────────────────────┬──────────────────────────────┘
                               │ BitBake Build Engine
┌──────────────────────────────▼──────────────────────────────┐
│ Recipes (.bb / .bbappend) -> Fetch -> Patch -> Compile      │
└──────────────────────────────┬──────────────────────────────┘
                               │
┌──────────────────────────────▼──────────────────────────────┐
│ Imagens Finais (U-Boot, Linux Kernel zImage, Rootfs, DTB)   │
└─────────────────────────────────────────────────────────────┘
```

---

## ⏱️ 2. Programação Concorrente com Zephyr RTOS (C POSIX)

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
        printk("Processando telemetria em tempo real no Zephyr RTOS\n");
        k_msleep(100);
    }
}

int main(void) {
    k_thread_create(&sensor_thread_data, sensor_stack,
                    K_THREAD_STACK_SIZEOF(sensor_stack),
                    sensor_worker, NULL, NULL, NULL,
                    PRIORITY, 0, K_NO_WAIT);
    
    // Dispara semáforo periodicamente
    while (1) {
        k_msleep(1000);
        k_sem_give(&data_ready_sem);
    }
    return 0;
}
```
