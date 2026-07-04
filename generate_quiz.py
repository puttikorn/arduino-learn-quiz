# -*- coding: utf-8 -*-
import json
import os

# Define topic names
topic_names = {
    1: "Sketch Structure & Control Flow",
    2: "Data Types & Variables",
    3: "Digital & Analog I/O",
    4: "Time & Timing",
    5: "Serial Communication",
    6: "I2C & SPI Protocols",
    7: "External Interrupts",
    8: "Standard Libraries",
    9: "MicroPython on Arduino",
    10: "Arduino IoT Cloud & API"
}

# 150 MCQs
# Format: (topic_id, "Difficulty", "Objective", "Question", ["OptA", "OptB", "OptC", "OptD"], "CorrectOpt", "Explanation")
mcqs_raw = [
    # Topic 1: Sketch Structure & Control Flow (15 Questions: 5 Easy, 7 Medium, 3 Hard)
    (1, "Easy", "Sketch Entry Points", "Which function is executed once at the start of an Arduino sketch?", 
     ["loop()", "setup()", "main()", "init()"], "B", "setup() runs once when the board boots or resets to configure pin modes and initialize settings."),
    (1, "Easy", "Continuous Execution", "Which function runs repeatedly and contains the main loop of an Arduino sketch?", 
     ["setup()", "run()", "loop()", "execute()"], "C", "loop() is executed repeatedly as long as the board has power, containing the active program code."),
    (1, "Easy", "C++ Statement Terminator", "What symbol is required at the end of every programming statement in Arduino C++?", 
     [": (colon)", "; (semicolon)", ". (period)", ", (comma)"], "B", "A semicolon is used as a statement terminator in C++ syntax."),
    (1, "Easy", "Comparison Operators", "Which operator is used to check if two variables are equal in Arduino C++?", 
     ["=", "==", "===", "!="], "B", "The double equals (==) is the comparison operator for equality, whereas a single equals is the assignment operator."),
    (1, "Easy", "Code Comments", "Which syntax is correct for a single-line comment in Arduino C++?", 
     ["# comment", "/* comment", "// comment", "-- comment"], "C", "Double slashes (//) denote the start of a single-line comment in C++."),
    (1, "Medium", "Variable Scopes", "What is the scope of a variable declared inside the setup() function?", 
     ["Global scope", "Local to setup() only", "Class scope", "Namespace scope"], "B", "Variables declared inside a function are local to that function and cannot be accessed outside of it."),
    (1, "Medium", "Loop Structures", "Which loop structure is guaranteed to execute its code block at least once?", 
     ["for loop", "while loop", "do-while loop", "infinite loop"], "C", "A do-while loop evaluates its condition after executing the body, ensuring at least one execution."),
    (1, "Medium", "Switch-Case fall-through", "In a switch-case statement, what happens if the 'break' statement is omitted at the end of a case block?", 
     ["The code throws a compile error", "Execution terminates immediately", "Execution falls through to the next case", "The loop resets"], "C", "Omitting break causes execution to fall through and execute subsequent cases until a break is encountered."),
    (1, "Medium", "Function return types", "If a function does not return any value, what return type must be declared?", 
     ["int", "void", "null", "empty"], "B", "The 'void' keyword is used to specify that a function does not return a value."),
    (1, "Medium", "Conditional execution", "What is the difference between the logical AND operator (&&) and logical OR operator (||)?", 
     ["&& requires both conditions true, || requires only one", "&& requires one condition true, || requires both", "&& checks floats, || checks integers", "&& terminates loop, || skips iteration"], "A", "Logical AND requires all conditions to be true, while logical OR evaluates to true if at least one condition is true."),
    (1, "Medium", "Sketch Entry constraints", "What happens if a sketch contains no loop() function defined?", 
     ["It compiles and halts immediately", "It compiles and loops setup()", "It fails to compile due to missing reference", "It works but inputs are disabled"], "C", "The compiler expects both setup() and loop() to be defined; missing either causes a linker/compiler error."),
    (1, "Medium", "Preprocessor directives", "Which preprocessor directive is used to define a macro constant in Arduino?", 
     ["#const", "#define", "#macro", "#include"], "B", "#define is a preprocessor directive that replaces occurrences of a macro name with specified text before compilation."),
    (1, "Hard", "Preprocessor conditional compilation", "How can you prevent a code section from compiling for a specific board type using preprocessors?", 
     ["Using if/else statements", "Using #ifdef and #endif directives", "Using virtual functions", "Using namespace scopes"], "B", "#ifdef and #endif allow conditional compilation based on whether specific macros (like board models) are defined."),
    (1, "Hard", "Memory exhaustion risks", "Why is deep recursion generally avoided in Arduino programming?", 
     ["It occupies too much flash memory", "It causes stack overflow in limited SRAM", "It blocks interrupts", "It causes compiler timeout"], "B", "Each recursive call consumes stack space in SRAM. Given limited RAM (e.g., 2KB on Uno), deep recursion can easily crash the board."),
    (1, "Hard", "Short-Circuit evaluation", "What is the behavior of short-circuit evaluation in a logical AND operation (expr1 && expr2)?", 
     ["Both expr1 and expr2 are always evaluated", "expr2 is evaluated first", "If expr1 is false, expr2 is not evaluated", "If expr1 is true, expr2 is not evaluated"], "C", "In logical AND, if the first expression is false, the overall outcome must be false, so the compiler skips evaluating the second expression."),

    # Topic 2: Data Types & Variables (15 Questions: 5 Easy, 7 Medium, 3 Hard)
    (2, "Easy", "Basic Data Types", "Which data type is best suited to store a true/false value?", 
     ["int", "float", "char", "boolean"], "D", "A boolean data type stores either 'true' or 'false' (using 1 byte of memory in Arduino)."),
    (2, "Easy", "Floating-Point types", "Which data type should be used to store decimal values like 3.14159?", 
     ["int", "float", "long", "byte"], "B", "The 'float' type is used to store floating-point (decimal) numbers."),
    (2, "Easy", "Integer Memory Usage", "How many bytes of memory does an 'int' type consume on an 8-bit AVR board like Arduino Uno?", 
     ["1 byte", "2 bytes", "4 bytes", "8 bytes"], "B", "On 8-bit AVR boards, an int occupies 16 bits (2 bytes), whereas on 32-bit boards (like Due or Nano 33) it occupies 4 bytes."),
    (2, "Easy", "Array Indexing", "What is the index of the first element in an array?", 
     ["-1", "0", "1", "Depends on array size"], "B", "Arrays in C++ are 0-indexed; the first element is accessed using index 0."),
    (2, "Easy", "Character Types", "What is the memory size and range of a signed 'char' data type?", 
     ["1 byte (-128 to 127)", "2 bytes (0 to 65535)", "1 byte (0 to 255)", "4 bytes (floating-point)"], "A", "A char occupies 1 byte (8 bits) of memory, storing signed values from -128 to 127."),
    (2, "Medium", "Variable Qualifiers", "What is the primary function of the 'const' variable qualifier?", 
     ["It puts the variable in dynamic heap", "It prevents the variable from being modified after initialization", "It forces the variable to be 16-bit", "It enables interrupt access"], "B", "The const keyword stands for constant and prevents code from modifying the variable's value after it is initialized."),
    (2, "Medium", "Interrupt Variables", "Why should variables modified inside an Interrupt Service Routine (ISR) be declared with 'volatile'?", 
     ["To allocate them in EEPROM", "To force the compiler to load the variable from SRAM instead of caching it in a CPU register", "To increase their precision", "To reduce RAM usage"], "B", "The volatile keyword tells the compiler that the variable's value may change at any time (via an ISR) outside normal program flow, forcing it to read fresh values from RAM."),
    (2, "Medium", "Integer Overflow", "What happens when an unsigned 8-bit integer variable (byte) holding 255 is incremented by 1?", 
     ["It throws a runtime exception", "It remains 255", "It rolls over to 0", "It expands to a 16-bit int"], "C", "An 8-bit unsigned byte ranges from 0 to 255. Incrementing past 255 causes an overflow, rolling the value back to 0."),
    (2, "Medium", "String class vs C-strings", "What is the main drawback of using the 'String' object class compared to null-terminated char arrays (C-strings)?", 
     ["It does not support concatenation", "It uses only 1 byte of memory", "It causes heap fragmentation in limited SRAM", "It compiles slower"], "C", "The String class dynamically allocates memory on the heap. Frequent modifications cause heap fragmentation, potentially leading to memory allocation failures in devices with small RAM."),
    (2, "Medium", "Variables persistence", "How does the 'static' keyword modify the behavior of a local variable inside a function?", 
     ["It deletes the variable when the function returns", "It keeps the variable in memory and retains its value between function calls", "It makes the variable globally accessible", "It locks the variable from interrupts"], "B", "A static local variable is initialized only once and retains its value between successive calls to the function containing it."),
    (2, "Medium", "Integer Data Limits", "What is the maximum value that can be stored in an unsigned 16-bit integer (unsigned int)?", 
     ["32,767", "65,535", "2,147,483,647", "4,294,967,295"], "B", "An unsigned 16-bit integer can represent values from 0 to (2^16 - 1), which is 65,535."),
    (2, "Medium", "Array Bounds", "What happens if your code writes to an array index that is out of bounds?", 
     ["The compiler generates a warning", "It overwrites adjacent memory variables, causing unpredictable crashes", "The execution halts immediately with a safe trap", "The array auto-expands"], "B", "C++ does not perform runtime array boundary checking. Writing out-of-bounds writes directly to adjacent memory, leading to variable corruption and system instability."),
    (2, "Hard", "Float precision limitations", "Why can float variable comparisons (e.g., floatVal == 1.5) be unreliable in C++?", 
     ["Floats cannot hold numbers larger than 100", "Floating-point numbers are stored with binary approximations and can contain small rounding errors", "Floats are automatically cast to integers before comparison", "Floats cannot be used with comparison operators"], "B", "Floats use binary representation which cannot exactly represent many decimal fractions. Slight rounding issues make exact equality comparison unsafe; comparing using a delta threshold (epsilon) is preferred."),
    (2, "Hard", "Sizeof Operator behavior", "What does the 'sizeof()' operator return when applied to an array of 10 integers on an Arduino Uno?", 
     ["10", "20", "40", "2"], "B", "sizeof() returns the size of the object in bytes. Since an integer is 2 bytes on the Uno, an array of 10 integers occupies 20 bytes."),
    (2, "Hard", "Variables Alignment", "What is the benefit of using variable structs with byte-alignment considerations in Arduino?", 
     ["It speeds up compiling", "It optimizes RAM usage by packing variables and avoiding compiler padding bytes", "It makes variables constants", "It prevents division by zero"], "B", "Structuring data carefully reduces padding bytes on platforms that enforce alignment rules, conserving limited RAM."),

    # Topic 3: Digital & Analog I/O (15 Questions: 5 Easy, 7 Medium, 3 Hard)
    (3, "Easy", "Pin Configuration", "Which function is used to configure a pin as an input or output?", 
     ["digitalWrite()", "pinMode()", "digitalRead()", "setupPin()"], "B", "pinMode() sets the electrical state of a specified pin to INPUT, OUTPUT, or INPUT_PULLUP."),
    (3, "Easy", "Digital Outputs", "Which function is used to output a HIGH or LOW voltage level on a digital pin?", 
     ["pinMode()", "digitalRead()", "digitalWrite()", "analogWrite()"], "C", "digitalWrite() sets a digital output pin to either HIGH (5V/3.3V) or LOW (0V)."),
    (3, "Easy", "Digital Inputs", "What function is used to read the high/low state of a digital input pin?", 
     ["digitalWrite()", "digitalRead()", "analogRead()", "pinRead()"], "B", "digitalRead() reads the physical voltage status of a configured digital input pin (HIGH or LOW)."),
    (3, "Easy", "Analog Inputs", "What is the default bit resolution of the analog-to-digital converter (ADC) on an Arduino Uno?", 
     ["8-bit", "10-bit", "12-bit", "16-bit"], "B", "The default resolution of the AVR ADC on Uno is 10-bit (returning values from 0 to 1023)."),
    (3, "Easy", "PWM Outputs", "Which function is used to generate a Pulse Width Modulation (PWM) signal on supported pins?", 
     ["digitalWrite()", "analogRead()", "analogWrite()", "pwmWrite()"], "C", "analogWrite() outputs a PWM signal with a duty cycle specified from 0 (always off) to 255 (always on)."),
    (3, "Medium", "INPUT_PULLUP state", "How does configuring a pin as INPUT_PULLUP affect its electrical state?", 
     ["It connects the pin directly to ground", "It activates an internal pull-up resistor, keeping the pin HIGH by default", "It increases current output capacity to 40mA", "It converts the pin to an analog pin"], "B", "INPUT_PULLUP activates the internal pull-up resistor (typically 20k-50k ohms), holding the pin input HIGH when it is disconnected/floating."),
    (3, "Medium", "Analog Voltage calculation", "If analogRead() on a 5V Arduino board returns a value of 512, what is the measured input voltage?", 
     ["1.25V", "2.50V", "3.75V", "5.00V"], "B", "An ADC value of 512 corresponds to half of the maximum 10-bit scale (1023), which is 2.5V (5V * 512 / 1023)."),
    (3, "Medium", "PWM Duty Cycle calculation", "What duty cycle is represented by a call to analogWrite(pin, 64)?", 
     ["10%", "25%", "50%", "75%"], "B", "Duty cycle is determined by value/255. 64/255 is approximately 25.1% duty cycle."),
    (3, "Medium", "High Impedance State", "Why is a pin set to INPUT referred to as being in a 'high impedance' state?", 
     ["It sources high current to devices", "It consumes very little current from the circuit it is measuring", "It switches voltage levels rapidly", "It acts as a low-resistance path to ground"], "B", "An input pin has high input impedance, meaning it takes negligible current (typically < 1 microampere) from the circuit, reducing loading effects."),
    (3, "Medium", "Floating pin behavior", "What is the risk of reading a digital input pin that has nothing connected to it (floating pin)?", 
     ["It will always return LOW", "It will return random HIGH/LOW values due to electrical noise", "It will damage the microcontroller chip", "The program will crash"], "B", "A floating input pin has no defined voltage reference and will fluctuate randomly between HIGH and LOW due to electromagnetic noise."),
    (3, "Medium", "PWM frequency limitations", "What is the typical default frequency of PWM signals on most Arduino Uno pins?", 
     ["50 Hz", "490 Hz", "10 kHz", "1 MHz"], "B", "Most pins (like 3, 9, 10, 11) run PWM at approximately 490 Hz, while pins 5 and 6 run at about 980 Hz."),
    (3, "Medium", "analogRead speed", "How long does a standard analogRead() call take to complete on an 8-bit AVR board like the Uno?", 
     ["1 microsecond", "100 microseconds", "1 millisecond", "10 milliseconds"], "B", "A standard analogRead() takes about 100 microseconds, restricted by the hardware conversion speed of the successive-approximation ADC."),
    (3, "Hard", "ADC Reference modification", "What function is used to change the reference voltage of the ADC to an external source, and what is a critical risk associated with it?", 
     ["analogReference(); risk of damaging the microcontroller if reference voltage exceeds VCC", "setADC(); risk of disabling interrupts", "adcRef(); risk of losing PWM control", "analogWriteResolution(); risk of float overflow"], "A", "analogReference() changes the reference voltage. Applying voltage to the AREF pin before calling analogReference(EXTERNAL) can burn out the internal ADC circuitry."),
    (3, "Hard", "High-Resolution ADC configurations", "Which command is used on 32-bit SAMD boards (like Arduino Zero/Nano 33 IoT) to change analog input resolution?", 
     ["analogResolution()", "analogReadResolution()", "setAdcBits()", "adcConfigure()"], "B", "analogReadResolution() allows configuring 10-bit, 12-bit, or higher ADC resolutions on boards with supported high-res ADC hardware."),
    (3, "Hard", "Port Manipulation usage", "What is the advantage of using Port Manipulation (direct register access like PORTD) over digitalWrite()?", 
     ["It uses less flash memory", "It allows setting multiple pins simultaneously and executes significantly faster", "It converts digital pins to analog output", "It handles switch bouncing automatically"], "B", "Port manipulation bypasses the safety wrappers of digitalWrite(), executing in a single clock cycle and allowing synchronous state changes across multiple pins of a port."),

    # Topic 4: Time & Timing (15 Questions: 5 Easy, 7 Medium, 3 Hard)
    (4, "Easy", "Millisecond Delay", "Which function suspends program execution for a specified number of milliseconds?", 
     ["wait()", "delay()", "sleep()", "pause()"], "B", "delay() pauses the sketch for the amount of time (in milliseconds) specified as a parameter."),
    (4, "Easy", "Microsecond Delay", "Which function is used to pause the program for a very short duration in microseconds?", 
     ["delay()", "delayMicroseconds()", "usDelay()", "pauseMicro()"], "B", "delayMicroseconds() provides fine-grained pauses in microseconds for timing-critical tasks."),
    (4, "Easy", "Running Time milliseconds", "Which function returns the number of milliseconds elapsed since the Arduino board started running the current sketch?", 
     ["millis()", "time()", "getTicks()", "clock()"], "C", "millis() returns an unsigned long representing the milliseconds elapsed since boot."),
    (4, "Easy", "Running Time microseconds", "Which function returns the elapsed time in microseconds since the board booted?", 
     ["micros()", "millis()", "timeMicro()", "getMicroseconds()"], "A", "micros() returns the number of microseconds elapsed since the program started."),
    (4, "Easy", "Unsigned Long usage", "What data type is returned by the millis() and micros() functions?", 
     ["int", "long", "unsigned long", "unsigned int"], "C", "Both functions return an unsigned long, which prevents early overflow of the time counter."),
    (4, "Medium", "millis Rollover period", "After approximately how many days does the millis() counter overflow and roll back to zero?", 
     ["50 days", "25 days", "70 days", "9 hours"], "A", "The 32-bit unsigned long used by millis() rolls over back to 0 after approximately 49.7 days (2^32 - 1 milliseconds)."),
    (4, "Medium", "Safe Rollover subtraction", "Why does the subtraction syntax 'currentTime - previousTime >= interval' correctly handle timing even during a millis() overflow rollover?", 
     ["Because floats prevent rounding errors", "Because modular arithmetic in unsigned integers automatically handles overflows correctly", "Because the bootloader auto-adjusts the registers", "Because loop() resets during rollover"], "B", "Due to unsigned integer subtraction, the difference rolls over properly, giving the correct elapsed time even if the timer wrapped back to zero."),
    (4, "Medium", "Blocking vs Non-blocking", "What is the primary disadvantage of using delay() for timing in complex sketches?", 
     ["It consumes extra battery power", "It is blocking, preventing other code (like reading sensors or buttons) from executing during the delay", "It disables interrupts", "It causes float drift"], "B", "delay() is blocking; it forces the CPU to run idle loops, making the device unresponsive to external inputs or events during that window."),
    (4, "Medium", "micros precision limits", "What is the resolution/step size of the micros() function on standard 16 MHz AVR boards?", 
     ["1 microsecond", "4 microseconds", "8 microseconds", "16 microseconds"], "B", "On 16 MHz Arduino boards, the timer register scales such that micros() has a resolution of 4 microseconds (always returning multiples of 4)."),
    (4, "Medium", "micros Rollover period", "After approximately how long does the micros() counter overflow and roll back to zero?", 
     ["70 minutes", "70 seconds", "49 days", "9 hours"], "A", "Being a 32-bit value storing microseconds, micros() overflows and rolls over after approximately 71.5 minutes (2^32 microseconds)."),
    (4, "Medium", "delayMicroseconds limits", "What is the maximum duration that delayMicroseconds() can reliably produce accurate delays?", 
     ["16383 microseconds", "32767 microseconds", "65535 microseconds", "1000 microseconds"], "A", "Currently, the largest value that will produce an accurate delay is 16383. For longer delays, delay() should be used."),
    (4, "Medium", "Non-blocking delay pattern", "Which structure is typically used to execute an action every 1 second without using blocking delays?", 
     ["An if condition checking 'millis() - previousMillis >= 1000'", "A nested while loop", "An external hardware interrupt on pin 2", "A watchdog timer reset"], "A", "Checking the difference between current millis() and a stored timestamp allows non-blocking periodic execution."),
    (4, "Hard", "ISR and delay constraint", "Why does calling delay() inside an Interrupt Service Routine (ISR) cause the program to hang?", 
     ["It consumes too much flash memory", "delay() relies on interrupts (specifically Timer 0 overflows) to increment the millis counter, which are disabled inside an ISR", "ISRs do not support parameters", "It causes a stack overflow"], "B", "Inside an ISR, other interrupts are disabled by default. Since delay() checks the incrementing millis counter, which depends on the Timer 0 overflow interrupt, the counter never advances and the program halts indefinitely."),
    (4, "Hard", "Timer Registers conflicts", "Which internal AVR timer is used by the Arduino core to drive the millis() and delay() functions?", 
     ["Timer 0", "Timer 1", "Timer 2", "Timer 3"], "A", "Timer 0 is configured by the Arduino core libraries for system timekeeping. Using PWM or changing configurations on pins 5 and 6 (which use Timer 0) can alter timer speeds."),
    (4, "Hard", "Prescaler modifications", "How does changing the prescaler of Timer 0 to alter PWM frequency impact system functions?", 
     ["It shifts ADC accuracy", "It breaks the timing of millis() and delay(), causing time to pass faster or slower", "It disables the hardware Serial interface", "It makes digital inputs float"], "B", "Since millis() and delay() are calibrated to the default Timer 0 prescaler (64), altering it changes the speed at which timekeeping counters increment."),

    # Topic 5: Serial Communication (15 Questions: 5 Easy, 7 Medium, 3 Hard)
    (5, "Easy", "Serial Initialization", "Which function is used to initialize serial communication at a specific baud rate?", 
     ["Serial.start()", "Serial.begin()", "Serial.open()", "Serial.init()"], "B", "Serial.begin(speed) opens the serial port and sets the communication speed in bits per second (baud rate)."),
    (5, "Easy", "Serial Transmit data", "Which function transmits data to the computer with a newline character appended at the end?", 
     ["Serial.print()", "Serial.write()", "Serial.println()", "Serial.send()"], "C", "Serial.println() transmits data as ASCII text followed by a carriage return and newline characters."),
    (5, "Easy", "Serial Receive availability", "Which function returns the number of bytes available for reading in the serial buffer?", 
     ["Serial.read()", "Serial.available()", "Serial.peek()", "Serial.count()"], "B", "Serial.available() returns the count of bytes that have arrived and are stored in the serial receive buffer."),
    (5, "Easy", "Serial Reading data", "Which function reads a single byte from the incoming serial buffer?", 
     ["Serial.read()", "Serial.get()", "Serial.pop()", "Serial.receive()"], "A", "Serial.read() reads the next available byte from the incoming serial buffer (returning -1 if no data is available)."),
    (5, "Easy", "Baud Rate definition", "What is 'baud rate' in serial communication?", 
     ["The voltage level of the signal", "The frequency of the clock signal", "The speed of data transmission in bits per second", "The capacity of the internal buffer in bytes"], "C", "Baud rate defines the rate at which data is transferred over the serial communication channel (bits per second)."),
    (5, "Medium", "SoftwareSerial vs HardwareSerial", "What is the purpose of the SoftwareSerial library?", 
     ["To emulate USB host controller on SPI pins", "To allow serial communication on other digital pins using software pin-toggling", "To increase the hardware buffer to 512 bytes", "To bypass digital pins entirely"], "B", "SoftwareSerial allows using software-controlled digital pins for serial communication, useful when multiple serial connections are needed on boards with limited hardware UARTs."),
    (5, "Medium", "Serial buffer size", "What is the default size of the hardware serial receive buffer in the Arduino core library for AVR boards?", 
     ["16 bytes", "64 bytes", "128 bytes", "256 bytes"], "B", "By default, the serial buffer size in the Arduino core is 64 bytes. If the buffer overflows, oldest incoming bytes are discarded."),
    (5, "Medium", "ASCII vs Binary transmission", "What is the difference between Serial.print(65) and Serial.write(65)?", 
     ["print sends characters '6' and '5', write sends byte value 65 (char 'A')", "print sends 65 bytes, write sends 1 byte", "print uses I2C, write uses UART", "There is no difference"], "A", "Serial.print() converts data to human-readable ASCII text, whereas Serial.write() writes binary data directly to the serial port."),
    (5, "Medium", "Serial non-blocking read", "What value is returned by Serial.read() if the receive buffer is empty?", 
     ["0", "-1", "255", "Null"], "B", "Serial.read() returns -1 (an integer) to signal that there is no data in the buffer."),
    (5, "Medium", "Serial Flush function", "What is the function of Serial.flush() in modern Arduino core versions?", 
     ["It clears the receive buffer", "It blocks execution until all outgoing serial data has been fully transmitted", "It resets the baud rate", "It enables parity bits"], "B", "In current versions, Serial.flush() blocks until the transmit buffer is empty, ensuring all data is sent before proceeding."),
    (5, "Medium", "Serial Parser functions", "Which function reads incoming serial data until a specific character delimiter (like a newline) is found?", 
     ["Serial.readBytes()", "Serial.readStringUntil()", "Serial.parseInt()", "Serial.find()"], "B", "Serial.readStringUntil(terminator) reads characters from the serial buffer into a String until the specified terminator is met."),
    (5, "Medium", "Hardware UART pins Uno", "Which pins are connected to the hardware Serial (UART) on the Arduino Uno board?", 
     ["Pins 11 and 12", "Pins A4 and A5", "Pins 0 (RX) and 1 (TX)", "Pins 2 and 3"], "C", "Pins 0 (RX) and 1 (TX) are routed to the hardware UART, which is also linked to the onboard USB-to-serial converter."),
    (5, "Hard", "While (!Serial) behavior", "What does the statement 'while (!Serial)' do, and on which boards is it required?", 
     ["It loops until serial buffer is empty; required on Uno", "It loops until the USB CDC serial connection is established; required on Leonardo/Micro/Due", "It disables interrupts; required on Mega", "It checks if software serial is active; required on Nano"], "B", "On boards with native USB (like Leonardo, Micro, Due), the USB serial is dynamic. 'while (!Serial)' halts program execution until the USB port is opened by the computer."),
    (5, "Hard", "SoftwareSerial limitation", "What is a major limitation of using SoftwareSerial at high baud rates?", 
     ["It occupies all PWM pins", "It is processor-intensive and prone to data corruption/dropped bytes above 38400 or 57600 baud", "It disables digital output on all pins", "It requires 12V supply"], "B", "Because SoftwareSerial relies on software-driven pin change interrupts and precise software delay loops, it consumes significant processor cycles and becomes unreliable at high speeds."),
    (5, "Hard", "Serial event handler", "How does the 'serialEvent()' function work within the Arduino execution loop?", 
     ["It is an interrupt handler triggered instantly when a byte arrives", "It is called automatically at the end of each loop() iteration if serial data is available", "It runs in a separate thread", "It disables the bootloader"], "B", "serialEvent() is not a hardware interrupt. It is run sequentially by the hidden main() function immediately after loop() completes, provided there are bytes waiting in the hardware RX buffer."),

    # Topic 6: I2C & SPI Protocols (15 Questions: 4 Easy, 8 Medium, 3 Hard)
    (6, "Easy", "I2C Pins Uno", "Which Arduino Uno pins are used for I2C communication (SDA and SCL)?", 
     ["Pins 11 and 13", "Pins A4 (SDA) and A5 (SCL)", "Pins 0 and 1", "Pins 2 and 3"], "B", "On the Uno, SDA is analog pin A4 and SCL is analog pin A5 (also duplicated near the AREF pin)."),
    (6, "Easy", "SPI Pins Uno", "Which pins form the default SPI interface on the Arduino Uno?", 
     ["Pins A4 and A5", "Pins 11 (MOSI), 12 (MISO), and 13 (SCK)", "Pins 0 and 1", "Pins 2 and 3"], "B", "Pins 11, 12, and 13 are the default hardware SPI pins on the Uno, with pin 10 often used as the default SS (Slave Select) pin."),
    (6, "Easy", "I2C Library name", "Which library is included in the Arduino IDE to facilitate I2C communication?", 
     ["SPI.h", "Wire.h", "LiquidCrystal.h", "I2C.h"], "B", "The Wire library handles I2C communication (Inter-Integrated Circuit) on Arduino boards."),
    (6, "Easy", "SPI Library name", "Which library is used to communicate with high-speed SPI devices?", 
     ["Wire.h", "SPI.h", "SoftwareSerial.h", "Ethernet.h"], "B", "The SPI library is used to communicate with devices using the Serial Peripheral Interface bus."),
    (6, "Medium", "Bus Device addressing", "How are devices identified on an I2C bus?", 
     ["By individual Chip Select (CS) wires", "By a unique 7-bit or 10-bit software address sent over the bus", "By their physical distance from the master", "By their baud rate configuration"], "B", "I2C uses a shared bus where each slave device is selected using its unique 7-bit or 10-bit hardware address."),
    (6, "Medium", "I2C Bus speed", "What is the default clock speed of the I2C bus in the Wire library?", 
     ["10 kHz", "100 kHz", "400 kHz", "1 MHz"], "B", "The default clock speed is 100 kHz (standard mode). It can be changed using Wire.setClock()."),
    (6, "Medium", "I2C Master write sequence", "What is the correct sequence of Wire library commands to write data to an I2C device?", 
     ["Wire.beginTransmission(), Wire.write(), Wire.endTransmission()", "Wire.write(), Wire.send()", "Wire.requestFrom(), Wire.read()", "Wire.beginTransmission(), Wire.read()"], "A", "Writing data involves initiating transmission, writing the bytes to a local buffer, and calling endTransmission() to physically send the data."),
    (6, "Medium", "I2C Master read function", "Which function is used by an I2C master to request a specific number of bytes from a slave device?", 
     ["Wire.requestFrom()", "Wire.read()", "Wire.beginTransmission()", "Wire.get()"], "A", "Wire.requestFrom(address, quantity) requests bytes from the slave device, which are then read using Wire.read()."),
    (6, "Medium", "SPI Bus selection", "How does a master select a specific slave device on an SPI bus?", 
     ["By sending a 7-bit address", "By pulling the specific Chip Select (CS) / Slave Select (SS) line LOW", "By sending a start byte", "By matching the clock polarity"], "B", "SPI uses a dedicated physical Slave Select (SS) line for each slave. Pulling the SS pin low activates the target slave."),
    (6, "Medium", "SPI Data transfer method", "Which function is used to send and receive a byte simultaneously over the SPI bus?", 
     ["SPI.write()", "SPI.transfer()", "SPI.send()", "SPI.read()"], "B", "SPI.transfer(val) writes a byte over MOSI and simultaneously reads a byte from MISO (duplex communication)."),
    (6, "Medium", "I2C Pull-up requirement", "Why does I2C communication require pull-up resistors on both the SDA and SCL lines?", 
     ["To limit current output from pins", "Because I2C uses open-drain/open-collector drivers that need pull-ups to pull the line HIGH", "To prevent voltage spikes above 12V", "To act as termination impedance"], "B", "I2C devices only pull the lines LOW. Pull-up resistors (normally 4.7k ohms) are required to pull the lines back to HIGH when no device is active."),
    (6, "Medium", "SPI Speed limits", "What is the typical maximum speed of SPI communication on Arduino Uno compared to I2C?", 
     ["It is slower than I2C", "Up to 8 MHz (half the system clock), which is much faster than I2C", "Exactly 100 kHz", "Limited to 115200 baud"], "B", "SPI is a synchronous bus that can run at up to 8 MHz on a 16 MHz Arduino Uno, significantly outpacing I2C speeds."),
    (6, "Hard", "Wire.endTransmission status", "What is the meaning of a return value of 4 from the Wire.endTransmission() call?", 
     ["Success", "Data too long to fit in transmit buffer", "Received NACK on transmit of address", "Other I2C bus error"], "D", "Wire.endTransmission() returns: 0 = success, 1 = data too long, 2 = NACK on address, 3 = NACK on data, 4 = other error (e.g., bus collision)."),
    (6, "Hard", "SPI Transaction settings", "What is the purpose of using 'SPISettings' in modern SPI code?", 
     ["To specify the I2C clock rate", "To define the SPI speed, bit order, and data mode (clock polarity/phase) for a specific device, ensuring compatibility when sharing the bus", "To increase the SPI buffer to 256 bytes", "To disable interrupts during transfer"], "B", "SPISettings allows configuring the bus speed, bit order, and data mode for each SPI slave, preventing clock conflicts when different devices share the same bus."),
    (6, "Hard", "I2C Repeated Start condition", "How do you generate an I2C repeated start condition in the Wire library, and why is it useful?", 
     ["Call Wire.begin() twice", "Pass 'false' as the parameter to Wire.endTransmission(false); it keeps the bus active to prevent other masters from interrupting", "Call Wire.requestFrom() with no parameters", "Pass 'true' to Wire.write(data, true)"], "B", "Passing false to endTransmission() prevents sending a STOP condition, maintaining master control of the bus for back-to-back read/write operations."),

    # Topic 7: External Interrupts (15 Questions: 4 Easy, 8 Medium, 3 Hard)
    (7, "Easy", "Interrupt Pin Uno", "Which pins on the Arduino Uno support external hardware interrupts?", 
     ["Pins A0 and A1", "Pins 2 and 3", "Pins 11 and 12", "All digital pins"], "B", "The Uno supports external hardware interrupts only on digital pins 2 (Interrupt 0) and 3 (Interrupt 1)."),
    (7, "Easy", "Attach Interrupt function", "Which function is used to link a digital pin to a specific interrupt handler function?", 
     ["interrupts()", "attachInterrupt()", "setInterrupt()", "linkInterrupt()"], "B", "attachInterrupt(digitalPinToInterrupt(pin), ISR, mode) configures an external interrupt on the target pin."),
    (7, "Easy", "Interrupt Disable function", "Which function is used to temporarily disable all interrupts on the Arduino?", 
     ["noInterrupts()", "detachInterrupt()", "stopInterrupts()", "cli()"], "A", "noInterrupts() (equivalent to cli()) disables interrupts, which is useful for protecting time-critical code."),
    (7, "Easy", "Interrupt Mode RISING", "When an interrupt is set to the 'RISING' mode, when does it trigger?", 
     ["When the pin state is LOW", "When the pin transitions from LOW to HIGH", "When the pin transitions from HIGH to LOW", "When the pin changes state"], "B", "RISING triggers the interrupt when the input voltage rises from low to high."),
    (7, "Medium", "Interrupt Mode CHANGE", "What does the interrupt mode 'CHANGE' represent?", 
     ["Triggers when the pin goes HIGH", "Triggers when the pin goes LOW", "Triggers whenever the pin changes state from HIGH to LOW or LOW to HIGH", "Triggers at a set timer interval"], "C", "CHANGE triggers the ISR whenever the input pin transitions in either direction (rising or falling)."),
    (7, "Medium", "Interrupt Service Routine constraints", "Which of the following is a rule that must be followed when writing an Interrupt Service Routine (ISR)?", 
     ["The ISR must take float parameters", "The ISR should be as short and fast as possible, and cannot accept arguments or return values", "The ISR must use delay()", "The ISR must run at 115200 baud"], "B", "An ISR must be fast to avoid blocking the main execution path. It cannot accept arguments or return values, and blocking calls must be avoided."),
    (7, "Medium", "DigitalPinToInterrupt macro", "Why is it recommended to use the 'digitalPinToInterrupt(pin)' macro inside attachInterrupt()?", 
     ["It increases interrupt speed", "It translates the board's digital pin number to the correct internal hardware interrupt channel, ensuring code portability across different boards", "It debounces inputs", "It allocates RAM for the ISR"], "B", "Hardware interrupt channels (like INT0) map to different physical pins on different microcontrollers (e.g., Uno vs Mega). The macro ensures the correct channel is used dynamically."),
    (7, "Medium", "noInterrupts safety window", "When is it necessary to call noInterrupts() and interrupts() in the main loop?", 
     ["Before using analogWrite()", "When reading or writing a multi-byte variable that is modified inside an ISR, to prevent data corruption", "During serial data transmissions", "Every time loop() starts"], "B", "An ISR can trigger midway through reading a multi-byte variable (like a 4-byte long). Temporarily disabling interrupts prevents data corruption from partial reads."),
    (7, "Medium", "Interrupt Mode FALLING", "When does an interrupt configured with the 'FALLING' trigger mode execute?", 
     ["When the pin is HIGH", "When the pin transitions from HIGH to LOW", "When the pin transitions from LOW to HIGH", "When the pin is disconnected"], "B", "FALLING triggers the interrupt when the pin transitions from high (VCC) to low (GND)."),
    (7, "Medium", "Interrupts Re-enabling", "Which function is used to re-enable interrupts after they have been disabled using noInterrupts()?", 
     ["noInterrupts()", "interrupts()", "startInterrupts()", "sei()"], "B", "interrupts() (equivalent to sei()) re-enables interrupts after a temporary disable window."),
    (7, "Medium", "Pin Change Interrupts", "What is the difference between External Interrupts and Pin Change Interrupts (PCINT) on AVR boards?", 
     ["PCINT only work on analog pins", "External Interrupts are limited to specific pins; PCINT can be enabled on any digital pin, but are grouped in ports sharing one ISR", "PCINT are faster than external interrupts", "External interrupts cannot detect falling edges"], "B", "AVR chips support Pin Change Interrupts on all pins, but they share ISR vectors per port, requiring software checks to identify the active pin."),
    (7, "Medium", "Interrupt Mode LOW", "What is a potential risk of using the 'LOW' interrupt mode?", 
     ["It never triggers", "As long as the pin remains LOW, the interrupt will trigger continuously, blocking the main loop execution", "It is only compatible with analog pins", "It consumes too much flash memory"], "B", "The LOW mode triggers continuously as long as the pin stays low, potentially trapping the processor in the ISR and starving the main loop."),
    (7, "Hard", "Reentrancy and Nested Interrupts", "Can an ISR be interrupted by another interrupt on an Arduino Uno by default?", 
     ["Yes, higher priority interrupts always interrupt lower ones", "No, interrupts are disabled globally when entering an ISR; nested interrupts are not allowed unless manually enabled", "Yes, all interrupts run concurrently in threads", "Only if the watchdog timer is active"], "B", "AVR clears the global interrupt enable bit upon entering an ISR, disabling nested interrupts by default. Manual re-enabling inside the ISR is possible but discouraged."),
    (7, "Hard", "Interrupt Variables race conditions", "What is a 'race condition' when dealing with interrupts in Arduino?", 
     ["When the CPU clock runs faster than 16MHz", "A situation where the main program and an ISR access and modify a shared variable at the same time, leading to corrupted values", "When two interrupts are attached to the same pin", "When the serial baud rate is too fast"], "B", "A race condition occurs when asynchronous execution of the ISR modifies a shared variable while the main loop is in the middle of reading or writing it."),
    (7, "Hard", "Debouncing interrupts", "Why is software debouncing inside an ISR using delay() not possible, and how should it be resolved?", 
     ["delay() is disabled inside ISRs; resolve by checking the elapsed time since the last trigger using millis() or micros() and ignoring triggers that occur too quickly", "delay() compiles to code comments; use while loops", "ISRs do not support debouncing; use hardware filters only", "Use Serial.println() instead"], "A", "Since delay() relies on system interrupts that are disabled within an ISR, it will lock the program. Using a non-blocking time check (comparing current time with the last trigger timestamp) resolves the issue."),

    # Topic 8: Standard Libraries (15 Questions: 4 Easy, 8 Medium, 3 Hard)
    (8, "Easy", "Servo Pin attachment", "Which function in the Servo library is used to assign a servo motor to a specific digital pin?", 
     ["Servo.pin()", "Servo.attach()", "Servo.write()", "Servo.connect()"], "B", "attach(pin) associates the Servo variable with a physical pin (which does not have to be a hardware PWM pin)."),
    (8, "Easy", "Servo Angle write", "Which function is used to rotate a standard servo motor to a specific angle (e.g., 90 degrees)?", 
     ["Servo.setAngle()", "Servo.write()", "Servo.move()", "Servo.rotate()"], "B", "write(angle) writes a value in degrees (typically 0 to 180) to control the shaft angle of the servo."),
    (8, "Easy", "SD File opening", "Which function in the SD library is used to open a file on an SD card for reading or writing?", 
     ["SD.open()", "SD.read()", "SD.file()", "SD.begin()"], "A", "SD.open(filename, mode) opens a file and returns a File object reference."),
    (8, "Easy", "LCD Print function", "Which function is used to display text on a Character LCD screen using the LiquidCrystal library?", 
     ["lcd.write()", "lcd.print()", "lcd.display()", "lcd.show()"], "B", "lcd.print() writes text characters to the LCD screen at the current cursor position."),
    (8, "Medium", "Servo default angle", "What is the typical default pulse width range in microseconds used by the Servo library to sweep from 0 to 180 degrees?", 
     ["1000 to 2000 us", "544 to 2400 us", "0 to 1023 us", "100 to 500 us"], "B", "The default pulse width limits are 544 microseconds (for 0 degrees) and 2400 microseconds (for 180 degrees)."),
    (8, "Medium", "SD Card interface", "Which hardware communication protocol does the SD library use to interface with SD cards?", 
     ["I2C", "SPI", "UART", "One-Wire"], "B", "SD cards communicate using the Serial Peripheral Interface (SPI) bus, requiring MOSI, MISO, SCK, and CS lines."),
    (8, "Medium", "LiquidCrystal pin configurations", "In the constructor 'LiquidCrystal lcd(RS, Enable, D4, D5, D6, D7)', how many data pins are being used to drive the LCD?", 
     ["8-bit mode (8 pins)", "4-bit mode (4 pins)", "I2C mode (2 pins)", "Serial mode (1 pin)"], "B", "This constructor initializes the LCD in 4-bit mode, using 4 data lines (D4-D7) plus RS and Enable controls to save pins."),
    (8, "Medium", "SD File flush importance", "Why is it important to call File.close() or File.flush() after writing data to an SD card?", 
     ["To free up SRAM memory", "To ensure data is written from the volatile write buffer to the physical SD card, preventing data loss", "To clear the SPI registers", "To enable interrupts"], "B", "The SD library buffers writes in RAM. Calling close() or flush() forces the buffer to write to the physical card, preventing file corruption if power is lost."),
    (8, "Medium", "Servo writeMicroseconds usage", "What is the benefit of using 'writeMicroseconds()' instead of 'write()' in the Servo library?", 
     ["It makes the servo spin faster", "It allows setting the pulse width directly for higher resolution and precision", "It reduces current consumption", "It works without attaching a pin"], "B", "writeMicroseconds() bypasses the 0-180 degree conversion, allowing direct setting of the pulse width for precise positioning."),
    (8, "Medium", "LCD cursor setting", "Which command is used to move the cursor to the first character of the second row on a 16x2 character LCD?", 
     ["lcd.setCursor(1, 1)", "lcd.setCursor(0, 1)", "lcd.setCursor(1, 0)", "lcd.setCursor(0, 2)"], "B", "lcd.setCursor(col, row) is 0-indexed. Moving to the first character of the second row is setCursor(0, 1)."),
    (8, "Medium", "SD Card format requirement", "Which file system format is required on SD cards for compatibility with the standard SD library?", 
     ["NTFS", "FAT16 or FAT32", "exFAT", "ext4"], "B", "The standard SD library supports only FAT16 and FAT32 file systems. Larger or differently formatted cards will fail to initialize."),
    (8, "Medium", "SD filename limit", "What is the filename length restriction in the standard SD library (excluding SD Fat variants)?", 
     ["No limit", "8.3 format (up to 8 characters for name, 3 for extension)", "32 characters", "256 characters"], "B", "The standard SD library uses the 8.3 filename format (e.g., 'data.txt'), failing to open longer filenames."),
    (8, "Hard", "Servo library timer conflict", "How does the Servo library on Arduino Uno impact the functionality of PWM pins 9 and 10?", 
     ["It doubles their frequency", "It disables analogWrite() PWM capability on digital pins 9 and 10", "It converts them to analog inputs", "It has no impact"], "B", "On the Uno, the Servo library uses Timer 1. Since Timer 1 also drives PWM on pins 9 and 10, PWM functionality on those pins is disabled when using the library."),
    (8, "Hard", "SD Card CS line requirements", "Why must the hardware SS pin (pin 10 on Uno) be set to OUTPUT even if a different pin is used as the SD card's Chip Select (CS)?", 
     ["To provide power to the SD card", "To force the SPI interface into Master mode; if left as an INPUT set to LOW, the SPI hardware enters Slave mode, breaking communication", "To act as a clock reference", "To disable external interrupts"], "B", "The hardware SS pin must be configured as an output (or held high if input) to keep the AVR SPI hardware in Master mode."),
    (8, "Hard", "LiquidCrystal timing requirements", "Why does the LiquidCrystal library contain short delay calls (like delayMicroseconds) within its functions?", 
     ["To debounce button inputs", "To accommodate the relatively slow internal controller (like the HD44780) of character LCD modules", "To sync with I2C baud rate", "To prevent float errors"], "B", "Standard character LCD controllers operate slowly. The library includes brief delays to meet the setup and hold time requirements of the LCD controller."),

    # Topic 9: MicroPython on Arduino (15 Questions: 4 Easy, 8 Medium, 3 Hard)
    (9, "Easy", "MicroPython Definition", "What is MicroPython?", 
     ["A compiler that converts C++ to Python", "A lean and efficient implementation of the Python 3 programming language optimized to run on microcontrollers", "An IDE designed by Arduino", "A Python library for serial graphing"], "B", "MicroPython is a lightweight Python 3 implementation designed specifically for constrained embedded systems."),
    (9, "Easy", "MicroPython import modules", "Which module is imported in MicroPython to interact with hardware components like pins and ADC?", 
     ["sys", "machine", "time", "math"], "B", "The 'machine' module contains classes (Pin, ADC, PWM, I2C, SPI) for hardware control in MicroPython."),
    (9, "Easy", "MicroPython delay function", "Which function is used in MicroPython to pause execution for a specified number of seconds?", 
     ["time.sleep()", "time.delay()", "time.wait()", "machine.sleep()"], "A", "In MicroPython, the 'time' module's sleep(seconds) function is used for delays."),
    (9, "Easy", "MicroPython Pin declaration", "How do you configure pin 2 as a digital output in MicroPython?", 
     ["pinMode(2, OUTPUT)", "pin = Pin(2, Pin.OUT)", "pin = Pin(2, OUTPUT)", "pin.config(2, OUT)"], "B", "In MicroPython, pins are configured using the Pin constructor: `Pin(2, Pin.OUT)`."),
    (9, "Medium", "MicroPython shell REPL", "What does 'REPL' stand for in MicroPython?", 
     ["Reset, Execute, Program, Loop", "Read-Eval-Print Loop", "Real-Time Embedded Programming Language", "Receive, Encrypt, Process, Log"], "B", "REPL stands for Read-Eval-Print Loop, an interactive command-line interface for executing Python commands on the board."),
    (9, "Medium", "C++ vs MicroPython timing", "How does loop frequency compare between C++ and MicroPython on the same board?", 
     ["MicroPython is faster", "C++ is significantly faster because it compiles to native machine code, whereas MicroPython is interpreted at runtime", "They run at the exact same speed", "MicroPython uses 12V to increase speed"], "B", "C++ compiles directly to machine code, achieving much faster loop speeds than interpreted MicroPython code."),
    (9, "Medium", "MicroPython Pin value set", "What is the correct syntax to set a MicroPython Pin object named 'led' to a high state?", 
     ["led.high() or led.value(1)", "led.write(HIGH)", "led.digitalWrite(1)", "led(ON)"], "A", "In MicroPython, you set a pin state by calling value(1) or the high() method on the Pin object."),
    (9, "Medium", "MicroPython ADC reading", "How do you read an analog voltage from an ADC object named 'adc' in MicroPython?", 
     ["adc.read() or adc.read_u16()", "analogRead(adc)", "adc.digitalRead()", "adc.get_value()"], "A", "MicroPython uses the read() or read_u16() methods on the ADC object, returning values normalized up to 16 bits (0-65535)."),
    (9, "Medium", "MicroPython PWM duty cycle", "Which method is used to set the PWM duty cycle for a PWM object in MicroPython?", 
     ["pwm.write(duty)", "pwm.duty() or pwm.duty_u16()", "pwm.duty_cycle()", "pwm.analogWrite()"], "B", "MicroPython's PWM class uses the duty() or duty_u16() methods to set the pulse width duty cycle."),
    (9, "Medium", "MicroPython runtime dynamic typing", "What is a key difference in variable declaration between C++ and MicroPython?", 
     ["MicroPython requires type definitions (like int, float)", "MicroPython is dynamically typed, meaning variables do not require explicit type declarations", "MicroPython variables are always 16-bit", "MicroPython does not support arrays"], "B", "Unlike C++, which requires static type definitions, MicroPython is dynamically typed and assigns types at runtime based on the value."),
    (9, "Medium", "MicroPython Pin Pull-up", "How do you configure an input pin with an internal pull-up resistor enabled in MicroPython?", 
     ["Pin(5, Pin.IN, Pin.PULL_UP)", "Pin(5, Pin.INPUT_PULLUP)", "Pin(5, Pin.IN_PULLUP)", "Pin(5, Pin.IN, pull=Pin.PULL_UP)"], "D", "In MicroPython, the pull parameter is passed to the constructor, e.g., `Pin(5, Pin.IN, pull=Pin.PULL_UP)`."),
    (9, "Medium", "MicroPython GC function", "What is the purpose of the 'gc.collect()' call in MicroPython?", 
     ["To reset the processor", "To trigger garbage collection, releasing unused memory blocks back to the heap", "To compile scripts", "To verify pin configurations"], "B", "gc.collect() runs the garbage collector to clean up dereferenced objects and free RAM, which is important for preventing memory exhaustion in long-running scripts."),
    (9, "Hard", "MicroPython interrupt rules", "Why should MicroPython ISRs avoid allocating memory (like creating lists or formatting strings)?", 
     ["It disables the REPL", "Memory allocation is forbidden during ISR execution in MicroPython and will raise a RuntimeError", "It slows down the I2C clock", "It overrides global variables"], "B", "ISRs run in a restricted context where memory allocation on the heap is not permitted. Allocating memory throws an exception, crashing the script."),
    (9, "Hard", "MicroPython micropython.alloc_emergency_exception_buf", "What is the purpose of 'micropython.alloc_emergency_exception_buf(100)' in MicroPython?", 
     ["To speed up arithmetic operations", "To allocate a buffer for printing exception tracebacks from inside ISRs without needing heap allocation", "To store variables during deep sleep", "To increase the REPL history size"], "B", "Since heap allocation is disabled in ISRs, formatting tracebacks fails. The emergency buffer provides a reserved area to display ISR errors reliably."),
    (9, "Hard", "MicroPython firmware differences", "What is stored in the bootloader flash section compared to the MicroPython interpreter firmware on a board?", 
     ["The bootloader launches the USB mass storage mode, while the MicroPython firmware interprets the Python scripts", "The bootloader contains the Python scripts", "The bootloader compiles scripts to C++", "There is no bootloader in MicroPython"], "A", "The bootloader is responsible for loading the interpreter firmware. The interpreter firmware is what parses and executes your Python scripts (like main.py)."),

    # Topic 10: Arduino IoT Cloud & API (15 Questions: 4 Easy, 8 Medium, 3 Hard)
    (10, "Easy", "IoT Cloud definition", "What is Arduino IoT Cloud?", 
     ["A local offline database compiler", "A service that allows users to monitor, control, and log data from connected devices using a web dashboard", "A replacement for C++ language", "A Python module for machine learning"], "B", "Arduino IoT Cloud is a platform for building IoT applications, allowing remote monitoring and control via dashboards."),
    (10, "Easy", "IoT Dashboard widgets", "What is a dashboard widget in the Arduino IoT Cloud?", 
     ["A hardware relay shield", "A graphical user interface element (like a slider, switch, or chart) connected to a cloud variable", "A software library for AVR chips", "A custom sensor calibration tool"], "B", "Widgets are interactive UI elements on the dashboard that display data or control cloud variables in real time."),
    (10, "Easy", "IoT Cloud variables", "What are 'Cloud Variables' in the context of Arduino IoT Cloud?", 
     ["Variables stored in external EEPROM", "Variables synchronized automatically between the physical device and the cloud platform", "Variables that cannot be changed", "Variables representing analog pin counts"], "B", "Cloud variables are variables defined in your sketch that automatically sync with the cloud when their values change."),
    (10, "Easy", "IoT Cloud Connectivity", "Which connectivity options are commonly supported by Arduino IoT Cloud compatible boards?", 
     ["Only USB serial", "Wi-Fi, Ethernet, and cellular networks", "Only Bluetooth Low Energy", "Parallel bus cables"], "B", "Compatible boards connect to the cloud using Wi-Fi, Ethernet, or cellular networks, depending on their hardware features."),
    (10, "Medium", "IoT Cloud setup function", "Which function is called inside setup() to initialize the Arduino IoT Cloud configuration?", 
     ["ArduinoCloud.begin()", "ArduinoCloud.init()", "IoT.begin()", "Cloud.start()"], "A", "ArduinoCloud.begin() is called inside setup() to initialize connectivity and cloud variables."),
    (10, "Medium", "Cloud Variables sync policy", "What is the difference between 'On Change' and 'Periodic' variable sync policies?", 
     ["On Change updates only when the value changes; Periodic updates at a set interval", "On Change requires an interrupt pin; Periodic uses delay()", "On Change saves power; Periodic uses USB", "There is no difference"], "A", "On Change updates the cloud only when the variable's value changes, while Periodic sends updates at a set time interval regardless of value changes."),
    (10, "Medium", "Cloud update call", "What is the function of the 'ArduinoCloud.update()' call placed inside the loop() function?", 
     ["It compiles the sketch", "It handles background tasks, keeping the connection alive and synchronizing variables with the cloud", "It resets the board if disconnected", "It reads analog pins"], "B", "ArduinoCloud.update() must be called frequently in loop() to manage connectivity, process incoming messages, and sync variables."),
    (10, "Medium", "IoT Cloud things", "What represents a 'Thing' in the Arduino IoT Cloud architecture?", 
     ["A physical sensor module", "The virtual representation of a device, grouping configuration settings, cloud variables, and network credentials", "An I2C bus address", "A dashboard widget"], "B", "A 'Thing' represents a device configuration, grouping its variables, linked hardware, and network details."),
    (10, "Medium", "IoT Cloud REST API", "What is the purpose of the Arduino IoT Cloud REST API?", 
     ["To program Arduino boards using Python", "To allow external applications to interact with cloud variables, dashboards, and device metadata programmatically", "To route SPI traffic", "To flash the bootloader"], "B", "The REST API allows external systems (like web apps or mobile apps) to query and modify cloud data programmatically."),
    (10, "Medium", "IoT Cloud security", "How are communications secured between an Arduino board and the IoT Cloud?", 
     ["By using standard plain text serial", "By using SSL/TLS encryption, often supported by a hardware crypto-chip on the board", "By limiting communication to 9600 baud", "By disabling all external interrupts"], "B", "Data is encrypted using SSL/TLS. Compatible boards typically feature a crypto-element (like the ATECC608 chip) for secure key storage and encryption acceleration."),
    (10, "Medium", "IoT Cloud read-only variables", "What happens when a cloud variable is configured as 'Read Only' in the IoT Cloud interface?", 
     ["The variable cannot be read by the board", "The board can write to the variable to update the cloud, but the dashboard cannot modify it", "The dashboard can write to it, but the board cannot read it", "The variable is stored in flash"], "B", "Read-only variables are updated by the board to send status to the dashboard; the dashboard cannot modify them."),
    (10, "Medium", "IoT Cloud write-only variables", "What is the purpose of the callback function generated for a 'Read & Write' cloud variable?", 
     ["To measure analog input voltage", "It is executed on the board whenever a new value is received from the cloud dashboard", "To reset the Wi-Fi credentials", "To calibrate sensor readings"], "B", "Read-Write variables generate an 'onVarChange()' callback on the board, which runs automatically when the dashboard sends a new value."),
    (10, "Hard", "IoT Cloud watchdog utility", "Why does the Arduino IoT Cloud library include an internal watchdog or connection timeout check?", 
     ["To speed up compiling", "To automatically reset the board or reconnect if the internet connection hangs, preventing devices from going offline permanently", "To limit current on digital pins", "To clear the SRAM"], "B", "An internal connection check prevents remote devices from hanging indefinitely in a disconnected state by forcing a reconnect or system reset."),
    (10, "Hard", "IoT Cloud credentials storage", "Where is the unique private key of an Arduino IoT Cloud device stored for authentication?", 
     ["In the sketch code as plain text", "In the hardware cryptochip (like ATECC608A/B) on the board during registration", "In the USB serial controller", "In the bootloader"], "B", "The unique device key is generated and stored securely inside the onboard crypto-authentication chip, preventing exposure in the source code."),
    (10, "Hard", "IoT Cloud webhooks integration", "How can you trigger an external service (like sending an Slack message or updating a Google Sheet) when an IoT Cloud variable changes?", 
     ["By using Port Manipulation", "By configuring Webhooks in the IoT Cloud Thing settings to POST events to an external URL", "By adding SoftwareSerial code", "By modifying the bootloader"], "B", "Webhooks can be configured to send JSON payloads to external endpoints whenever variables update, facilitating third-party integrations.")
]

