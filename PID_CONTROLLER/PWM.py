# from machine import Pin, PWM
import time

# Pin Definitions
pwm_pin = 18  # GPIO18 can be used for PWM

# Initialize PWM on pwm_pin
pwm = PWM(Pin(pwm_pin), freq=1000)  # Set frequency to 1000Hz

try:
    while True:
        for duty_cycle in range(0, 1024, 102):  # Increase duty cycle from 0 to 1023 in steps of 102
            pwm.duty(duty_cycle)
            print(f"Duty Cycle: {duty_cycle / 1023 * 100:.2f}%")
            time.sleep(1)  # Wait for 1 second
        for duty_cycle in range(1023, -1, -102):  # Decrease duty cycle from 1023 to 0 in steps of 102
            pwm.duty(duty_cycle)
            print(f"Duty Cycle: {duty_cycle / 1023 * 100:.2f}%")
            time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    pass

# Cleanup
pwm.deinit()  # Deinitialize PWM
