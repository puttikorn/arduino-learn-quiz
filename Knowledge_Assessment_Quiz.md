# Arduino Learning Course: Knowledge Assessment Quiz

This document contains the complete set of questions, correct answers, and explanations.

## Section A: Multiple Choice Questions (MCQs)

### MCQ_001: Where was the Arduino project founded in 2005?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Easy
  A. MIT, USA
  B. Interaction Design Institute Ivrea, Italy
  C. Munich, Germany
  D. Tokyo, Japan
- Correct Answer: B
- Explanation: Arduino was created at the Interaction Design Institute Ivrea in Italy.

### MCQ_002: Which microcontroller chip is used on the Arduino UNO R3?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Easy
  A. ATmega2560
  B. ATmega32U4
  C. ATmega328P
  D. ATtiny85
- Correct Answer: C
- Explanation: The Arduino UNO R3 uses the ATmega328P microcontroller.

### MCQ_003: What is the standard operating voltage of the Arduino UNO board components?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Easy
  A. 3.3V
  B. 5.0V
  C. 9.0V
  D. 12.0V
- Correct Answer: B
- Explanation: The ATmega328P microcontroller on the UNO operates at 5V.

### MCQ_004: How many analog input pins are available on the Arduino UNO R3?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Easy
  A. 4
  B. 6
  C. 8
  D. 16
- Correct Answer: B
- Explanation: The Arduino UNO has 6 analog inputs (A0 to A5).

### MCQ_005: What is the clock frequency of the crystal oscillator on the Arduino UNO R3?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Medium
  A. 8 MHz
  B. 16 MHz
  C. 20 MHz
  D. 84 MHz
- Correct Answer: B
- Explanation: The Arduino UNO uses a 16 MHz crystal oscillator.

### MCQ_006: How much Static RAM (SRAM) is available on the ATmega328P on Arduino UNO?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Medium
  A. 1 KB
  B. 2 KB
  C. 4 KB
  D. 32 KB
- Correct Answer: B
- Explanation: The ATmega328P has 2 KB of SRAM for storing variables during execution.

### MCQ_007: How much Flash memory is available on the ATmega328P microcontroller?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Medium
  A. 16 KB
  B. 32 KB
  C. 64 KB
  D. 128 KB
- Correct Answer: B
- Explanation: The ATmega328P features 32 KB of flash memory (with 0.5 KB used by bootloader).

### MCQ_008: Which microcontroller chip is used on the Arduino Mega 2560 R3?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Medium
  A. ATmega328P
  B. ATmega32U4
  C. ATmega2560
  D. SAM3X8E
- Correct Answer: C
- Explanation: The Arduino Mega 2560 is based on the ATmega2560 microcontroller.

### MCQ_009: What is the operating voltage of the Arduino Due board?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Medium
  A. 1.8V
  B. 3.3V
  C. 5.0V
  D. 9.0V
- Correct Answer: B
- Explanation: The Arduino Due is powered by an ARM Cortex-M3 processor which operates at 3.3V.

### MCQ_010: Why can the Arduino Leonardo connect directly as a USB keyboard or mouse?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Medium
  A. It has a separate Atmega16U2 chip
  B. It uses the ATmega32U4 which has built-in USB transceiver
  C. It runs a specialized software library in SRAM
  D. It has a hardware USB host shield built-in
- Correct Answer: B
- Explanation: The ATmega32U4 on the Leonardo features native USB communication support.

### MCQ_011: What is the recommended input voltage (VIN) range for the Arduino UNO?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Medium
  A. 5V - 6V
  B. 7V - 12V
  C. 12V - 20V
  D. 15V - 24V
- Correct Answer: B
- Explanation: The recommended input voltage range is 7V to 12V to ensure stable power regulation.

### MCQ_012: What is the absolute maximum continuous DC current allowed per digital I/O pin?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Medium
  A. 10 mA
  B. 20 mA
  C. 40 mA
  D. 100 mA
- Correct Answer: C
- Explanation: Exceeding 40mA per I/O pin on the ATmega328P will cause permanent damage to the silicon port drivers.

### MCQ_013: What is the combined maximum current limit that all I/O pins can source or sink together?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Medium
  A. 100 mA
  B. 200 mA
  C. 400 mA
  D. 500 mA
- Correct Answer: B
- Explanation: The maximum continuous current limit for the VCC or GND pin of the ATmega328P package is 200mA.

### MCQ_014: Which processor core is used on the Arduino Due?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Hard
  A. 8-bit AVR
  B. 32-bit ARM Cortex-M3
  C. 16-bit PIC
  D. 32-bit ESP32
- Correct Answer: B
- Explanation: The Arduino Due is based on the SAM3X8E 32-bit ARM Cortex-M3 microcontroller.

### MCQ_015: What is the primary role of the bootloader pre-programmed on the ATmega328P?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Hard
  A. Compiling C code into hex files
  B. Allowing sketches to be uploaded via Serial interface without programmer hardware
  C. Protecting the microcontroller from overvoltage
  D. Caching variables to speed up code execution
- Correct Answer: B
- Explanation: The bootloader is a small program that handles programming over the serial interface during startup.

### MCQ_016: Which function in an Arduino sketch runs once at the very beginning of execution?
- Topic: Arduino C Programming Basics
- Difficulty: Easy
  A. loop()
  B. setup()
  C. init()
  D. main()
- Correct Answer: B
- Explanation: The setup() function is called once when the sketch starts and is used for initialization.

### MCQ_017: Which function runs continuously in an Arduino sketch after initialization?
- Topic: Arduino C Programming Basics
- Difficulty: Easy
  A. setup()
  B. run()
  C. loop()
  D. execute()
- Correct Answer: C
- Explanation: The loop() function repeats infinitely and contains the main logic of the application.

### MCQ_018: What character is used to terminate statements in the C programming language?
- Topic: Arduino C Programming Basics
- Difficulty: Easy
  A. Colon (:)
  B. Semicolon (;)
  C. Period (.)
  D. Comma (,)
- Correct Answer: B
- Explanation: A semicolon (;) is used to mark the end of a statement in C.

### MCQ_019: Which symbol is used to create a single-line comment in C?
- Topic: Arduino C Programming Basics
- Difficulty: Easy
  A. /*
  B. //
  C. #
  D. ;
- Correct Answer: B
- Explanation: // is used for single-line comments in C/C++.

### MCQ_020: Which syntax is used for multi-line block comments in C?
- Topic: Arduino C Programming Basics
- Difficulty: Easy
  A. //...//
  B. /*...*/
  C. #...#
  D. <!--...-->
- Correct Answer: B
- Explanation: /* starts a block comment and */ terminates it.

### MCQ_021: Which of the following is a valid variable name in C?
- Topic: Arduino C Programming Basics
- Difficulty: Medium
  A. 2sensorVal
  B. sensor_Val
  C. sensor-Val
  D. sensor Val
- Correct Answer: B
- Explanation: Variables cannot start with numbers, contain spaces, or contain hyphens. Underscores are allowed.

### MCQ_022: How many bytes of memory does an 'int' data type occupy on an Arduino UNO?
- Topic: Arduino C Programming Basics
- Difficulty: Medium
  A. 1 byte
  B. 2 bytes
  C. 4 bytes
  D. 8 bytes
- Correct Answer: B
- Explanation: On 8-bit AVR boards like the Arduino UNO, an integer (int) occupies 2 bytes (16 bits) of SRAM.

### MCQ_023: Which data type is used to store a single character in C, and how many bytes does it use?
- Topic: Arduino C Programming Basics
- Difficulty: Medium
  A. string (2 bytes)
  B. char (1 byte)
  C. float (4 bytes)
  D. boolean (1 byte)
- Correct Answer: B
- Explanation: The char data type is used to store single characters and occupies 1 byte (8 bits) of memory.

### MCQ_024: What are the predefined boolean constants used in Arduino C?
- Topic: Arduino C Programming Basics
- Difficulty: Medium
  A. HIGH and LOW
  B. INPUT and OUTPUT
  C. true and false
  D. 1 and -1
- Correct Answer: C
- Explanation: In C/C++, true and false are boolean constants (true maps to 1, false to 0).

### MCQ_025: Which operator is used to calculate the remainder of an integer division in C?
- Topic: Arduino C Programming Basics
- Difficulty: Medium
  A. Slash (/)
  B. Percent (%)
  C. Asterisk (*)
  D. Ampersand (&)
- Correct Answer: B
- Explanation: The modulo operator (%) yields the remainder of the division of one integer by another.

### MCQ_026: Which comparison operator is used to check if two values are equal in C?
- Topic: Arduino C Programming Basics
- Difficulty: Medium
  A. =
  B. ==
  C. ===
  D. !=
- Correct Answer: B
- Explanation: The equality operator in C is ==. The single = is the assignment operator.

### MCQ_027: What does the expression 'x += 5' evaluate to?
- Topic: Arduino C Programming Basics
- Difficulty: Hard
  A. x is multiplied by 5
  B. x is assigned the value 5
  C. x is incremented by 5
  D. x is compared with 5
- Correct Answer: C
- Explanation: x += 5 is shorthand for x = x + 5, which adds 5 to the current value of x and assigns the result back to x.

### MCQ_028: Which operator represents logical AND in C?
- Topic: Arduino C Programming Basics
- Difficulty: Easy
  A. &
  B. &&
  C. |
  D. ||
- Correct Answer: B
- Explanation: && is the logical AND operator. A single & is the bitwise AND operator.

### MCQ_029: Which operator represents logical OR in C?
- Topic: Arduino C Programming Basics
- Difficulty: Easy
  A. |
  B. ||
  C. !
  D. &&
- Correct Answer: B
- Explanation: || is the logical OR operator. A single | is the bitwise OR operator.

### MCQ_030: If a variable is declared inside the loop() function, where can it be accessed?
- Topic: Arduino C Programming Basics
- Difficulty: Hard
  A. Only inside the loop() function
  B. Anywhere in the entire sketch
  C. Only inside setup()
  D. In both setup() and loop()
- Correct Answer: A
- Explanation: Variables declared inside a function have local scope and are only visible/accessible within that function.

### MCQ_031: Which function is used to configure a digital pin as an INPUT or OUTPUT?
- Topic: Basic I/O Components
- Difficulty: Easy
  A. digitalWrite()
  B. pinMode()
  C. digitalRead()
  D. analogWrite()
- Correct Answer: B
- Explanation: pinMode() configures the specified pin to behave either as an input or an output.

### MCQ_032: Which function is used to write a HIGH or LOW value to a digital output pin?
- Topic: Basic I/O Components
- Difficulty: Easy
  A. digitalRead()
  B. pinMode()
  C. digitalWrite()
  D. analogWrite()
- Correct Answer: C
- Explanation: digitalWrite() is used to set the output voltage of a digital pin to 5V (HIGH) or 0V (LOW).

### MCQ_033: Which function is used to read the state of a digital pin?
- Topic: Basic I/O Components
- Difficulty: Easy
  A. digitalRead()
  B. digitalWrite()
  C. pinMode()
  D. analogRead()
- Correct Answer: A
- Explanation: digitalRead() reads the value from a specified digital pin, either HIGH or LOW.

### MCQ_034: When a push button is pressed in an active-low configuration with a pull-up resistor, what voltage level is read by the input pin?
- Topic: Basic I/O Components
- Difficulty: Easy
  A. 5V (HIGH)
  B. 0V (LOW)
  C. Floating state
  D. 2.5V
- Correct Answer: B
- Explanation: In an active-low pull-up configuration, the pin is pulled to HIGH (5V) by default, and pressing the button connects the pin to GND, pulling it to LOW (0V).

### MCQ_035: Which pin should you connect a buzzer to if you want to use the tone() function?
- Topic: Basic I/O Components
- Difficulty: Medium
  A. Only analog inputs
  B. Any digital pin
  C. Only hardware PWM pins
  D. Only pin 13
- Correct Answer: B
- Explanation: The tone() function can generate a square wave of specified frequency on any digital pin.

### MCQ_036: What are the three parameters passed to the tone() function: tone(pin, frequency, duration)?
- Topic: Basic I/O Components
- Difficulty: Easy
  A. Pin number, analog value, delay time
  B. Pin number, frequency in Hz, duration in milliseconds
  C. Pin number, volume, pulse width
  D. Pin number, duty cycle, period
- Correct Answer: B
- Explanation: The parameters are: pin number, frequency of the tone in Hertz, and duration in milliseconds (optional).

### MCQ_037: What is the primary purpose of a relay in an Arduino project?
- Topic: Basic I/O Components
- Difficulty: Medium
  A. To convert AC voltage to DC voltage
  B. To amplify low-voltage signals into high-frequency sounds
  C. To control high-voltage/high-current circuits using a low-voltage control signal
  D. To read analog voltages from a light sensor
- Correct Answer: C
- Explanation: A relay is an electrically operated switch that allows a low-voltage Arduino output (5V) to isolate and control high-power circuits (e.g., 220V AC appliances).

### MCQ_038: Why is a flyback diode connected across a relay's control coil?
- Topic: Basic I/O Components
- Difficulty: Medium
  A. To increase the speed of the relay closing
  B. To protect the Arduino from high-voltage spikes caused by inductive kickback when the coil is de-energized
  C. To restrict current to flow only to the relay
  D. To step down the voltage from 12V to 5V
- Correct Answer: B
- Explanation: Inductors (like relay coils) store energy in a magnetic field. When the current is switched off, the magnetic field collapses, generating a high-voltage spike. The flyback diode provides a path for this current to dissipate safely.

### MCQ_039: What do the abbreviations NO and NC stand for on a relay terminal?
- Topic: Basic I/O Components
- Difficulty: Medium
  A. New Output / Net Current
  B. Normally Open / Normally Closed
  C. Negative Output / Neutral Common
  D. Node Open / Node Closed
- Correct Answer: B
- Explanation: NO stands for Normally Open (contact is open when coil is off), and NC stands for Normally Closed (contact is closed when coil is off).

### MCQ_040: In an active-high push button configuration using a pull-down resistor, what is the default state of the pin when the button is NOT pressed?
- Topic: Basic I/O Components
- Difficulty: Medium
  A. HIGH
  B. LOW
  C. Floating
  D. 5V
- Correct Answer: B
- Explanation: A pull-down resistor pulls the input pin to GND (LOW) when the button is open. Pressing the button connects it to 5V, pulling it HIGH.

### MCQ_041: What happens when you configure a pin using 'pinMode(pin, INPUT_PULLUP)'?
- Topic: Basic I/O Components
- Difficulty: Medium
  A. The pin is configured as output with high resistance
  B. The internal pull-up resistor of the ATmega328P is enabled
  C. An external resistor must be soldered to the pin
  D. The pin is locked to prevent writing
- Correct Answer: B
- Explanation: INPUT_PULLUP configures the pin as input and enables the internal 20K-50K ohm pull-up resistor, simplifying button wiring by eliminating external resistors.

### MCQ_042: Why can't an Arduino digital pin directly power a 12V relay coil?
- Topic: Basic I/O Components
- Difficulty: Medium
  A. The Arduino pin cannot output current
  B. The Arduino output pin provides only 5V and a maximum of 40mA, which is insufficient for the relay coil voltage and current requirements
  C. The relay coil requires AC current
  D. The bootloader blocks direct relay connections
- Correct Answer: B
- Explanation: An Arduino digital pin operates at 5V and max 40mA. A 12V relay requires 12V, and even 5V relays typically draw 70-100mA, which exceeds the pin current limit and can damage the Arduino. A transistor switch (e.g. NPN) is required.

### MCQ_043: In a relay driver circuit, what is the purpose of using an NPN transistor?
- Topic: Basic I/O Components
- Difficulty: Hard
  A. To amplify the frequency of the control signal
  B. To act as a buffer that uses the 5V low-current Arduino pin to switch a higher current from an external power supply through the relay coil
  C. To regulate the 12V power supply to 5V for the Arduino
  D. To prevent AC noise from reaching the USB port
- Correct Answer: B
- Explanation: The transistor acts as a switch: a small base current from the Arduino pin turns on the collector-emitter path, allowing a larger current to flow through the relay coil from an external power source.

### MCQ_044: Under normal operation when the Arduino digital output is driving the transistor to activate a relay coil, is the flyback diode forward-biased or reverse-biased?
- Topic: Basic I/O Components
- Difficulty: Hard
  A. Forward-biased
  B. Reverse-biased
  C. Conducting current
  D. Shorted out
- Correct Answer: B
- Explanation: During normal activation, the diode is reverse-biased (pointing from GND/transistor side to VCC) and does not conduct. It only conducts when the transistor switches off and the coil's collapsing magnetic field creates a reverse voltage spike.