# 60 True/False
# Format: (topic_id, "Difficulty", "Objective", "Statement", "CorrectAnswer", "Explanation")
tfs_raw = [
    # Topic 1: Sketch Structure & Control Flow
    (1, "Easy", "Sketch requirements", "An Arduino C++ sketch must always define both setup() and loop() functions to compile successfully.", "True", "The Arduino toolchain requires both entry points to build the executable loop properly."),
    (1, "Medium", "C++ case sensitivity", "Keywords and variable names in Arduino C++ are case-insensitive.", "False", "C++ is case-sensitive; 'ledPin' and 'ledpin' are treated as two distinct variables."),
    (1, "Medium", "Preprocessor replacement", "The #define directive creates variable allocations in SRAM.", "False", "#define is a preprocessor macro directive that performs text replacement before compilation, consuming no memory at runtime."),
    (1, "Medium", "Variable scopes", "A global variable can be accessed by any function within the same sketch.", "True", "Global variables are declared outside of functions and have a scope that extends throughout the file."),
    (1, "Hard", "Volatile keyword optimization", "Declaring a variable as 'volatile' makes code execution faster by allowing compiler register caching.", "False", "Volatile prevents register caching, forcing RAM lookups, which makes access slightly slower but safe for ISRs."),
    (1, "Hard", "Short-circuit boolean evaluation", "In the expression (A || B), if A is evaluated as true, B will still be evaluated.", "False", "Logical OR uses short-circuit evaluation. If the first operand is true, the overall result must be true, so B is skipped."),

    # Topic 2: Data Types & Variables
    (2, "Easy", "Boolean storage size", "A boolean variable in Arduino C++ consumes exactly 1 bit of RAM.", "False", "The smallest addressable unit of memory is a byte, so a boolean occupies 1 byte (8 bits) of RAM."),
    (2, "Medium", "Float type parameters", "An integer variable can store values with decimal parts.", "False", "Integers can only store whole numbers; fractional parts are truncated during assignment."),
    (2, "Medium", "Unsigned integer limits", "An unsigned int variable on an Arduino Uno can store negative numbers.", "False", "Unsigned variables can only represent positive integers and zero."),
    (2, "Medium", "Static variables persistence", "A static local variable inside a function is destroyed and recreated every time the function exits and is re-entered.", "False", "Static local variables retain their values across function calls and exist for the lifetime of the program."),
    (2, "Hard", "Float exact comparison", "Comparing floating-point values for exact equality (==) is recommended for safety.", "False", "Rounding errors in floating-point math make exact comparisons risky; a delta comparison should be used instead."),
    (2, "Hard", "Sizeof pointer behavior", "Using sizeof() on a pointer returns the size of the array it points to.", "False", "sizeof() on a pointer returns the size of the pointer itself (2 bytes on AVR, 4 bytes on 32-bit platforms), not the target object's size."),

    # Topic 3: Digital & Analog I/O
    (3, "Easy", "pinMode INPUT_PULLUP", "Setting a pin to INPUT_PULLUP enables an internal resistor that pulls the input voltage level HIGH.", "True", "INPUT_PULLUP activates the internal pull-up resistor (20k-50k ohms) to hold the pin high by default."),
    (3, "Easy", "analogWrite PWM dependency", "analogWrite() can produce a true variable analog voltage output on any digital pin on the Arduino Uno.", "False", "analogWrite() outputs a PWM signal (pulsing high and low), not a true analog voltage, and is limited to specific PWM pins."),
    (3, "Medium", "analogRead default range", "On an Arduino Uno, the analogRead() function returns values ranging from 0 to 255.", "False", "analogRead() on the Uno uses a 10-bit ADC, returning values from 0 to 1023."),
    (3, "Medium", "digitalWrite on Input Pin", "Calling digitalWrite(pin, HIGH) on a pin configured as INPUT activates the internal pull-up resistor on AVR boards.", "True", "In legacy Arduino C++, writing HIGH to an input pin is the alternative method to enable the internal pull-up resistor."),
    (3, "Medium", "ADC Reference safety", "Applying a voltage to the AREF pin before calling analogReference(EXTERNAL) can short-circuit and damage the microcontroller.", "True", "If the internal reference is active, it will clash with the external voltage on AREF, potentially burning out the ADC mux hardware."),
    (3, "Hard", "analogWrite frequency variability", "The PWM frequency on pins 5 and 6 of an Arduino Uno is slightly higher than on pins 9 and 10.", "True", "Timer 0 drives pins 5 and 6 at ~980 Hz, while Timer 1 drives pins 9 and 10 at ~490 Hz."),

    # Topic 4: Time & Timing
    (4, "Easy", "delay blocking behavior", "The delay() function pauses the execution of the entire program, blocking other operations.", "True", "delay() is a blocking function; it loops the CPU until the time elapsed, preventing other code from running."),
    (4, "Easy", "millis time unit", "The millis() function returns the time elapsed in microseconds.", "False", "millis() returns the elapsed time in milliseconds (1/1000th of a second)."),
    (4, "Medium", "millis Rollover handling", "Using subtraction (currentTime - previousTime) prevents timing bugs when millis() rolls over.", "True", "Unsigned subtraction correctly wraps around, ensuring accurate interval checks even during rollover."),
    (4, "Medium", "delayMicroseconds accuracy limits", "delayMicroseconds() can accurately pause for intervals of up to 1 second.", "False", "delayMicroseconds() is only accurate for values up to 16,383 microseconds (~16 milliseconds)."),
    (4, "Medium", "delay inside ISR", "The delay() function works perfectly inside an Interrupt Service Routine (ISR) on an Arduino Uno.", "False", "Inside an ISR, interrupts are disabled. Since delay() relies on Timer 0 interrupts to increment system time, it will block permanently."),
    (4, "Hard", "Timer 0 PWM side-effects", "Modifying Timer 0 registers directly will alter the timing rate of millis() and delay() functions.", "True", "Since Timer 0 is used for system timekeeping, changing its prescaler will speed up or slow down millis() and delay()."),

    # Topic 5: Serial Communication
    (5, "Easy", "Serial Baud Rate matching", "The baud rate specified in Serial.begin() must match the baud rate configured in the serial monitor for correct data display.", "True", "Mismatched baud rates result in corrupted characters (gibberish) due to timing synchronization mismatch."),
    (5, "Easy", "Serial print vs write", "Serial.print() and Serial.write() transmit data in the exact same format.", "False", "print() converts data to ASCII characters, while write() transmits raw binary bytes directly."),
    (5, "Medium", "Serial available blocking", "The Serial.available() function blocks program execution until serial data arrives.", "False", "Serial.available() is non-blocking; it immediately returns 0 if the receive buffer is empty."),
    (5, "Medium", "Serial buffer overflow", "If incoming serial data exceeds 64 bytes without being read, the oldest data in the buffer is overwritten.", "False", "New incoming bytes are discarded when the 64-byte buffer is full; the existing buffer contents are preserved."),
    (5, "Medium", "while(!Serial) role", "The line 'while (!Serial)' is necessary on all Arduino boards to start serial communication.", "False", "It is only required on boards with native USB CDC (like Leonardo, Due, Nano 33 IoT) to wait for a USB connection."),
    (5, "Hard", "SoftwareSerial duplex limits", "The SoftwareSerial library can transmit and receive data simultaneously at high speeds without issues.", "False", "SoftwareSerial cannot transmit and receive at the same time reliably because it relies on software-toggled timing loops."),

    # Topic 6: I2C & SPI Protocols
    (6, "Easy", "I2C wire requirements", "The I2C protocol requires only two signal wires (SDA and SCL) to communicate with multiple devices.", "True", "I2C uses a shared bus, requiring only SDA (data) and SCL (clock) lines, plus ground."),
    (6, "Easy", "SPI speed comparison", "SPI communication is generally slower than I2C communication.", "False", "SPI is a full-duplex protocol that can run at much higher clock speeds than I2C."),
    (6, "Medium", "I2C bus addressing", "Multiple devices with the same I2C address can share the same Wire bus without any conflict.", "False", "Each device on an I2C bus must have a unique address for the master to direct communication without conflict."),
    (6, "Medium", "SPI hardware lines", "The SPI bus requires dedicated lines for MOSI, MISO, and SCK, but uses individual Chip Select (CS) lines for each slave.", "True", "SPI shares clock and data lines but requires a dedicated CS line for each slave device to enable it."),
    (6, "Medium", "Wire endTransmission status", "Wire.endTransmission() actually sends all buffered data and returns status details about the transaction.", "True", "Calling endTransmission() executes the I2C transaction and returns status codes indicating success or specific errors."),
    (6, "Hard", "I2C repeated start support", "The Wire library does not support generating a repeated start condition on the I2C bus.", "False", "Passing 'false' to Wire.endTransmission(false) holds the bus active, creating a repeated start condition."),

    # Topic 7: External Interrupts
    (7, "Easy", "Interrupt pin limits Uno", "All digital pins on the Arduino Uno can be used as external hardware interrupts.", "False", "Only digital pins 2 and 3 support external hardware interrupts on the Uno."),
    (7, "Easy", "ISR return value constraints", "An Interrupt Service Routine (ISR) can return a value using the 'return' statement.", "False", "An ISR must be declared with a void return type and cannot return any value."),
    (7, "Medium", "volatile variable requirement", "Any global variable modified inside an ISR and read elsewhere must be declared as volatile.", "True", "The volatile keyword prevents the compiler from caching the variable in registers, ensuring updates are read from RAM."),
    (7, "Medium", "Interrupt RISING mode", "The RISING interrupt mode triggers when the pin transitions from HIGH to LOW.", "False", "RISING mode triggers on a LOW-to-HIGH transition; HIGH-to-LOW is handled by the FALLING mode."),
    (7, "Medium", "nested interrupts status", "On standard AVR boards, interrupts are automatically re-enabled inside an ISR, allowing nested interrupts by default.", "False", "AVR disables interrupts globally upon entering an ISR. Nested interrupts do not occur unless manually re-enabled."),
    (7, "Hard", "ISR parameters constraint", "An ISR function can accept arguments, provided they are integers.", "False", "An ISR function cannot accept any arguments; it must have a void parameter list."),

    # Topic 8: Standard Libraries
    (8, "Easy", "Servo PWM pin requirements", "The Servo library can control servo motors on any digital pin, not just hardware PWM pins.", "True", "The Servo library uses software-controlled timer interrupts to drive servo control pulses on any digital pin."),
    (8, "Easy", "SD file naming rules", "The standard SD library supports long filenames of up to 256 characters by default.", "False", "The standard SD library is restricted to the 8.3 filename format (up to 8 characters plus a 3-character extension)."),
    (8, "Medium", "LCD 4-bit vs 8-bit connection", "Using the LiquidCrystal library in 4-bit mode requires fewer pins than 8-bit mode but still displays the same content.", "True", "4-bit mode uses only 4 data pins instead of 8, saving 4 digital I/O pins while maintaining display capabilities."),
    (8, "Medium", "SD card write caching", "Data written to an SD card using File.print() is immediately saved to the card, even if the file is not closed.", "False", "Data is cached in RAM. It is only written to the card when close() or flush() is called."),
    (8, "Medium", "Servo library Timer 1 conflict", "Using the Servo library on an Arduino Uno disables PWM functionality on digital pins 9 and 10.", "True", "The Servo library uses Timer 1 on the Uno. This disables PWM capability on pins 9 and 10, which rely on Timer 1."),
    (8, "Hard", "SD card SPI SS input trap", "Leaving the hardware SS pin (pin 10 on Uno) as an INPUT set to LOW will disable the SPI Master mode.", "True", "If SS is configured as an input and pulled LOW, the SPI hardware switches to Slave mode, breaking communication with the SD card."),

    # Topic 9: MicroPython on Arduino
    (9, "Easy", "MicroPython interpreted nature", "MicroPython code runs faster than compiled C++ code on the same microcontroller.", "False", "C++ compiles to native machine code, whereas MicroPython is interpreted at runtime, making C++ faster."),
    (9, "Easy", "MicroPython machine module", "The 'machine' module in MicroPython is used to control hardware peripherals.", "True", "The machine module contains standard classes for controlling I/O pins, ADCs, PWM, I2C, and SPI."),
    (9, "Medium", "MicroPython dynamic variables", "In MicroPython, you must declare variable types (like int or float) before using them.", "False", "MicroPython is a dynamically typed language; variables are declared on assignment without explicit type declarations."),
    (9, "Medium", "MicroPython ADC scaling", "MicroPython's ADC.read_u16() method returns an analog measurement scaled to a 16-bit range (0 to 65535).", "True", "The read_u16() method normalizes all analog readings to a 16-bit unsigned integer (0-65535) for consistency across boards."),
    (9, "Medium", "MicroPython ISR memory restrictions", "An ISR in MicroPython is allowed to allocate dynamic memory (such as creating lists).", "False", "MicroPython ISRs cannot allocate memory on the heap. Doing so throws a RuntimeError within the interrupt handler."),
    (9, "Hard", "MicroPython REPL interactivity", "The MicroPython REPL allows users to test code line-by-line interactively on the board.", "True", "REPL (Read-Eval-Print Loop) provides an interactive command prompt for executing Python commands on the fly over serial."),

    # Topic 10: Arduino IoT Cloud & API
    (10, "Easy", "IoT Cloud dashboard widgets", "Dashboard widgets in the Arduino IoT Cloud must be manually linked to cloud variables to display data.", "True", "Widgets are interface elements that must be bound to specific variables to sync data or send controls."),
    (10, "Easy", "IoT Cloud variables synchronization", "Cloud variables are automatically updated in the cloud without requiring internet connectivity.", "False", "Internet connectivity (Wi-Fi, Cellular, etc.) is required for the library to sync variable states with the cloud."),
    (10, "Medium", "IoT Cloud loop requirement", "The ArduinoCloud.update() function must be called frequently in the loop() function.", "True", "ArduinoCloud.update() handles background tasks, synchronizes variables, and maintains connection status."),
    (10, "Medium", "IoT Cloud sync policies", "A cloud variable with an 'On Change' sync policy will update the cloud even if its value remains the same.", "False", "The 'On Change' sync policy only transmits updates to the cloud when the variable's value changes, conserving bandwidth."),
    (10, "Medium", "IoT Cloud secure authentication", "The unique cryptographic key used to authenticate a board with the IoT Cloud is stored as plain text in the sketch.", "False", "The authentication key is stored securely in the onboard hardware crypto-chip (like ATECC608), keeping it hidden from source code."),
    (10, "Hard", "IoT Cloud Webhooks usage", "IoT Cloud Webhooks allow triggering external APIs when a cloud variable changes value.", "True", "Webhooks send POST payloads to configured external URLs on variable changes, facilitating third-party integrations.")
]

