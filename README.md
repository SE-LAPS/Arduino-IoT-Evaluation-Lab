# Arduino IoT Evaluation Lab
## Sensor Monitoring & Actuator Control with Arduino Uno R3

![Arduino IoT](https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Version](https://img.shields.io/badge/Version-1.0-green.svg)

This project demonstrates a complete IoT evaluation system using Arduino Uno R3 that integrates multiple sensors and actuators to create an intelligent environmental monitoring and control system.

## 🎯 Project Objectives

- **Distance Measurement**: Monitor proximity using HC-SR04 ultrasonic sensor
- **Environmental Monitoring**: Track temperature and humidity with DHT22 sensor
- **Smart LED Control**: Visual feedback based on proximity detection
- **Motor Control**: Automated fan control based on environmental conditions
- **IoT Integration**: Combine all components into a unified system

## 🔧 Hardware Requirements

### Components
- **Arduino Uno R3** - Main microcontroller
- **HC-SR04 Ultrasonic Sensor** - Distance measurement
- **DHT22 Temperature/Humidity Sensor** - Environmental monitoring
- **5mm LED** - Visual indicator
- **220Ω Resistor** - LED current limiting
- **5V DC Motor with Fan** (≤250mA) - Actuator control
- **10kΩ Resistor** - DHT22 pull-up (if not included on breakout)
- **Breadboard** - Circuit assembly
- **Jumper Wires** - Connections
- **USB Cable** (Type-A to Type-B) - Programming and power

### Optional
- **NPN Transistor** (TIP120) or **MOSFET** - For safe motor control
- **Flyback Diode** - Motor protection

## 📊 Pin Configuration

| Component | Arduino Pin | Function | Notes |
|-----------|-------------|----------|-------|
| HC-SR04 VCC | 5V | Power | 5V supply |
| HC-SR04 GND | GND | Ground | Common ground |
| HC-SR04 Trig | D7 | Output | Trigger pulse |
| HC-SR04 Echo | D6 | Input | Echo detection |
| DHT22 VCC | 5V | Power | 5V supply |
| DHT22 GND | GND | Ground | Common ground |
| DHT22 Data | D2 | Digital I/O | With 10kΩ pull-up |
| LED Anode | D9 | Output | Through 220Ω resistor |
| LED Cathode | GND | Ground | Common ground |
| Motor VCC | 5V | Power | Direct connection |
| Motor GND | GND | Ground | Common ground |
| Motor Control | D3 | Output | Optional transistor control |

## 🚀 Getting Started

### 1. Environment Setup
```bash
# Install Arduino IDE (if not already installed)
# Download from: https://www.arduino.cc/en/software

# Install required libraries:
# 1. Open Arduino IDE
# 2. Go to Sketch → Include Library → Manage Libraries
# 3. Search and install:
#    - "DHT sensor library" by Adafruit
#    - "Adafruit Unified Sensor"
```

### 2. Wiring the Circuit

#### HC-SR04 Connections
```
HC-SR04    →    Arduino Uno
VCC        →    5V
GND        →    GND  
Trig       →    D7
Echo       →    D6
```

#### DHT22 Connections
```
DHT22      →    Arduino Uno
VCC        →    5V
GND        →    GND
Data       →    D2 (with 10kΩ pull-up to 5V)
```

#### LED Circuit
```
LED        →    Arduino Uno
Anode      →    220Ω Resistor → D9
Cathode    →    GND
```

#### Motor Circuit
```
Motor      →    Arduino Uno
VCC        →    5V
GND        →    GND
Control    →    D3 (through transistor - optional)
```

### 3. Programming Steps

1. **Test Individual Components** (Parts B, C, D)
2. **Upload Combined System** (Part E)
3. **Monitor Serial Output** (9600 baud)
4. **Verify Functionality**

## 📂 Code Structure

### Part B: Distance Sensor Test
- Basic HC-SR04 functionality
- Serial output of distance measurements
- 500ms update interval

### Part C: Environmental Sensor Test
- DHT22 temperature and humidity reading
- Error handling for sensor failures
- 2-second update interval

### Part D: Actuator Test
- LED blinking pattern
- Motor continuous operation
- Basic I/O verification

### Part E: Integrated IoT System
- **Smart Proximity Detection**: LED activates when objects < 10cm
- **Environmental Monitoring**: Continuous temp/humidity tracking
- **Intelligent Motor Control**: Auto-off when humidity > 80%
- **Serial Monitoring**: Real-time data display

## 🎛️ System Behavior

### Normal Operation
```
Distance: 25 cm    Temp: 23.5 °C  Humidity: 45.2 %
Motor: ON
```

### Proximity Alert
```
Distance: 8 cm     Temp: 23.7 °C  Humidity: 46.1 %
Motor: ON
[LED: ON - Object detected within 10cm]
```

### High Humidity Response
```
Distance: 15 cm    Temp: 24.1 °C  Humidity: 82.3 %
Motor: OFF (High Humidity)
[Automatic motor shutdown for safety]
```

## 🔍 Troubleshooting

### Common Issues

| Problem | Possible Cause | Solution |
|---------|----------------|----------|
| No distance readings | Wiring error | Check Trig/Echo connections |
| DHT22 errors | Missing pull-up resistor | Add 10kΩ resistor between Data and 5V |
| LED not responding | Incorrect polarity | Check anode/cathode orientation |
| Motor not spinning | Insufficient power | Verify 5V connection and current draw |
| Erratic readings | Loose connections | Secure all jumper wires |

### Sensor Calibration
- **Distance**: Accuracy ±1-2cm, range 2-400cm
- **Temperature**: ±0.5°C accuracy, -40°C to +80°C range  
- **Humidity**: ±2-5% accuracy, 0-100% RH range

## 📋 Lab Deliverables

### Required Submissions
1. **Serial Monitor Screenshot** - Showing all sensor readings and motor status
2. **Hardware Photo** - Clear image of wired breadboard setup
3. **Technical Report** - 1-2 paragraphs covering:
   - Individual sensor performance analysis
   - Troubleshooting steps taken
   - Answers to final observation questions

### Evaluation Checklist
- [ ] HC-SR04 provides accurate distance measurements
- [ ] DHT22 reports temperature and humidity values
- [ ] LED responds to proximity (< 10cm threshold)
- [ ] Motor control responds to humidity levels
- [ ] Serial Monitor displays all data correctly
- [ ] All wiring is secure and properly documented

## 🔬 Advanced Extensions

### Optional Improvements
- **LCD Display** - Add 16x2 LCD for standalone operation
- **Data Logging** - Store readings to SD card
- **WiFi Connectivity** - ESP8266/ESP32 integration for remote monitoring
- **Mobile App** - Bluetooth communication for smartphone control
- **Multiple Sensors** - Add more environmental sensors
- **Web Dashboard** - Real-time data visualization

### Code Enhancements
- **PID Control** - Smooth motor speed regulation
- **Calibration Routines** - Auto-calibration procedures
- **Error Recovery** - Robust error handling and recovery
- **Configuration Mode** - Adjustable thresholds via serial commands

## 🛡️ Safety Considerations

⚠️ **Important Safety Notes**
- Never exceed Arduino's current limits (40mA per pin, 200mA total)
- Use appropriate resistors for LED circuits
- Consider using transistors for motor control to prevent damage
- Ensure proper grounding for all components
- Double-check polarity before powering on

## 📚 Learning Outcomes

After completing this lab, you will understand:
- **Sensor Integration** - How to combine multiple sensor types
- **Digital I/O Control** - Managing actuators with Arduino
- **Serial Communication** - Debug and monitor system performance  
- **Conditional Logic** - Implementing intelligent system responses
- **IoT Fundamentals** - Basic concepts of connected device systems

## 🤝 Contributing

Feel free to submit improvements, bug fixes, or additional features:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify all wiring connections
3. Ensure libraries are properly installed
4. Review serial monitor for error messages

---

**Happy Coding!** 🚀

*Built with ❤️ for Arduino IoT learning*