### MCQ_045: What is a side effect of using the tone() function on an Arduino UNO?
- Topic: Basic I/O Components
- Difficulty: Hard
  A. It disables analog inputs
  B. It interferes with PWM outputs on pins 3 and 11 because they share the same internal hardware timer (Timer 2)
  C. It slows down the Serial transmission rate
  D. It resets the bootloader
- Correct Answer: B
- Explanation: The tone() function uses Timer 2. Using tone() prevents PWM output (analogWrite) on pins 3 and 11.

### MCQ_046: How many pins are present on a standard parallel Character LCD 1602 without an I2C interface?
- Topic: Character LCD & I2C Interface
- Difficulty: Easy
  A. 4 pins
  B. 8 pins
  C. 12 pins
  D. 16 pins
- Correct Answer: D
- Explanation: A standard LCD 1602 has 16 pins for power, backlight, contrast adjustment, and parallel data lines.

### MCQ_047: How many connections are required between the Arduino UNO and an LCD 1602 using an I2C interface backpack?
- Topic: Character LCD & I2C Interface
- Difficulty: Easy
  A. 2 pins
  B. 4 pins
  C. 8 pins
  D. 16 pins
- Correct Answer: B
- Explanation: An I2C LCD requires only 4 connections: VCC, GND, SDA, and SCL.

### MCQ_048: What is the most common default I2C address for the LCD 1602 I2C backpack interface?
- Topic: Character LCD & I2C Interface
- Difficulty: Easy
  A. 0x00
  B. 0x27
  C. 0x80
  D. 0xFF
- Correct Answer: B
- Explanation: The default I2C address for the PCF8574-based LCD backpack is usually 0x27 (or sometimes 0x3F).

### MCQ_049: Which analog input pins on the Arduino UNO double as the SDA and SCL pins for I2C communication?
- Topic: Character LCD & I2C Interface
- Difficulty: Easy
  A. A0 and A1
  B. A2 and A3
  C. A4 and A5
  D. A4 and pin 13
- Correct Answer: C
- Explanation: On the Arduino UNO, pin A4 is SDA and A5 is SCL.

### MCQ_050: Which LiquidCrystal_I2C function is used to erase all text from the LCD screen?
- Topic: Character LCD & I2C Interface
- Difficulty: Medium
  A. lcd.erase()
  B. lcd.clean()
  C. lcd.clear()
  D. lcd.reset()
- Correct Answer: C
- Explanation: The lcd.clear() function clears the display screen and moves the cursor to the top-left corner.

### MCQ_051: Which function is used to output text on the LCD screen?
- Topic: Character LCD & I2C Interface
- Difficulty: Medium
  A. lcd.write()
  B. lcd.print()
  C. lcd.display()
  D. lcd.show()
- Correct Answer: B
- Explanation: lcd.print() is used to print readable characters and numbers to the LCD display.

### MCQ_052: How is the contrast of the text adjusted on an I2C LCD 1602 module?
- Topic: Character LCD & I2C Interface
- Difficulty: Medium
  A. Via the Arduino software code
  B. By turning the potentiometer on the I2C backpack board
  C. By changing the input voltage from 5V to 3.3V
  D. By adjusting the backlight using PWM on pin 9
- Correct Answer: B
- Explanation: The blue potentiometer located on the back of the I2C backpack is turned manually to adjust the contrast of the LCD characters.

### MCQ_053: On a 16x2 LCD screen, what is the column and row index coordinates of the very first character in the top-left corner?
- Topic: Character LCD & I2C Interface
- Difficulty: Medium
  A. (1, 1)
  B. (0, 0)
  C. (0, 1)
  D. (1, 0)
- Correct Answer: B
- Explanation: The LCD library uses 0-based indexing, so the top-left character is at column 0, row 0.

### MCQ_054: To write text at the beginning of the second line of a 16x2 LCD, what arguments should you pass to lcd.setCursor()?
- Topic: Character LCD & I2C Interface
- Difficulty: Medium
  A. lcd.setCursor(0, 1)
  B. lcd.setCursor(1, 0)
  C. lcd.setCursor(1, 2)
  D. lcd.setCursor(2, 1)
- Correct Answer: A
- Explanation: The first argument is the column (0) and the second argument is the row (1 for the second line).

### MCQ_055: What are the parameters passed to the LiquidCrystal_I2C constructor: LiquidCrystal_I2C lcd(addr, cols, rows)?
- Topic: Character LCD & I2C Interface
- Difficulty: Medium
  A. I2C Address, number of rows, number of columns
  B. I2C Address, number of columns, number of rows
  C. Pin numbers, width, height
  D. SDA pin, SCL pin, address
- Correct Answer: B
- Explanation: The arguments are: I2C Address (e.g. 0x27), number of columns (16), and number of rows (2).

### MCQ_056: How do you turn on the LCD backlight using the LiquidCrystal_I2C library?
- Topic: Character LCD & I2C Interface
- Difficulty: Medium
  A. lcd.backlight()
  B. lcd.setBacklight(HIGH)
  C. lcd.lightOn()
  D. lcd.powerBacklight()
- Correct Answer: A
- Explanation: The lcd.backlight() function turns on the LED backlight of the LCD display.

### MCQ_057: What is the primary advantage of using an I2C LCD backpack over direct parallel wiring?
- Topic: Character LCD & I2C Interface
- Difficulty: Hard
  A. It speeds up the character rendering rate on the screen
  B. It saves 12 digital I/O pins on the Arduino by using only two communication pins
  C. It allows the LCD to display color images
  D. It eliminates the need for a 5V power supply line
- Correct Answer: B
- Explanation: By using the I2C serial protocol, the pin count required to drive the LCD is reduced from at least 6 digital pins to just 2 (SDA and SCL).

### MCQ_058: Why does the I2C bus require pull-up resistors on the SDA and SCL lines?
- Topic: Character LCD & I2C Interface
- Difficulty: Medium
  A. To prevent short circuits when pins are set to output LOW
  B. To pull the bus lines to high logic level (VCC) because I2C devices use open-drain outputs to pull them LOW
  C. To limit current to the LCD
  D. To filter out high-frequency noise from the lines
- Correct Answer: B
- Explanation: I2C lines are open-drain, meaning devices can only pull the lines LOW. Pull-up resistors are required to pull the lines HIGH when no device is driving the bus LOW.

### MCQ_059: What happens to the displayed text on the LCD screen if the Arduino enters an infinite empty loop: while(true) {}?
- Topic: Character LCD & I2C Interface
- Difficulty: Hard
  A. The text immediately disappears
  B. The text starts flashing
  C. The text remains visible on the screen
  D. The LCD resets and shows its default address
- Correct Answer: C
- Explanation: The LCD has its own controller (HD44780) and memory. Once text is written to the LCD, it stays on the display until overwritten, cleared, or powered off, even if the Arduino stops sending data.

### MCQ_060: Can you connect multiple I2C LCDs or other I2C devices to the same SDA/SCL pins of the Arduino UNO?
- Topic: Character LCD & I2C Interface
- Difficulty: Hard
  A. No, I2C only supports one device per bus
  B. Yes, as long as they have different I2C addresses
  C. Yes, but they must share the same address
  D. Yes, but only if one is powered at 3.3V and the other at 5V
- Correct Answer: B
- Explanation: The I2C bus is an addressable bus, allowing multiple slave devices to share the same two lines (SDA and SCL) as long as each device has a unique address.

### MCQ_061: What does LDR stand for?
- Topic: LDR Light Sensors
- Difficulty: Easy
  A. Light Detection Regulator
  B. Light Dependent Resistor
  C. Low Distortion Resistor
  D. Laser Diode Receiver
- Correct Answer: B
- Explanation: LDR stands for Light Dependent Resistor (also known as a photocell or photoresistor).

### MCQ_062: How does the resistance of an LDR change as light intensity increases?
- Topic: LDR Light Sensors
- Difficulty: Easy
  A. Resistance increases
  B. Resistance decreases
  C. Resistance remains constant
  D. Resistance fluctuates randomly
- Correct Answer: B
- Explanation: The resistance of an LDR decreases dramatically when exposed to brighter light (from megaohms in darkness to a few hundred ohms in bright light).

### MCQ_063: What type of sensor is an LDR, and which pins is it typically connected to on Arduino for reading continuous values?
- Topic: LDR Light Sensors
- Difficulty: Easy
  A. Digital sensor / Digital pins
  B. Analog sensor / Analog input pins (A0-A5)
  C. Serial sensor / RX/TX pins
  D. PWM sensor / PWM output pins
- Correct Answer: B
- Explanation: An LDR is an analog sensor whose resistance varies continuously. It is read using the analog input pins (A0-A5) via analogRead().

### MCQ_064: Why do we need a fixed resistor in series with an LDR to read it with an Arduino?
- Topic: LDR Light Sensors
- Difficulty: Easy
  A. To limit the current and protect the LDR from burning out
  B. To create a voltage divider circuit that translates resistance changes into voltage changes
  C. To pull the digital pin HIGH
  D. To filter out AC voltage noise
- Correct Answer: B
- Explanation: The Arduino analog input pins measure voltage (0-5V), not resistance. A voltage divider circuit converts the LDR's resistance changes into a varying voltage that the Arduino can measure.

### MCQ_065: What is the range of integers returned by the analogRead() function on an Arduino UNO?
- Topic: LDR Light Sensors
- Difficulty: Medium
  A. 0 to 255
  B. 0 to 511
  C. 0 to 1023
  D. 0 to 4095
- Correct Answer: C
- Explanation: The Arduino UNO features a 10-bit analog-to-digital converter (ADC), which yields values from 0 to 1023 corresponding to 0V to 5V.

### MCQ_066: If analogRead(A0) returns 512 on an Arduino UNO with a 5V reference, what is the measured voltage?
- Topic: LDR Light Sensors
- Difficulty: Medium
  A. 1.25 V
  B. 2.5 V
  C. 3.3 V
  D. 5.0 V
- Correct Answer: B
- Explanation: Voltage = (read_value * 5.0) / 1023.0. For 512, the voltage is approximately 2.5V (exactly midpoint).

### MCQ_067: Which function is used to scale the analog read values (0-1023) from an LDR to a percentage range (0-100)?
- Topic: LDR Light Sensors
- Difficulty: Medium
  A. scale()
  B. map()
  C. constrain()
  D. convert()
- Correct Answer: B
- Explanation: The map() function is used to map/scale a number from one range to another (e.g. map(val, 0, 1023, 0, 100)).

### MCQ_068: In a voltage divider where the LDR is connected between 5V and the analog pin, and a fixed resistor is connected between the analog pin and GND, what happens to the analog pin voltage when it gets dark?
- Topic: LDR Light Sensors
- Difficulty: Medium
  A. The voltage increases toward 5V
  B. The voltage decreases toward 0V
  C. The voltage remains constant
  D. The voltage goes negative
- Correct Answer: B
- Explanation: In darkness, the LDR resistance is extremely high. Since the LDR is in the upper part of the divider, its high resistance drop causes most of the voltage to drop across it, resulting in the analog pin voltage dropping close to 0V (GND).

### MCQ_069: In the same circuit (LDR between 5V and analog pin, fixed resistor to GND), what happens to the output voltage in bright light?
- Topic: LDR Light Sensors
- Difficulty: Medium
  A. The voltage increases toward 5V
  B. The voltage decreases toward 0V
  C. The voltage remains constant
  D. The voltage drops to 0.958V
- Correct Answer: A
- Explanation: In bright light, the LDR resistance drops very low (hundreds of ohms). The voltage at the analog pin rises close to 5V.

### MCQ_070: What are the parameters passed to the map function: map(value, fromLow, fromHigh, toLow, toHigh)?
- Topic: LDR Light Sensors
- Difficulty: Medium
  A. Value to map, current lower bound, current upper bound, target lower bound, target upper bound
  B. Value, output range, input range, step size, factor
  C. Value, min input, max input, offset, precision
  D. Value, scale, shift, threshold, limit
- Correct Answer: A
- Explanation: The map function requires five parameters: the input value, the lower and upper bounds of the input range, and the lower and upper bounds of the target output range.

### MCQ_071: What semiconductor material is most commonly used to manufacture LDRs?
- Topic: LDR Light Sensors
- Difficulty: Medium
  A. Silicon
  B. Germanium
  C. Cadmium Sulfide (CdS)
  D. Gallium Arsenide
- Correct Answer: C
- Explanation: Cadmium Sulfide (CdS) is the standard photo-conductive material used to make light-dependent resistors.

### MCQ_072: How long does a standard analogRead() conversion take on an Arduino UNO (16 MHz AVR)?
- Topic: LDR Light Sensors
- Difficulty: Hard
  A. 1 microsecond
  B. 100 microseconds
  C. 1 millisecond
  D. 10 milliseconds
- Correct Answer: B
- Explanation: On the Arduino UNO, a standard analogRead() conversion takes about 100 microseconds (specifically, 13 ADC clock cycles at a prescaler of 128).

### MCQ_073: How can you configure the Arduino to use the internal 1.1V reference voltage for analog inputs instead of the default 5V?
- Topic: LDR Light Sensors
- Difficulty: Hard
  A. analogReference(INTERNAL)
  B. analogReference(DEFAULT)
  C. analogReference(EXTERNAL)
  D. By connecting the AREF pin to GND
- Correct Answer: A
- Explanation: analogReference(INTERNAL) sets the analog reference voltage to 1.1V on the ATmega328P, which increases precision for small analog signals.

### MCQ_074: If an LDR with resistance R_LDR is connected between 5V and the analog pin A0, and a 10k ohm resistor is connected between A0 and GND, what is the formula for the voltage V_out at A0?
- Topic: LDR Light Sensors
- Difficulty: Hard
  A. V_out = 5 * (R_LDR / (R_LDR + 10000))
  B. V_out = 5 * (10000 / (R_LDR + 10000))
  C. V_out = 5 * (R_LDR * 10000)
  D. V_out = 5 / (R_LDR + 10000)
- Correct Answer: B
- Explanation: The standard voltage divider formula is V_out = V_in * (R_bottom / (R_top + R_bottom)). Here, R_bottom is the 10k ohm fixed resistor, and R_top is the R_LDR.

### MCQ_075: What is the mathematical quantization error (resolution limit) of the 10-bit ADC on the Arduino UNO operating at 5V?
- Topic: LDR Light Sensors
- Difficulty: Hard
  A. About 1 mV
  B. About 4.9 mV
  C. About 10 mV
  D. About 50 mV
- Correct Answer: B
- Explanation: The resolution limit is VCC / 1024 = 5.0V / 1024 = 4.88 mV (approximately 4.9 mV) per ADC step.

### MCQ_076: What does the abbreviation PIR stand for in PIR sensor?
- Topic: PIR Motion Sensors
- Difficulty: Easy
  A. Photo Induction Regulator
  B. Passive Infrared
  C. Polarized Infrared Receiver
  D. Pulse Infrared Relay
- Correct Answer: B
- Explanation: PIR stands for Passive Infrared.

### MCQ_077: What does a PIR sensor measure to detect motion?
- Topic: PIR Motion Sensors
- Difficulty: Easy
  A. Ultrasonic sound waves reflecting off moving targets
  B. Changes in ambient infrared radiation (heat signatures)
  C. The electrical resistance of air between two pins
  D. Laser beam breakages
- Correct Answer: B
- Explanation: PIR sensors detect motion by measuring changes in the infrared radiation levels emitted by surrounding objects (such as humans or animals).

### MCQ_078: What is the purpose of the white plastic dome (Fresnel lens) covering a PIR sensor?
- Topic: PIR Motion Sensors
- Difficulty: Easy
  A. To protect the sensor from water and physical damage
  B. To filter out visible light and focus infrared radiation onto the pyroelectric sensor element
  C. To amplify sound waves
  D. To house status indication LEDs
- Correct Answer: B
- Explanation: The Fresnel lens focuses infrared light onto the pyroelectric element and segments the detection area to create distinct sectors of sensitivity.

### MCQ_079: What type of electrical signal does a standard PIR sensor output when motion is detected?
- Topic: PIR Motion Sensors
- Difficulty: Easy
  A. A continuous analog voltage from 0V to 5V
  B. A high digital signal (typically 3.3V TTL)
  C. A variable frequency square wave
  D. An I2C data stream
- Correct Answer: B
- Explanation: A PIR sensor outputs a digital HIGH signal (usually 3.3V TTL level) when motion is detected, and LOW (0V) when idle.

### MCQ_080: Why does a PIR sensor require a warm-up time (calibration delay) of 10 to 60 seconds after power-on?
- Topic: PIR Motion Sensors
- Difficulty: Medium
  A. To heat up the internal optical lens
  B. To allow the sensor to calibrate itself to the ambient infrared environment of the room
  C. To charge the bootloader memory
  D. To initialize serial communications