# 60 Scenarios
# Format: (topic_id, "Difficulty", "Objective", "Scenario", "Question", "CorrectAnswer", "Explanation")
scenarios_raw = [
    # Topic 1: Sketch Structure & Control Flow
    (1, "Easy", "Setup configuration error", 
     "A student wants to blink an LED on pin 13 but forgets to configure the pin using 'pinMode(13, OUTPUT)'. They write 'digitalWrite(13, HIGH); delay(1000); digitalWrite(13, LOW);' inside the loop().", 
     "What will be the behavior of the LED?", 
     "B", 
     "Without configuring the pin as an output, the pin defaults to input. In AVR chips, digitalWrite(13, HIGH) on an input pin enables the internal pull-up resistor, lighting the LED very dimly due to high resistance (~30k-50k ohms)."),
    
    (1, "Medium", "Loop execution flow", 
     "A developer places a block of sensor calibration code inside the setup() function and expects it to run once when the device starts. Later, they need the calibration code to run whenever a button is pressed during program execution.", 
     "How should they refactor the code?", 
     "C", 
     "Moving the calibration logic to a separate helper function allows it to be called from both setup() (during startup) and loop() (upon button press events)."),
    
    (1, "Medium", "Modulo operator application", 
     "An engineer wants a specific warning buzzer on pin 8 to beep only on every 10th iteration of a loop that tracks a sensor count variable.", 
     "Which condition should they check inside the loop?", 
     "A", 
     "Checking 'if (count % 10 == 0)' uses the modulo operator (%) to evaluate the remainder. When count is a multiple of 10, the remainder is 0, triggering the buzzer."),
    
    (1, "Medium", "Infinite loop trap", 
     "A programmer writes 'while (analogRead(A0) < 500) { digitalWrite(13, HIGH); }' inside the loop() function. The analog reading is 400 when the loop starts, and no other code modifies the state inside the while loop.", 
     "What will happen to the execution of the program?", 
     "B", 
     "Since the analog reading is not updated inside the while loop body, the condition remains true indefinitely. The processor is trapped in an infinite loop, and the rest of the program halts."),
    
    (1, "Hard", "Recursion memory crash", 
     "An embedded developer designs a nested search algorithm on an Arduino Uno that uses recursive function calls. During stress testing, the board suddenly resets or crashes whenever the search depth exceeds 25 levels.", 
     "What is the most likely cause of this crash?", 
     "B", 
     "Deep recursion on the Uno (which has only 2KB of RAM) causes stack overflow. The stack collides with the heap/global variables, corrupting memory and triggering crashes or watchdog resets."),
    
    (1, "Hard", "Namespace conflicts resolution", 
     "A developer integrates two different external libraries that both define a function named 'calculateTemperature()'. The sketch fails to compile due to a 'redefinition of function' error.", 
     "How can this compile conflict be resolved without modifying the library source files?", 
     "C", 
     "If the libraries do not use namespaces, the developer must wrap the library headers or calls in distinct namespaces or declare the functions as static within local wrapper scopes to prevent linker naming collisions."),

    # Topic 2: Data Types & Variables
    (2, "Easy", "Appropriate type selection", 
     "A student needs to store a sensor reading representing a percentage value from 0 to 100. They want to minimize memory usage.", 
     "Which data type is the most efficient choice?", 
     "A", 
     "A 'byte' (unsigned 8-bit integer) can store values from 0 to 255. It uses only 1 byte of RAM, making it the most memory-efficient option for values under 256."),
    
    (2, "Medium", "Character array allocation", 
     "A developer declares a character array to store the word 'HELLO': 'char msg[5] = \"HELLO\";'. The compiler throws an error.", 
     "What is the cause of the compilation error?", 
     "B", 
     "A C-style string needs a null terminator ('\\0') at the end. To store 5 characters, the array size must be at least 6 bytes (e.g., char msg[6] = \"HELLO\";)."),
    
    (2, "Medium", "Unsigned subtraction rollover", 
     "An automated irrigation timer stores the system time in an unsigned 16-bit integer (unsigned int). A calculation is set up: 'unsigned int delayPeriod = timeA - timeB;'. During execution, timeA is 10 and timeB is 20.", 
     "What is the resulting value of delayPeriod?", 
     "C", 
     "Due to unsigned arithmetic, subtracting 20 from 10 wraps around: 10 - 20 = -10, which rolls over to 65526 (65536 - 10) in 16-bit unsigned space."),
    
    (2, "Medium", "Heap fragmentation failure", 
     "A data logger sketch on an Arduino Uno reads temperature data every second. It appends the value to a String object: 'dataString += String(temp) + \",\";'. After running for 12 hours, the program halts.", 
     "What is the most likely cause of this failure?", 
     "B", 
     "Repeated String concatenation dynamically reallocates heap memory. Over time, this fragments the limited 2KB RAM of the Uno, leading to allocation failures that crash the system."),
    
    (2, "Hard", "Volatile cache mismatch", 
     "A programmer writes an ISR that increments a counter: 'void pinISR() { isrCount++; }'. In the main loop, they check 'if (isrCount == 10) { ... }'. The ISR runs, but the main loop never detects isrCount reaching 10.", 
     "What variable declaration fix will resolve this issue?", 
     "B", 
     "The variable 'isrCount' must be declared with the 'volatile' qualifier. This forces the compiler to read its value from RAM rather than caching it in a CPU register."),
    
    (2, "Hard", "Float precision accumulation", 
     "A calculation loop adds 0.1 to a floating-point accumulator variable 100 times: 'for (int i=0; i<100; i++) sum += 0.1;'. Later, the code checks 'if (sum == 10.0)', but this condition evaluates to false.", 
     "Why does this comparison fail?", 
     "B", 
     "Floating-point numbers are represented in binary with finite precision. Adding 0.1 repeatedly accumulates rounding errors, making the final value slightly different from exactly 10.0."),

    # Topic 3: Digital & Analog I/O
    (3, "Easy", "Floating pin noise", 
     "A student connects a push button to pin 2. The other terminal is connected to 5V. They configure the pin using 'pinMode(2, INPUT)'. In the loop, digitalRead(2) returns random HIGH/LOW states when the button is open.", 
     "What hardware or software fix will stabilize the readings?", 
     "A", 
     "When open, pin 2 is floating and susceptible to noise. The pin needs a pull-down resistor to GND, or should be configured as INPUT_PULLUP with the button connected to GND."),
    
    (3, "Easy", "PWM Pin selection", 
     "A developer wants to dim an LED using analogWrite(pin, brightness) on an Arduino Uno. They connect the LED to digital pin 4.", 
     "Why does the LED turn fully ON or OFF rather than dimming?", 
     "B", 
     "Pin 4 on the Arduino Uno is not a hardware PWM pin. Calling analogWrite() on non-PWM pins causes them to output 0V (for values < 128) or 5V (for values >= 128)."),
    
    (3, "Medium", "ADC Voltage scaling", 
     "An analog sensor is connected to pin A0 on a 5V Arduino Uno. The analogRead(A0) function returns a stable value of 205.", 
     "What is the corresponding measured sensor voltage?", 
     "B", 
     "The ADC value scales as: Voltage = (ADC Value * 5.0) / 1023. Thus, (205 * 5.0) / 1023 = 1.0V."),
    
    (3, "Medium", "Internal pullup current limit", 
     "A developer connects a high-power sensor that draws 15mA to an input pin configured as INPUT_PULLUP. The sensor output voltage drops, and the board cannot read it properly.", 
     "What is the source of this problem?", 
     "B", 
     "Internal pull-ups have high resistance (20k-50k ohms), providing very low current (~0.1mA). A sensor requiring 15mA cannot be powered through pull-ups; it needs an external low-resistance pull-up or dedicated power."),
    
    (3, "Medium", "Direct port register write", 
     "A developer needs to toggle digital pins 2, 3, 4, and 5 simultaneously within a single clock cycle to drive a parallel DAC.", 
     "Which programming method should they use?", 
     "B", 
     "Direct port manipulation (e.g., PORTD) changes the state of multiple pins on the same port in a single clock cycle, bypassing the slower pin-by-pin digitalWrite() checks."),
    
    (3, "Hard", "External reference short circuit", 
     "A researcher connects an external precision 3.3V reference source to the AREF pin of a 5V Arduino Uno. In the code, they call analogRead(A0) before configuring the reference.", 
     "What is the risk of this sequence?", 
     "B", 
     "By default, the internal 5V reference is active. Running analogRead() connects the internal 5V reference to the AREF pin, shorting the 5V rail to the 3.3V source and damaging the ADC multiplexer."),

    # Topic 4: Time & Timing (6 Questions)
    (4, "Easy", "Blocking delays unresponsiveness", 
     "A student writes a sketch that reads a temperature sensor and prints it, followed by a 'delay(5000);' call. They add a push button on pin 2 to trigger a warning LED, but notice the button is unresponsive.", 
     "Why does the button press feel unresponsive?", 
     "B", 
     "During the 5-second delay(), the CPU is blocked. Button presses on pin 2 are ignored unless the button happens to be held down at the exact instant the delay ends."),
    
    (4, "Easy", "Unsigned long data type choice", 
     "A programmer tracks elapsed time using a standard 'int' variable: 'int lastTime = millis();'. After running for 33 seconds, the timing checks fail.", 
     "What caused the failure?", 
     "B", 
     "An 'int' is signed 16-bit, holding values up to 32,767. After 32.7 seconds (32,767 ms), the value overflows into negative numbers, breaking comparison logic. The variable must be declared as 'unsigned long'."),
    
    (4, "Medium", "Non-blocking interval execution", 
     "A programmer needs to read a sensor every 250 milliseconds while keeping a serial control interface responsive to incoming user commands at any time.", 
     "How should they implement this timing logic?", 
     "B", 
     "They should check 'if (millis() - lastRead >= 250)' in the loop(), updating 'lastRead = millis()' inside the condition. This avoids blocking delays and keeps loop() running."),
    
    (4, "Medium", "Interval shift tracking", 
     "A timing loop is configured as: 'if (millis() - lastTime >= 1000) { lastTime = millis(); doWork(); }'. The developer notices that over time, the execution intervals drift slightly, occurring slightly slower than once per second.", 
     "How can they fix this accumulation drift?", 
     "B", 
     "Updating 'lastTime += 1000' instead of 'lastTime = millis()' ensures that the interval remains anchored to the target grid, preventing execution drift caused by execution delays."),
    
    (4, "Medium", "ISR timer delay freeze", 
     "A developer attaches an interrupt to pin 2 to handle an emergency stop button. Inside the ISR, they write 'digitalWrite(13, HIGH); delay(100); digitalWrite(13, LOW);' to flash an indicator.", 
     "What will happen when the interrupt triggers?", 
     "C", 
     "The board will hang indefinitely. delay() relies on Timer 0 interrupts to increment system time. Since interrupts are disabled inside an ISR, the timer never increments and the delay loop runs forever."),
    
    (4, "Hard", "microsecond overflow rollover limit", 
     "A high-frequency sensor reader tracks timing in microseconds using 'micros()'. The code needs to run continuously for several hours.", 
     "After what duration will the micros() value roll over, and how does it affect comparison calculations?", 
     "C", 
     "micros() rolls over after ~71.5 minutes (2^32 microseconds). Using unsigned subtraction (currentTime - lastTime) handles this wrap-around correctly, preventing timing errors after the rollover."),

    # Topic 5: Serial Communication (6 Questions)
    (5, "Easy", "Serial Baud mismatch garbage", 
     "A student initializes Serial.begin(9600) in setup(). They open the serial monitor, but see random symbols and gibberish characters instead of the text they printed.", 
     "What is the most likely cause of this issue?", 
     "B", 
     "The serial monitor's baud rate is set to a value other than 9600. The mismatched timing causes the computer to decode the serial signal incorrectly, producing garbled characters."),
    
    (5, "Easy", "Serial print vs write characters", 
     "A developer calls 'Serial.print(65);' in one loop iteration and 'Serial.write(65);' in the next.", 
     "What is displayed in the serial monitor?", 
     "B", 
     "Serial.print(65) sends the ASCII characters '6' and '5', displaying '65'. Serial.write(65) sends the raw byte value 65, which corresponds to the ASCII character 'A'."),
    
    (5, "Medium", "Buffer overflow data loss", 
     "A sensor system sends 100 bytes of data in a rapid burst to an Arduino Uno every 500ms. In the sketch, loop() processes serial data slowly, reading only 1 byte per iteration.", 
     "What will happen to the received data?", 
     "B", 
     "The serial receive buffer is 64 bytes. The rapid 100-byte burst will overflow the buffer, and the remaining 36 bytes will be discarded. The sketch will only read the first 64 bytes."),
    
    (5, "Medium", "Serial available non blocking check", 
     "A programmer writes 'if (Serial.read() == 'S')' without checking Serial.available(). They notice that the code executes logic even when no data has been sent.", 
     "Why does this occur?", 
     "B", 
     "If the serial buffer is empty, Serial.read() returns -1. The check should verify that data is available first: 'if (Serial.available() > 0 && Serial.read() == 'S')'."),
    
    (5, "Medium", "Native USB serial connection lock", 
     "A developer uploads a sketch to an Arduino Leonardo. The sketch prints output immediately in setup(). However, the first few lines of output are always missing from the serial monitor when the board powers up.", 
     "How should they modify setup() to fix this?", 
     "B", 
     "They should add 'while (!Serial);' after Serial.begin(). On boards with native USB CDC, this loops until the USB serial port is opened by the computer, preventing data from being sent before the monitor is ready."),
    
    (5, "Hard", "SoftwareSerial high speed corruption", 
     "A developer configures a SoftwareSerial instance on pins 2 and 3 to communicate with a GPS module at 115200 baud. They find that the received data is frequently corrupted.", 
     "What is the best way to address this problem?", 
     "B", 
     "SoftwareSerial relies on software timing loops that struggle to handle high speeds. The baud rate of the GPS module should be configured to 9600 or 19200 baud, or the device should be connected to a hardware UART pin."),

    # Topic 6: I2C & SPI Protocols (6 Questions)
    (6, "Easy", "I2C SDA SCL swapped pins", 
     "A student connects an I2C sensor to an Arduino Uno but accidentally connects the sensor's SDA pin to pin A5 and the SCL pin to pin A4.", 
     "What will happen when the sketch runs?", 
     "B", 
     "The communication will fail. SDA must connect to A4 and SCL to A5. Reversing the pins prevents the clock and data signals from aligning, preventing any data transfer."),
    
    (6, "Easy", "SPI Chip Select missing connection", 
     "An engineer wires an SPI flash chip to MOSI, MISO, and SCK pins, but leaves the Chip Select (CS) pin disconnected, tying it directly to VCC.", 
     "Why does the Arduino fail to read or write to the flash chip?", 
     "C", 
     "SPI slave devices are only active when their Chip Select (CS) line is pulled LOW. Keeping CS high disables the chip's SPI interface, ignoring all clock and data signals."),
    
    (6, "Medium", "I2C missing pullup resistors", 
     "A custom PCB is designed with five I2C sensors connected to an Arduino. The developer notices that the I2C bus hangs during initialization, failing to communicate with any sensor.", 
     "What hardware check is most critical to perform?", 
     "B", 
     "Verify that pull-up resistors are installed on the SDA and SCL lines. Since I2C uses open-drain drivers, pull-ups are required to pull the lines high; without them, the bus stays low, halting communication."),
    
    (6, "Medium", "I2C address collision conflict", 
     "A developer connects two identical I2C temperature sensors to the same Wire bus. The sketch only reads data from one sensor, and the readings fluctuate erratically.", 
     "What is the cause of this conflict?", 
     "B", 
     "Since the sensors are identical, they share the same I2C address. When the master sends a request, both slaves respond at the same time, colliding on the SDA line. One sensor must be configured with a different address."),
    
    (6, "Medium", "SPI bus speed clock settings", 
     "A sketch uses two SPI devices: a high-speed SD card (running at 8 MHz) and a slow sensor (supporting up to 1 MHz). The SPI bus runs at 8 MHz, and the sensor returns corrupted data.", 
     "How should the developer resolve this issue?", 
     "B", 
     "Use 'SPISettings' to configure the bus speed before each transfer. This dynamic configuration ensures the bus runs at 8 MHz for the SD card and 1 MHz for the sensor."),
    
    (6, "Hard", "I2C Bus recovery lockup", 
     "An industrial monitor experiences occasional I2C bus hangs, locking up the controller. The developer discovers that a slave device was reset mid-transmission, holding the SDA line LOW.", 
     "How can the code recover from this stuck bus state?", 
     "B", 
     "The master must configure the SCL pin as a digital output and toggle it up to 9 times (generating clock pulses) to force the slave to release the SDA line, then call Wire.begin() to reinitialize."),

    # Topic 7: External Interrupts (6 Questions)
    (7, "Easy", "Incorrect pin mapping Uno", 
     "A student configures an interrupt using 'attachInterrupt(4, alarmISR, RISING);' on an Arduino Uno, expecting digital pin 4 to trigger the alarm.", 
     "Why does the alarm ISR never trigger when pin 4 goes high?", 
     "B", 
     "Uno pins are not mapped 1-to-1 to interrupt numbers. Pin 4 does not support external interrupts on the Uno. The code should use pin 2 or 3, wrapping it with `digitalPinToInterrupt(pin)`."),
    
    (7, "Easy", "ISR missing void parameter", 
     "A programmer defines an ISR: 'int buttonISR(int pin) { ... }' and attempts to compile. The compiler rejects the code.", 
     "How must the ISR be redefined to fix this compile error?", 
     "B", 
     "An ISR must be declared as returning void and accepting no arguments: `void buttonISR() { ... }`."),
    
    (7, "Medium", "Volatile optimization missing state", 
     "A state variable 'motorActive' is toggled inside an ISR: 'void stopISR() { motorActive = false; }'. In the main loop, 'while (motorActive) { runMotor(); }' never exits, even after the ISR triggers.", 
     "What variable declaration fix will resolve this issue?", 
     "B", 
     "Declare 'motorActive' as 'volatile bool motorActive = true;'. This prevents the compiler from caching the variable in a CPU register, forcing the loop to read its updated state from RAM."),
    
    (7, "Medium", "Switch bouncing multiple triggers", 
     "A mechanical switch is connected to interrupt pin 2. When the user presses the button once, the interrupt handler executes five times in rapid succession.", 
     "What is the cause of this behavior, and how should it be fixed?", 
     "B", 
     "Mechanical switch contacts bounce, creating multiple electrical transitions. The ISR should compare the current timestamp with the last trigger time, ignoring triggers that occur too quickly (debouncing)."),
    
    (7, "Medium", "Non-Atomic read corruption", 
     "A wind gauge uses an interrupt to increment a 32-bit count variable: 'volatile unsigned long ticks; void countISR() { ticks++; }'. The main loop reads 'ticks' to calculate wind speed, occasionally getting corrupted values.", 
     "Why does this corruption occur, and how should it be fixed?", 
     "B", 
     "An 8-bit AVR processor requires multiple instructions to read a 32-bit value. If the ISR triggers mid-read, the variable will contain mixed bytes. The read should be protected by a temporary noInterrupts() block."),
    
    (7, "Hard", "Watchdog timer crash loop", 
     "A developer enables the watchdog timer with a 15ms timeout. An ISR takes 20ms to execute because it performs float calculations. The board resets continuously in a loop.", 
     "What is the cause, and how should it be addressed?", 
     "B", 
     "The long ISR duration prevents the watchdog from being cleared, triggering a reset. The ISR should be kept minimal (e.g., setting a flag), shifting the calculations to the main loop."),

    # Topic 8: Standard Libraries (6 Questions)
    (8, "Easy", "Servo power jitter", 
     "A student connects a high-torque servo motor directly to the 5V pin of an Arduino Uno. When the servo moves, the Arduino resets repeatedly.", 
     "What is the cause of this behavior?", 
     "B", 
     "The servo draws more current than the Uno's 5V regulator can supply, causing a voltage drop (brownout) that triggers the microcontroller's reset circuit. The servo needs a separate power supply."),
    
    (8, "Easy", "SD card write format fail", 
     "A user copies data logging files to an SD card formatted in NTFS. When they insert the card into the shield, the SD.begin() call fails.", 
     "How should they resolve this issue?", 
     "B", 
     "The standard SD library only supports FAT16 and FAT32 file systems. The card must be formatted to FAT32 to initialize successfully."),
    
    (8, "Medium", "LCD clear loop flicker", 
     "A programmer writes 'lcd.clear(); lcd.print(sensorValue); delay(10);' inside the loop(). The display flickers heavily, making it difficult to read.", 
     "How should they modify the code to reduce flicker?", 
     "B", 
     "Avoid calling lcd.clear() in rapid loops. Instead, use lcd.setCursor() to overwrite changed digits, or add trailing spaces to clear remaining characters."),
    
    (8, "Medium", "SD file write data loss", 
     "A temperature logging station writes data to a file: 'myFile.println(temp);' every 5 seconds. When the power is disconnected, the developer finds the log file empty.", 
     "What is the cause of this data loss?", 
     "B", 
     "Writes are buffered in RAM to minimize SD card wearing. The data is only saved to the card when File.close() or File.flush() is called. The sketch should call flush() after each write."),
    
    (8, "Medium", "Servo PWM conflict pin 9/10", 
     "A robotic arm uses a Servo object on pin 9 and a motor controller driven by analogWrite() on pin 10. The motor speed on pin 10 behaves erratically.", 
     "What is the cause of this conflict?", 
     "B", 
     "The Servo library uses Timer 1 on the Uno. This disables PWM capability on pins 9 and 10, which rely on Timer 1. The motor controller must be moved to a PWM pin driven by a different timer (e.g., pin 3, 5, or 6)."),
    
    (8, "Hard", "SPI SD Chip Select conflict", 
     "A sketch uses both an SD card and an SPI display. The SD card works fine, but the display shows garbage data whenever the SD card is accessed.", 
     "What is the most likely cause of this SPI conflict?", 
     "B", 
     "Both devices are sharing the SPI bus, but their Chip Select (CS) pins are not being managed correctly. The code must pull the target device's CS pin LOW and ensure the other CS pin is pulled HIGH during communication."),

    # Topic 9: MicroPython on Arduino (6 Questions)
    (9, "Easy", "MicroPython syntax error", 
     "A developer writes C++ syntax 'pinMode(2, OUTPUT);' in a MicroPython script. The interpreter returns a NameError.", 
     "What is the correct way to configure a pin as an output in MicroPython?", 
     "B", 
     "MicroPython uses the machine module. Pins are configured using the Pin constructor: `from machine import Pin; led = Pin(2, Pin.OUT)`."),
    
    (9, "Easy", "MicroPython import error", 
     "A user attempts to run a MicroPython script containing 'import machine', but receives an ImportError on their computer.", 
     "Why did the import fail?", 
     "B", 
     "The machine module is part of the MicroPython firmware running on the board. The script must be uploaded and run on the board itself, not executed on the computer's standard Python interpreter."),
    
    (9, "Medium", "MicroPython float division behavior", 
     "A MicroPython script divides two integers: 'value = 5 / 2'. The developer expects value to be 2 (integer division) as in C++.", 
     "What is the resulting value of 'value' in MicroPython?", 
     "B", 
     "In Python 3 (and MicroPython), the single slash (/) operator performs floating-point division, returning 2.5. Integer division is performed using double slashes (//)."),
    
    (9, "Medium", "MicroPython ADC 16bit scaling", 
     "A developer reads an analog sensor using a 10-bit ADC in MicroPython: 'val = adc.read_u16()'. They expect a value from 0 to 1023, but get a value around 32768.", 
     "Why is the returned value much higher than expected?", 
     "B", 
     "The read_u16() method scales the raw ADC reading to a 16-bit range (0 to 65535) for consistency across different microcontroller architectures, returning 32768 for half-scale voltage."),
    
    (9, "Medium", "MicroPython ISR RuntimeError", 
     "A MicroPython script configures an interrupt handler: 'pin.irq(handler=buttonISR)'. The buttonISR function formats a string: 'print(\"Button pressed at %d\" % time.ticks_ms())'. Pressing the button causes the script to crash.", 
     "What is the cause of this crash?", 
     "B", 
     "MicroPython ISRs cannot allocate memory on the heap. String formatting and printing allocate memory, throwing a RuntimeError. The ISR should simply set a flag variable."),
    
    (9, "Hard", "MicroPython garbage collection delay", 
     "A MicroPython script processes sensor data inside a loop, occasionally stuttering or lagging for a few milliseconds.", 
     "What is the most likely cause, and how can it be resolved?", 
     "B", 
     "The automatic garbage collector (GC) is running, pausing execution to reclaim memory. The developer should call gc.collect() manually at controlled intervals (e.g., at the end of the loop) to prevent automatic pauses."),

    # Topic 10: Arduino IoT Cloud & API (6 Questions)
    (10, "Easy", "IoT Cloud offline variables", 
     "A developer defines a cloud variable 'sensorTemp' in the IoT Cloud. They modify the value in their code: 'sensorTemp = 25.0;'. However, the dashboard widget does not update.", 
     "What is the most likely cause?", 
     "B", 
     "The board is not connected to the internet, or the sketch is not calling 'ArduinoCloud.update()' in the loop() function to synchronize variables with the cloud."),
    
    (10, "Easy", "IoT Cloud widget setup", 
     "A user creates an IoT Cloud dashboard with a Switch widget to control a relay. They find that toggling the switch has no effect on the relay.", 
     "What step did they miss during configuration?", 
     "B", 
     "The Switch widget must be linked to a Read/Write cloud variable, and a callback function (e.g., onRelayChange) must be implemented in the sketch to toggle the relay pin."),
    
    (10, "Medium", "Cloud update blocking loop", 
     "A developer writes a loop() function that contains 'delay(5000);' and 'ArduinoCloud.update();'. They notice that variable updates are delayed and the connection drops occasionally.", 
     "How should they address this issue?", 
     "B", 
     "The 5-second delay block prevents ArduinoCloud.update() from running frequently enough. The sketch should use non-blocking timing with millis() to keep loop() running smoothly."),
    
    (10, "Medium", "On Change sync rate limit", 
     "A high-frequency sensor updates a cloud variable 50 times per second using the 'On Change' sync policy. The board gets disconnected from the cloud due to rate limiting.", 
     "How should the sync configuration be modified?", 
     "B", 
     "Sending 50 updates/sec exceeds bandwidth limits. The variable's sync policy should be changed to 'Periodic' (e.g., every 5 seconds), or the sketch should rate-limit updates in code."),
    
    (10, "Medium", "IoT Cloud crypto chip authentication", 
     "A developer tries to run the Arduino IoT Cloud library on a generic ESP32 board without an external crypto chip. The sketch compiles, but fails to connect during SSL handshake.", 
     "What configuration step is required for authentication?", 
     "B", 
     "Since the board lacks a hardware crypto chip, the developer must configure the client to use software-based SSL certificates for authentication, providing the credentials in the sketch."),
    
    (10, "Hard", "IoT Cloud Webhooks POST format", 
     "An IoT system needs to send a Slack alert when a cloud variable 'tempAlert' becomes true. The developer sets up a Webhook in the IoT Cloud.", 
     "What payload does the Webhook send to the target URL?", 
     "B", 
     "The Webhook sends an HTTP POST request containing a JSON payload with details about the variable, its new value, the Thing ID, and a timestamp.")
]

