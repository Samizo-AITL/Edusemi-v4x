// sw_riscv/llm_interface.c

#include <stdint.h>
#include "mmio.h"  // ベースアドレス定義（別ヘッダ）

#define LLM_BASE_ADDR     0x40000000
#define REG_ACTION        (*(volatile uint32_t*)(LLM_BASE_ADDR + 0x00))  // FSM override
#define REG_REF_OVERRIDE  (*(volatile uint32_t*)(LLM_BASE_ADDR + 0x04))  // PID override
#define REG_MODE_SELECT   (*(volatile uint32_t*)(LLM_BASE_ADDR + 0x08))  // FSM/PIDモード切替
#define REG_STATUS_READ   (*(volatile uint32_t*)(LLM_BASE_ADDR + 0x0C))  // 状態取得

void send_action(uint32_t action_code) {
    REG_ACTION = action_code;
}

void override_ref(int16_t value) {
    REG_REF_OVERRIDE = (uint32_t)value;
}

void set_control_mode(uint32_t mode) {
    REG_MODE_SELECT = mode;
}

uint32_t read_status(void) {
    return REG_STATUS_READ;
}

int main(void) {
    // 例：LLMが「歩け」という判断を下したとき
    send_action(0x1);         // FSMをWALKへ
    override_ref(1000);       // PID目標値を強制設定
    set_control_mode(0x1);    // overrideモード

    // 状態取得（デバッグ用）
    uint32_t status = read_status();

    // 永続ループ（実用ならイベント駆動へ）
    while (1) {
        // LLMイベント待ち、またはセンサポーリングなど
    }

    return 0;
}
