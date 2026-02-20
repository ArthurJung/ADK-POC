"""Mock product catalog, orders, and support contacts."""

PRODUCTS = {
    "AC-001": {
        "id": "AC-001",
        "name": "CoolBreeze 9000 BTU Inverter Air Conditioner",
        "category": "Air Conditioners",
        "brand": "CoolBreeze",
        "price": 12900.0,
        "currency": "THB",
        "in_stock": True,
        "specs": {
            "cooling_capacity": "9000 BTU",
            "type": "Inverter",
            "energy_rating": "5 stars",
            "room_size": "12-18 sq.m.",
            "noise_level": "26 dB (indoor)",
            "refrigerant": "R32",
            "wifi_control": True,
            "warranty": "10 years compressor, 2 years parts",
        },
        "description": (
            "Energy-efficient inverter air conditioner with 9000 BTU cooling capacity. "
            "Inverter technology adjusts compressor speed continuously for precise "
            "temperature control and up to 40% energy savings compared to fixed-speed units. "
            "Features quiet operation at 26 dB and Wi-Fi smart control."
        ),
    },
    "AC-002": {
        "id": "AC-002",
        "name": "CoolBreeze 12000 BTU Fixed-Speed Air Conditioner",
        "category": "Air Conditioners",
        "brand": "CoolBreeze",
        "price": 8900.0,
        "currency": "THB",
        "in_stock": True,
        "specs": {
            "cooling_capacity": "12000 BTU",
            "type": "Fixed-speed",
            "energy_rating": "3 stars",
            "room_size": "18-25 sq.m.",
            "noise_level": "38 dB (indoor)",
            "refrigerant": "R32",
            "wifi_control": False,
            "warranty": "5 years compressor, 1 year parts",
        },
        "description": (
            "Affordable fixed-speed air conditioner with 12000 BTU cooling power. "
            "Suitable for medium to large rooms. Fixed-speed compressor runs at full "
            "power and cycles on/off to maintain temperature. Lower upfront cost but "
            "higher energy consumption than inverter models."
        ),
    },
    "TV-001": {
        "id": "TV-001",
        "name": 'VisionPro 55" 4K OLED Smart TV',
        "category": "Televisions",
        "brand": "VisionPro",
        "price": 34900.0,
        "currency": "THB",
        "in_stock": True,
        "specs": {
            "screen_size": '55"',
            "resolution": "4K Ultra HD (3840 x 2160)",
            "panel_type": "OLED",
            "refresh_rate": "120 Hz",
            "hdr": "Dolby Vision, HDR10+",
            "smart_platform": "Google TV",
            "hdmi_ports": "4 (HDMI 2.1)",
            "speakers": "40W Dolby Atmos",
            "warranty": "2 years",
        },
        "description": (
            "Premium 55-inch 4K OLED Smart TV with self-emitting pixels for perfect "
            "blacks and infinite contrast. 120Hz refresh rate ideal for gaming and sports. "
            "Dolby Vision and HDR10+ support for cinematic viewing. Built-in Google TV "
            "with access to all major streaming apps."
        ),
    },
    "PH-001": {
        "id": "PH-001",
        "name": "TechMax Pro 256GB Smartphone",
        "category": "Smartphones",
        "brand": "TechMax",
        "price": 29900.0,
        "currency": "THB",
        "in_stock": False,
        "restock_date": "2026-03-15",
        "specs": {
            "display": '6.7" AMOLED, 144Hz',
            "processor": "Snapdragon 8 Gen 3",
            "ram": "12 GB",
            "storage": "256 GB",
            "camera": "200MP main + 50MP ultrawide + 12MP telephoto",
            "battery": "5500 mAh, 120W fast charge",
            "os": "Android 15",
            "water_resistance": "IP68",
            "warranty": "1 year",
        },
        "description": (
            "Flagship smartphone with 200MP camera system and 6.7-inch AMOLED display "
            "at 144Hz. Powered by Snapdragon 8 Gen 3 with 12GB RAM for demanding apps "
            "and games. 5500mAh battery with 120W fast charging (0-100% in 25 minutes). "
            "Currently out of stock — restock expected March 2026."
        ),
    },
    "WM-001": {
        "id": "WM-001",
        "name": "CleanMaster 10kg Front Load Washing Machine",
        "category": "Washing Machines",
        "brand": "CleanMaster",
        "price": 15900.0,
        "currency": "THB",
        "in_stock": True,
        "specs": {
            "capacity": "10 kg",
            "type": "Front Load",
            "spin_speed": "1400 RPM",
            "energy_rating": "4.5 stars",
            "wash_programs": 16,
            "steam_wash": True,
            "inverter_motor": True,
            "noise_level": "52 dB (wash) / 70 dB (spin)",
            "warranty": "12 years motor, 2 years parts",
        },
        "description": (
            "Large-capacity 10kg front-load washing machine with inverter direct-drive "
            "motor for quiet, efficient operation. 16 wash programs including steam wash "
            "for deep sanitization. 1400 RPM spin speed for faster drying. Smart sensor "
            "auto-adjusts water and detergent levels."
        ),
    },
    "SH-001": {
        "id": "SH-001",
        "name": "TrailBlazer X2 Trail Running Shoes",
        "category": "Footwear",
        "brand": "TrailBlazer",
        "price": 4290.0,
        "currency": "THB",
        "in_stock": True,
        "specs": {
            "type": "Trail Running",
            "upper_material": "Engineered mesh with TPU overlays",
            "sole": "Vibram Megagrip outsole",
            "cushioning": "Dual-density EVA + gel heel insert",
            "drop": "6mm",
            "weight": "285g (US men's 9)",
            "waterproof": "Water-resistant (DWR coating)",
            "available_sizes": "US 6-13",
            "colors": ["Black/Orange", "Grey/Blue", "Green/Black"],
            "warranty": "6 months",
        },
        "description": (
            "High-performance trail running shoes with Vibram Megagrip outsole for "
            "superior traction on wet and dry terrain. Engineered mesh upper with TPU "
            "overlays for breathability and support. Dual-density EVA midsole with gel "
            "heel insert for impact absorption on rocky trails. 6mm drop for natural "
            "running form."
        ),
    },
    # -----------------------------------------------------------------------
    # Laptops
    # -----------------------------------------------------------------------
    "LP-001": {
        "id": "LP-001",
        "name": 'ByteForce Pro 15.6" Laptop',
        "category": "Laptops",
        "brand": "ByteForce",
        "price": 42900.0,
        "currency": "THB",
        "in_stock": True,
        "specs": {
            "display": '15.6" IPS, 2560x1440, 165Hz',
            "processor": "Intel Core i7-14700H",
            "gpu": "NVIDIA RTX 4060 8GB",
            "ram": "16 GB DDR5",
            "storage": "512 GB NVMe SSD",
            "battery": "72 Wh, up to 7 hours",
            "weight": "2.1 kg",
            "os": "Windows 11 Home",
            "ports": "2x USB-C (Thunderbolt 4), 3x USB-A, HDMI 2.1, SD card",
            "warranty": "2 years",
        },
        "description": (
            "Versatile performance laptop with 14th-gen Intel Core i7 and RTX 4060 "
            "graphics. 15.6-inch QHD display at 165Hz for smooth visuals in gaming "
            "and creative work. 16GB DDR5 RAM and 512GB NVMe SSD for fast multitasking. "
            "Thunderbolt 4 connectivity and 72Wh battery for all-day productivity."
        ),
    },
    "LP-002": {
        "id": "LP-002",
        "name": 'ByteForce Air 14" Ultrabook',
        "category": "Laptops",
        "brand": "ByteForce",
        "price": 27900.0,
        "currency": "THB",
        "in_stock": True,
        "specs": {
            "display": '14" OLED, 2880x1800, 90Hz',
            "processor": "Intel Core Ultra 7 155H",
            "gpu": "Intel Arc integrated",
            "ram": "16 GB LPDDR5x",
            "storage": "512 GB NVMe SSD",
            "battery": "75 Wh, up to 12 hours",
            "weight": "1.29 kg",
            "os": "Windows 11 Home",
            "ports": "2x USB-C (Thunderbolt 4), 1x USB-A, HDMI 2.0",
            "warranty": "2 years",
        },
        "description": (
            "Ultra-thin 14-inch laptop with stunning OLED display at 2880x1800 "
            "resolution. Weighs just 1.29kg for maximum portability. Intel Core Ultra 7 "
            "with NPU for AI-accelerated tasks. 75Wh battery delivers up to 12 hours "
            "of use. Ideal for professionals and students who need premium quality on the go."
        ),
    },
    # -----------------------------------------------------------------------
    # Headphones
    # -----------------------------------------------------------------------
    "HP-001": {
        "id": "HP-001",
        "name": "SoundWave Pro ANC Wireless Headphones",
        "category": "Headphones",
        "brand": "SoundWave",
        "price": 8990.0,
        "currency": "THB",
        "in_stock": True,
        "specs": {
            "type": "Over-ear, Wireless",
            "driver_size": "40mm",
            "frequency_response": "20Hz - 40kHz",
            "anc": "Adaptive Active Noise Cancellation",
            "battery": "30 hours (ANC on), 45 hours (ANC off)",
            "charging": "USB-C, 5 min = 3 hours playback",
            "bluetooth": "5.3 with multipoint (2 devices)",
            "codec": "LDAC, AAC, SBC",
            "weight": "250g",
            "warranty": "1 year",
        },
        "description": (
            "Premium wireless headphones with adaptive noise cancellation that adjusts "
            "to your environment. 40mm custom drivers deliver rich, detailed audio with "
            "Hi-Res support via LDAC codec. 30 hours of battery life with ANC on. "
            "Multipoint Bluetooth 5.3 lets you switch between two devices seamlessly. "
            "Quick charge gives 3 hours of playback from just 5 minutes of charging."
        ),
    },
    "HP-002": {
        "id": "HP-002",
        "name": "SoundWave Buds Pro True Wireless Earbuds",
        "category": "Headphones",
        "brand": "SoundWave",
        "price": 4490.0,
        "currency": "THB",
        "in_stock": False,
        "restock_date": "2026-02-28",
        "specs": {
            "type": "In-ear, True Wireless",
            "driver_size": "11mm",
            "frequency_response": "20Hz - 20kHz",
            "anc": "Hybrid Active Noise Cancellation",
            "battery": "8 hours (buds), 32 hours (with case)",
            "charging": "USB-C, Qi wireless charging",
            "bluetooth": "5.3",
            "codec": "AAC, SBC",
            "water_resistance": "IPX5",
            "weight": "5.4g per earbud",
            "warranty": "1 year",
        },
        "description": (
            "Compact true wireless earbuds with hybrid ANC and 11mm drivers for deep "
            "bass. IPX5 water resistance makes them suitable for workouts and rainy "
            "commutes. 8 hours of listening per charge with an additional 24 hours from "
            "the wireless-charging case. Lightweight at just 5.4g per earbud for "
            "all-day comfort. Currently out of stock — restock expected late February 2026."
        ),
    },
    # -----------------------------------------------------------------------
    # Refrigerators
    # -----------------------------------------------------------------------
    "RF-001": {
        "id": "RF-001",
        "name": "FrostKing 415L Inverter Two-Door Refrigerator",
        "category": "Refrigerators",
        "brand": "FrostKing",
        "price": 18900.0,
        "currency": "THB",
        "in_stock": True,
        "specs": {
            "capacity": "415 litres (295L fridge / 120L freezer)",
            "type": "Two-door, top freezer",
            "compressor": "Inverter linear",
            "energy_rating": "5 stars",
            "cooling_system": "Multi-airflow",
            "noise_level": "35 dB",
            "dimensions": "690 x 1780 x 720 mm (W x H x D)",
            "features": "Door cooling+, humidity crisper, LED lighting",
            "warranty": "10 years compressor, 2 years parts",
        },
        "description": (
            "Spacious 415-litre two-door refrigerator with inverter linear compressor "
            "for energy-efficient, quiet operation at just 35 dB. Multi-airflow cooling "
            "keeps every corner at a consistent temperature. Door cooling+ delivers "
            "cold air directly to the door shelves to keep beverages chilled. Humidity "
            "controlled crisper drawer keeps fruits and vegetables fresh longer."
        ),
    },
    "RF-002": {
        "id": "RF-002",
        "name": "FrostKing 550L Side-by-Side Refrigerator with Water Dispenser",
        "category": "Refrigerators",
        "brand": "FrostKing",
        "price": 32900.0,
        "currency": "THB",
        "in_stock": True,
        "specs": {
            "capacity": "550 litres (350L fridge / 200L freezer)",
            "type": "Side-by-side",
            "compressor": "Digital inverter",
            "energy_rating": "4 stars",
            "cooling_system": "Twin cooling plus",
            "ice_maker": "Automatic ice and water dispenser",
            "noise_level": "39 dB",
            "dimensions": "912 x 1780 x 716 mm (W x H x D)",
            "smart_features": "Wi-Fi, touchscreen panel",
            "warranty": "10 years compressor, 2 years parts",
        },
        "description": (
            "Premium 550-litre side-by-side refrigerator with twin cooling system that "
            "maintains independent temperature and humidity in fridge and freezer "
            "compartments. Built-in water and ice dispenser. Wi-Fi connectivity and "
            "touchscreen control panel for smart home integration. Digital inverter "
            "compressor ensures energy efficiency and quiet performance."
        ),
    },
    # -----------------------------------------------------------------------
    # Tablets
    # -----------------------------------------------------------------------
    "TB-001": {
        "id": "TB-001",
        "name": 'TechMax Tab S10 11" Tablet',
        "category": "Tablets",
        "brand": "TechMax",
        "price": 18900.0,
        "currency": "THB",
        "in_stock": True,
        "specs": {
            "display": '11" LCD, 2560x1600, 120Hz',
            "processor": "Dimensity 9200+",
            "ram": "8 GB",
            "storage": "128 GB (expandable via microSD)",
            "camera": "13MP rear + 8MP front",
            "battery": "8600 mAh, 45W fast charge",
            "os": "Android 15",
            "connectivity": "Wi-Fi 6E, Bluetooth 5.3",
            "stylus_support": True,
            "weight": "500g",
            "warranty": "1 year",
        },
        "description": (
            "Versatile 11-inch tablet with 120Hz LCD display for smooth scrolling and "
            "drawing. Dimensity 9200+ chipset with 8GB RAM handles multitasking and "
            "split-screen apps with ease. 8600mAh battery lasts up to 14 hours of video "
            "playback. Supports stylus input for note-taking and creative work. "
            "Expandable storage via microSD for extra flexibility."
        ),
    },
    "TB-002": {
        "id": "TB-002",
        "name": 'TechMax Tab Pro 12.4" Tablet',
        "category": "Tablets",
        "brand": "TechMax",
        "price": 32900.0,
        "currency": "THB",
        "in_stock": False,
        "restock_date": "2026-04-01",
        "specs": {
            "display": '12.4" Super AMOLED, 2800x1752, 120Hz',
            "processor": "Snapdragon 8 Gen 3",
            "ram": "12 GB",
            "storage": "256 GB",
            "camera": "13MP rear + 12MP ultrawide front",
            "battery": "10090 mAh, 45W fast charge",
            "os": "Android 15",
            "connectivity": "Wi-Fi 7, Bluetooth 5.3, optional 5G",
            "stylus_support": True,
            "keyboard_support": True,
            "weight": "565g",
            "warranty": "1 year",
        },
        "description": (
            "Professional-grade 12.4-inch tablet with Super AMOLED display for vivid "
            "colours and deep blacks. Powered by Snapdragon 8 Gen 3 with 12GB RAM for "
            "desktop-class performance. Supports keyboard attachment and stylus for a "
            "full laptop replacement experience. 10090mAh battery delivers up to 16 hours "
            "of use. Currently out of stock — restock expected April 2026."
        ),
    },
    # -----------------------------------------------------------------------
    # Cameras
    # -----------------------------------------------------------------------
    "CM-001": {
        "id": "CM-001",
        "name": "LensArt Z50 Mirrorless Camera (Body Only)",
        "category": "Cameras",
        "brand": "LensArt",
        "price": 38900.0,
        "currency": "THB",
        "in_stock": True,
        "specs": {
            "sensor": "26.1 MP APS-C CMOS",
            "processor": "EXPEED 7",
            "iso_range": "100-51200 (expandable to 204800)",
            "autofocus": "209-point hybrid AF, eye/animal detection",
            "video": "4K 30fps, 1080p 120fps",
            "stabilization": "5-axis in-body (IBIS), 4.5 stops",
            "viewfinder": "2.36M-dot OLED EVF",
            "display": '3.2" vari-angle touchscreen',
            "card_slot": "Single SD UHS-II",
            "weight": "405g (body only)",
            "warranty": "2 years",
        },
        "description": (
            "Compact mirrorless camera with 26.1MP APS-C sensor and EXPEED 7 processor "
            "for fast, accurate performance. 209-point hybrid autofocus with eye and "
            "animal detection keeps subjects sharp. 5-axis in-body stabilization for "
            "steady handheld shooting. 4K video recording and vari-angle touchscreen "
            "make it ideal for content creators and photography enthusiasts."
        ),
    },
    # -----------------------------------------------------------------------
    # Additional Television
    # -----------------------------------------------------------------------
    "TV-002": {
        "id": "TV-002",
        "name": 'VisionPro 43" 4K LED Smart TV',
        "category": "Televisions",
        "brand": "VisionPro",
        "price": 12900.0,
        "currency": "THB",
        "in_stock": True,
        "specs": {
            "screen_size": '43"',
            "resolution": "4K Ultra HD (3840 x 2160)",
            "panel_type": "LED (VA panel)",
            "refresh_rate": "60 Hz",
            "hdr": "HDR10",
            "smart_platform": "Google TV",
            "hdmi_ports": "3 (HDMI 2.0)",
            "speakers": "20W stereo",
            "warranty": "2 years",
        },
        "description": (
            "Budget-friendly 43-inch 4K LED Smart TV with VA panel for good contrast "
            "in dimly lit rooms. HDR10 support for enhanced colour and brightness. "
            "Built-in Google TV gives access to Netflix, YouTube, and thousands of apps. "
            "Three HDMI ports for connecting gaming consoles, streaming devices, and "
            "soundbars. Great option for bedrooms and smaller living spaces."
        ),
    },
    # -----------------------------------------------------------------------
    # Additional Smartphone
    # -----------------------------------------------------------------------
    "PH-002": {
        "id": "PH-002",
        "name": "TechMax Lite 128GB Smartphone",
        "category": "Smartphones",
        "brand": "TechMax",
        "price": 9990.0,
        "currency": "THB",
        "in_stock": True,
        "specs": {
            "display": '6.5" IPS LCD, 90Hz',
            "processor": "Snapdragon 6 Gen 1",
            "ram": "6 GB",
            "storage": "128 GB (expandable via microSD)",
            "camera": "50MP main + 8MP ultrawide + 2MP macro",
            "battery": "5000 mAh, 33W fast charge",
            "os": "Android 15",
            "water_resistance": "IP54",
            "warranty": "1 year",
        },
        "description": (
            "Affordable mid-range smartphone with a 6.5-inch 90Hz display for smooth "
            "everyday use. Snapdragon 6 Gen 1 processor with 6GB RAM handles social "
            "media, messaging, and casual gaming. 50MP main camera captures detailed "
            "photos in good light. 5000mAh battery with 33W charging lasts a full day. "
            "Expandable storage via microSD for users who need extra space."
        ),
    },
    # -----------------------------------------------------------------------
    # Additional Footwear
    # -----------------------------------------------------------------------
    "SH-002": {
        "id": "SH-002",
        "name": "UrbanStep Classic Leather Sneakers",
        "category": "Footwear",
        "brand": "UrbanStep",
        "price": 3490.0,
        "currency": "THB",
        "in_stock": True,
        "specs": {
            "type": "Casual Sneaker",
            "upper_material": "Full-grain leather",
            "sole": "Rubber cupsole",
            "cushioning": "OrthoLite insole",
            "drop": "10mm",
            "weight": "340g (US men's 9)",
            "waterproof": "No",
            "available_sizes": "US 6-12",
            "colors": ["White", "White/Navy", "Black"],
            "warranty": "6 months",
        },
        "description": (
            "Minimalist leather sneakers for everyday casual wear. Full-grain leather "
            "upper develops a natural patina over time. OrthoLite insole provides "
            "cushioning and moisture management for all-day comfort. Durable rubber "
            "cupsole with herringbone tread for reliable grip on city streets. Clean, "
            "versatile design pairs with jeans, chinos, or casual suits."
        ),
    },
    # -----------------------------------------------------------------------
    # Robot Vacuums
    # -----------------------------------------------------------------------
    "RV-001": {
        "id": "RV-001",
        "name": "CleanMaster RoboVac X1 Robot Vacuum & Mop",
        "category": "Robot Vacuums",
        "brand": "CleanMaster",
        "price": 14900.0,
        "currency": "THB",
        "in_stock": True,
        "specs": {
            "suction_power": "5500 Pa",
            "navigation": "LiDAR + 3D structured light",
            "battery": "5200 mAh, up to 180 min runtime",
            "dustbin": "400 ml (auto-empty dock included)",
            "water_tank": "200 ml (electronic water control)",
            "mopping": "Vibrating mop pad, 3000 RPM",
            "noise_level": "65 dB (standard mode)",
            "mapping": "Multi-floor mapping, no-go zones",
            "smart_features": "Wi-Fi, app control, voice assistant compatible",
            "warranty": "2 years",
        },
        "description": (
            "Advanced robot vacuum and mop combo with 5500Pa suction and LiDAR navigation "
            "for precise room mapping. Auto-empty dock holds up to 60 days of dust. "
            "Vibrating mop pad at 3000 RPM tackles sticky stains on hard floors. "
            "Creates multi-floor maps with customisable no-go zones via the smartphone "
            "app. 180-minute runtime covers large homes in a single charge."
        ),
    },
}