- Correct Answer: B
- Explanation: The calibration period allows the sensor's internal amplifier circuitry to adapt to the baseline infrared environment, preventing false triggers.

### MCQ_081: What are the two physical adjustment potentiometers on a PIR sensor module used for?
- Topic: PIR Motion Sensors
- Difficulty: Medium
  A. Adjusting output voltage and frequency
  B. Adjusting sensitivity (range) and output delay time
  C. Adjusting I2C address and baud rate
  D. Adjusting operating temperature and threshold
- Correct Answer: B
- Explanation: The two potentiometers adjust the detection range/sensitivity (typically 3 to 7 meters) and the delay time (how long the output remains HIGH after motion stops, usually 3 seconds to 5 minutes).

### MCQ_082: What are the standard pin names on a PIR sensor module interface?
- Topic: PIR Motion Sensors
- Difficulty: Medium
  A. SDA, SCL, GND
  B. VCC, OUT, GND
  C. TX, RX, VCC
  D. A0, D0, GND
- Correct Answer: B
- Explanation: A standard PIR sensor has 3 pins: VCC (power), OUT (digital output), and GND (ground).

### MCQ_083: What is the typical detection angle coverage of a standard HC-SR501 PIR sensor?
- Topic: PIR Motion Sensors
- Difficulty: Medium
  A. 45 degrees
  B. 110 degrees
  C. 180 degrees
  D. 360 degrees
- Correct Answer: B
- Explanation: A standard HC-SR501 PIR sensor has a detection cone of approximately 110 degrees.

### MCQ_084: If a PIR sensor is connected to digital pin 7, how is motion detected in code?
- Topic: PIR Motion Sensors
- Difficulty: Medium
  A. if (analogRead(7) > 500)
  B. if (digitalRead(7) == HIGH)
  C. if (Serial.read() == 7)
  D. if (pulseIn(7) == 1)
- Correct Answer: B
- Explanation: Since the PIR sensor outputs a digital signal, you use digitalRead(7) and check if it is HIGH.

### MCQ_085: Which of the following environmental factors is most likely to cause false triggers on a PIR sensor?
- Topic: PIR Motion Sensors
- Difficulty: Medium
  A. Changes in room ambient lighting
  B. Rapid temperature changes, drafts, or direct sunlight on the sensor
  C. Silent music playing in the background
  D. High humidity level below 80%
- Correct Answer: B
- Explanation: PIR sensors are sensitive to infrared changes, so hot air currents (drafts), heaters, and direct sunlight can cause false motion triggers.

### MCQ_086: What do the 'L' and 'H' jumper settings represent on a PIR module?
- Topic: PIR Motion Sensors
- Difficulty: Medium
  A. Low and High sensitivity
  B. Single trigger (L) and Repeatable trigger (H)
  C. Light sensor enable and Humidity sensor enable
  D. Line output and Hardware output
- Correct Answer: B
- Explanation: The jumper selects the trigger mode: 'L' for non-repeatable trigger (output goes LOW immediately after delay expires even if motion continues) and 'H' for repeatable/retriggerable (delay resets with every movement, keeping output HIGH).

### MCQ_087: The PIR sensor outputs a 3.3V digital signal when triggered. Can this be connected directly to an Arduino UNO input pin operating at 5V?
- Topic: PIR Motion Sensors
- Difficulty: Hard
  A. No, it will damage the PIR output pin
  B. No, because 3.3V is not recognized as a HIGH level by the Arduino UNO
  C. Yes, because the Arduino UNO digital pin recognizes any voltage above 3.0V as HIGH, and 3.3V is safe for the input pin
  D. Yes, but only through an analog pin
- Correct Answer: C
- Explanation: Yes, because on a 5V ATmega328P, the minimum threshold for a digital HIGH signal is 3.0V (0.6 * VCC). A 3.3V signal is safely recognized as HIGH without needing level conversion.

### MCQ_088: What is the 'block time' or 'sleep time' of a PIR sensor after the output goes LOW?
- Topic: PIR Motion Sensors
- Difficulty: Medium
  A. The time the PIR sensor takes to restart
  B. A short period (typically 2.5 seconds) during which the PIR sensor ignores all motion to prevent self-triggering
  C. The time required to recharge the capacitors
  D. The period the Arduino delays in setup
- Correct Answer: B
- Explanation: The block time (usually 2.5s) occurs after the PIR output returns to LOW. During this block time, the sensor is blind to motion, allowing the pyroelectric element to stabilize.

### MCQ_089: What active material inside a PIR sensor generates an electrical charge when exposed to infrared radiation?
- Topic: PIR Motion Sensors
- Difficulty: Hard
  A. Cadmium Sulfide
  B. Silicon Photodiode
  C. Pyroelectric crystal material (e.g., lithium tantalate)
  D. Gallium Nitride
- Correct Answer: C
- Explanation: PIR sensors contain a pyroelectric sensor made of crystalline material that generates an electrical charge when it absorbs infrared radiation (heat).

### MCQ_090: Why do PIR sensors typically use a dual-element or quad-element pyroelectric sensor design?
- Topic: PIR Motion Sensors
- Difficulty: Hard
  A. To double the detection range
  B. To cancel out ambient temperature changes and trigger only when there is a difference in heat between the two elements (i.e. movement)
  C. To measure temperature and humidity at the same time
  D. To allow communication via I2C
- Correct Answer: B
- Explanation: The two elements are wired in series-opposition. Uniform temperature changes (like room warming up) affect both elements equally and cancel out, whereas a moving human source crosses one element before the other, generating a differential signal.

### MCQ_091: How many pins are on a bare DHT11 temperature and humidity sensor chip?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Easy
  A. 2 pins
  B. 3 pins
  C. 4 pins
  D. 5 pins
- Correct Answer: C
- Explanation: A bare DHT11 sensor has 4 pins: VDD, DATA, NC (Not Connected), and GND. (Some pre-mounted breakout modules have only 3 pins).

### MCQ_092: What communication protocol or bus is used by the DHT11 sensor to transmit data?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Easy
  A. I2C
  B. SPI
  C. Single-wire custom serial protocol
  D. Standard RS232 Serial
- Correct Answer: C
- Explanation: The DHT11 uses a custom single-wire serial bus protocol that requires precise timing, different from Dallas 1-wire.

### MCQ_093: What is the standard operating voltage range for the DHT11 sensor?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Easy
  A. 1.8V to 2.5V
  B. 3.0V to 5.5V
  C. 7.0V to 12.0V
  D. 12.0V to 24.0V
- Correct Answer: B
- Explanation: The DHT11 operates on a power supply of 3.0V to 5.5V DC.

### MCQ_094: What humidity range can the DHT11 sensor measure, and with what accuracy?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Easy
  A. 0-100% RH with 1% accuracy
  B. 20-90% RH with 5% accuracy
  C. 50-100% RH with 10% accuracy
  D. 10-50% RH with 2% accuracy
- Correct Answer: B
- Explanation: The DHT11 has a humidity measuring range of 20% to 90% RH with an accuracy of +/- 5%.

### MCQ_095: What temperature range can the DHT11 sensor measure, and with what accuracy?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Easy
  A. -40 to 125 *C with 0.1 *C accuracy
  B. 0 to 50 *C with +/- 2 *C accuracy
  C. -10 to 80 *C with +/- 5 *C accuracy
  D. 25 to 100 *C with +/- 1 *C accuracy
- Correct Answer: B
- Explanation: The DHT11 measures temperature from 0 *C to 50 *C with an accuracy of +/- 2.0 *C.

### MCQ_096: What is the maximum frequency at which you should read data from the DHT11 sensor to avoid reading stale data or overheating the sensor?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Medium
  A. Every 100 milliseconds
  B. Every 1 second
  C. Every 2 seconds (0.5 Hz)
  D. Every 10 seconds
- Correct Answer: C
- Explanation: The DHT11 requires at least 2 seconds between consecutive reads (0.5 Hz sampling rate) to ensure stable data extraction.

### MCQ_097: How many bits of data does the DHT11 sensor transmit to the microcontroller in a single complete readout?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Medium
  A. 8 bits
  B. 16 bits
  C. 32 bits
  D. 40 bits
- Correct Answer: D
- Explanation: A complete data transmission from the DHT11 consists of 40 bits (5 bytes) sent serially.

### MCQ_098: What is the breakdown of the 40 bits of data sent by the DHT11 sensor?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Medium
  A. 16-bit Temp + 16-bit Humidity + 8-bit Checksum
  B. 8-bit integral RH + 8-bit decimal RH + 8-bit integral Temp + 8-bit decimal Temp + 8-bit Checksum
  C. 32-bit Temp-Humidity combined + 8-bit address
  D. 24-bit raw values + 16-bit CRC
- Correct Answer: B
- Explanation: The 40 bits are structured as: 8-bit integer Relative Humidity, 8-bit decimal Relative Humidity (always 0 on DHT11), 8-bit integer Temperature, 8-bit decimal Temperature (always 0 on DHT11), and 8-bit checksum.

### MCQ_099: How is the 8-bit checksum calculated in the DHT11 protocol?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Medium
  A. By performing an XOR of the first 4 bytes
  B. By adding the first 4 bytes together (Integral RH + Decimal RH + Integral T + Decimal T) and taking the lowest 8 bits of the sum
  C. By taking the average of the temperature and humidity values
  D. By running a 16-bit CRC polynomial
- Correct Answer: B
- Explanation: The checksum is validated by checking if the sum of the first 4 bytes matches the 5th byte (checksum byte).

### MCQ_100: How does the microcontroller initiate communication with the DHT11 sensor?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Medium
  A. By sending an I2C start command at address 0x27
  B. By pulling the DATA line low for at least 18 milliseconds (ms) and then releasing the line to let it go high
  C. By sending a 9600 baud serial character 'S'
  D. By supplying 5V to the data pin
- Correct Answer: B
- Explanation: To start communication, the MCU pulls the data bus low for at least 18ms to allow the DHT11 to detect the start signal, then pulls it high and waits for the sensor's response.

### MCQ_101: After the MCU releases the data line, how does the DHT11 signal that it is ready to transmit data?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Medium
  A. It pulls the line low for 80us, then pulls it high for 80us
  B. It sends a series of 8 pulses at 100 kHz
  C. It pulls the line high for 18ms
  D. It starts transmitting serial characters immediately
- Correct Answer: A
- Explanation: The DHT11 responds by pulling the data bus low for 80 microseconds, and then high for 80 microseconds before starting data transmission.

### MCQ_102: How are the data bits '0' and '1' distinguished in the DHT11 single-wire signal?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Medium
  A. Bit '0' is 0V and Bit '1' is 5V
  B. Both start with a 50us low time, but a '0' has a 26-28us high time, while a '1' has a 70us high time
  C. Bit '0' has a frequency of 1 kHz, while '1' is 2 kHz
  D. Bit '0' is a 12us high pulse, '1' is a 24us high pulse
- Correct Answer: B
- Explanation: In the DHT11 format, each data bit begins with a 50us low-voltage interval. The subsequent high-voltage interval determines the bit: 26-28us indicates '0', and 70us indicates '1'.

### MCQ_103: What external component is recommended to connect between the DHT11 VCC and DATA pins in long wire runs?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Medium
  A. A 220 ohm current limiting resistor
  B. A 5.1V Zener diode
  C. A 4.7k to 10k ohm pull-up resistor
  D. A 100nF decoupling capacitor
- Correct Answer: C
- Explanation: A pull-up resistor of about 5K-10K ohms is recommended to keep the data line HIGH when the line is idle.

### MCQ_104: Which library is most commonly used in the Arduino IDE to read the DHT11 sensor easily?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Hard
  A. LiquidCrystal_12C.h
  B. DHT.h (usually by Adafruit)
  C. SPI.h
  D. Wire.h
- Correct Answer: B
- Explanation: The Adafruit DHT-sensor-library providing 'DHT.h' is the standard library used to read DHT11/DHT22 sensors.

### MCQ_105: What is a key difference between the DHT11 and the DHT22 (AM2302) sensors?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Hard
  A. The DHT11 uses I2C, while DHT22 uses SPI
  B. The DHT22 has higher accuracy (+/- 2% RH, +/- 0.5 *C), wider ranges (-40 to 80 *C, 0-100% RH), and transmits decimal values in the temperature and humidity fields
  C. The DHT11 operates at 12V, while DHT22 operates at 5V
  D. The DHT22 requires a 12V supply, while DHT11 operates at 5V
- Correct Answer: B
- Explanation: The DHT22 is higher precision and covers a wider measurement range, and unlike the DHT11 (where decimal data is always 0), the DHT22 returns actual decimal fractional values.

### MCQ_106: What is the output voltage scaling factor of the LM35 temperature sensor?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Easy
  A. 1 mV per degree Celsius
  B. 10 mV per degree Celsius
  C. 100 mV per degree Celsius
  D. 1V per degree Celsius
- Correct Answer: B
- Explanation: The LM35 outputs a linear voltage of 10 mV per degree Celsius (e.g., 250 mV corresponds to 25 *C).

### MCQ_107: Which formula correctly calculates temperature in Celsius from the LM35 read value (using 5V reference and 10-bit ADC)?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Easy
  A. Temp = read_value * 5 * 100
  B. Temp = (read_value * 5 * 100) / 1023
  C. Temp = (read_value * 1023 * 100) / 5
  D. Temp = read_value / 10.23
- Correct Answer: B
- Explanation: The formula converts the digital reading to voltage: Voltage = read_value * 5.0 / 1023.0. Since 10mV = 0.01V represents 1 *C, we multiply by 100: Temp = Voltage * 100 = (read_value * 5.0 * 100.0) / 1023.0.

### MCQ_108: What is the standard temperature measurement range of the LM35 Precision Centigrade Temperature Sensor?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Easy
  A. 0 *C to 100 *C
  B. -55 *C to +150 *C
  C. -40 *C to 125 *C
  D. -100 *C to +100 *C
- Correct Answer: B
- Explanation: The LM35 is rated to operate over a temperature range of -55 *C to +150 *C.

### MCQ_109: What type of output does the HIH4030 humidity sensor provide?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Easy
  A. I2C digital output
  B. SPI digital output
  C. Analog voltage output
  D. Variable frequency output
- Correct Answer: C
- Explanation: The HIH4030 is an analog humidity sensor that outputs a near-linear voltage proportional to relative humidity.

### MCQ_110: What are the three pins of the LM35 sensor in a TO-92 package?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Medium
  A. VCC, OUT, GND
  B. SDA, SCL, GND
  C. VCC, RX, TX
  D. ANALOG, DIGITAL, GND
- Correct Answer: A
- Explanation: The LM35 has 3 pins: VCC (Power supply, 4-30V), OUT (Analog voltage output), and GND (Ground).

### MCQ_111: What is the formula to calculate relative humidity (%RH) at 25 *C from the HIH4030 output voltage?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Medium
  A. %RH = (Voltage - 0.958) / 0.0307
  B. %RH = (Voltage * 1023) / 0.0307
  C. %RH = Voltage * 30.7
  D. %RH = (Voltage - 0.0307) / 0.958
- Correct Answer: A
- Explanation: The standard formula provided in the document for the HIH4030 at 25 *C is %RH = (Voltage - 0.958) / 0.0307.

### MCQ_112: Which formula is used for temperature-compensated relative humidity (%True RH) for the HIH4030 sensor?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Medium
  A. %True RH = %RH * (1.0546 - 0.00216 * T)
  B. %True RH = (%RH) / (1.0546 - 0.00216 * T)
  C. %True RH = %RH / (Voltage - T)
  D. %True RH = %RH + 0.00216 * T
- Correct Answer: B
- Explanation: The temperature compensation formula is %True RH = (%RH) / (1.0546 - 0.00216 * T) where T is temperature in Celsius.

### MCQ_113: What is the main advantage of using an IC temperature sensor like the LM35 over a thermistor?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Medium
  A. It is much cheaper
  B. It has a linear voltage output, so it does not require complex non-linear math or calibration tables
  C. It does not require any power connection
  D. It outputs a digital signal
- Correct Answer: B
- Explanation: Thermistors change resistance non-linearly with temperature, requiring the Steinhart-Hart equation. The LM35 provides a highly linear voltage output directly proportional to Celsius, simplifying code.

### MCQ_114: What is 'self-heating' in the context of the LM35 sensor, and how is it minimized?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Medium
  A. The sensor heats the room; it is minimized by fans
  B. The sensor heats itself due to internal current consumption; it is minimized by operating at low currents in still air (typically drawing less than 60uA)
  C. The sensor burns out; minimized by fuses
  D. The sensor has a software thermal lock