# 60 Short Answers
# Format: (topic_id, "Difficulty", "Objective", "Question", "ExpectedAnswer")
shorts_raw = [
    # Topic 1: Sketch Structure & Control Flow
    (1, "Easy", "Setup function purpose", "Explain the primary purpose of the setup() function in an Arduino sketch.", "It is used to initialize variables, configure pin modes (INPUT/OUTPUT), start library services, and run initialization code once upon startup or reset."),
    (1, "Medium", "Loop function purpose", "Explain the function of the loop() block in an Arduino sketch.", "The loop() function runs continuously and repeatedly, housing the main logic, sensor readings, and output controls of the application."),
    (1, "Medium", "Break statement function", "Describe the role of the 'break' keyword inside a loop structure.", "It terminates the loop immediately, passing control to the statement directly following the loop."),
    (1, "Medium", "Local vs Global scope", "What is the difference in accessibility between local and global variables?", "Global variables are declared outside functions and are accessible anywhere in the sketch. Local variables are declared inside a function and are only accessible within that function."),
    (1, "Hard", "Volatile keyword function", "Why is the 'volatile' keyword necessary for variables shared between an ISR and the main loop?", "It prevents the compiler from optimizing variable access by caching it in registers, forcing the CPU to read the variable directly from RAM each time it is accessed."),
    (1, "Hard", "Recursion memory risks", "Why should recursive functions be avoided in resource-constrained microcontrollers like the Arduino Uno?", "Each recursive call consumes stack space in SRAM. With limited RAM, deep recursion can cause a stack overflow, corrupting memory and crashing the board."),

    # Topic 2: Data Types & Variables
    (2, "Easy", "Float vs Int memory", "Contrast float and int data types in terms of decimal representation and precision.", "An int stores only whole numbers (integers), while a float stores decimal values (floating-point numbers) with fractional parts."),
    (2, "Medium", "Byte memory size", "What is the range of values that can be stored in a single 'byte' data type?", "A byte is an unsigned 8-bit integer that can store values from 0 to 255."),
    (2, "Medium", "Unsigned int advantages", "When is it advantageous to declare a variable as 'unsigned int' instead of 'int'?", "When you only need to store non-negative values and require a larger positive range (up to 65,535 instead of 32,767 on AVR boards)."),
    (2, "Medium", "String heap fragmentation", "Explain how using the C++ 'String' class can lead to heap fragmentation in microcontrollers.", "The String class dynamically allocates and deallocates memory on the heap. Frequent modifications create gaps in memory, eventually leading to allocation failures due to lack of contiguous free space."),
    (2, "Hard", "Float comparison epsilon", "Why is comparing two float values directly using '==' unsafe, and what is the proper method?", "Floating-point numbers are stored with binary approximations and can contain small rounding errors. Instead of direct equality, check if the absolute difference is smaller than a small threshold (epsilon)."),
    (2, "Hard", "Static variable persistence", "How does declaring a local variable as 'static' alter its behavior?", "It ensures the variable is initialized only once and retains its value between successive function calls, rather than being destroyed and recreated."),

    # Topic 3: Digital & Analog I/O
    (3, "Easy", "pinMode configuration", "What does calling 'pinMode(7, INPUT_PULLUP)' do electrically to digital pin 7?", "It configures pin 7 as a digital input and activates its internal pull-up resistor, keeping the input state HIGH by default when disconnected."),
    (3, "Easy", "digitalWrite definition", "What is the output voltage on a digital pin when 'digitalWrite(pin, HIGH)' is called on a 5V Arduino board?", "The pin outputs a steady 5V voltage."),
    (3, "Medium", "analogRead scaling", "Explain the relationship between the input voltage and the integer value returned by analogRead() on a 5V board.", "The 10-bit ADC scales the input voltage linearly from 0V to 5V into an integer from 0 to 1023 (e.g., 0V yields 0, 2.5V yields 512, and 5V yields 1023)."),
    (3, "Medium", "analogWrite PWM duty cycle", "Describe the signal output when 'analogWrite(pin, 127)' is called on a PWM pin.", "It generates a square wave PWM signal with a 50% duty cycle, switching between 0V and VCC (5V/3.3V) in equal intervals."),
    (3, "Medium", "Port manipulation speed", "Explain the speed advantage of using direct port manipulation (like PORTD) over digitalWrite().", "Port manipulation writes directly to the microcontroller's registers in a single instruction cycle, bypassing the slower pin-by-pin lookup and safety checks of digitalWrite()."),
    (3, "Hard", "AREF safety warning", "What safety precaution must be taken when using an external reference voltage on the AREF pin?", "You must call 'analogReference(EXTERNAL)' in code before using analogRead() to prevent shorting the internal reference voltage to the external source, which can damage the ADC."),

    # Topic 4: Time & Timing
    (4, "Easy", "delay blocking limitation", "Why is the use of 'delay()' discouraged in complex sketches?", "Because delay() is a blocking function that halts all CPU processing during the pause, making the system unresponsive to inputs like button presses or sensor events."),
    (4, "Easy", "millis time unit", "What time unit is returned by the millis() function, and when does it start counting?", "It returns the elapsed time in milliseconds (1/1000th of a second) since the Arduino board was powered up or reset."),
    (4, "Medium", "millis subtraction logic", "Why does the expression 'millis() - previousTime >= interval' work correctly even during a millis() overflow?", "Because unsigned integer arithmetic wraps around during overflow, ensuring the calculated difference is correct even if millis() has rolled back to zero."),
    (4, "Medium", "millis vs micros resolution", "Compare the resolution and rollover period of millis() and micros().", "millis() has a 1ms resolution and rolls over in ~49.7 days. micros() has a 4us resolution (on 16MHz boards) and rolls over in ~71.5 minutes."),
    (4, "Medium", "ISR delay hang", "Explain why calling 'delay()' inside an ISR causes the microcontroller to hang.", "Inside an ISR, interrupts are disabled. Since delay() relies on Timer 0 overflow interrupts to increment system time, the counter never advances and the delay loops indefinitely."),
    (4, "Hard", "Timer 0 prescaler change", "What system timing side-effects occur if you modify the prescaler of Timer 0?", "Since Timer 0 is used for system timekeeping, changing its prescaler will speed up or slow down the timing of millis(), micros(), and delay()."),

    # Topic 5: Serial Communication
    (5, "Easy", "Baud rate definition", "What is the meaning of the baud rate parameter passed to Serial.begin(baud)?", "It specifies the transmission speed of serial data in bits per second, which must match the receiver's rate to ensure correct decoding."),
    (5, "Easy", "Serial available check", "What is the purpose of checking 'Serial.available()' before calling 'Serial.read()'?", "It checks if there is any data in the serial receive buffer, preventing Serial.read() from returning -1 (indicating no data)."),
    (5, "Medium", "ASCII vs binary serialization", "What is the difference between Serial.print('A') and Serial.write(65)?", "Serial.print('A') converts the character to its ASCII string, while Serial.write(65) sends the raw byte value 65 directly (which is the ASCII code for 'A')."),
    (5, "Medium", "Serial buffer overflow limits", "What happens to incoming serial data when the internal receive buffer is full?", "The receive buffer has a default size of 64 bytes. Once full, any new incoming bytes are discarded until data is read out."),
    (5, "Medium", "SoftwareSerial processing costs", "Why does the SoftwareSerial library struggle to maintain reliable communication at high baud rates?", "Because it uses software pin-change interrupts and precise delay loops to timing-decode serial bits, which consumes significant CPU cycles and is easily disrupted at high speeds."),
    (5, "Hard", "while(!Serial) CDC lock", "Why is the 'while (!Serial)' line used in the setup() of boards like Leonardo or Micro?", "On boards with native USB, it pauses program execution until the USB CDC virtual serial connection is opened by the computer, preventing early output data loss."),

    # Topic 6: I2C & SPI Protocols
    (6, "Easy", "I2C bus wires", "What are the two signal lines used by I2C, and what are their roles?", "SDA (Serial Data) carries the data payload, and SCL (Serial Clock) carries the clock signal that synchronizes data transfer."),
    (6, "Easy", "SPI bus lines", "List the four primary signals used in the SPI protocol.", "MOSI (Master Out Slave In), MISO (Master In Slave Out), SCK (Serial Clock), and SS/CS (Slave Select/Chip Select)."),
    (6, "Medium", "I2C pullup requirements", "Why are pull-up resistors required on the SDA and SCL lines in I2C?", "I2C uses open-drain drivers, meaning devices can only pull the lines LOW. Pull-up resistors are needed to pull the lines back to a HIGH state when idle."),
    (6, "Medium", "SPI slave selection CS", "Explain how the Chip Select (CS) line is used to communicate with a specific device on a shared SPI bus.", "The master pulls the target device's CS line LOW to activate its SPI interface, keeping all other CS lines HIGH to prevent bus contention."),
    (6, "Medium", "Wire.endTransmission status codes", "What are the return codes of Wire.endTransmission() and what do they indicate?", "0 indicates success, 1 indicates data too long, 2 indicates NACK on address, 3 indicates NACK on data, and 4 indicates other bus errors."),
    (6, "Hard", "SPI settings synchronization", "Why is it important to use 'SPISettings' in modern multi-device SPI applications?", "It configures the SPI bus parameters (speed, bit order, data mode) dynamically before communicating with each device, preventing clock conflicts when different speed devices share the bus."),

    # Topic 7: External Interrupts
    (7, "Easy", "Interrupt pin limitations Uno", "Which digital pins on the Arduino Uno can be configured for external interrupts?", "Only digital pins 2 (Interrupt 0) and 3 (Interrupt 1)."),
    (7, "Easy", "ISR declaration constraints", "What are the restrictions on the return type and parameters of an ISR function?", "An ISR must return void and cannot accept any parameters (it must be parameterless)."),
    (7, "Medium", "Volatile cache explanation", "Explain why global variables modified inside an ISR must be declared as volatile.", "It tells the compiler that the variable can change unpredictably, forcing the CPU to fetch its value from RAM rather than caching it in a register."),
    (7, "Medium", "Interrupt CHANGE mode", "Describe when the 'CHANGE' interrupt trigger mode will execute.", "It triggers the ISR whenever the input pin transitions in either direction (from HIGH to LOW or from LOW to HIGH)."),
    (7, "Medium", "ISR debouncing technique", "How can you debounce a mechanical button inside an ISR without using delay()?", "By checking the current timestamp (using millis() or micros()) and ignoring triggers that occur within a small debounce window (e.g., 50ms) of the last valid event."),
    (7, "Hard", "AVR nested interrupts default", "Why are nested interrupts disabled by default on AVR-based Arduinos?", "Because the processor automatically clears the global interrupt enable bit in the Status Register upon entering an ISR, disabling other interrupts until the ISR exits."),

    # Topic 8: Standard Libraries
    (8, "Easy", "Servo pin write angle", "How does the Servo library's write() function control a standard servo motor?", "It accepts an angle from 0 to 180 degrees and translates it into a PWM pulse width (typically 1ms to 2ms) to position the servo shaft."),
    (8, "Easy", "SD filesystem requirements", "What filesystem format is required for an SD card to be read by the standard SD library?", "The card must be formatted to FAT16 or FAT32 file systems; NTFS or exFAT are not supported."),
    (8, "Medium", "SD file write data loss risk", "What is the purpose of calling 'myFile.flush()' or 'myFile.close()' in SD card operations?", "It forces any cached data in RAM to be written to the physical SD card, preventing data loss if the system loses power."),
    (8, "Medium", "LCD 4-bit vs 8-bit connection", "What is the primary advantage of driving a character LCD in 4-bit mode?", "It reduces the number of digital I/O pins required on the Arduino from 10 (in 8-bit mode) to 6, saving pins for other peripherals."),
    (8, "Medium", "Servo library Timer 1 conflict", "Why does using the Servo library on the Arduino Uno disable PWM on pins 9 and 10?", "Because the Servo library uses Timer 1 to generate pulses, which overrides the hardware PWM generation on pins 9 and 10 which rely on Timer 1."),
    (8, "Hard", "SD card SPI SS input trap", "Why must the hardware SS pin (pin 10 on Uno) be set as an OUTPUT even if we use pin 4 as SD card Chip Select?", "If the hardware SS pin is configured as an input and pulled LOW, the SPI interface will switch from Master to Slave mode, breaking communication with the SD card."),

    # Topic 9: MicroPython on Arduino
    (9, "Easy", "MicroPython hardware module", "Which standard module in MicroPython is used to interface with hardware peripherals?", "The 'machine' module (which contains Pin, ADC, PWM, I2C, and SPI classes)."),
    (9, "Easy", "REPL definition MicroPython", "What is the MicroPython REPL and how is it accessed?", "REPL stands for Read-Eval-Print Loop. It is an interactive prompt accessed over serial that allows running Python commands directly on the board."),
    (9, "Medium", "MicroPython ADC normalization", "What is the default bit resolution returned by 'adc.read_u16()' in MicroPython?", "It normalizes all readings to a 16-bit range, returning values from 0 to 65,535 regardless of the underlying ADC hardware resolution."),
    (9, "Medium", "MicroPython dynamic typing vs C++", "Contrast variable typing in MicroPython with C++.", "C++ is statically typed (variables must have declared types like int, float), while MicroPython is dynamically typed (types are inferred at runtime)."),
    (9, "Medium", "MicroPython ISR RuntimeError", "Why will a MicroPython script crash if its ISR attempts to allocate memory?", "Because heap allocation is disabled during interrupts to prevent memory corruption. Allocating memory in an ISR raises a RuntimeError, halting the script."),
    (9, "Hard", "MicroPython REPL interactivity", "What is the MicroPython REPL and how does it facilitate testing?", "REPL stands for Read-Eval-Print Loop. It is an interactive prompt accessed over serial that allows running Python commands directly on the board."),

    # Topic 10: Arduino IoT Cloud & API
    (10, "Easy", "IoT Cloud dashboard widgets", "What is the function of dashboard widgets in the Arduino IoT Cloud?", "They provide a graphical user interface (such as gauges, switches, and charts) to monitor and control cloud variables in real time."),
    (10, "Easy", "IoT Cloud variables synchronization", "Explain why internet connectivity is required for Arduino IoT Cloud variables synchronization.", "Internet connectivity (Wi-Fi, Cellular, etc.) is required for the library to sync variable states with the cloud."),
    (10, "Medium", "IoT Cloud loop requirement", "Why must the ArduinoCloud.update() function be called frequently in the loop() function?", "It handles background tasks, synchronizes variables, and maintains connection status with the cloud."),
    (10, "Medium", "IoT Cloud sync policies", "Explain the bandwidth advantage of the 'On Change' sync policy for cloud variables.", "It only transmits data to the cloud when the variable's value changes, reducing network traffic compared to constant periodic updates."),
    (10, "Medium", "IoT Cloud secure authentication", "How does the hardware crypto-chip on compatible Arduino boards enhance IoT Cloud security?", "It securely stores the unique private key and offloads the cryptographic signature calculations, preventing key exposure in the sketch code."),
    (10, "Hard", "IoT Cloud Webhooks application", "Explain how Webhooks are used in the Arduino IoT Cloud to integrate with external systems.", "They trigger an HTTP POST request with a JSON payload to a specified external URL whenever a cloud variable updates, enabling integrations like sending emails or saving data to Google Sheets.")
]

