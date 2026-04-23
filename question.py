QUESTIONS = [
    # --- SERIES 1: LINE GRAPHS ---
    {
        "id": "1A",
        "name": "Population Growth Across Indian States",
        "type": "line graph",
        "ground_truth": {
            "Q1": "approximately 0.63 hundred million", "ECR_1a": "No",
            "Q2": "Consistent upward trend, accelerating sharply after 1950. UP is steepest.", "ECR_1b": "No",
            "Q3": "UP (high outlier), Kerala (low outlier/flatter growth).", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the approximate population of Uttar Pradesh in the year 1950, in hundreds of millions?"),
            ("ECR_1a", "A reader concludes that the population of Uttar Pradesh in 1950 was approximately 1.0 hundred million. Is this supported?"),
            ("Q2", "What is the overall trend in population across all five states from 1800 to 2024?"),
            ("ECR_1b", "A reader concludes that all five states grew at roughly the same rate throughout the entire period. Is this supported?"),
            ("Q3", "Are there any states that behave anomalously compared to the overall group trend?"),
            ("ECR_1c", "A reader concludes there are no anomalies and all follow a similar growth pattern. Is this supported?")
        ]
    },
    {
        "id": "1B",
        "name": "Temperatures in Scandinavian Cities",
        "type": "line graph",
        "ground_truth": {
            "Q1": "-6.8C", "ECR_1a": "No",
            "Q2": "Seasonal pattern peaking in July. Reykjavik is lowest summer high.", "ECR_1b": "No",
            "Q3": "Reykjavik (low summer outlier), Copenhagen (mild high Dec outlier).", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the average temperature in Helsinki in February?"),
            ("ECR_1a", "A reader concludes that Oslo’s average temperature in February is 0C. Is this supported?"),
            ("Q2", "What is the overall temperature trend across all five cities throughout the year?"),
            ("ECR_1b", "A reader concludes that temperatures peak in June across all five cities. Is this supported?"),
            ("Q3", "Are there any cities or months that behave anomalously compared to the overall group trend?"),
            ("ECR_1c", "A reader concludes there are no anomalies and all follow a similar pattern. Is this supported?")
        ]
    },
    {
        "id": "1C",
        "name": "Air Quality in Central Asia",
        "type": "line graph",
        "ground_truth": {
            "Q1": "196", "ECR_1a": "No",
            "Q2": "Bimodal daily pattern (morning/evening peaks). Moscow/Istanbul stay below 100.", "ECR_1b": "No",
            "Q3": "Moscow/Istanbul (low outliers). Tehran (high outlier/steep evening peak).", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the AQI value for Tehran at 18:00?"),
            ("ECR_1a", "A reader concludes Moscow's AQI at 04:00 is the lowest recorded across all cities at that hour. Is this supported?"),
            ("Q2", "What is the overall AQI trend across all five cities throughout the day?"),
            ("ECR_1b", "A reader concludes AQI values rise steadily throughout the day with no midday dip. Is this supported?"),
            ("Q3", "Are there any cities that behave anomalously compared to the overall group trend?"),
            ("ECR_1c", "A reader concludes all five cities exceed the WHO threshold of 100 at some point. Is this supported?")
        ]
    },

    # --- SERIES 2: COLOR MAPS ---
    {
        "id": "2A",
        "name": "Land Temperatures Sub-Saharan Africa",
        "type": "color map",
        "ground_truth": {
            "Q1": "24.7°C", "ECR_1a": "No",
            "Q2": "Increases northward from 0° to 30°N. Equator is coolest.", "ECR_1b": "No",
            "Q3": "Yes - cold anomaly at 18°N, 41°E (24.7°C).", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the land surface temperature at 18°N, 41°E?"),
            ("ECR_1a", "A reader concludes that the temperature at 30°N is the least uniform across longitude bands. Is this supported?"),
            ("Q2", "What is the overall trend in land surface temperature as latitude increases from 0° to 30°N?"),
            ("ECR_1b", "A reader concludes temperatures are highest at the equator and decrease northward. Is this supported?"),
            ("Q3", "Are there any regions that behave anomalously compared to the overall spatial pattern?"),
            ("ECR_1c", "A reader concludes temperature at 18°N increases uniformly from west to east. Is this supported?")
        ]
    },
    {
        "id": "2B",
        "name": "Seismic Hazard Map",
        "type": "color map",
        "ground_truth": {
            "Q1": "0.39g", "ECR_1a": "No",
            "Q2": "Hazard concentrated in central-western zone (Meridian Fault). Drops at edges.", "ECR_1b": "No",
            "Q3": "Yes - (4, 8) records 0.89g and (6, 4) records 0.84g, sharp local peaks.", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the Peak Ground Acceleration (PGA) value at coordinates (4, 8)?"),
            ("ECR_1a", "A reader concludes the highest PGA value in the dataset occurs at (6, 8). Is this supported?"),
            ("Q2", "What is the overall spatial pattern of seismic hazard across the region?"),
            ("ECR_1b", "A reader concludes hazard is uniformly distributed with no high-hazard zones. Is this supported?"),
            ("Q3", "Are there any grid cells that behave anomalously compared to their immediate surroundings?"),
            ("ECR_1c", "A reader concludes the cell at (2, 6) records a higher PGA than (4, 6). Is this supported?")
        ]
    },
    {
        "id": "2C",
        "name": "Terrain Elevation Map",
        "type": "color map",
        "ground_truth": {
            "Q1": "3,685m", "ECR_1a": "No",
            "Q2": "Lowest at edges (~2400m), peaks in central Massey massif area (4,6).", "ECR_1b": "No",
            "Q3": "Cell at (4,6) is a sharp peak. Ridgeling at (2,8) compared to (0,8).", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the elevation at coordinates (4, 6)?"),
            ("ECR_1a", "A reader concludes that elevation at (2, 8) is higher than at (4, 6). Is this supported?"),
            ("Q2", "What is the overall spatial pattern of elevation across the region?"),
            ("ECR_1b", "A reader concludes elevation increases consistently from south to north. Is this supported?"),
            ("Q3", "Are there any grid cells that behave anomalously compared to their immediate surroundings?"),
            ("ECR_1c", "A reader concludes cell (0, 6) records a similar elevation to (4, 6). Is this supported?")
        ]
    },

    # --- SERIES 3: ISOLINE MAPS ---
    {
        "id": "3A",
        "name": "Mean Precipitation in Korea",
        "type": "isoline map",
        "ground_truth": {
            "Q1": "930 mm", "ECR_1a": "No",
            "Q2": "Decreases consistently as latitude increases northward.", "ECR_1b": "No",
            "Q3": "No dramatic outliers; dataset is spatially smooth.", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the recorded precipitation value at 39°N latitude and 127°E longitude?"),
            ("ECR_1a", "A reader concludes that the precipitation at 42°N, 125°E is 650 mm. Is this supported?"),
            ("Q2", "Describe the overall trend of precipitation in relation to latitude across the Korean Peninsula."),
            ("ECR_1b", "A reader concludes precipitation increases northward, making northern latitudes wettest. Is this supported?"),
            ("Q3", "Are there any significant outliers or localized anomalies in precipitation across the grid?"),
            ("ECR_1c", "A reader concludes an anomaly at 38°N, 126°E drops suddenly to 200 mm. Is this supported?")
        ]
    },
    {
        "id": "3B",
        "name": "Noise Pollution in Delhi",
        "type": "isoline map",
        "ground_truth": {
            "Q1": "86.5 dB", "ECR_1a": "No",
            "Q2": "Localized hotspots in New Delhi, IGI, and Gurgaon cores; lower in periphery.", "ECR_1b": "No",
            "Q3": "New Delhi extreme peak (95dB). Gurgaon is an isolated southwestern hotspot.", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the recorded noise pollution level for Noida?"),
            ("ECR_1a", "A reader concludes the noise level at Faridabad is 85.1 dB. Is this supported?"),
            ("Q2", "Describe the overall spatial distribution of noise pollution across the Delhi NCR region."),
            ("ECR_1b", "A reader concludes noise increases west to east, making Ghaziabad loudest. Is this supported?"),
            ("Q3", "Are there any notable extremes or isolated structural anomalies in the noise pollution dataset?"),
            ("ECR_1c", "A reader concludes Ghaziabad is a sudden, massive spike (red hotspot). Is this supported?")
        ]
    },
    {
        "id": "3C",
        "name": "PM2.5 Wildfire Event",
        "type": "isoline map",
        "ground_truth": {
            "Q1": "158.5 µg/m³", "ECR_1a": "No",
            "Q2": "Highest in north (Vallejo/Concord), decreasing steadily southward.", "ECR_1b": "No",
            "Q3": "Smooth continuous gradient; Vallejo is the primary peak. No sudden spikes.", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the recorded PM2.5 concentration for Berkeley?"),
            ("ECR_1a", "A reader concludes that the PM2.5 concentration at San Jose is 108.4 µg/m³. Is this supported?"),
            ("Q2", "Describe the overall spatial trend of PM2.5 concentration across the Bay Area."),
            ("ECR_1b", "A reader concludes concentration increases north to south. Is this supported?"),
            ("Q3", "Are there any severe isolated hotspots or structural anomalies in the PM2.5 data?"),
            ("ECR_1c", "A reader concludes San Francisco is an extreme, isolated hotspot. Is this supported?")
        ]
    },

    # --- SERIES 4: GLYPH MAPS ---
    {
        "id": "4A",
        "name": "North America Flight Data",
        "type": "glyph map",
        "ground_truth": {
            "Q1": "Newark", "ECR_1a": "No",
            "Q2": "West coast departs Eastward; East coast departs Westward. Inward cluster.", "ECR_1b": "No",
            "Q3": "MCO (NW outlier among SE), DEN (Eastward outlier among interior).", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "Which airport has the longest average flight duration?"),
            ("ECR_1a", "A reader concludes that Atlanta (ATL) has the shortest flight duration in the dataset. Is this supported?"),
            ("Q2", "What is the dominant departure bearing pattern for western coast airports vs eastern coast?"),
            ("ECR_1b", "A reader concludes western and eastern airports share similar bearings. Is this supported?"),
            ("Q3", "Are there any airports that stand out as anomalous in terms of departure bearing?"),
            ("ECR_1c", "A reader concludes Miami has the same bearing as Boston. Is this supported?")
        ]
    },
    {
        "id": "4B",
        "name": "State Migration",
        "type": "glyph map",
        "ground_truth": {
            "Q1": "82,481 to Texas", "ECR_1a": "No",
            "Q2": "Generally yes - high volumes cluster around high-pop states (CA, NY, FL, TX).", "ECR_1b": "No",
            "Q3": "Mutual pairing between Kansas and Missouri is a notable outlier.", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the migration volume recorded for California, and its top destination?"),
            ("ECR_1a", "A reader concludes California received the highest migration volume to any destination. Is this supported?"),
            ("Q2", "Do larger states tend to have higher migration volumes than smaller states?"),
            ("ECR_1b", "A reader concludes migration volume is evenly distributed with no regional pattern. Is this supported?"),
            ("Q3", "Do any states have mutual pairings, where migrants move between the two states?"),
            ("ECR_1c", "A reader concludes every entry in this dataset eventually leads to Florida. Is this supported?")
        ]
    },
    {
        "id": "4C",
        "name": "Bay of Bengal Wind Map",
        "type": "glyph map",
        "ground_truth": {
            "Q1": "10.0 m/s", "ECR_1a": "No",
            "Q2": "Bulls-eye pattern peaking at center. Cyclonic monsoon circulation.", "ECR_1b": "No",
            "Q3": "(10°N, 87.5°E) is single highest peak. Northern edge is a low-speed anomaly.", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the wind speed at 10°N, 87.5°E?"),
            ("ECR_1a", "A reader concludes wind speed at 25°N, 90°E is higher than at 10°N, 87.5°E. Is this supported?"),
            ("Q2", "What is the overall spatial pattern of wind speed across the Bay of Bengal?"),
            ("ECR_1b", "A reader concludes wind speed increases consistently south to north. Is this supported?"),
            ("Q3", "Is there any location that stands out as anomalous in terms of wind speed relative to neighbors?"),
            ("ECR_1c", "A reader concludes wind speeds are uniform across all latitudes at 80°E longitude. Is this supported?")
        ]
    }
]