- Correct Answer: B
- Explanation: Self-heating is the temperature rise caused by current flowing through the sensor. Because the LM35 draws very low current (approx 60uA), its self-heating is extremely low (less than 0.1 *C in still air).

### MCQ_115: What supply voltage does the HIH4030 sensor typically require for operation?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Medium
  A. 1.8V to 2.5V
  B. 4.0V to 5.8V (typically 5V)
  C. 7V to 12V
  D. 12V to 24V
- Correct Answer: B
- Explanation: The HIH4030 operates on a supply voltage range of 4.0V to 5.8V DC, commonly powered by the Arduino's 5V rail.

### MCQ_116: What relative humidity range can the HIH4030 sensor measure?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Medium
  A. 0% to 100% RH
  B. 20% to 80% RH
  C. 30% to 90% RH
  D. 10% to 50% RH
- Correct Answer: A
- Explanation: The HIH4030 is designed to measure relative humidity from 0% to 100% RH.

### MCQ_117: To measure negative temperatures below 0 *C with the LM35, what hardware modification is required?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Hard
  A. No modification is required
  B. A pull-down resistor must be added between the OUT pin and a negative supply voltage
  C. The sensor must be powered at 3.3V
  D. A capacitor must be placed in series with the OUT pin
- Correct Answer: B
- Explanation: To measure negative temperatures, the LM35 output must be able to go negative relative to GND. This requires adding a resistor from the output pin to a negative voltage rail (e.g., -5V).

### MCQ_118: If you change the analog reference of the Arduino UNO to the internal 1.1V instead of 5V, what is the maximum temperature the LM35 can measure, and what happens to the resolution?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Medium
  A. 150 *C, resolution remains same
  B. 110 *C, resolution increases (becomes more precise)
  C. 50 *C, resolution decreases
  D. 110 *C, resolution decreases
- Correct Answer: B
- Explanation: Since the reference is 1.1V (1100 mV), the maximum readable output voltage is 1.1V, which corresponds to 110 *C. However, the resolution increases because 1024 steps are distributed over 1.1V instead of 5V, providing ~0.1 *C steps instead of ~0.5 *C steps.

### MCQ_119: Why is it important to connect the HIH4030 output to a high impedance input like the Arduino analog pin?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Hard
  A. To avoid loading the sensor output, which has a minimum load resistance requirement of 80k ohms to prevent measurement errors
  B. To speed up the ADC reading
  C. To protect the sensor from shorting to ground
  D. To block noise
- Correct Answer: A
- Explanation: The HIH4030 has a high output impedance and requires a load impedance of at least 80k ohms (the Arduino input impedance is ~100M ohms, which is ideal) to prevent voltage drop and reading inaccuracy.

### MCQ_120: Which software technique is most commonly used in Arduino code to reduce high-frequency electrical noise from analog sensor readings?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Hard
  A. Increasing the baud rate of the Serial port
  B. Taking multiple consecutive readings (e.g., 10 samples) and calculating their average
  C. Using delay(1000) after each reading
  D. Calling pinMode() in loop() repeatedly
- Correct Answer: B
- Explanation: Oversampling and averaging (calculating the mean of multiple readings) acts as a low-pass filter, smoothing out noise and improving measurement accuracy.

### MCQ_121: What is the primary function of the DS1302 chip in an electronics project?
- Topic: DS1302 Real-Time Clock
- Difficulty: Easy
  A. It acts as a high-speed micro-controller
  B. It is a Real-Time Clock (RTC) chip that keeps track of the current date and time
  C. It is an analog-to-digital converter
  D. It is a flash memory storage device
- Correct Answer: B
- Explanation: The DS1302 is a Real-Time Clock (RTC) chip that maintains time and calendar information (seconds, minutes, hours, date, month, day, year).

### MCQ_122: Why does a Real-Time Clock module typically include a small button-cell battery?
- Topic: DS1302 Real-Time Clock
- Difficulty: Easy
  A. To run the Arduino board when the power goes out
  B. To keep the DS1302 chip running and maintaining time even when the main Arduino board is powered off
  C. To charge the main power capacitors
  D. To power the serial connection
- Correct Answer: B
- Explanation: The backup battery (such as a CR2032) powers the RTC chip in low-power standby mode when main system power is lost, preventing the clock from resetting.

### MCQ_123: What is the frequency of the external crystal oscillator required by the DS1302 RTC chip?
- Topic: DS1302 Real-Time Clock
- Difficulty: Easy
  A. 16 MHz
  B. 32.768 kHz
  C. 100 kHz
  D. 8 MHz
- Correct Answer: B
- Explanation: The DS1302 uses a standard watch crystal oscillator running at 32.768 kHz to maintain accurate time counting.

### MCQ_124: How many pins are on the DS1302 RTC DIP chip?
- Topic: DS1302 Real-Time Clock
- Difficulty: Easy
  A. 4 pins
  B. 8 pins
  C. 16 pins
  D. 28 pins
- Correct Answer: B
- Explanation: The DS1302 chip in a dual in-line package (DIP) has exactly 8 pins.

### MCQ_125: What are the three serial interface signals used to communicate with the DS1302?
- Topic: DS1302 Real-Time Clock
- Difficulty: Medium
  A. SDA, SCL, GND
  B. MOSI, MISO, SCK
  C. CE (or RST), I/O (or DAT), SCLK (or CLK)
  D. TX, RX, CTS
- Correct Answer: C
- Explanation: The DS1302 communicates via a 3-wire interface: CE (Chip Enable / Reset), I/O (Data Line), and SCLK (Serial Clock).

### MCQ_126: Up to what year does the DS1302 internal calendar compensate for leap years?
- Topic: DS1302 Real-Time Clock
- Difficulty: Medium
  A. 2050
  B. 2099
  C. 2100
  D. 3000
- Correct Answer: C
- Explanation: The DS1302 calendar is programmed to automatically handle leap years, including month day adjustments, valid up to the year 2100.

### MCQ_127: What is the purpose of the 'Clock Halt' (CH) bit in the DS1302 seconds register?
- Topic: DS1302 Real-Time Clock
- Difficulty: Medium
  A. To speed up the clock
  B. To stop the oscillator and place the chip in an ultra-low power state, typically used during shipping or storage
  C. To reset the date to 2000
  D. To enable write protection
- Correct Answer: B
- Explanation: The CH bit (bit 7 of register 0) stops the oscillator. When enabled, it stops the time-keeping function, saving battery power when the module is not in use.

### MCQ_128: How much auxiliary battery-backed SRAM is available on the DS1302 for user data storage?
- Topic: DS1302 Real-Time Clock
- Difficulty: Medium
  A. 31 bytes
  B. 64 bytes
  C. 1 KB
  D. 32 KB
- Correct Answer: A
- Explanation: The DS1302 contains 31 bytes of non-volatile RAM that can be used to store configuration data or status bytes.

### MCQ_129: What is the function of the Write Protect (WP) register in the DS1302?
- Topic: DS1302 Real-Time Clock
- Difficulty: Medium
  A. To prevent reading time data
  B. To prevent accidental writes to the clock/calendar registers or RAM
  C. To encrypt the date data
  D. To block external noise
- Correct Answer: B
- Explanation: When the write protect bit is set, data cannot be written to any clock/calendar registers or the RAM, preventing corruption from code glitches.

### MCQ_130: In the DS1302 library, which function is used to set the clock to a specific time?
- Topic: DS1302 Real-Time Clock
- Difficulty: Medium
  A. rtc.setTime(hour, minute, second)
  B. rtc.setClock(time)
  C. rtc.writeTime(h, m, s)
  D. rtc.adjust(hour, min, sec)
- Correct Answer: A
- Explanation: The standard library uses `rtc.setTime(hour, minute, second)` to set the current time.

### MCQ_131: Which argument is typically passed to rtc.setDOW() to set the day of the week to Friday?
- Topic: DS1302 Real-Time Clock
- Difficulty: Medium
  A. 5
  B. FRIDAY
  C. 6
  D. Friday
- Correct Answer: B
- Explanation: The library defines constants like FRIDAY, so `rtc.setDOW(FRIDAY)` is used.

### MCQ_132: What is the 'Trickle Charger' feature in the DS1302?
- Topic: DS1302 Real-Time Clock
- Difficulty: Hard
  A. A software algorithm to charge the Arduino
  B. A programmable hardware circuit inside the DS1302 that can charge a rechargeable battery or supercapacitor connected to VCC2
  C. A device that protects the crystal
  D. A booster for the serial bus
- Correct Answer: B
- Explanation: The trickle charge register allows the user to configure a internal diode and resistor circuit to safely charge a secondary rechargeable cell or supercapacitor from the primary supply.

### MCQ_133: What is the difference between Single-Byte Transfer and Burst Mode in DS1302?
- Topic: DS1302 Real-Time Clock
- Difficulty: Hard
  A. Single-Byte writes only to RAM, while Burst Mode writes to registers
  B. Single-Byte accesses one register at a time, while Burst Mode reads/writes all 8 clock registers sequentially in a single operation, preventing time-inconsistency errors
  C. Single-Byte is faster
  D. Burst Mode uses I2C
- Correct Answer: B
- Explanation: Burst Mode allows reading/writing all clock registers in a single transmission. This avoids 'time roll-over' errors, such as reading 11:59:59 and then 12:00:00 mid-read, which would yield a corrupt value of 11:59:00 or 12:59:59.

### MCQ_134: What is the difference between the VCC1 and VCC2 pins on the DS1302?
- Topic: DS1302 Real-Time Clock
- Difficulty: Hard
  A. VCC1 is for logic, VCC2 is for the motor
  B. VCC1 is the primary power supply input, and VCC2 is the backup battery connection pin
  C. VCC2 is the primary power supply input (usually 5V), and VCC1 is the backup power supply (usually 3V battery)
  D. VCC1 is positive, VCC2 is negative
- Correct Answer: C
- Explanation: VCC2 is the primary power pin (connected to system 5V), while VCC1 is the backup power input pin connected to the 3V backup battery.

### MCQ_135: What is the primary factor that causes quartz-crystal-based RTCs like the DS1302 to drift (lose or gain seconds over time)?
- Topic: DS1302 Real-Time Clock
- Difficulty: Hard
  A. Baud rate fluctuations
  B. Temperature variations affecting the crystal's resonant frequency
  C. Code execution speed in the loop() function
  D. Input voltage fluctuations on VCC2
- Correct Answer: B
- Explanation: Quartz crystals are sensitive to temperature. Changes in temperature cause small changes in the crystal's oscillation frequency, resulting in clock drift (often a few seconds per day).

### MCQ_136: Which communication interface is used by the Arduino to read and write data to an SD card?
- Topic: SD Cards & Data Logging
- Difficulty: Easy
  A. I2C interface
  B. SPI interface
  C. Standard RS232 Serial
  D. Analog interface
- Correct Answer: B
- Explanation: SD cards communicate with the microcontroller using the high-speed Serial Peripheral Interface (SPI) bus.

### MCQ_137: What are the standard hardware SPI pins on the Arduino UNO (MOSI, MISO, SCK)?
- Topic: SD Cards & Data Logging
- Difficulty: Easy
  A. Pins 2, 3, 4
  B. Pins 11 (MOSI), 12 (MISO), 13 (SCK)
  C. Pins A4, A5, pin 2
  D. Pins 0 (RX), 1 (TX), 10 (CS)
- Correct Answer: B
- Explanation: On the Arduino UNO, Pin 11 is MOSI, Pin 12 is MISO, and Pin 13 is SCK.

### MCQ_138: Which file system formats are compatible with the standard Arduino SD library?
- Topic: SD Cards & Data Logging
- Difficulty: Easy
  A. NTFS and ext4
  B. FAT16 and FAT32
  C. exFAT and APFS
  D. HFS+ and FAT8
- Correct Answer: B
- Explanation: The standard Arduino SD library only supports SD cards formatted with the FAT16 or FAT32 file systems.

### MCQ_139: What pin on the SD card shield is commonly used as the Chip Select (CS) line, and is passed to SD.begin()?
- Topic: SD Cards & Data Logging
- Difficulty: Easy
  A. Pin 0
  B. Pin 4 or Pin 10
  C. Pin A0
  D. Pin 13
- Correct Answer: B
- Explanation: Pin 4 (on Ethernet/SD shields) or Pin 10 (standard hardware SS pin) are commonly used as the Chip Select pin.

### MCQ_140: Which constant is passed as the second argument to SD.open() to open a file for appending data?
- Topic: SD Cards & Data Logging
- Difficulty: Medium
  A. FILE_READ
  B. FILE_WRITE
  C. FILE_APPEND
  D. FILE_CREATE
- Correct Answer: B
- Explanation: The SD library uses the constant `FILE_WRITE` to open a file for both reading and writing, positioning the file pointer at the end of the file (appending data).

### MCQ_141: What does the file extension '.csv' stand for?
- Topic: SD Cards & Data Logging
- Difficulty: Medium
  A. Command Saved Values
  B. Comma-Separated Values
  C. Computer System Variables
  D. Control Serial Values
- Correct Answer: B
- Explanation: CSV stands for Comma-Separated Values, a simple text format used to store tabular data.

### MCQ_142: Which code snippet correctly checks if the SD card has initialized successfully?
- Topic: SD Cards & Data Logging
- Difficulty: Medium
  A. if (SD.begin(chipSelect))
  B. if (SD.cardState() == 1)
  C. if (SD.open('datalog.txt'))
  D. if (SD.connected())
- Correct Answer: A
- Explanation: The SD.begin(chipSelect) function returns a boolean: true if initialization succeeded, and false if it failed.

### MCQ_143: Why is it critical to call dataFile.close() after writing data to the SD card?
- Topic: SD Cards & Data Logging
- Difficulty: Medium
  A. To clear the RAM variables
  B. To ensure all buffered data is physically written to the card and to close the file handle safely, preventing data corruption
  C. To disconnect the SPI bus
  D. To power down the SD card
- Correct Answer: B
- Explanation: Writing to SD card is buffered. Calling close() flushes any remaining data from the buffer to the card and updates the directory structure, ensuring no data is lost.

### MCQ_144: Which function is used in the SD library to check if a file already exists on the card?
- Topic: SD Cards & Data Logging
- Difficulty: Medium
  A. SD.exists(filename)
  B. SD.find(filename)
  C. SD.check(filename)
  D. SD.open(filename, FILE_CHECK)
- Correct Answer: A
- Explanation: SD.exists(filename) returns true if the specified file exists on the card, otherwise false.

### MCQ_145: How do you delete a file from the SD card using the SD library?
- Topic: SD Cards & Data Logging
- Difficulty: Medium
  A. SD.delete(filename)
  B. SD.remove(filename)
  C. SD.erase(filename)
  D. SD.clear(filename)
- Correct Answer: B
- Explanation: The function `SD.remove(filename)` is used to delete a file from the SD card.

### MCQ_146: What is the difference between dataFile.write() and dataFile.print() in the SD library?
- Topic: SD Cards & Data Logging
- Difficulty: Medium
  A. write() writes binary data, while print() writes readable ASCII text characters
  B. print() only writes to the console, not the file
  C. write() is slower
  D. They are identical in function
- Correct Answer: A
- Explanation: dataFile.write() writes raw bytes directly, while dataFile.print() converts values to human-readable text characters before writing.

### MCQ_147: Standard SD cards operate at 3.3V. Why is a level shifter chip (like the 74LVC125A) required on a 5V Arduino UNO SD card shield?
- Topic: SD Cards & Data Logging
- Difficulty: Hard
  A. To step up the 3.3V SD card signals to 5V
  B. To step down the 5V SPI signals from the Arduino (MOSI, SCK, CS) to the 3.3V logic level required by the SD card to prevent damaging it
  C. To increase the SPI transfer speed
  D. To convert SPI to I2C
- Correct Answer: B
- Explanation: SD cards will be damaged if they receive 5V signals on their input pins. A level shifter converts the 5V logic signals from the Arduino to 3.3V logic signals for the SD card.

### MCQ_148: In SPI communication, what is the role of the MISO line and when does it enter a high-impedance state?
- Topic: SD Cards & Data Logging
- Difficulty: Hard
  A. Master In Slave Out; it is high-impedance when the Chip Select (CS) line is HIGH (device is deselected) to allow other SPI devices to use the line
  B. Master In Slave Out; it is high-impedance during writes
  C. Master Out Slave In; high-impedance when active
  D. Master Out Slave In; high-impedance when clock is high