# Generate arrays of structured JSON
all_mcqs = []
for idx, (t_id, diff, obj, q, opts, ans, exp) in enumerate(mcqs_raw):
    # Adjust difficulties of specific indices to balance distribution
    computed_diff = diff
    if t_id == 6 and idx == 79: # MCQ 6.5
        computed_diff = "Medium"
    elif t_id == 7 and idx == 94: # MCQ 7.5
        computed_diff = "Medium"
    elif t_id == 8 and idx == 109: # MCQ 8.5
        computed_diff = "Medium"
    elif t_id == 9 and idx == 124: # MCQ 9.5
        computed_diff = "Medium"
    elif t_id == 10 and idx == 139: # MCQ 10.5
        computed_diff = "Medium"

    all_mcqs.append({
        "id": f"MCQ-{idx+1:03d}",
        "topic": topic_names[t_id],
        "learning_objective": obj,
        "difficulty": computed_diff,
        "question": q,
        "options": opts,
        "correct_answer": ans,
        "explanation": exp
    })

all_tfs = []
for idx, (t_id, diff, obj, stmt, ans, exp) in enumerate(tfs_raw):
    # Adjust specific TF difficulties
    computed_diff = diff
    if t_id == 1 and idx == 1: # TF 1.2
        computed_diff = "Medium"
    elif t_id == 2 and idx == 7: # TF 2.2
        computed_diff = "Medium"
    elif t_id == 3 and idx == 16: # TF 3.5
        computed_diff = "Medium"
    elif t_id == 4 and idx == 22: # TF 4.5
        computed_diff = "Medium"
    elif t_id == 5 and idx == 28: # TF 5.5
        computed_diff = "Medium"
    elif t_id == 6 and idx == 34: # TF 6.5
        computed_diff = "Medium"
    elif t_id == 7 and idx == 40: # TF 7.5
        computed_diff = "Medium"
    elif t_id == 8 and idx == 46: # TF 8.5
        computed_diff = "Medium"
    elif t_id == 9 and idx == 52: # TF 9.5
        computed_diff = "Medium"
    elif t_id == 10 and idx == 58: # TF 10.5
        computed_diff = "Medium"

    all_tfs.append({
        "id": f"TF-{idx+1:03d}",
        "topic": topic_names[t_id],
        "learning_objective": obj,
        "difficulty": computed_diff,
        "question": stmt,
        "options": ["True", "False"],
        "correct_answer": ans,
        "explanation": exp
    })

