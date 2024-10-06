import RPi.GPIO as GPIO
import time

# List of GPIO pins to test (this list includes all GPIO pins available for output on Raspberry Pi 4)
output_pins = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

# Setup GPIO mode to BCM (Broadcom pin numbering)
GPIO.setmode(GPIO.BCM)

# Setup all pins as output
for pin in output_pins:
    GPIO.setup(pin, GPIO.OUT)

# Function to toggle each pin on and off
def test_gpio_pins(pins):
    try:
        for pin in pins:
            print(f"Testing GPIO pin {pin}")
            GPIO.output(pin, GPIO.HIGH)  # Turn on
            time.sleep(1)                # Wait for 1 second
            GPIO.output(pin, GPIO.LOW)   # Turn off
            time.sleep(1)                # Wait for 1 second
    except KeyboardInterrupt:
        print("Test interrupted")
    finally:
        GPIO.cleanup()  # Reset all GPIO pins

# Run the test
test_gpio_pins(output_pins)