- Correct Answer: A
- Explanation: MISO (Master In Slave Out) is the line used by the slave to send data to the master. When the device's Chip Select (CS) pin is high (inactive), it must put its MISO pin in a high-impedance (tri-state) state so it doesn't interfere with other slaves sharing the bus.

### MCQ_149: What file naming constraint does the standard Arduino SD library enforce?
- Topic: SD Cards & Data Logging
- Difficulty: Hard
  A. Names can be up to 255 characters long
  B. 8.3 filename format (maximum of 8 characters for the name, a dot, and a 3-character extension)
  C. No extensions allowed
  D. Names must be in all-lowercase
- Correct Answer: B
- Explanation: The standard SD library only supports the short 8.3 filename format (e.g., 'datalog.csv'). Long filenames are not supported.

### MCQ_150: If a datalogger writes data every 10 seconds, but you do not want to close and reopen the file each time, which function can you call to force-write buffered data to the SD card?
- Topic: SD Cards & Data Logging
- Difficulty: Hard
  A. dataFile.flush()
  B. dataFile.sync()
  C. dataFile.save()
  D. dataFile.update()
- Correct Answer: A
- Explanation: The flush() function writes any buffered data to the SD card immediately, updating the file size and directory without closing the file, ensuring data safety in case of power failure.

## Section B: True / False Questions

### TF_001: The Arduino project was originally created at the Interaction Design Institute Ivrea in Italy.
- Topic: Introduction to Arduino & Hardware
- Difficulty: Easy
- Correct Answer: True
- Explanation: The Arduino project was developed in Ivrea, Italy, in 2005.

### TF_002: The Arduino UNO R3 operates natively at a logic level of 3.3V.
- Topic: Introduction to Arduino & Hardware
- Difficulty: Easy
- Correct Answer: False
- Explanation: The Arduino UNO R3 operates natively at a logic level of 5.0V.

### TF_003: The ATmega328P microcontroller on the Arduino UNO features 1 KB of EEPROM memory.
- Topic: Introduction to Arduino & Hardware
- Difficulty: Medium
- Correct Answer: True
- Explanation: The ATmega328P has 32 KB Flash, 2 KB SRAM, and 1 KB EEPROM.

### TF_004: The bootloader program must run continuously in the background while the user's sketch is running on the Arduino.
- Topic: Introduction to Arduino & Hardware
- Difficulty: Medium
- Correct Answer: False
- Explanation: The bootloader only runs at startup to check for uploads; it hands control over to the user's sketch once execution begins.

### TF_005: The Arduino Leonardo board has native USB support because it utilizes the ATmega32U4 microcontroller instead of a separate USB-to-serial chip.
- Topic: Introduction to Arduino & Hardware
- Difficulty: Medium
- Correct Answer: True
- Explanation: The ATmega32U4 has an on-chip USB interface, unlike the ATmega328P which requires a separate chip like the ATmega16U2.

### TF_006: A single digital I/O pin on the Arduino UNO can safely source or sink up to 100 mA of current continuously.
- Topic: Introduction to Arduino & Hardware
- Difficulty: Hard
- Correct Answer: False
- Explanation: The absolute maximum limit per I/O pin is 40 mA, with 20 mA being the recommended safe operating limit.

### TF_007: The setup() function in an Arduino sketch runs exactly once when the board is powered on or reset.
- Topic: Arduino C Programming Basics
- Difficulty: Easy
- Correct Answer: True
- Explanation: The setup() function is called only once at startup for initialization.

### TF_008: In Arduino C, comments starting with '//' are compiled into machine code and executed by the microcontroller.
- Topic: Arduino C Programming Basics
- Difficulty: Easy
- Correct Answer: False
- Explanation: Comments are ignored by the compiler; they are only for human readers.

### TF_009: An 'int' variable in Arduino C on an Arduino UNO uses 2 bytes (16 bits) of memory.
- Topic: Arduino C Programming Basics
- Difficulty: Medium
- Correct Answer: True
- Explanation: On 8-bit AVR boards like the Arduino UNO, 'int' is 16-bit. On 32-bit boards (like Due/ESP32), it is 32-bit.

### TF_010: The assignment operator in C is written as '=='.
- Topic: Arduino C Programming Basics
- Difficulty: Medium
- Correct Answer: False
- Explanation: The assignment operator is a single '='. The double '==' is the comparison operator for equality.

### TF_011: The modulo operator (%) calculates the remainder of an integer division.
- Topic: Arduino C Programming Basics
- Difficulty: Medium
- Correct Answer: True
- Explanation: For example, 7 % 3 evaluates to 1, since 7 divided by 3 leaves a remainder of 1.

### TF_012: A local variable declared inside the loop() function can be accessed directly by setup().
- Topic: Arduino C Programming Basics
- Difficulty: Hard
- Correct Answer: False
- Explanation: Local variables are restricted to the block/function in which they are declared and cannot be accessed externally.

### TF_013: The pinMode() function must be called in setup() to configure a digital pin as an INPUT or OUTPUT before using it.
- Topic: Basic I/O Components
- Difficulty: Easy
- Correct Answer: True
- Explanation: pinMode() sets the electrical state of the pin to act as input or output.

### TF_014: In an active-low push button configuration with an external pull-up resistor, the input pin reads HIGH when the button is pressed.
- Topic: Basic I/O Components
- Difficulty: Easy
- Correct Answer: False
- Explanation: When pressed, the button connects the pin to GND, resulting in a LOW reading.

### TF_015: A flyback diode is connected across a relay's control coil to suppress high-voltage inductive spikes when the coil is turned off.
- Topic: Basic I/O Components
- Difficulty: Medium
- Correct Answer: True
- Explanation: The diode dissipates the inductive kickback spike safely, protecting the driver transistor/microcontroller.

### TF_016: The tone() function can only be used on pins that support PWM (marked with ~).
- Topic: Basic I/O Components
- Difficulty: Medium
- Correct Answer: False
- Explanation: The tone() function can generate a square wave on any digital pin, not just PWM pins.

### TF_017: An Arduino digital pin can output enough current to directly power a standard 5V or 12V electromagnetic relay coil without a transistor driver.
- Topic: Basic I/O Components
- Difficulty: Hard
- Correct Answer: False
- Explanation: Standard relays require 70-100mA or more, which exceeds the Arduino pin's 40mA max limit. A transistor driver is required.

### TF_018: When an Arduino output pin drives a transistor to activate a relay coil, the flyback diode is forward-biased under normal operation.
- Topic: Basic I/O Components
- Difficulty: Hard
- Correct Answer: False
- Explanation: The diode is reverse-biased during normal operation. It only becomes forward-biased to suppress the voltage spike when the coil is deactivated.

### TF_019: An LCD 1602 display fitted with an I2C serial backpack requires only 4 connections to the Arduino UNO.
- Topic: Character LCD & I2C Interface
- Difficulty: Easy
- Correct Answer: True
- Explanation: The connections are VCC, GND, SDA, and SCL.

### TF_020: The default SDA and SCL pins on the Arduino UNO board are pins A0 and A1.
- Topic: Character LCD & I2C Interface
- Difficulty: Easy
- Correct Answer: False
- Explanation: The I2C pins are A4 (SDA) and A5 (SCL).

### TF_021: The most common default I2C address for an LCD 1602 I2C backpack module is 0x27.
- Topic: Character LCD & I2C Interface
- Difficulty: Medium
- Correct Answer: True
- Explanation: Most PCF8574-based I2C backpacks use 0x27 as their default address.

### TF_022: The first character on the second line of a 16x2 character LCD is located at coordinates (0, 0).
- Topic: Character LCD & I2C Interface
- Difficulty: Medium
- Correct Answer: False
- Explanation: The first character on the second line is at column 0, row 1 (0, 1) because rows are 0-indexed.

### TF_023: The blue potentiometer located on the back of the I2C LCD backpack is used to adjust the backlight brightness of the screen.
- Topic: Character LCD & I2C Interface
- Difficulty: Medium
- Correct Answer: False
- Explanation: It adjusts the contrast of the characters, not the backlight brightness (which is controlled by software or a jumper).

### TF_024: The LiquidCrystal_I2C library constructor requires the user to specify the SDA and SCL pin numbers.
- Topic: Character LCD & I2C Interface
- Difficulty: Hard
- Correct Answer: False
- Explanation: The constructor takes the I2C address, column count, and row count. The Wire library automatically handles the hardware SDA/SCL pins.

### TF_025: LDR stands for Light Dependent Resistor.
- Topic: LDR Light Sensors
- Difficulty: Easy
- Correct Answer: True
- Explanation: LDR is the common name for a light-sensitive resistor.

### TF_026: The electrical resistance of an LDR increases when exposed to brighter light.
- Topic: LDR Light Sensors
- Difficulty: Easy
- Correct Answer: False
- Explanation: The resistance decreases in bright light and increases in darkness.

### TF_027: Arduino UNO analog input pins measure continuous voltage levels from 0V to 5V.
- Topic: LDR Light Sensors
- Difficulty: Medium
- Correct Answer: True
- Explanation: The ADC converts this voltage range to a digital value from 0 to 1023.

### TF_028: The analogRead() function on the Arduino UNO returns a value from 0 to 255.
- Topic: LDR Light Sensors
- Difficulty: Medium
- Correct Answer: False
- Explanation: analogRead() returns a 10-bit value from 0 to 1023. digitalRead() returns 0 or 1.

### TF_029: A voltage divider circuit is necessary to convert an LDR's resistance changes into voltage changes that the Arduino can measure.
- Topic: LDR Light Sensors
- Difficulty: Medium
- Correct Answer: True
- Explanation: The Arduino ADC can only measure voltage, so a fixed resistor is paired with the LDR to form a voltage divider.

### TF_030: Changing the analog reference voltage to INTERNAL (1.1V) decreases the resolution of analog inputs on the Arduino UNO.
- Topic: LDR Light Sensors
- Difficulty: Hard
- Correct Answer: False
- Explanation: It increases the resolution for small signals because the 1024 steps are mapped to 0-1.1V (~1.07mV per step) instead of 0-5V (~4.88mV per step).

### TF_031: PIR stands for Passive Infrared.
- Topic: PIR Motion Sensors
- Difficulty: Easy
- Correct Answer: True
- Explanation: PIR stands for Passive Infrared.

### TF_032: PIR sensors actively emit infrared rays to detect objects in their path.
- Topic: PIR Motion Sensors
- Difficulty: Easy
- Correct Answer: False
- Explanation: PIR sensors are passive; they do not emit any radiation. They only detect infrared radiation emitted or reflected by other objects.

### TF_033: The two potentiometers on a PIR sensor module adjust the sensitivity (detection range) and the output delay time.
- Topic: PIR Motion Sensors
- Difficulty: Medium
- Correct Answer: True
- Explanation: One pot adjusts the sensitivity/range, and the other adjusts the delay time (how long output stays HIGH).

### TF_034: A PIR sensor outputs a continuous analog signal representing the distance of the moving object.
- Topic: PIR Motion Sensors
- Difficulty: Medium
- Correct Answer: False
- Explanation: A PIR sensor outputs a digital signal (HIGH when motion is detected, LOW when idle). It does not measure distance.

### TF_035: The white plastic dome on a PIR sensor is a Fresnel lens.
- Topic: PIR Motion Sensors
- Difficulty: Medium
- Correct Answer: True
- Explanation: The Fresnel lens focuses infrared light onto the pyroelectric sensor elements.

### TF_036: On the Arduino UNO, a 3.3V digital input signal from a PIR sensor will damage the 5V digital pin.
- Topic: PIR Motion Sensors
- Difficulty: Hard
- Correct Answer: False
- Explanation: A 3.3V input is completely safe for a 5V Arduino digital pin, and is recognized as a valid digital HIGH (since 3.3V > 3.0V minimum HIGH threshold).

### TF_037: The DHT11 sensor measures both temperature and humidity.
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Easy
- Correct Answer: True
- Explanation: The DHT11 is a composite sensor that reads relative humidity and temperature.

### TF_038: The DHT11 sensor communicates using the standard I2C communication protocol.
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Easy
- Correct Answer: False
- Explanation: The DHT11 uses a custom single-wire serial protocol, not I2C.

### TF_039: The DHT11 transmits a total of 40 bits (5 bytes) of data in one complete readout.
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Medium
- Correct Answer: True
- Explanation: The 40 bits contain 16-bit humidity, 16-bit temperature, and an 8-bit checksum.

### TF_040: The DHT11 sensor can be sampled reliably every 100 milliseconds.
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Medium
- Correct Answer: False
- Explanation: The DHT11 has a slow response time and should be read at most once every 2 seconds (0.5 Hz).

### TF_041: The DHT11 checksum is calculated by adding the first 4 bytes of data together.
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Medium
- Correct Answer: True
- Explanation: The checksum is the sum of: Integral RH + Decimal RH + Integral T + Decimal T.

### TF_042: In the DHT11 protocol, a bit '1' is represented by a 50us low time followed by a 26-28us high time.
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Hard
- Correct Answer: False
- Explanation: A bit '1' has a high time of 70us. A bit '0' has a high time of 26-28us.