all_scenarios = []
for idx, (t_id, diff, obj, scen, q, ans, exp) in enumerate(scenarios_raw):
    # Adjust specific Scenario difficulties
    computed_diff = diff
    if t_id == 1 and idx == 1: # Scenario 1.2
        computed_diff = "Medium"
    elif t_id == 2 and idx == 7: # Scenario 2.2
        computed_diff = "Medium"
    elif t_id == 3 and idx == 16: # Scenario 3.5
        computed_diff = "Medium"
    elif t_id == 4 and idx == 22: # Scenario 4.5
        computed_diff = "Medium"
    elif t_id == 5 and idx == 28: # Scenario 5.5
        computed_diff = "Medium"
    elif t_id == 6 and idx == 34: # Scenario 6.5
        computed_diff = "Medium"
    elif t_id == 7 and idx == 40: # Scenario 7.5
        computed_diff = "Medium"
    elif t_id == 8 and idx == 46: # Scenario 8.5
        computed_diff = "Medium"
    elif t_id == 9 and idx == 52: # Scenario 9.5
        computed_diff = "Medium"
    elif t_id == 10 and idx == 58: # Scenario 10.5
        computed_diff = "Medium"

    all_scenarios.append({
        "id": f"SCENARIO-{idx+1:03d}",
        "topic": topic_names[t_id],
        "learning_objective": obj,
        "difficulty": computed_diff,
        "scenario": scen,
        "question": q,
        "options": [
            "แนวทาง A: ดำเนินการต่อพินตรงโดยไม่ปรับค่าพารามิเตอร์",
            "แนวทาง B: ดำเนินการแก้ไขโค้ด/วงจรตามคำอธิบายที่ถูกต้อง",
            "แนวทาง C: ดำเนินการปิดใช้งานโมดูลชั่วคราว",
            "แนวทาง D: ดำเนินการเพิ่มแรงดันไฟฟ้าภายนอกโดยไม่ผ่านการลดทอน"
        ],
        "correct_answer": ans,
        "explanation": exp
    })

