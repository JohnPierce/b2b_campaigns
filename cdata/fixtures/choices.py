# choices.py

SEMI_DESIGN_FLOW_CHOICES = [
    ('HLS_FLOW', 'High-Level Synthesis Flow'),
    ('RTL_FLOW', 'RTL Design Flow'),
    ('FUNC_VER_FLOW', 'Functional Verification Flow'),
    ('SYNTH_FLOW', 'Synthesis Flow'),
    ('PLACE_ROUTE_FLOW', 'Place and Route Flow'),
    ('TIMING_ANAL_FLOW', 'Timing Analysis Flow'),
    ('PHYS_VER_FLOW', 'Physical Verification Flow'),
    ('SOC_FLOW', 'System-on-Chip (SoC) Design Flow'),
    ('MCM_FLOW', 'Multi-Chip Module (MCM) Design Flow'),
    ('PCB_FLOW', 'Printed Circuit Board (PCB) Design Flow'),
    ('HARD_IP_FLOW', 'Hard IP Core Flow'),
    ('SOFT_IP_FLOW', 'Soft IP Core Flow'),
    ('FIRM_IP_FLOW', 'Firm IP Core Flow'),
    ('ANALOG_CIRC_FLOW', 'Analog Circuit Design Flow'),
    ('MIXED_SIGNAL_FLOW', 'Mixed-Signal Design Flow'),
    ('FULL_CUSTOM_FLOW', 'Full Custom Design Flow'),
    ('EMBED_SYS_FLOW', 'Embedded Systems Design Flow'),
    ('LOW_POWER_FLOW', 'Low-Power Design Flow'),
    ('TEST_VER_FLOW', 'Test and Verification Flow'),
]


COMPANY_CHOICES = [
    ('aero', 'Aerospace Corporation'),
    ('afferex', 'Afferex'),
    ('acrhon', 'Achronix Semiconductor Corporation'),
    ('alpha', 'Alphabet Inc'),
    ('alphaw', 'Alphawave IP'),
    ('amz', 'Amazoncom'),
    ('amd', 'AMD - Advanced Micro Devices Inc'),
    ('analog', 'Aanalog Devices Inc.'),
    ('apple', 'Apple Inc'),
    ('argonne', 'Argonne National Laboratory'),
    ('atlazo', 'Atlazo'),
    ('ayar', 'Ayar Labs'),
    ('bae', 'BAE Systems'),
    ('belden', 'Belden Inc'),
    ('blacksesame', 'Black Sesame Technologies Shanghai Co Ltd'),
    ('bluespec', 'Bluespec Inc'),
    ('boeing', 'Boeing Co'),
    ('broadcom', 'Broadcom Limited'),
    ('brookhaven', 'Brookhaven National Laboratory'),
    ('bytedance', 'ByteDance'),
    ('ciena', 'Ciena Corp'),
    ('cirrus', 'Cirrus Logic Inc'),
    ('cirtec', 'Cirtec Medical Systems LLC'),
    ('cisco', 'Cisco Systems Inc'),
    ('compound photonics', 'Compound Photonics LTD'),
    ('cruise', 'Cruise Automation'),
    ('diamler', 'Daimler AG'),
    ('deepvision', 'Deep Vision AI'),
    ('epicblock', 'Epic Blockchain Technologies'),
    ('epson', 'Epson'),
    ('ericsson', 'Ericsson Inc'),
    ('Etopus', 'Etopus Technology'),
    ('f5net', 'F5 Networks'),
	('intel', 'Intel Corp.'),
	('msft', 'Microsoft'),
	('nvda', 'Nvidia'),
]

SEMICONDUCTOR_PLATFORM_CHOICES = [
    # TSMC process nodes
    ('TSMC 180nm', 'TSMC 180nm'),
    ('TSMC 130nm', 'TSMC 130nm'),
    ('TSMC 90nm', 'TSMC 90nm'),
    ('TSMC 65nm', 'TSMC 65nm'),
    ('TSMC 40nm', 'TSMC 40nm'),
    ('TSMC 28nm', 'TSMC 28nm'),
    ('TSMC 20nm', 'TSMC 20nm'),
    ('TSMC 16nm', 'TSMC 16nm'),
    ('TSMC 10nm', 'TSMC 10nm'),
    ('TSMC 7nm', 'TSMC 7nm'),
    ('TSMC 7nm LPP', 'TSMC 7nm LPP'),
    ('TSMC 5nm', 'TSMC 5nm'),
    ('TSMC 3nm', 'TSMC 3nm'),
    ('TSMC 2nm', 'TSMC 2nm'),
    ('TSMC 1.4nm', 'TSMC 1.4nm'),

    # Samsung process nodes
    ('Samsung 14nm LPP', 'Samsung 14nm LPP'),
    ('Samsung 10nm', 'Samsung 10nm'),
    ('Samsung 7nm', 'Samsung 7nm'),
    ('Samsung 5nm', 'Samsung 5nm'),
    ('Samsung 3nm', 'Samsung 3nm'),
    ('Samsung 2nm', 'Samsung 2nm'),
    ('Samsung 1.4nm', 'Samsung 1.4nm'),

    # UMC process nodes
    ('UMC 180nm', 'UMC 180nm'),
    ('UMC 90nm', 'UMC 90nm'),
    ('UMC 65nm', 'UMC 65nm'),
    ('UMC 40nm', 'UMC 40nm'),
    ('UMC 28nm', 'UMC 28nm'),

    # TowerJazz process nodes
    ('TowerJazz 180nm', 'TowerJazz 180nm'),
    ('TowerJazz 130nm', 'TowerJazz 130nm'),
    ('TowerJazz 65nm', 'TowerJazz 65nm'),

    # Intel process nodes
    ('Intel 22nm', 'Intel 22nm'),
    ('Intel 14nm', 'Intel 14nm'),
    ('Intel 10SF', 'Intel 10SF'),
    ('Intel 7', 'Intel 7'),
    ('Intel 4', 'Intel 4'),
    ('Intel 3', 'Intel 3'),
    ('Intel 20A', 'Intel 20A'),
    ('Intel 18A', 'Intel 18A'),

    # GlobalFoundries process nodes
    ('GlobalFoundries 28nm', 'GlobalFoundries 28nm'),
    ('GlobalFoundries 14nm', 'GlobalFoundries 14nm'),
    ('GlobalFoundries 12nm', 'GlobalFoundries 12nm'),
    ('GlobalFoundries 7nm', 'GlobalFoundries 7nm'),

    # FPGA platforms
    ('Xilinx Virtex', 'Xilinx Virtex'),
    ('Xilinx Kintex', 'Xilinx Kintex'),
    ('Xilinx Artix', 'Xilinx Artix'),
    ('Xilinx Zynq', 'Xilinx Zynq'),
    ('Xilinx Spartan', 'Xilinx Spartan'),

    ('Altera Cyclone', 'Altera Cyclone'),
    ('Altera Arria', 'Altera Arria'),
    ('Altera Stratix', 'Altera Stratix'),

    ('Microsemi ProASIC3', 'Microsemi ProASIC3'),
    ('Microsemi IGLOO', 'Microsemi IGLOO'),
]