ORDERS = {
    "ORD-10001": {
        "order_id": "ORD-10001",
        "customer_name": "Somchai",
        "product_id": "AC-001",
        "product_name": "CoolBreeze 9000 BTU Inverter Air Conditioner",
        "status": "shipped",
        "tracking_number": "TH20260205XYZ",
        "carrier": "Kerry Express",
        "estimated_delivery": "2026-02-12",
        "order_date": "2026-02-05",
    },
    "ORD-10002": {
        "order_id": "ORD-10002",
        "customer_name": "Nari",
        "product_id": "TV-001",
        "product_name": 'VisionPro 55" 4K OLED Smart TV',
        "status": "processing",
        "tracking_number": None,
        "carrier": None,
        "estimated_delivery": "2026-02-14",
        "order_date": "2026-02-08",
    },
    "ORD-10003": {
        "order_id": "ORD-10003",
        "customer_name": "Lek",
        "product_id": "SH-001",
        "product_name": "TrailBlazer X2 Trail Running Shoes",
        "status": "delivered",
        "tracking_number": "TH20260201ABC",
        "carrier": "Flash Express",
        "estimated_delivery": "2026-02-04",
        "delivered_date": "2026-02-03",
        "order_date": "2026-02-01",
    },
}

SUPPORT_DEPARTMENTS = {
    "returns": {
        "department": "Returns & Refunds",
        "phone": "02-123-4567 ext. 1",
        "email": "returns@shop-demo.example",
        "hours": "Mon-Fri 9:00-18:00",
    },
    "warranty": {
        "department": "Warranty & Repairs",
        "phone": "02-123-4567 ext. 2",
        "email": "warranty@shop-demo.example",
        "hours": "Mon-Fri 9:00-18:00",
    },
    "delivery": {
        "department": "Delivery & Logistics",
        "phone": "02-123-4567 ext. 3",
        "email": "delivery@shop-demo.example",
        "hours": "Mon-Sat 8:00-20:00",
    },
    "payment": {
        "department": "Payment & Billing",
        "phone": "02-123-4567 ext. 4",
        "email": "billing@shop-demo.example",
        "hours": "Mon-Fri 9:00-17:00",
    },
    "general": {
        "department": "General Inquiries",
        "phone": "02-123-4567",
        "email": "support@shop-demo.example",
        "hours": "Mon-Sun 8:00-22:00",
    },
}