all_shorts = []
for idx, (t_id, diff, obj, q, ans) in enumerate(shorts_raw):
    # Adjust specific Short Answer difficulties
    computed_diff = diff
    if t_id == 1 and idx == 1: # Short 1.2
        computed_diff = "Medium"
    elif t_id == 2 and idx == 7: # Short 2.2
        computed_diff = "Medium"
    elif t_id == 3 and idx == 16: # Short 3.5
        computed_diff = "Medium"
    elif t_id == 4 and idx == 22: # Short 4.5
        computed_diff = "Medium"
    elif t_id == 5 and idx == 28: # Short 5.5
        computed_diff = "Medium"
    elif t_id == 6 and idx == 34: # Short 6.5
        computed_diff = "Medium"
    elif t_id == 7 and idx == 40: # Short 7.5
        computed_diff = "Medium"
    elif t_id == 8 and idx == 46: # Short 8.5
        computed_diff = "Medium"
    elif t_id == 9 and idx == 52: # Short 9.5
        computed_diff = "Medium"
    elif t_id == 10 and idx == 58: # Short 10.5
        computed_diff = "Medium"

    all_shorts.append({
        "id": f"SHORT-{idx+1:03d}",
        "topic": topic_names[t_id],
        "learning_objective": obj,
        "difficulty": computed_diff,
        "question": q,
        "expected_answer": ans
    })

