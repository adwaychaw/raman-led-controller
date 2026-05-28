from led_controller import LEDController
import time

with LEDController() as led:

    print("--- Brightness steps ---")
    led.turn_on(64)
    time.sleep(1)
    led.turn_on(128)
    time.sleep(1)
    led.turn_on(192)
    time.sleep(1)
    led.turn_on(255)
    time.sleep(1)

    print("--- Fade out ---")
    led.fade_out(duration=2.0)
    time.sleep(1)

    print("--- Fade in ---")
    led.fade_in(target=255, duration=2.0)
    time.sleep(1)

    print("--- Preset levels ---")
    led.turn_on(LEDController.BRIGHTNESS_LOW)
    time.sleep(1)
    led.turn_on(LEDController.BRIGHTNESS_MEDIUM)
    time.sleep(1)
    led.turn_on(LEDController.BRIGHTNESS_HIGH)
    time.sleep(1)
    led.turn_on(LEDController.BRIGHTNESS_FULL)
    time.sleep(1)

    led.turn_off()
    print("Done")