### TF_043: The LM35 temperature sensor outputs a voltage of 10 mV per degree Celsius.
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Easy
- Correct Answer: True
- Explanation: The LM35 has a linear sensitivity of 10mV/*C.

### TF_044: The HIH4030 is a digital humidity sensor.
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Easy
- Correct Answer: False
- Explanation: The HIH4030 is an analog humidity sensor that outputs a voltage proportional to relative humidity.

### TF_045: The LM35 outputs voltage linearly with temperature.
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Medium
- Correct Answer: True
- Explanation: The LM35 is an IC sensor that provides a highly linear output voltage directly proportional to Celsius.

### TF_046: The formula for relative humidity at 25 *C using the HIH4030 is %RH = (Voltage - 0.0307) / 0.958.
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Medium
- Correct Answer: False
- Explanation: The correct formula is %RH = (Voltage - 0.958) / 0.0307.

### TF_047: Temperature compensation is necessary for accurate relative humidity measurements using the HIH4030 sensor.
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Medium
- Correct Answer: True
- Explanation: Relative humidity measurements are temperature-dependent, so temperature compensation increases accuracy.

### TF_048: The LM35 can measure negative temperatures directly without an external pull-down resistor or negative voltage supply.
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Hard
- Correct Answer: False
- Explanation: Measuring negative temperatures requires a negative voltage supply connected to the OUT pin via a resistor.

### TF_049: The DS1302 is a Real-Time Clock (RTC) chip.
- Topic: DS1302 Real-Time Clock
- Difficulty: Easy
- Correct Answer: True
- Explanation: The DS1302 is a dedicated RTC chip for keeping time.

### TF_050: The DS1302 requires a 16 MHz crystal oscillator to keep time.
- Topic: DS1302 Real-Time Clock
- Difficulty: Easy
- Correct Answer: False
- Explanation: The DS1302 requires a 32.768 kHz watch crystal oscillator.

### TF_051: The DS1302 has a 3-wire serial interface (CE, I/O, SCLK).
- Topic: DS1302 Real-Time Clock
- Difficulty: Medium
- Correct Answer: True
- Explanation: Communication with the DS1302 is done via the Chip Enable, Data Input/Output, and Serial Clock lines.

### TF_052: The DS1302 calendar does not support leap years and must be manually adjusted every four years.
- Topic: DS1302 Real-Time Clock
- Difficulty: Medium
- Correct Answer: False
- Explanation: The DS1302 has built-in leap year compensation valid up to the year 2100.

### TF_053: The backup battery keeps the RTC running when main power to the Arduino is disconnected.
- Topic: DS1302 Real-Time Clock
- Difficulty: Medium
- Correct Answer: True
- Explanation: The backup battery provides power to the RTC chip so it does not lose time when power is off.

### TF_054: The DS1302 Write Protect (WP) bit prevents the Arduino from reading the date/time data.
- Topic: DS1302 Real-Time Clock
- Difficulty: Hard
- Correct Answer: False
- Explanation: The Write Protect bit prevents writing/modifying the clock data. It does not block reading.

### TF_055: SD cards require formatting to FAT16 or FAT32 for the standard Arduino SD library.
- Topic: SD Cards & Data Logging
- Difficulty: Easy
- Correct Answer: True
- Explanation: The standard SD library only supports FAT16/FAT32 file systems.

### TF_056: The standard SD library supports long filenames up to 255 characters.
- Topic: SD Cards & Data Logging
- Difficulty: Easy
- Correct Answer: False
- Explanation: The standard SD library only supports short 8.3 filenames (e.g. 8 chars name, 3 chars extension).

### TF_057: MOSI stands for Master Out Slave In.
- Topic: SD Cards & Data Logging
- Difficulty: Medium
- Correct Answer: True
- Explanation: MOSI is the line carrying data from the master (Arduino) to the slave (SD card).

### TF_058: When Chip Select (CS) is HIGH, the SD card's MISO pin must remain active to drive the line.
- Topic: SD Cards & Data Logging
- Difficulty: Medium
- Correct Answer: False
- Explanation: When CS is HIGH (deselected), the MISO pin must be in high-impedance state to let other devices use the bus.

### TF_059: FILE_WRITE mode opens a file for writing and appends new data to the end of the file.
- Topic: SD Cards & Data Logging
- Difficulty: Medium
- Correct Answer: True
- Explanation: FILE_WRITE opens the file, creates it if missing, and places the cursor at the end to append data.

### TF_060: An SD card operating at 3.3V can receive 5V signals directly from the Arduino without a level shifter.
- Topic: SD Cards & Data Logging
- Difficulty: Hard
- Correct Answer: False
- Explanation: An SD card requires 3.3V logic levels. Sending 5V logic signals directly will damage the SD card.

## Section C: Scenario-Based Questions

### SCENARIO_001: You are designing a smart jacket that tracks movement and has built-in LEDs. The design requires the electronics to be sewn directly into fabric.
**Question:** Which official Arduino board is best suited for this application?
  A. Arduino UNO R3
  B. Arduino Mega 2560
  C. LilyPad Arduino
  D. Arduino Due
- Correct Answer: C
- Explanation: The LilyPad Arduino is designed specifically for wearables and e-textiles, featuring large sewable pads and a low profile.

### SCENARIO_002: Your client wants a smart home automation system that requires controlling 40 digital relay channels and reading 10 analog sensors simultaneously.
**Question:** Which Arduino board would support this number of direct I/O pins without external multiplexers?
  A. Arduino Nano
  B. Arduino UNO R3
  C. Arduino Leonardo
  D. Arduino Mega 2560 R3
- Correct Answer: D
- Explanation: The Arduino Mega 2560 R3 has 54 digital I/O pins and 16 analog inputs, making it ideal for projects with high I/O counts.

### SCENARIO_003: An engineer powers an Arduino UNO using a 24V industrial DC power supply connected to the DC barrel jack. After 5 minutes, the Arduino stops working and the power regulator chip is extremely hot to the touch.
**Question:** What caused the failure, and how should it be resolved?
  A. The USB port failed; connect a different USB cable
  B. The input voltage exceeded limits, causing the regulator to overheat; step down the input voltage to 7-12V
  C. The bootloader crashed; re-flash the chip
  D. The input current was too low; increase current limits
- Correct Answer: B
- Explanation: The recommended input voltage for the DC jack is 7-12V. Running at 24V forces the linear regulator to drop 19V, generating excess heat and triggering thermal shutdown or damage.

### SCENARIO_004: You need to build a custom gamepad that sends standard keyboard keystrokes to a PC over a USB cable.
**Question:** Which board should you choose and why: Arduino UNO or Arduino Leonardo?
  A. Arduino UNO, because it has more memory
  B. Arduino Leonardo, because its ATmega32U4 has a built-in USB transceiver to emulate keyboard inputs natively
  C. Arduino UNO, because it runs at a higher clock speed
  D. Arduino Leonardo, because it operates at 3.3V
- Correct Answer: B
- Explanation: The Leonardo uses ATmega32U4 which natively supports USB HID protocols. The UNO uses ATmega328P which cannot emulate USB devices natively without complex firmware modifications to the secondary USB-to-serial chip.

### SCENARIO_005: Your battery-powered Arduino UNO project reads a light sensor. When the battery drains from 9V to 6.5V, the light sensor readings start fluctuating and drift upward, even though the ambient light remains constant.
**Question:** Why are the readings changing with battery voltage?
  A. The LDR sensor burned out from low voltage
  B. The 5V voltage regulator began to sag below 5V, lowering the ADC's default reference voltage and causing readings to report artificially high
  C. The clock speed of the Arduino slowed down
  D. The SD card interface drew too much power
- Correct Answer: B
- Explanation: The ADC reference voltage defaults to VCC (5V). If VCC sags because the input voltage is too low, the step size of the ADC decreases, causing analog readings to report artificially high values.

### SCENARIO_006: A student connects a 12V high-power solenoid directly to digital pin 9 of the Arduino UNO. When the pin is set to HIGH, the solenoid clicks briefly, the Arduino resets, and pin 9 no longer works.
**Question:** Explain what happened electrically and how to prevent it.
  A. Solenoids require AC voltage; use a transformer
  B. The solenoid drew far more current than the pin's 40mA absolute maximum limit, damaging the pin; use a transistor switch to isolate it
  C. The code had a compilation error; re-upload the sketch
  D. The pin was set to INPUT mode; set it to OUTPUT
- Correct Answer: B
- Explanation: Solenoids are low resistance inductive loads that draw high currents. The Arduino digital pin can only supply up to 40mA. Direct connection overloads the pin, causing voltage sag (reset) and silicon junction burnout. Use a transistor driver.

### SCENARIO_007: You write a program and click 'Verify' in the Arduino IDE. The compiler highlights a line inside loop() and displays: 'expected ';' before '}' token'.
**Question:** What is the error and how do you fix it?
  A. Add a colon at the end of the line
  B. A semicolon is missing at the end of the statement immediately preceding the highlighted line; add a ';'
  C. Change setup() to loop()
  D. Delete the closing curly brace
- Correct Answer: B
- Explanation: In C, every statement must end with a semicolon. The compiler detects the missing semicolon when it encounters the closing curly brace.

### SCENARIO_008: In your sketch, you declare 'int speed = 100;' inside the setup() function. Inside the loop() function, you write 'analogWrite(9, speed);'. The compiler fails with 'speed was not declared in this scope'.
**Question:** Why did the compilation fail?
  A. The variable speed is a keyword in C
  B. The variable 'speed' was declared locally inside setup() and is not visible in loop(); declare it as global
  C. Pin 9 does not support PWM
  D. The setup() function did not run
- Correct Answer: B
- Explanation: Local variables are only accessible within the function they are defined. Global variables are accessible throughout the entire file.

### SCENARIO_009: A programmer uses 'int count = 32000;' on an Arduino UNO. The code increments 'count' by 1000. When printed to the serial monitor, the value displays as '-32536' instead of '33000'.
**Question:** Explain what happened and how to fix it.
  A. The variable overflowed the 16-bit signed integer limit of 32,767; change the type to 'unsigned int' or 'long'
  B. The print function failed; use Serial.write
  C. The crystal resonator is inaccurate
  D. SRAM memory was full
- Correct Answer: A
- Explanation: A signed 16-bit integer ranges from -32,768 to 32,767. When 32,000 + 1,000 exceeds 32,767, it wraps around to the negative range. A 'long' (32-bit) can store up to 2 billion.

### SCENARIO_010: You are calculating exact sensor averages. You write 'float average = 5 / 2;'. However, when you print 'average' to the Serial Monitor, it displays '2.00' instead of '2.50'.
**Question:** Why is the decimal part lost, and how do you correct the code?
  A. The average variable should be type int
  B. Integer division discards the remainder before assignment; write 'float average = 5.0 / 2.0;'
  C. The serial monitor does not print decimals
  D. The map() function should be used
- Correct Answer: B
- Explanation: In C, dividing two integers results in an integer. Casting or using float literals (e.g. 5.0) forces the compiler to perform floating-point math.

### SCENARIO_011: You write 'int val = analogRead(A0); while(val > 500) { delay(10); }' to wait until a sensor value drops. However, when the sensor value drops below 500, the program remains stuck in the loop forever.
**Question:** What causes this loop to become infinite?
  A. The A0 pin is disconnected
  B. The loop condition variable 'val' is never updated inside the loop body; read the sensor inside the loop
  C. The delay function blocks the ADC
  D. The bootloader crashed
- Correct Answer: B
- Explanation: If the variable in the loop condition is not updated within the loop body, the condition remains true forever, causing an infinite loop. The sensor must be read inside the loop: 'val = analogRead(A0);'

### SCENARIO_012: You write an expression: 'int result = 10 + 5 * 2;'. You expected the result to be 30 (adding 10 and 5, then multiplying by 2), but the variable prints as 20.
**Question:** Explain the reason and how to fix it.
  A. Multiplication has higher precedence than addition; use parentheses: '(10 + 5) * 2'
  B. The operator * is not supported; use multiplication function
  C. The variable type must be float
  D. SRAM memory was full
- Correct Answer: A
- Explanation: In C, multiplication and division have higher precedence than addition and subtraction. Parentheses are used to override default operator precedence.

### SCENARIO_013: A student connects a push button between digital pin 2 and 5V. When the button is NOT pressed, digitalRead(2) randomly alternates between HIGH and LOW, causing erratic behavior.
**Question:** What is causing this, and how do you fix it?
  A. The button is broken; replace it
  B. The input pin is floating when the button is open; enable internal pull-up or add a pull-down resistor
  C. The pin operates at 3.3V
  D. The tone() function interferes
- Correct Answer: B
- Explanation: Without a pull-up or pull-down resistor, a CMOS digital input has extremely high impedance and picks up electrostatic noise, causing random readings. Resistor forces a default state.

### SCENARIO_014: You connect a piezo buzzer to pin 8 and write 'digitalWrite(8, HIGH); delay(500); digitalWrite(8, LOW);'. Instead of a clean tone, the buzzer just makes a single 'click' sound.
**Question:** Why did the buzzer not make a tone, and how do you fix it?
  A. The buzzer is dead
  B. digitalWrite() only applies static DC voltage; use tone(8, 1000) to generate an oscillating square wave
  C. Buzzer requires analog pin
  D. PWM is disabled on pin 8
- Correct Answer: B
- Explanation: A buzzer requires an oscillating AC signal to vibrate the piezo element at an audible frequency. tone() generates a square wave of the desired frequency.

### SCENARIO_015: Every time the Arduino activates a 5V relay coil connected to an output pin (via a transistor), the Arduino UNO resets or disconnects from the computer's USB port.
**Question:** What is the electrical cause of this reset?
  A. The relay coil voltage is too low
  B. The relay coil current surge causes a VCC rail voltage dip below brownout threshold; power it from external supply
  C. The bootloader has crashed
  D. The flyback diode is shorting
- Correct Answer: B
- Explanation: A USB port can supply 500mA. If the relay coil draws high current, the current surge can drop the VCC rail voltage below the microcontroller's brownout threshold, resetting the chip.

### SCENARIO_016: You build a relay control circuit on a breadboard. It works fine for three switches, but on the fourth switch, the driver transistor burns out and stops functioning. You notice you forgot to connect the diode across the relay coil.
**Question:** Explain why the transistor failed.
  A. The transistor base resistor was too low
  B. The high-voltage inductive spike (flyback voltage) from de-energizing the coil destroyed the transistor; add a flyback diode
  C. The relay coil drew too much voltage
  D. The ground connection was lost
- Correct Answer: B
- Explanation: When current to an inductor is cut off, the magnetic field collapses and generates a large reverse-voltage spike (V = L * di/dt) that easily destroys transistors. A diode suppresses it.

### SCENARIO_017: You are designing a heating system. If the Arduino fails or loses power, the heater must turn OFF immediately for safety.
**Question:** Should you connect the heater control circuit to the Normally Open (NO) or Normally Closed (NC) contacts of the relay?
  A. Normally Closed (NC) contact
  B. Normally Open (NO) contact
  C. VCC contact
  D. Ground contact
- Correct Answer: B
- Explanation: NO contact ensures the heater is disconnected when the relay coil is unpowered. NC would turn the heater ON if the Arduino loses power, creating a safety hazard.

### SCENARIO_018: You wire a push button using 'pinMode(2, INPUT_PULLUP);' and connect the button between pin 2 and GND.
**Question:** Write the conditional code block that executes a function 'activateDevice()' only when the button is actively pressed.
  A. if (digitalRead(2) == HIGH) { activateDevice(); }
  B. if (digitalRead(2) == LOW) { activateDevice(); }
  C. if (analogRead(2) == 0) { activateDevice(); }
  D. if (digitalRead(2) == 2) { activateDevice(); }
- Correct Answer: B
- Explanation: Using INPUT_PULLUP pulls the pin HIGH when idle. Pressing the button pulls it to GND, so a LOW reading indicates the button is pressed.

### SCENARIO_019: You power on your project with an I2C LCD. The screen backlight lights up, but it only displays a row of solid white blocks on the first line, and no text.
**Question:** What is the most likely cause, and how do you fix it?
  A. The I2C address is wrong; upload new sketch
  B. The contrast is set too high; adjust the blue potentiometer on the back of the I2C backpack
  C. The LCD screen is broken; replace it
  D. The power lines are swapped
- Correct Answer: B
- Explanation: White blocks indicate the LCD is powered but the contrast is set too high or the controller has not initialized correctly. Potentiometer adjustment usually solves this.

### SCENARIO_020: Your code contains 'LiquidCrystal_I2C lcd(0x27, 16, 2);'. The code compiles and uploads successfully, but the LCD displays absolutely nothing. You run an I2C scanner sketch, and it reports a device found at '0x3F'.
**Question:** How do you fix this issue?
  A. Change the SDA wire to SCL
  B. Change the constructor address in your code from '0x27' to '0x3F': 'LiquidCrystal_I2C lcd(0x3F, 16, 2);'
  C. Connect the LCD to A0 and A1
  D. Set the digital pin 2 to HIGH
- Correct Answer: B
- Explanation: The library cannot communicate with the LCD if the I2C address in the code does not match the hardware address of the backpack chip.

### SCENARIO_021: You write a program to display a long message: 'lcd.print('Room Temperature Monitoring System');'. The screen only displays 'Room Temperature'.
**Question:** What is the issue and how do you display the full text?
  A. The LCD buffer overflowed; reset the board
  B. A 16x2 LCD is physically limited to 16 characters per line; split the string and set the cursor to print on the second line
  C. The text contains non-ASCII characters
  D. VCC voltage is too low
- Correct Answer: B
- Explanation: The display is physically limited to 16 columns. Writing beyond column 15 results in characters being clipped or wrapping in unexpected ways depending on the controller configuration.

### SCENARIO_022: A student puts 'lcd.clear(); lcd.print(temp); delay(100);' inside the loop() function. The temperature display on the LCD is very hard to read because it is flickering constantly.
**Question:** What is causing the flicker and how do you fix it?
  A. The delay time is too long; change to delay(1000)
  B. Repeatedly calling lcd.clear() in a fast loop clears screen memory frequently; overwrite specific coordinates instead of clearing
  C. The contrast potentiometer is loose
  D. The I2C bus is experiencing collisions
- Correct Answer: B
- Explanation: lcd.clear() takes several milliseconds to execute and clears the entire screen memory. Frequent calls lead to visible blanking/flicker. Overwriting specific positions is cleaner.

### SCENARIO_023: You connect SDA of the LCD to A5 and SCL to A4 on the Arduino UNO. The LCD does not display text and serial monitor shows I2C errors.
**Question:** What is the wiring mistake?
  A. The SCL should be connected to A0
  B. The SDA should be connected to A4, and SCL should be connected to A5
  C. The LCD requires digital pin 13
  D. The VCC and GND wires are swapped
- Correct Answer: B
- Explanation: SDA is serial data (A4 on UNO) and SCL is serial clock (A5 on UNO). Swapping them prevents clock synchronization and data transfer.

### SCENARIO_024: You want to display a custom degree symbol (*) on the LCD screen, but the standard character set does not have it.
**Question:** Explain how this can be achieved using the LiquidCrystal_I2C library.
  A. It is not possible to display custom symbols on 1602 LCD
  B. Define the custom character as an 8x5 byte array, register it in setup() using lcd.createChar(0, array), and print it in loop() using lcd.write(0)
  C. Change the I2C address of the backpack
  D. Use the standard print() function with degree symbol
- Correct Answer: B
- Explanation: Character LCDs have RAM (CGRAM) for up to 8 custom characters (0-7). The user defines the pixel grid as a byte array and uploads it to CGRAM.

### SCENARIO_025: An LDR is wired to A0. In the dark, analogRead(A0) returns 1023. In bright light, it still returns 1023.
**Question:** What is the most likely wiring error?
  A. The LDR resistance is too low
  B. The analog pin A0 is shorted directly to 5V, or the connection to the pull-down resistor/GND is broken
  C. The reference voltage is wrong
  D. The code did not run
- Correct Answer: B
- Explanation: If the analog pin reads a constant 1023 (5V), it means the pin is shorted to the 5V rail or lacks a connection to GND through the resistor divider.

### SCENARIO_026: Your automatic night light turns the light OFF when it gets dark, and ON when it gets bright. You want the opposite behavior.
**Question:** How can you fix this in code without changing the physical wiring?
  A. Swap the VCC and GND connections on LDR
  B. Reverse the conditional check from 'if (lightVal > threshold)' to 'if (lightVal < threshold)'
  C. Connect LDR to digital pin 2
  D. Use external pull-up resistor
- Correct Answer: B
- Explanation: Reversing the logic operator (greater than to less than) flips the behavior of the control loop.

### SCENARIO_027: An automatic street light project turns a relay ON when the LDR reading falls below 400. In the evening, when light is close to 400, the relay clicks on and off rapidly and repeatedly.
**Question:** What is this problem called, and how do you resolve it?
  A. Voltage drop; increase power supply
  B. Threshold jitter; implement hysteresis (turn ON below 380, OFF above 420) or use averaging filters
  C. Inductive spike; add flyback diode
  D. Pin floating; add pull-down resistor
- Correct Answer: B
- Explanation: Without hysteresis, minor noise fluctuations at the threshold cause the system to rapidly oscillate between states. Hysteresis adds a buffer zone.

### SCENARIO_028: Your LDR voltage divider yields values between 150 (very dark) and 900 (very bright). You want to display this on a scale of 0 to 100 percent.
**Question:** Write the line of code using map() to accomplish this.
  A. int lightPercent = map(analogRead(A0), 0, 1023, 0, 100);
  B. int lightPercent = map(analogRead(A0), 150, 900, 0, 100);
  C. int lightPercent = map(analogRead(A0), 900, 150, 100, 0);
  D. int lightPercent = map(analogRead(A0), 150, 100, 900, 0);
- Correct Answer: B
- Explanation: The map() function maps the input range [150, 900] to the output range [0, 100].

### SCENARIO_029: You are reading an LDR and a potentiometer in the same loop. The readings from the LDR seem to bleed into the potentiometer readings.
**Question:** What causes this analog channel crosstalk, and how do you fix it?
  A. The ADC resolution is too low; use external ADC
  B. The shared internal ADC capacitor does not have enough time to charge; take two consecutive analogRead() calls per channel and discard the first
  C. The pins are shorted on breadboard
  D. The delay() function is too short
- Correct Answer: B
- Explanation: The Arduino has one ADC shared among pins. When switching pins, residual charge in the sample-and-hold capacitor can affect the next reading. Discarding the first reading allows capacitor stabilization.

### SCENARIO_030: You deploy your light-tracking solar panel to a new room. The pre-programmed thresholds in the code no longer work because the room's ambient light is different.
**Question:** How can you make the code self-calibrating at startup?
  A. Use a 3.3V reference instead of 5V
  B. Run a 5-second calibration loop in setup() to record max and min ambient values and use these as limits in map() during loop()
  C. Soldering a different value resistor in series
  D. Increase clock frequency of the processor
- Correct Answer: B
- Explanation: Dynamic calibration during setup() measures the actual light levels in the environment, adjusting the mapping range programmatically.

### SCENARIO_031: You power up a PIR sensor security system. The LED connected to the alarm pin is continuously HIGH, even when the room is empty and there is no motion.
**Question:** What physical adjustment or state should you check first?
  A. Check if VCC is connected to A0
  B. Check if the delay time potentiometer is turned to maximum or wait for calibration warm-up (10-60s) to finish
  C. Swap the VCC and GND wires
  D. Decrease the serial baud rate
- Correct Answer: B
- Explanation: The PIR output stays HIGH for a duration set by the delay pot. If set to maximum, it stays HIGH for up to 5 minutes, appearing 'always on' if motion occurred during setup.

### SCENARIO_032: A PIR sensor is installed in an office near an air conditioning vent. The alarm triggers randomly during the night when the building is empty.
**Question:** What is causing these false alarms, and how do you resolve it?
  A. The A/C electrical noise; add decoupling capacitor
  B. Air conditioner drafts cause rapid infrared changes; relocate the sensor away from vents and direct sunlight
  C. The sensor is low on current; use battery
  D. The room is too dark; turn on background LED
- Correct Answer: B
- Explanation: PIR sensors detect changes in infrared radiation (heat). Fast-moving drafts of air can shift the thermal balance of the pyroelectric elements, triggering false alarms.

### SCENARIO_033: You want an alarm LED to stay ON for exactly 10 seconds after a PIR sensor detects motion, using the delay() function.
**Question:** Write the loop code to read the PIR on pin 7 and control the LED on pin 13.
  A. if(digitalRead(7)==HIGH){digitalWrite(13,HIGH);delay(10);digitalWrite(13,LOW);}
  B. if(digitalRead(7)==HIGH){digitalWrite(13,HIGH);delay(10000);digitalWrite(13,LOW);}
  C. if(analogRead(7)>500){digitalWrite(13,HIGH);delay(10000);}
  D. if(digitalRead(7)==LOW){digitalWrite(13,HIGH);delay(10000);}
- Correct Answer: B
- Explanation: When pin 7 goes HIGH, pin 13 is set HIGH, and the code blocks for 10 seconds (10,000ms) before turning the LED off.

### SCENARIO_034: You want to detect motion using a PIR sensor, but you cannot use delay() because the Arduino must also monitor a push button continuously.
**Question:** How can you implement the PIR alarm timing without blocking code execution?
  A. Use tone() function to blink the LED
  B. Use millis() to record trigger timestamp, turn LED on, and check if 'millis() - motionTime >= 10000' in loop to turn it off
  C. Run the loop at a faster baud rate
  D. Configure pin as INPUT_PULLUP
- Correct Answer: B
- Explanation: Non-blocking timing using millis() compares the current time against a saved timestamp, allowing other tasks to run in parallel in the loop.

### SCENARIO_035: You want the PIR output to go LOW immediately when motion stops, even if the person remains in the room, so you can track each movement individually.
**Question:** Which jumper setting (L or H) should you select on the PIR module?
  A. H jumper setting (Repeatable trigger)
  B. L jumper setting (Single trigger)
  C. M jumper setting (Medium trigger)
  D. No jumper needed
- Correct Answer: B
- Explanation: In Single Trigger (L) mode, the output goes LOW after the delay time expires, even if motion is still occurring, requiring a new motion event to trigger again.

### SCENARIO_036: Your PIR sensor triggers when people walk in the hallway outside the room, which you want to ignore. You only want to detect motion within 2 meters.
**Question:** How do you adjust the sensor's physical range?
  A. Increase the operating voltage to 12V
  B. Turn the sensitivity adjustment potentiometer counter-clockwise to reduce the detection range
  C. Increase the delay time potentiometer
  D. Place the sensor inside a dark box
- Correct Answer: B
- Explanation: Adjusting the sensitivity potentiometer changes the internal amplifier gain, reducing or increasing the detection distance of the sensor.

### SCENARIO_037: You write a DHT11 logging script. The Serial Monitor displays 'Humidity: nan %  Temperature: nan *C'.
**Question:** What does 'nan' mean, and what is the typical cause?
  A. No Analog Network; incorrect VCC connection
  B. 'nan' stands for 'Not a Number'; indicating read error due to disconnected DATA pin, missing pull-up resistor, or reading too fast (<2s)
  C. Negative Analog Node; sensor is too cold
  D. No Address Named; wrong I2C address
- Correct Answer: B
- Explanation: When the DHT library fails to read valid data pulses from the sensor, it returns NaN. Check the data pin connection and the reading frequency.

### SCENARIO_038: You have a DHT11 sensor read statement inside the loop() function of your sketch with no delay. The program compiles, but reads fail consistently.
**Question:** How do you fix this code?
  A. Increase the pull-up resistor to 100k ohms
  B. Add a delay of at least 2000 milliseconds ('delay(2000);') in the loop
  C. Change the pin mode to INPUT_PULLUP
  D. Power the sensor with 12V
- Correct Answer: B
- Explanation: The DHT11 has a slow physical response time and requires at least 2 seconds between reads to update its internal registers and transmit stable data.

### SCENARIO_039: Your DHT11 readings are occasionally incorrect. When you print the raw bytes, you see: Byte1=40, Byte2=0, Byte3=25, Byte4=0, Checksum=80.
**Question:** Is this data valid? Explain why or why not.
  A. Yes, data is valid since temperature is positive
  B. No, invalid; sum of first 4 bytes is 65 (40+0+25+0), but received checksum is 80; data is corrupted
  C. Yes, valid since checksum is positive
  D. No, invalid because decimal fields are 0
- Correct Answer: B
- Explanation: The checksum must equal the sum of the first 4 bytes. If they do not match, the data was corrupted during transmission (e.g., due to electrical noise).

### SCENARIO_040: You extend the cable to your DHT11 sensor to 20 meters. The Arduino starts reporting checksum errors and read failures frequently.
**Question:** What hardware component should you add to resolve this signal degradation?
  A. A 220 ohm current limiting resistor
  B. A 4.7k ohm pull-up resistor between the DATA line and VCC close to the Arduino
  C. A 100nF decoupling capacitor in series
  D. A 12V power supply to data pin
- Correct Answer: B
- Explanation: Long cable runs increase bus capacitance, slowing down the signal rise time. A lower value pull-up resistor (like 4.7k or 2.2k) helps pull the line HIGH faster, restoring signal integrity.

### SCENARIO_041: You read a DHT11 sensor and print the decimal values of temperature and humidity. The decimal values are always '.00'.
**Question:** Is this a bug in your code? Why or why not?
  A. Yes, the float variables must be converted to int
  B. No, not a bug; DHT11 hardware only outputs integer values; the decimal data bytes are always 0
  C. Yes, the library lacks decimal capabilities; reinstall library
  D. No, because the temperature is exactly room temperature
- Correct Answer: B
- Explanation: The DHT11 protocol specification allocates bytes for decimal values, but the DHT11 sensor chip does not support fractional resolution; it always transmits 0 for these bytes.

### SCENARIO_042: You are not allowed to use the Adafruit DHT library. You must write a function to read the DHT11 raw pulses.
**Question:** Outline the steps your code must take to read the start response from the sensor.
  A. Set pin to output, write HIGH for 18ms, set pin to input, read I2C
  B. Configure pin as output, pull low for 18ms, release high for 30us, configure pin as input, wait for low (80us) and high (80us) response from sensor
  C. Set pin to input, pull low for 30us, set pin to output, read pulse
  D. Call digitalRead() at 9600 baud
- Correct Answer: B
- Explanation: Implementing the custom single-wire protocol requires manual pin direction switching and timing using microsecond delays (delayMicroseconds) or pulse width measuring (pulseIn).

### SCENARIO_043: You wire an LM35 sensor to A0. When you touch the sensor to warm it up, the temperature reading decreases. In cold water, it increases.
**Question:** What wiring error is causing this inverted behavior?
  A. The sensor is broken; replace it
  B. The VCC and GND pins of the LM35 are swapped
  C. The ADC reference is set to INTERNAL
  D. The LDR is interfering with A0
- Correct Answer: B
- Explanation: Swapping the power and ground pins reverses the sensor output behavior and can cause the chip to heat up rapidly and be damaged.

### SCENARIO_044: Your code prints 'Temp = 120.00 *C' when the room is actually at 24 *C. You used 'Temp = analogRead(A0);'.
**Question:** How do you correct the calculation?
  A. Temp = analogRead(A0) / 100
  B. Apply formula: 'Temp = (analogRead(A0) * 5.0 * 100.0) / 1023.0;'
  C. Temp = map(analogRead(A0), 0, 1023, 0, 50)
  D. Temp = analogRead(A0) * 5
- Correct Answer: B
- Explanation: The raw ADC reading (0-1023) must be converted to voltage (multiply by 5/1023) and then to temperature (100 *C per volt).

### SCENARIO_045: Your HIH4030 humidity sensor readings are accurate in a room at 25 *C. When the system is placed in an incubator at 45 *C, the humidity readings drift and show high errors.
**Question:** How do you fix this in your code?
  A. Step up the supply voltage to 9V
  B. Apply temperature compensation formula: %True RH = (%RH) / (1.0546 - 0.00216 * T), using temperature T from LM35 or DHT11
  C. Change the analog reference to INTERNAL
  D. Use the map() function
- Correct Answer: B
- Explanation: Relative humidity output from the HIH4030 is temperature-sensitive. The compensation formula adjusts the raw RH using the current temperature.

### SCENARIO_046: An LM35 sensor is connected to A0. The analog readings fluctuate by +/- 3 *C continuously, even when temperature is stable.
**Question:** What hardware and software changes can improve the stability of the readings?
  A. Replace LM35 with digital LDR
  B. Add a 100nF decoupling capacitor across VCC/GND close to LM35 and average 10-20 samples in code
  C. Use a 12V external supply for the sensor
  D. Remove the pull-up resistor
- Correct Answer: B
- Explanation: Decoupling capacitors filter out power supply noise. Averaging readings digitally smooths out high-frequency noise from the ADC conversion process.

### SCENARIO_047: A student connects a 1k ohm resistor in parallel with the HIH4030 output pin to GND. The humidity readings drop to almost zero.
**Question:** Explain why this occurred.
  A. The output was shorted to VCC
  B. The 1k ohm resistor overloaded the high-impedance output of the HIH4030; the sensor requires a load impedance of at least 80k ohms
  C. The code reset the Arduino
  D. The sensor requires a pull-up resistor instead
- Correct Answer: B
- Explanation: HIH4030 outputs a very low current. A low resistance load pulls the output voltage down to GND, corrupting the analog signal.

### SCENARIO_048: You are designing a clinical thermometer using an LM35. You need the highest possible measurement resolution for temperatures between 20 *C and 45 *C.
**Question:** Which reference voltage setting should you use on the Arduino UNO and why?
  A. Use DEFAULT (5V); it covers the wider range
  B. Use INTERNAL (1.1V); it restricts the ADC range to 0-110 *C, increasing resolution to ~0.1 *C per ADC step
  C. Use EXTERNAL (3.3V); it matches 3.3V systems
  D. No reference setting is needed
- Correct Answer: B
- Explanation: By setting the reference to 1.1V, the 1024 steps of the ADC represent 0 to 1.1V, making each step equal to 1.07mV (0.107 *C), compared to 4.88mV (0.488 *C) with the 5V reference.

### SCENARIO_049: Your Arduino clock project works fine, but every time you unplug the USB cable and plug it back in, the time resets to '00:00:00 01/01/2000'.
**Question:** What is the most likely cause of this issue?
  A. The I2C bus is missing pull-ups
  B. The CR2032 backup coin-cell battery on the RTC module is dead, missing, or backward
  C. The clock code is in setup() instead of loop()
  D. The crystal is running at 16 MHz
- Correct Answer: B
- Explanation: If the backup battery is not providing power, the DS1302 volatile time registers reset to their default start time whenever primary VCC is disconnected.

### SCENARIO_050: You display the time from the RTC on the LCD. The screen shows '12:30:00' constantly and the seconds do not increment.
**Question:** What bit in the DS1302 registers is likely causing this clock halt?
  A. The Write Protect (WP) bit
  B. The Clock Halt (CH) bit (bit 7 of the seconds register) is set to 1, stopping the oscillator
  C. The leap year register
  D. The SPI Chip Select pin
- Correct Answer: B
- Explanation: The DS1302 seconds register contains the Clock Halt bit. If CH=1, the internal oscillator is disabled, stopping time keeping.

### SCENARIO_051: A DS1302 module is installed in a high-temperature industrial enclosure. Over a month, the clock loses 5 minutes compared to actual time.
**Question:** What causes this drift, and how can it be addressed?
  A. Voltage fluctuations on digital pins
  B. The frequency of the 32.768 kHz crystal drifts due to temperature changes; use a temperature-compensated RTC like DS3231
  C. The serial baud rate was set to 9600
  D. The battery ran out of charge
- Correct Answer: B
- Explanation: Standard quartz crystals are cut to be accurate at 25 *C. High temperatures alter their resonant frequency, causing drift. DS3231 contains an internal temperature sensor to compensate for this.

### SCENARIO_052: You want to sound a buzzer connected to pin 8 for 1 second when the RTC time hits exactly '07:30:00'.
**Question:** Write the conditional code check using rtc.getTimeStr().
  A. if (rtc.getTimeStr() == '07:30:00') { tone(8, 1000, 1000); }
  B. if (strcmp(rtc.getTimeStr(), '07:30:00') == 0) { tone(8, 1000, 1000); }
  C. if (analogRead(8) > 500) { tone(8, 1000, 1000); }
  D. if (rtc.getTime() == 730) { tone(8, 1000, 1000); }
- Correct Answer: B
- Explanation: The rtc.getTimeStr() function returns a string in the format 'HH:MM:SS'. We compare this string to '07:30:00' using strcmp() to trigger the alarm.

### SCENARIO_053: You connect the DS1302 SCLK pin to Pin 13 (which is also the SPI SCK for the SD card). The SD card works, but the RTC returns corrupt data.
**Question:** Explain the conflict and how to resolve it.
  A. Both require I2C logic; add pull-ups
  B. The DS1302 uses a custom 3-wire protocol, not SPI; sharing clock pin 13 causes conflicts; relocate SCLK to a non-SPI digital pin (e.g. Pin 7)
  C. The DS1302 runs at 12V
  D. The CS pin should be connected to GND
- Correct Answer: B
- Explanation: Unlike SPI devices which release the bus when CS is inactive, custom 3-wire interfaces like the DS1302 can interpret SPI clocks as data clocks if connected to the same line.

### SCENARIO_054: You are writing a raw DS1302 driver. You read the seconds register, then the minutes register, then the hours register.
**Question:** What race condition (time inconsistency) can occur, and how does Burst Mode prevent it?
  A. The battery will drain faster
  B. If time rolls over (e.g., from 11:59:59 to 12:00:00) during individual reads, data gets corrupted; Burst Mode reads all registers in one operation, freezing the buffer during read
  C. The I2C bus will stall
  D. The write protect register will lock
- Correct Answer: B
- Explanation: Burst Mode copies all 8 time-keeping registers to a secondary register buffer at the instant the read starts, preventing roll-over errors during multi-byte transfers.

### SCENARIO_055: You connect an SD card module to the Arduino. The Serial Monitor displays 'Initializing SD card...initialization card failed'. The card is inserted and wired correctly.
**Question:** What is the most likely cause related to the SD card formatting?
  A. The SD card is formatted with exFAT or NTFS which are unsupported; format the card to FAT16 or FAT32
  B. The SD card has a capacity of 128 GB
  C. The file was opened in FILE_READ mode
  D. The CS pin is connected to Ground
- Correct Answer: B
- Explanation: The standard Arduino SD library only supports FAT16 and FAT32 file systems. Formatting the card to these standards is required.

### SCENARIO_056: Your datalogger code runs for 10 minutes. You eject the SD card and open datalog.txt on your PC. The file exists, but it is completely empty (0 bytes).
**Question:** What critical line of code did you forget to call after writing data?
  A. SD.begin(CS)
  B. You forgot to call 'dataFile.close();' to flush the RAM data buffer to the physical card
  C. pinMode(10, OUTPUT)
  D. dataFile.print()
- Correct Answer: B
- Explanation: Data written via dataFile.print() is stored in a 512-byte RAM buffer. It is only written to the physical SD card when the buffer fills or close()/flush() is called.

### SCENARIO_057: You try to open a file using 'SD.open('daily_temperature_log.csv', FILE_WRITE)'. The function fails and returns a null file handle.
**Question:** What is the naming error, and how do you fix it?
  A. The filename contains underscores
  B. The filename exceeds the 8.3 filename format limit; change the name to a shorter format like 'temp_log.csv'
  C. The extension must be .txt only
  D. The filename must be in all uppercase
- Correct Answer: B
- Explanation: The standard SD library only supports the DOS 8.3 filename standard. File names longer than 8 characters will fail to open.

### SCENARIO_058: You need to log temperature and humidity values to a CSV file on the SD card in the format: 'Temp,Humidity' on each line.
**Question:** Write the lines of code to write these values and insert a comma and a newline.
  A. dataFile.print(temp); dataFile.print(','); dataFile.print(humidity);
  B. dataFile.print(temp); dataFile.print(','); dataFile.println(humidity);
  C. dataFile.println(temp); dataFile.print(','); dataFile.println(humidity);
  D. dataFile.write(temp); dataFile.write(','); dataFile.write(humidity);
- Correct Answer: B
- Explanation: print() outputs the values without a newline, printing the comma in between. println() terminates the line with a newline character.

### SCENARIO_059: You have both an SD card module and an SPI Ethernet module connected to the same Arduino UNO. When you initialize both, only the SD card works; the Ethernet fails.
**Question:** What hardware pins must be kept separate for multiple SPI devices, and how are they controlled?
  A. They must use different MISO pins
  B. Each SPI device must have a unique Chip Select (CS) pin, controlled in code to enable/disable devices
  C. They must use different clock frequencies
  D. They must have separate VCC connections
- Correct Answer: B
- Explanation: SPI devices share the MOSI, MISO, and SCK lines. The master selects which slave is active by pulling its unique CS pin LOW.

### SCENARIO_060: Your solar-powered datalogger writes data to an SD card every 10 seconds. In the evening, when the battery dies, the last 15 minutes of log data are lost, and the file system is corrupted.
**Question:** What software change can prevent this data loss, and how does it work?
  A. Use a larger SD card
  B. Use 'dataFile.flush();' after each write, or open and close the file for every log entry to force-write the buffer immediately
  C. Change SPI speed to half-rate
  D. Use the INTERNAL reference
- Correct Answer: B
- Explanation: Opening and closing the file, or calling flush(), ensures the file directory table and buffer are updated on the card, minimizing data loss if power fails.

## Section D: Short Answer Questions

### SHORT_001: What is the name of the company that manufactures the ATmega328P microcontroller chip used on the Arduino UNO R3?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Easy
- Expected Answer: Microchip Technology (formerly Atmel)

### SHORT_002: What letter prefix is used to designate the analog input pins on the Arduino UNO board?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Easy
- Expected Answer: A (e.g. A0, A1, A2)

### SHORT_003: How many kilobytes (KB) of SRAM are available on the Arduino UNO R3 (ATmega328P)?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Medium
- Expected Answer: 2 KB

### SHORT_004: What is the default operating voltage (in volts) of the internal components and microchip of the Arduino UNO?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Medium
- Expected Answer: 5V

### SHORT_005: What is the frequency of the crystal oscillator (in MHz) on the Arduino Mega 2560 board?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Medium
- Expected Answer: 16 MHz

### SHORT_006: How much flash memory (in kilobytes) is reserved for the bootloader program on the ATmega328P microcontroller chip on the Arduino UNO?
- Topic: Introduction to Arduino & Hardware
- Difficulty: Hard
- Expected Answer: 0.5 KB

### SHORT_007: What is the name of the built-in function in an Arduino sketch that runs repeatedly after initialization?
- Topic: Arduino C Programming Basics
- Difficulty: Easy
- Expected Answer: loop()

### SHORT_008: What specific character must be written at the end of every programming statement in C?
- Topic: Arduino C Programming Basics
- Difficulty: Easy
- Expected Answer: ; (semicolon)

### SHORT_009: How many bytes of memory does an 'int' data type variable occupy on an 8-bit Arduino UNO board?
- Topic: Arduino C Programming Basics
- Difficulty: Medium
- Expected Answer: 2 bytes

### SHORT_010: How many bytes of memory does a single 'char' variable occupy?
- Topic: Arduino C Programming Basics
- Difficulty: Medium
- Expected Answer: 1 byte

### SHORT_011: What is the exact numerical result of the C expression '14 % 4'?
- Topic: Arduino C Programming Basics
- Difficulty: Medium
- Expected Answer: 2

### SHORT_012: Where are local variables declared inside a function accessible or visible in the code?
- Topic: Arduino C Programming Basics
- Difficulty: Hard
- Expected Answer: Only inside that specific function (local scope)

### SHORT_013: Which function is called in setup() to define whether a digital pin is an INPUT or an OUTPUT?
- Topic: Basic I/O Components
- Difficulty: Easy
- Expected Answer: pinMode()

### SHORT_014: What is the name of the built-in Arduino function used to generate a square wave of a specific frequency on a digital pin to play a sound on a buzzer?
- Topic: Basic I/O Components
- Difficulty: Easy
- Expected Answer: tone()

### SHORT_015: What component is placed in parallel across an electromagnetic relay coil to protect the controller from high-voltage spikes?
- Topic: Basic I/O Components
- Difficulty: Medium
- Expected Answer: Flyback diode (or suppression diode)

### SHORT_016: Can the tone() function be used on digital pin 4 of the Arduino UNO? (Answer Yes or No)
- Topic: Basic I/O Components
- Difficulty: Medium
- Expected Answer: Yes

### SHORT_017: What is the maximum continuous current (in mA) recommended for an Arduino digital pin to operate safely?
- Topic: Basic I/O Components
- Difficulty: Hard
- Expected Answer: 20 mA

### SHORT_018: What terminal contact on a relay is physically open/disconnected when the control coil is not energized?
- Topic: Basic I/O Components
- Difficulty: Hard
- Expected Answer: Normally Open (NO)

### SHORT_019: How many pins are required on the Arduino UNO board to connect an LCD screen using an I2C backpack interface (excluding power pins)?
- Topic: Character LCD & I2C Interface
- Difficulty: Easy
- Expected Answer: 2 pins (SDA and SCL)

### SHORT_020: What does SCL stand for in I2C serial communication?
- Topic: Character LCD & I2C Interface
- Difficulty: Easy
- Expected Answer: Serial Clock

### SHORT_021: Which physical analog pin on the Arduino UNO acts as the SDA (Serial Data) pin?
- Topic: Character LCD & I2C Interface
- Difficulty: Medium
- Expected Answer: A4

### SHORT_022: What function is called in the LiquidCrystal_I2C library to clear the screen and return the cursor to position (0, 0)?
- Topic: Character LCD & I2C Interface
- Difficulty: Medium
- Expected Answer: lcd.clear()

### SHORT_023: What is the default hexadecimal I2C address of a standard PCF8574-based LCD backpack?
- Topic: Character LCD & I2C Interface
- Difficulty: Medium
- Expected Answer: 0x27

### SHORT_024: What is the row index coordinate (in 0-based indexing) for the second line of a 16x2 character LCD screen?
- Topic: Character LCD & I2C Interface
- Difficulty: Hard
- Expected Answer: 1

### SHORT_025: What does LDR stand for?
- Topic: LDR Light Sensors
- Difficulty: Easy
- Expected Answer: Light Dependent Resistor

### SHORT_026: Does LDR resistance increase or decrease when the ambient light gets brighter?
- Topic: LDR Light Sensors
- Difficulty: Easy
- Expected Answer: Decrease

### SHORT_027: How many bits of resolution does the internal analog-to-digital converter (ADC) on the Arduino UNO have?
- Topic: LDR Light Sensors
- Difficulty: Medium
- Expected Answer: 10-bit

### SHORT_028: What is the maximum integer value returned by analogRead() on the Arduino UNO?
- Topic: LDR Light Sensors
- Difficulty: Medium
- Expected Answer: 1023

### SHORT_029: If analogRead() returns 512, what voltage (in volts) is measured at the analog input pin (assuming 5V reference)?
- Topic: LDR Light Sensors
- Difficulty: Medium
- Expected Answer: 2.5V

### SHORT_030: What is the exact voltage value of the internal reference on the ATmega328P when configured using 'analogReference(INTERNAL)'?
- Topic: LDR Light Sensors
- Difficulty: Hard
- Expected Answer: 1.1V

### SHORT_031: What does a PIR sensor detect to determine motion?
- Topic: PIR Motion Sensors
- Difficulty: Easy
- Expected Answer: Infrared radiation (heat signatures)

### SHORT_032: What digital state (HIGH or LOW) does a PIR sensor output when motion is detected?
- Topic: PIR Motion Sensors
- Difficulty: Easy
- Expected Answer: HIGH

### SHORT_033: What is the typical calibration warm-up time (in seconds) required by a PIR sensor after powering on?
- Topic: PIR Motion Sensors
- Difficulty: Medium
- Expected Answer: 10 to 60 seconds

### SHORT_034: What type of lens is the white plastic cover of the PIR sensor?
- Topic: PIR Motion Sensors
- Difficulty: Medium
- Expected Answer: Fresnel lens

### SHORT_035: How many pins are on the physical connector of a standard PIR motion sensor module?
- Topic: PIR Motion Sensors
- Difficulty: Medium
- Expected Answer: 3 pins (VCC, OUT, GND)

### SHORT_036: What jumper state letter (L or H) selects the repeatable trigger mode on the PIR sensor module?
- Topic: PIR Motion Sensors
- Difficulty: Hard
- Expected Answer: H

### SHORT_037: What two physical parameters does the DHT11 sensor measure?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Easy
- Expected Answer: Temperature and Humidity

### SHORT_038: How many lines on the communication bus does the DHT11 use to transmit data?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Easy
- Expected Answer: 1 wire (Single-wire custom serial protocol)

### SHORT_039: What is the minimum delay time (in seconds) recommended between consecutive reads of a DHT11 sensor?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Medium
- Expected Answer: 2 seconds

### SHORT_040: How many total bytes (not bits) of data are sent by the DHT11 in one transmission?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Medium
- Expected Answer: 5 bytes (40 bits)

### SHORT_041: Which byte index (1st, 2nd, 3rd, 4th, or 5th) in the DHT11 data payload acts as the checksum?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Medium
- Expected Answer: 5th byte

### SHORT_042: What is the decimal fractional value of temperature always returned by a DHT11 sensor?
- Topic: DHT11 Temperature & Humidity Sensor
- Difficulty: Hard
- Expected Answer: 0

### SHORT_043: What is the linear scaling factor (in mV per degree Celsius) of the LM35 temperature sensor?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Easy
- Expected Answer: 10 mV/*C

### SHORT_044: What type of voltage signal (analog or digital) does the HIH4030 sensor output?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Easy
- Expected Answer: Analog

### SHORT_045: How many pins are on the standard TO-92 package of the LM35 temperature sensor?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Medium
- Expected Answer: 3 pins

### SHORT_046: What is the maximum relative humidity percentage (%RH) that the HIH4030 sensor can measure?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Medium
- Expected Answer: 100%

### SHORT_047: What is the accuracy (in degrees Celsius) of the LM35 sensor at room temperature (25 *C)?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Medium
- Expected Answer: +/- 0.5 *C

### SHORT_048: What is the minimum load resistance (in kOhm) required at the output pin of the HIH4030 to prevent voltage errors?
- Topic: LM35 & HIH4030 Analog Sensors
- Difficulty: Hard
- Expected Answer: 80 kOhm

### SHORT_049: What is the model number of the 3-wire Real-Time Clock chip studied in the curriculum?
- Topic: DS1302 Real-Time Clock
- Difficulty: Easy
- Expected Answer: DS1302

### SHORT_050: What is the frequency of the external quartz crystal (in kHz) used by the DS1302 RTC?
- Topic: DS1302 Real-Time Clock
- Difficulty: Easy
- Expected Answer: 32.768 kHz

### SHORT_051: What is the nominal voltage (in volts) of the CR2032 button battery used on the RTC module?
- Topic: DS1302 Real-Time Clock
- Difficulty: Medium
- Expected Answer: 3V

### SHORT_052: How many active signal lines are used in the DS1302 serial bus interface (excluding power and ground)?
- Topic: DS1302 Real-Time Clock
- Difficulty: Medium
- Expected Answer: 3 lines (CE, I/O, SCLK)

### SHORT_053: Which bit abbreviation is set to 1 in the seconds register of the DS1302 to halt the clock oscillator?
- Topic: DS1302 Real-Time Clock
- Difficulty: Medium
- Expected Answer: CH

### SHORT_054: How many bytes of battery-backed RAM are available for user storage inside the DS1302 chip?
- Topic: DS1302 Real-Time Clock
- Difficulty: Hard
- Expected Answer: 31 bytes

### SHORT_055: What standard high-speed interface protocol does the Arduino use to write data to an SD card?
- Topic: SD Cards & Data Logging
- Difficulty: Easy
- Expected Answer: SPI

### SHORT_056: What file system formatting is required for an SD card to be compatible with the Arduino SD library?
- Topic: SD Cards & Data Logging
- Difficulty: Easy
- Expected Answer: FAT16 or FAT32

### SHORT_057: What does the SPI line abbreviation MOSI stand for?
- Topic: SD Cards & Data Logging
- Difficulty: Medium
- Expected Answer: Master Out Slave In

### SHORT_058: What library constant is passed to SD.open() to open a file for writing and appending new data?
- Topic: SD Cards & Data Logging
- Difficulty: Medium
- Expected Answer: FILE_WRITE

### SHORT_059: What file name format standard (e.g. 8.3) is enforced by the basic Arduino SD library?
- Topic: SD Cards & Data Logging
- Difficulty: Medium
- Expected Answer: 8.3 format

### SHORT_060: Which function is called on an open file object to write buffered data to the SD card without closing it?
- Topic: SD Cards & Data Logging
- Difficulty: Hard
- Expected Answer: flush()

