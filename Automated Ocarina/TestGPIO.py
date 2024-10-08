import RPi.GPIO as GPIO
import time

seconds = 1


# List of actual physical GPIO pins to test
output_pins = [11, 12, 13, 15, 16, 18, 22, 29, 31, 32, 33, 35]

# Setup GPIO mode to BOARD (to use physical pin numbers)
GPIO.setmode(GPIO.BOARD)

# Setup all pins as output and set them to LOW initially
for pin in output_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)  # Set all pins to LOW initially

# Function to toggle each pin on and off
def test_gpio_pins(pins):
    try:
        for pin in pins:
            print(f"Testing GPIO pin {pin}")
            GPIO.output(pin, GPIO.HIGH)  # Turn on
            time.sleep(seconds)                 # Wait for 1 second
            GPIO.output(pin, GPIO.LOW)    # Turn off
            time.sleep(seconds)                 # Wait for 1 second
    except KeyboardInterrupt:
        print("Test interrupted")
    finally:
        GPIO.cleanup()  # Reset all GPIO pins

# Run the test
test_gpio_pins(output_pins)