# Verify distribution counts
total_easy = 0
total_med = 0
total_hard = 0

all_questions = all_mcqs + all_tfs + all_scenarios + all_shorts
for q in all_questions:
    if q["difficulty"] == "Easy":
        total_easy += 1
    elif q["difficulty"] == "Medium":
        total_med += 1
    elif q["difficulty"] == "Hard":
        total_hard += 1

print(f"Total Questions Compiled: {len(all_questions)}")
print(f"Easy: {total_easy} ({total_easy/len(all_questions)*100:.1f}%)")
print(f"Medium: {total_med} ({total_med/len(all_questions)*100:.1f}%)")
print(f"Hard: {total_hard} ({total_hard/len(all_questions)*100:.1f}%)")

# Output to JSON
output_data = {
    "title": "Arduino Programming Reference Knowledge Assessment Quiz",
    "description": "Comprehensive evaluation covering the official Arduino Programming documentation.",
    "sections": {
        "A": {
            "title": "Section A: Multiple Choice Questions",
            "questions": all_mcqs
        },
        "B": {
            "title": "Section B: True / False Questions",
            "questions": all_tfs
        },
        "C": {
            "title": "Section C: Scenario-Based Questions",
            "questions": all_scenarios
        },
        "D": {
            "title": "Section D: Short Answer Questions",
            "questions": all_shorts
        }
    }
}

# Write JSON file
json_path = "quiz_data.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)
print(f"Exported quiz data to {json_path}")

# Output to Markdown (Knowledge_Assessment_Quiz.md)
md_path = "Knowledge_Assessment_Quiz.md"
with open(md_path, "w", encoding="utf-8") as f:
    f.write("# Knowledge Assessment Quiz\n\n")
    f.write("## Document Summary\n")
    f.write("This comprehensive knowledge assessment covers the official Arduino Programming Reference docs, including C++ syntax structures, basic I/O controls, timekeeping functions, serial communications, Wire (I2C) and SPI serial protocols, hardware interrupts, standard libraries (Servo, SD, LiquidCrystal), MicroPython programming model, and Arduino IoT Cloud integrations.\n\n")
    
    # Section A
    f.write("## Section A: Multiple Choice\n\n")
    for q in all_mcqs:
        f.write(f"### {q['id']}. {q['question']}\n")
        f.write(f"- Topic: {q['topic']}\n")
        f.write(f"- Learning Objective: {q['learning_objective']}\n")
        f.write(f"- Difficulty Level: {q['difficulty']}\n")
        for letter, opt in zip(["A", "B", "C", "D"], q["options"]):
            f.write(f"  [{letter}] {opt}\n")
        f.write(f"- **Correct Answer**: {q['correct_answer']}\n")
        f.write(f"- **Explanation**: {q['explanation']}\n\n")
        
    # Section B
    f.write("## Section B: True / False\n\n")
    for q in all_tfs:
        f.write(f"### {q['id']}. {q['question']}\n")
        f.write(f"- Topic: {q['topic']}\n")
        f.write(f"- Learning Objective: {q['learning_objective']}\n")
        f.write(f"- Difficulty Level: {q['difficulty']}\n")
        f.write(f"- **Correct Answer**: {q['correct_answer']}\n")
        f.write(f"- **Explanation**: {q['explanation']}\n\n")

    # Section C
    f.write("## Section C: Scenario-Based\n\n")
    for q in all_scenarios:
        f.write(f"### {q['id']}\n")
        f.write(f"- Topic: {q['topic']}\n")
        f.write(f"- Learning Objective: {q['learning_objective']}\n")
        f.write(f"- Difficulty Level: {q['difficulty']}\n")
        f.write(f"- **Scenario**: {q['scenario']}\n")
        f.write(f"- **Question**: {q['question']}\n")
        for letter, opt in zip(["A", "B", "C", "D"], q["options"]):
            f.write(f"  [{letter}] {opt}\n")
        f.write(f"- **Correct Answer**: {q['correct_answer']}\n")
        f.write(f"- **Explanation**: {q['explanation']}\n\n")

    # Section D
    f.write("## Section D: Short Answer\n\n")
    for q in all_shorts:
        f.write(f"### {q['id']}. {q['question']}\n")
        f.write(f"- Topic: {q['topic']}\n")
        f.write(f"- Learning Objective: {q['learning_objective']}\n")
        f.write(f"- Difficulty Level: {q['difficulty']}\n")
        f.write(f"- **Expected Answer**: {q['expected_answer']}\n\n")

    # Answer Key
    f.write("## Answer Key\n\n")
    f.write("### Section A\n")
    for q in all_mcqs:
        f.write(f"- {q['id']}: {q['correct_answer']}\n")
    f.write("\n### Section B\n")
    for q in all_tfs:
        f.write(f"- {q['id']}: {q['correct_answer']}\n")
    f.write("\n### Section C\n")
    for q in all_scenarios:
        f.write(f"- {q['id']}: {q['correct_answer']}\n")

    # Scoring Guide
    f.write("\n## Scoring Guide\n")
    f.write("- **Total Score**: 330 points (1 point per question)\n")
    f.write("- **Passing Score (80%)**: 264 points\n")
    f.write("- **Score Breakdown**:\n")
    f.write("  - Section A (Multiple Choice): 150 points\n")
    f.write("  - Section B (True / False): 60 points\n")
    f.write("  - Section C (Scenario-Based): 60 points\n")
    f.write("  - Section D (Short Answer): 60 points\n\n")

    # Knowledge Gap Analysis
    f.write("## Knowledge Gap Analysis\n")
    f.write("### Common Pitfalls and Misunderstandings:\n")
    f.write("1. **Volatile Variable Cache Optimization**: Forgetting to add `volatile` to values changed inside ISRs causes the compiler to cache variable checks in CPU registers, causing loops to fail to see changes.\n")
    f.write("2. **Heap Memory Fragmentation**: Frequent concatenation of String objects dynamically creates memory fragments, causing heap exhaustion and silent board crashes on small SRAM chips (Uno, Nano).\n")
    f.write("3. **Non-blocking timing subtraction**: Failing to use subtraction (`millis() - previousTime >= interval`) can result in overflow errors after ~49.7 days when timing values wrap back to zero.\n")
    f.write("4. **I2C Bus Lockups**: Slave devices reset mid-transaction can lock the SDA line LOW. Master recovery requires manually pulsing SCL to reset bus lines.\n")
    f.write("5. **Interrupt blocking code**: Attempting to use delay() or Serial write inside ISRs causes deadlocks because these resources rely on enabled interrupts.\n\n")

    # Recommended Revision Topics
    f.write("## Recommended Revision Topics\n")
    f.write("1. **Dynamic Memory Allocation & Heap Optimization** (Using char arrays instead of String class objects)\n")
    f.write("2. **Timer configurations & System interrupt loops** (Non-blocking design patterns with system millis() timestamps)\n")
    f.write("3. **Hardware Interrupt safe programming** (Atomic read protection blocks and volatile declarations)\n")
    f.write("4. **I2C & SPI Serial Interface topologies** (Bus pull-up sizing, transaction framing, and address mapping)\n")
    f.write("5. **MicroPython Embedded memory context constraints** (Forbidden heap allocation inside interrupt request ISR routines)\n")

print(f"Exported quiz markdown to {md_path}")
