from graphviz import Digraph

# Define diagrams for each of the four setups

def create_hcsr04_diagram():
    dot = Digraph(comment='HC-SR04 Ultrasonic Sensor Wiring')
    dot.attr(rankdir='LR')
    dot.node('A', 'Arduino Uno')
    dot.node('S', 'HC-SR04 Sensor')
    dot.edges([('A', 'S')])
    dot.edge('A', 'S', label='5V → VCC')
    dot.edge('A', 'S', label='GND → GND')
    dot.edge('A', 'S', label='D7 → Trig')
    dot.edge('A', 'S', label='D6 → Echo')
    return dot

def create_dht22_diagram():
    dot = Digraph(comment='DHT22 Sensor Wiring')
    dot.attr(rankdir='LR')
    dot.node('A', 'Arduino Uno')
    dot.node('D', 'DHT22 Sensor')
    dot.edge('A', 'D', label='5V → VCC')
    dot.edge('A', 'D', label='GND → GND')
    dot.edge('A', 'D', label='D2 → Data\n(+10kΩ Pull-up to 5V)')
    return dot

def create_led_motor_diagram():
    dot = Digraph(comment='LED and Motor Wiring')
    dot.attr(rankdir='LR')
    dot.node('A', 'Arduino Uno')
    dot.node('L', 'LED + 220Ω Resistor')
    dot.node('M', '5V Motor')
    dot.edge('A', 'L', label='D9 → Anode')
    dot.edge('L', 'A', label='Cathode → GND')
    dot.edge('A', 'M', label='5V → Motor +')
    dot.edge('M', 'A', label='Motor - → GND')
    return dot

def create_combined_diagram():
    dot = Digraph(comment='Combined IoT Circuit')
    dot.attr(rankdir='LR')
    dot.node('A', 'Arduino Uno')
    dot.node('H', 'HC-SR04')
    dot.node('D', 'DHT22')
    dot.node('L', 'LED + Resistor')
    dot.node('T', 'Transistor\n(e.g., TIP120)')
    dot.node('M', '5V Motor')
    dot.edge('A', 'H', label='D7 → Trig\nD6 → Echo\n5V/GND')
    dot.edge('A', 'D', label='D2 → Data\n(+10kΩ)\n5V/GND')
    dot.edge('A', 'L', label='D9 → Anode\nCathode → GND')
    dot.edge('A', 'T', label='D3 → Base')
    dot.edge('T', 'M', label='Collector → Motor -')
    dot.edge('M', 'T', label='Motor + → 5V')
    dot.edge('T', 'A', label='Emitter → GND\n+ Flyback Diode')
    return dot

# Generate all diagrams
diagrams = {
    "hcsr04": create_hcsr04_diagram(),
    "dht22": create_dht22_diagram(),
    "led_motor": create_led_motor_diagram(),
    "combined": create_combined_diagram()
}

# Save as PDFs
pdf_paths = []
for name, diagram in diagrams.items():
    path = f"/mnt/data/{name}_diagram.pdf"
    diagram.render(filename=path, format='pdf', cleanup=True)
    pdf_paths.append(path + ".pdf")

pdf_paths
