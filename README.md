# Raman Illumination Controller

Python software stack for driving a COB LED illumination subsystem in a Raman spectroscopy imaging system, developed at the [Carney Lab](https://carney.ucdavis.edu/), UC Davis.

The LED provides sample edge detection lighting between laser scan positions. It is driven by an IRF520 MOSFET circuit controlled via PWM from an Arduino Nano (CH340), with this software handling serial communication, and GUI control.

---

## Hardware

| Component | Part |
|---|---|
| LED | COB LED strip |
| Driver | IRF520 MOSFET (TO-220-3), custom KiCad PCB |
| Microcontroller | Arduino Nano (CH340, Old Bootloader) |
| Interface | USB serial, 9600 baud |

The Arduino receives a single integer (0–255) over serial and sets the PWM duty cycle accordingly.

---

## Software

```
led_controller.py        # LEDController class — serial comms, brightness, fades
led_control_gui.py       # ttkbootstrap GUI widget (Publisher/Subscriber)
publisher_subscriber.py  # Lightweight Pub/Sub event system
main.py                  # Demo / hardware test script
```

### LEDController

```python
from led_controller import LEDController

with LEDController() as led:       # auto-detects Arduino port
    led.turn_on(128)               # 50% brightness
    led.fade_in(target=255, duration=2.0)
    led.fade_out(duration=1.5)
```

Preset brightness constants: `BRIGHTNESS_LOW` (64), `BRIGHTNESS_MEDIUM` (128), `BRIGHTNESS_HIGH` (192), `BRIGHTNESS_FULL` (255).

### GUI

```python
python led_control_gui.py
```

Launches a `ttkbootstrap` darkly-themed panel with a toggle button and brightness slider. Publishes `led_on`, `led_off`, and `led_brightness_change` events for integration with the scan workflow.

---

## Scan Workflow Integration

```python
from led_controller import LEDController, on_calibration_complete, on_edge_detected, on_scan_complete

led = LEDController()
on_calibration_complete(led)   # turns on at full brightness for edge detection
on_edge_detected(led)          # turns off before laser fires
on_scan_complete(led)          # safety fallback — forces off between positions
```

---

## Requirements

```
pip install pyserial ttkbootstrap pillow
```

Python 3.10+ required (uses `str | None` union syntax).

---

## Context

Part of a larger Raman spectroscopy imaging system under development at the Carney Lab targeting non-invasive cancer detection. The full system integrates this illumination subsystem with a motorized XY stage (Rambot), a spectrometer, and an Olympus 60× objective.
