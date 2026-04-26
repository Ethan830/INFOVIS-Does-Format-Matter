# question.py

QUESTIONS = [
    # ==========================================
    # SERIES 1: LINE GRAPHS
    # ==========================================
    {
        "id": "1A",
        "name": "Population Growth Across Indian States",
        "type": "line graph",
        "ground_truth": {
            "Q1": "~0.63", "ECR_1a": "No",
            "Q2": "All five states show a consistent upward trend, with growth accelerating sharply after 1950. Uttar Pradesh shows the steepest acceleration.", "ECR_1b": "No",
            "Q3": "Uttar Pradesh is the clear outlier — its post-1950 growth rate far exceeds all other states. Kerala is a secondary outlier on the low end, showing notably flatter growth.", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the approximate population of Uttar Pradesh in the year 1950, in hundreds of millions? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the population of Uttar Pradesh in 1950 was approximately 1.0 hundred million. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall trend in population across all five states from 1800 to 2024? Rate your confidence."),
            ("ECR_1b", "A reader concludes that all five states grew at roughly the same rate throughout the entire period. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any states that behave anomalously compared to the overall group trend? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that there are no anomalies in this dataset and all states follow a similar growth pattern. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "1B",
        "name": "Temperatures in Scandinavian Cities",
        "type": "line graph",
        "ground_truth": {
            "Q1": "-6.8C", "ECR_1a": "No",
            "Q2": "All five cities follow the same seasonal pattern — temperatures are negative or near zero in winter (Dec–Feb), rise steadily through spring, peak in July, then decline symmetrically through autumn. Reykjavik consistently records the lowest summer highs while the other four cities are more closely grouped.", "ECR_1b": "No",
            "Q3": "Reykjavik is a consistent outlier on the low end — its summer temperatures are notably cooler than the other four cities. Copenhagen is a mild outlier in December, remaining above freezing (0.4°C) while all others drop below zero.", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the average temperature in Helsinki in February? Rate your confidence."),
            ("ECR_1a", "A reader concludes that Oslo’s average temperature in February is 0C. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall temperature trend across all five cities throughout the year? Rate your confidence."),
            ("ECR_1b", "A reader concludes that temperatures peak in June across all five cities. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any cities or months that behave anomalously compared to the overall group trend? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that there are no anomalies in this dataset and all countries follow a similar pattern. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "1C",
        "name": "Air Quality in Central Asia",
        "type": "line graph",
        "ground_truth": {
            "Q1": "196", "ECR_1a": "No",
            "Q2": "All five cities follow a bimodal daily pattern — AQI dips to its lowest in the early morning hours (03:00–05:00), rises to a morning peak around 08:00–09:00, dips slightly through midday, then rises again to an evening peak around 17:00–18:00 before declining overnight. Moscow and Istanbul remain consistently below the WHO threshold of 100 throughout the day. Tashkent, Almaty, and Tehran remain consistently and substantially above it.", "ECR_1b": "No",
            "Q3": "Moscow and Istanbul are clear outliers on the low end — their AQI values remain below or near the WHO threshold of 100 throughout the entire day, while Tashkent, Almaty, and Tehran consistently exceed 100 by a wide margin. Tehran is a mild outlier on the high end, recording the single highest value in the dataset (196 at 18:00) and showing the steepest evening peak.", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the AQI value for Tehran at 18:00? Rate your confidence."),
            ("ECR_1a", "A reader concludes that Moscow's AQI at 04:00 is the lowest recorded value across all cities at that hour. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall AQI trend across all five cities throughout the day? Rate your confidence."),
            ("ECR_1b", "A reader concludes that AQI values rise steadily throughout the day across all cities with no midday dip. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any cities that behave anomalously compared to the overall group trend? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that all five cities exceed the WHO AQI threshold of 100 at some point during the day. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "1D",
        "name": "Renewable Electricity Share",
        "type": "line graph",
        "ground_truth": {
            "Q1": "67.8", "ECR_1a": "No",
            "Q2": "Steady increase (monotonically), overall upward for all countries", "ECR_1b": "No",
            "Q3": "Brazil", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the renewable electricity share value for Denmark in 2020? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the renewable electricity share value for China in 2008 is 7.9. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall trend for renewable electricity share across all countries? Rate your confidence."),
            ("ECR_1b", "A reader concludes that renewable electricity share for all countries remained flat from 2004-2016. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any countries that behave anomalously compared to the overall group trend? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that all seven countries begin at similar renewable shares and grow at similar rates. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "1E",
        "name": "Reservoir Storage Levels",
        "type": "line graph",
        "ground_truth": {
            "Q1": "~83.6%", "ECR_1a": "No",
            "Q2": "Steady decrease (monotonic decrease) for all reservoir", "ECR_1b": "No",
            "Q3": "No strong outliers.", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the storage level of Reservoir D on Day 20, in percent of capacity? Rate your confidence."),
            ("ECR_1a", "A reader concludes that Reservoir D is at approximately 90% capacity on Day 20. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall trend in storage across all five reservoirs from Day 1 to Day 30? Rate your confidence."),
            ("ECR_1b", "A reader concludes that most reservoirs remain stable or increase slightly over the month. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any reservoirs that behave anomalously compared to the rest? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that one reservoir shows a sudden sharp decrease while the others decline steadily. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "1F",
        "name": "Quarterly Retail Sales",
        "type": "line graph",
        "ground_truth": {
            "Q1": "334", "ECR_1a": "No",
            "Q2": "There is a visible disruption around 2020-Q1, especially in clothing and electronics, while grocery remains relatively resilient and continues to grow. Otherwise, mostly gradual increase", "ECR_1b": "No",
            "Q3": "Grocery is the clearest outlier because it stays much higher than the other categories and does not dip in 2020", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the grocery sales value in 2022-Q3, in million USD? Rate your confidence."),
            ("ECR_1a", "A reader concludes that grocery sales in 2022-Q3 were approximately 250 million USD. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall trend in quarterly retail sales across product categories from 2018 to 2024? Rate your confidence."),
            ("ECR_1b", "A reader concludes that all product categories grew smoothly with no sign of disruption around 2020. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any product categories that behave anomalously compared to the others? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that grocery behaves just like clothing and electronics across the entire period. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "1G",
        "name": "Server Latency Cycle",
        "type": "line graph",
        "ground_truth": {
            "Q1": "142", "ECR_1a": "No",
            "Q2": "Lowest in nights and rising through the morning, peak at midday and decrease after late evening", "ECR_1b": "No",
            "Q3": "Not really", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the average latency in India at 16:00, in milliseconds? Rate your confidence."),
            ("ECR_1a", "A reader concludes that India’s latency at 16:00 is approximately 90 ms. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall temporal pattern in server latency across the six data centers over the 24-hour cycle? Rate your confidence."),
            ("ECR_1b", "A reader concludes that latency is essentially constant across the full day in Singapore. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any data centers that behave anomalously compared to the rest? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that all six data centers operate at roughly the same latency level throughout the day. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "1H",
        "name": "Influenza Incidence",
        "type": "line graph",
        "ground_truth": {
            "Q1": "67", "ECR_1a": "Yes",
            "Q2": "Strong seasonal cycles, peaking in Jan each year, and troughs in July.", "ECR_1b": "No",
            "Q3": "No", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the influenza incidence in Province B in January 2024, in cases per 100,000 persons? Rate your confidence."),
            ("ECR_1a", "A reader concludes that Province B records approximately 67 cases per 100,000 persons in January 2024. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall pattern of influenza incidence across provinces from 2022 to 2024? Rate your confidence."),
            ("ECR_1b", "A reader concludes that influenza incidence steadily declines across all provinces from 2022 to 2024. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any provinces that behave anomalously compared to the overall group trend? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that all provinces have nearly identical influenza incidence at every time point. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "1I",
        "name": "Crop Yield Trends",
        "type": "line graph",
        "ground_truth": {
            "Q1": "4.7", "ECR_1a": "Yes",
            "Q2": "Steady upward trend (monotonic increase) over time for all 5 zones", "ECR_1b": "No",
            "Q3": "No", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the crop yield in Zone 4 in the year 2020, in tonnes per hectare? Rate your confidence."),
            ("ECR_1a", "A reader concludes that Zone 5 has a crop yield of approximately 3.6 tonnes per hectare in 2020. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall trend in crop yield across all five agricultural zones from 1995 to 2024? Rate your confidence."),
            ("ECR_1b", "A reader concludes that crop yields are flat or declining in most zones between 1995 and 2024. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any zones that behave anomalously compared to the overall group trend? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that Zone 5 sharply outperforms all other zones by the end of the period. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "1J",
        "name": "Transit Passenger Counts",
        "type": "line graph",
        "ground_truth": {
            "Q1": "201", "ECR_1a": "No",
            "Q2": "Rise to peak around 8:00, then decline", "ECR_1b": "No",
            "Q3": "None", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the approximate passenger count on the Red Line at 08:00, in passengers per minute? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the Red Line carries approximately 120 passengers per minute at 08:00. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall trend in passenger counts across all five transit lines from 06:00 to 10:00? Rate your confidence."),
            ("ECR_1b", "A reader concludes that passenger counts increase steadily throughout the entire 06:00 to 10:00 period with no peak or decline. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any transit lines that behave anomalously compared to the rest? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that all five transit lines have essentially the same passenger profile and volume throughout the morning peak. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },

    # ==========================================
    # SERIES 2: COLOR MAPS
    # ==========================================
    {
        "id": "2A",
        "name": "Land Temperatures Sub-Saharan Africa",
        "type": "color map",
        "ground_truth": {
            "Q1": "24.7°C", "ECR_1a": "No",
            "Q2": "Temperature increases consistently as latitude increases northward. The equatorial band (0°) records the coolest values at 22.4°C uniformly across all longitudes. Temperatures rise steadily through 6°N (26.0°C), 12°N (29.9–30.0°C), and 24°N (37.4–38.9°C), peaking at 30°N (41.6–41.7°C). The gradient is smooth and consistent across almost all longitude bands with the notable exception of the 18°N, 38°E–45°E region.", "ECR_1b": "No",
            "Q3": "Yes — there is a striking cold anomaly centred around 18°N, 41°E, where the temperature drops to 24.7°C, far below the expected value of approximately 33–34°C for that latitude. This is visible as the deep blue region in the colour map. A secondary, milder cool anomaly exists around 15°N, 20°E in the colour map, though it is less dramatic in the table data.", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the land surface temperature at 18°N, 41°E? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the temperature at 30°N is the least uniform across all longitude bands. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall trend in land surface temperature as latitude increases from 0° to 30°N? Rate your confidence."),
            ("ECR_1b", "A reader concludes that temperatures are highest at the equator and decrease as latitude increases northward. Is this supported? Rate your confidence."),
            ("Q3", "Are there any regions that behave anomalously compared to the overall spatial temperature pattern? If so, state which region(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that the temperature at 18°N increases uniformly from west to east across all longitude bands. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "2B",
        "name": "Seismic Hazard Map",
        "type": "color map",
        "ground_truth": {
            "Q1": "0.39g", "ECR_1a": "No",
            "Q2": "Seismic hazard is highly concentrated in the central-western portion of the region, peaking around coordinates (4, 8) and (2, 4)–(4, 4), which correspond to the Meridian Fault zone. Values drop sharply toward all edges of the map, with the northern row (N=10), southern row (N=0), and eastern and western edges all recording negligible to low hazard (0.04–0.13g). A secondary hazard concentration exists in the east-central area around (6, 4)–(8, 8), corresponding to the Eastern Rift zone.", "ECR_1b": "No",
            "Q3": "Yes — two cells stand out as local anomalies. The cell at (4, 8) records 0.89g, which is dramatically higher than all adjacent cells in row N=8 (0.42g to the west, 0.39g to the east) and the row above (0.13g at N=10). The cell at (6, 4) records 0.84g, which is notably higher than its neighbours at (4, 4) which records 0.27g — a sharp discontinuity suggesting a localised high-hazard fault intersection. The entire bottom row (N=0) and top row (N=10) are uniformly low, making any elevated reading in those rows anomalous by comparison.", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the Peak Ground Acceleration value at coordinates (4, 8) on the N→S / W→E grid? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the highest PGA value in the entire dataset occurs at coordinates (6, 8). Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial pattern of seismic hazard across the region? Rate your confidence."),
            ("ECR_1b", "A reader concludes that seismic hazard is uniformly distributed across the region with no concentrated high-hazard zones. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any grid cells that behave anomalously compared to their immediate surroundings? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that the cell at (2, 6) records a higher PGA than the cell at (4, 6). Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "2C",
        "name": "Terrain Elevation Map",
        "type": "color map",
        "ground_truth": {
            "Q1": "3,685m", "ECR_1a": "No",
            "Q2": "Elevation is lowest and highly uniform along all edges of the map, with all border cells recording values close to 2,400m. Elevation rises sharply toward the central and upper-central portion of the region, peaking around coordinates (4, 6) at 3,685m and (6, 4) at 3,105m. The gradient is steep on the western and northern faces of the central massif and more gradual toward the south and east. The summit area visible in the colour map corresponds to the highest concentration of elevated cells in the (2–6, 4–8) zone.", "ECR_1b": "No",
            "Q3": "Yes — the cell at (4, 6) records 3,685m, which is the single highest value in the dataset and represents a sharp local peak relative to its neighbours at (2, 6) which records 2,729m and (6, 6) which records 3,660m. The entire top row (N=10) and bottom row (N=0) are anomalously uniform and low relative to the interior, consistent with a flat peripheral lowland. The cell at (2, 8) records 2,926m, which is notably elevated compared to its western neighbour at (0, 8) recording 2,420m, suggesting a sharp ridgeline running north-south on the western face.", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the elevation at coordinates (4, 6)? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the elevation at (2, 8) is higher than the elevation at (4, 6). Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial pattern of elevation across the region? Rate your confidence."),
            ("ECR_1b", "A reader concludes that elevation increases consistently from south to north across the entire region. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any grid cells that behave anomalously compared to their immediate surroundings? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that the cell at (0, 6) records a similar elevation to the cell at (4, 6), as both appear to be in the mid-section of the map. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "2D",
        "name": "Sea Surface Temperature",
        "type": "color map",
        "ground_truth": {
            "Q1": "30.5", "ECR_1a": "No",
            "Q2": "Temperature generally increases from north to south and from west to east", "ECR_1b": "No",
            "Q3": "None", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the sea surface temperature at 12°N 76°E, in degrees Celsius? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the sea surface temperature at 12°N 76°E is 28.0°C. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial pattern of sea surface temperature across the Arabian Sea grid? Rate your confidence."),
            ("ECR_1b", "A reader concludes that sea surface temperature decreases steadily toward the southeast. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any locations that behave anomalously compared to the overall group pattern? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that there is a cold anomaly in the southeastern corner that sharply breaks the overall pattern. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "2E",
        "name": "Groundwater Salinity",
        "type": "color map",
        "ground_truth": {
            "Q1": "5.9", "ECR_1a": "No",
            "Q2": "Low at outdoor edges and increase sharply toward the center right, with a strong core visible", "ECR_1b": "No",
            "Q3": "Yes, (4,6)", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the groundwater salinity at north-south coordinate 4 and west-east coordinate 6, in parts per thousand? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the groundwater salinity at coordinate (4,6) is 2.0 ppt. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial pattern of groundwater salinity across the basin? Rate your confidence."),
            ("ECR_1b", "A reader concludes that groundwater salinity is spatially uniform across the basin with only minor variation. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any cells that behave anomalously relative to the surrounding pattern? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that there are no localized anomalies and no contaminated hotspot in the basin. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "2F",
        "name": "Solar Irradiance",
        "type": "color map",
        "ground_truth": {
            "Q1": "298", "ECR_1a": "No",
            "Q2": "General rise moving southward from 35°N to 20°N and northward from 10°N to 20°N; slight increase from west to east.", "ECR_1b": "No",
            "Q3": "No", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the solar irradiance at 20°N, 20°E, in watts per square metre? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the solar irradiance at 20°N 20°E is 250 W/m2. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial pattern of solar irradiance across North Africa? Rate your confidence."),
            ("ECR_1b", "A reader concludes that solar irradiance steadily decreases toward lower latitudes everywhere in the grid. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any cells that behave anomalously compared to the overall pattern? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that the grid contains a single sharply abnormal low-irradiance cell near the center. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "2G",
        "name": "Urban Heat Island",
        "type": "color map",
        "ground_truth": {
            "Q1": "6.3", "ECR_1a": "No",
            "Q2": "Low intensity around edges and increases to center, with a hotspot in the middle", "ECR_1b": "No",
            "Q3": "Yes, the central hotspot at (4,6)", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the urban heat island intensity at north-south coordinate 4 and west-east coordinate 6, in degrees Celsius? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the urban heat island intensity at (4,6) is 2.0°C. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial pattern of urban heat island intensity across the metropolitan region? Rate your confidence."),
            ("ECR_1b", "A reader concludes that urban heat island intensity is highest at the outer boundary and weakest in the center. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any cells that behave anomalously relative to the overall field? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that there is no meaningful hotspot and all cells remain within a narrow range. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "2H",
        "name": "Soil Moisture Plain",
        "type": "color map",
        "ground_truth": {
            "Q1": "36.3", "ECR_1a": "No",
            "Q2": "Lower at southern and western edges and rises to the central/central-eastern portion, where there is a hotspot.", "ECR_1b": "No",
            "Q3": "Yes the hotspot at (6,6) and (6,8)", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the soil moisture at north-south coordinate 6 and west-east coordinate 8, in volumetric water content percent? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the soil moisture at (6,8) is 20%. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial pattern of soil moisture across the plain? Rate your confidence."),
            ("ECR_1b", "A reader concludes that soil moisture declines smoothly from west to east with no wet central region. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any cells that behave anomalously compared to the surrounding field? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that there are no localized high-moisture zones and the grid contains only gentle variation. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "2I",
        "name": "Pollen Concentration Valley",
        "type": "color map",
        "ground_truth": {
            "Q1": "146", "ECR_1a": "Yes",
            "Q2": "Low on outer edges, rises to the central eastern area, with a hotspot in the middle-eastern area.", "ECR_1b": "No",
            "Q3": "Yes 38°N 124°E", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the pollen concentration at 38°N 124°E, in grains per cubic metre? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the pollen concentration at 38°N 124°E is 140. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial pattern of pollen concentration across the valley system? Rate your confidence."),
            ("ECR_1b", "A reader concludes that pollen concentration is highest on the far western edge and steadily decreases eastward. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any locations that behave anomalously relative to the broader spatial pattern? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that the field contains no localized pollen plume or hotspot. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "2J",
        "name": "Peak Wind Gust Europe",
        "type": "color map",
        "ground_truth": {
            "Q1": "18.1", "ECR_1a": "No",
            "Q2": "Peak at Northwest and decline toward the southeast", "ECR_1b": "No",
            "Q3": "Yes 60°N 10°W", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the peak wind gust at 50°N 10°E, in metres per second? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the peak wind gust at 50°N 10°E is 24m/s. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial pattern of peak wind gust across coastal Europe? Rate your confidence."),
            ("ECR_1b", "A reader concludes that peak wind gust intensifies toward the southeastern corner of the grid. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any locations that behave anomalously compared to the overall field? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that a single central grid cell forms a sharp wind-gust anomaly disconnected from the surrounding pattern. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },

    # ==========================================
    # SERIES 3: ISOLINE MAPS
    # ==========================================
    {
        "id": "3A",
        "name": "Mean Precipitation in Korea",
        "type": "isoline map",
        "ground_truth": {
            "Q1": "930 mm", "ECR_1a": "No",
            "Q2": "Precipitation decreases consistently as latitude increases northward. Southern latitudes (34–36°N) record the highest values (1,280–1,450 mm) while northern latitudes (42–43°N) record the lowest (450–630 mm). The gradient is smooth and monotonic across all longitude columns.", "ECR_1b": "No",
            "Q3": "No dramatic outliers exist — the dataset is spatially smooth. However, the 129°E column shows a mild local peak relative to its neighbours at several mid-latitudes, suggesting a subtle eastward precipitation enhancement. No single cell deviates sharply enough to be considered a strong outlier.", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the recorded precipitation value at 39°N latitude and 127°E longitude? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the precipitation at 42°N, 125°E is 650 mm. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "Describe the overall trend of precipitation in relation to latitude across the Korean Peninsula. Rate your confidence."),
            ("ECR_1b", "A reader concludes that precipitation increases consistently as one moves northward, making the northernmost latitudes (42–43°N) the wettest regions on the map. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any significant outliers or localized anomalies in precipitation across the recorded grid? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that there is a severe anomaly at 38°N, 126°E where precipitation suddenly drops to 200 mm, creating a massive outlier compared to its surrounding grid points. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "3B",
        "name": "Noise Pollution in Delhi",
        "type": "isoline map",
        "ground_truth": {
            "Q1": "86.5 dB", "ECR_1a": "No",
            "Q2": "Noise pollution is not uniformly distributed but forms distinct, highly localized hotspots. The most severe noise (above 85 dB) is concentrated in the central and western urban cores (New Delhi, Patel Nagar, IGI Airport, Gurgaon), while the outer peripheral locations (Rohini, Faridabad, Ghaziabad) record significantly lower levels, creating steep gradients dropping off away from the city centers.", "ECR_1b": "No",
            "Q3": "Yes, New Delhi represents an extreme peak at 95.0 dB, sitting at the center of the largest high-noise cluster. Additionally, Gurgaon (85.1 dB) forms its own distinct, isolated high-noise hotspot in the southwest, separated from the main New Delhi/Patel Nagar cluster by a noticeable dip in the gradient.", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the recorded noise pollution level for Noida? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the noise level at Faridabad is 85.1 dB. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "Describe the overall spatial distribution of noise pollution across the Delhi NCR region. Rate your confidence."),
            ("ECR_1b", "A reader concludes that noise pollution smoothly and consistently increases as one moves from west to east across the entire map, making the easternmost location (Ghaziabad) the loudest. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any notable extremes or isolated structural anomalies in the noise pollution dataset? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that Ghaziabad represents a sudden, massive spike in noise pollution, forming a severe and isolated red hotspot in the far east of the map. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "3C",
        "name": "PM2.5 Wildfire Event",
        "type": "isoline map",
        "ground_truth": {
            "Q1": "158.5 µg/m³", "ECR_1a": "No",
            "Q2": "PM2.5 concentrations are highest in the northern region (Vallejo and Concord) forming a primary pollution peak, and they steadily decrease as one moves south. This creates a continuous, dissipating gradient that reaches its lowest recorded levels in the southernmost locations (San Jose and Los Gatos).", "ECR_1b": "No",
            "Q3": "The data primarily follows a smooth, continuous dissipation gradient without severe, isolated hotspots in the lower latitudes. Vallejo forms the primary peak (185.4 µg/m³) at the northern boundary, and the pollution plume smoothly diffuses southward without any sudden, disconnected spikes disrupting the regional trend.", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the recorded PM2.5 concentration for Berkeley? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the PM2.5 concentration at San Jose is 108.4 µg/m³. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "Describe the overall spatial trend of PM2.5 concentration across the Bay Area during this event. Rate your confidence."),
            ("ECR_1b", "A reader concludes that the PM2.5 concentration smoothly and consistently increases as one moves from north to south, making the southernmost cities (San Jose and Los Gatos) the most heavily polluted. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any severe isolated hotspots or structural anomalies in the PM2.5 data, or does it follow a continuous gradient? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that San Francisco represents an extreme, isolated hotspot of pollution that is significantly higher than all of its immediate northern and eastern neighbors (such as Oakland and Berkeley). Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "3D",
        "name": "Annual Snowfall Alps",
        "type": "isoline map",
        "ground_truth": {
            "Q1": "296", "ECR_1a": "No",
            "Q2": "Highest in the center of the grid, decreasing outward", "ECR_1b": "No",
            "Q3": "Yes, 46.1°N 11°E", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the annual snowfall at 46.1°N 11°E, in centimetres? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the annual snowfall at 46.1°N 11°E is 180 cm. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial pattern of snowfall across the Alps grid? Rate your confidence."),
            ("ECR_1b", "A reader concludes that snowfall is spatially uniform across the Alps grid with no strong center-to-edge variation. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any cells that behave anomalously relative to the broader field? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that there are no prominent snowfall peaks in the central Alps and no cell stands out strongly from the surrounding field. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "3E",
        "name": "Ground-level Ozone SoCal",
        "type": "isoline map",
        "ground_truth": {
            "Q1": "94", "ECR_1a": "No",
            "Q2": "Lower at the coast and rises toward inland. Peak at San Bernardino", "ECR_1b": "No",
            "Q3": "Yes, San Bernardino", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the ground-level ozone concentration at San Bernardino, in parts per billion? Rate your confidence."),
            ("ECR_1a", "A reader concludes that San Bernardino records 60ppb ozone. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial pattern of ozone concentration across the Southern California monitoring sites? Rate your confidence."),
            ("ECR_1b", "A reader concludes that ozone concentrations are highest along the immediate coast and decline inland. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any sites that behave anomalously relative to the broader group pattern? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that all monitoring sites have similar ozone concentrations with no clear inland hotspot. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "3F",
        "name": "Noise Exposure Tokyo",
        "type": "isoline map",
        "ground_truth": {
            "Q1": "91", "ECR_1a": "Yes",
            "Q2": "Highest near Shibuya and Shinjuku. Decreasing toward Tokyo and Ueno", "ECR_1b": "No",
            "Q3": "Yes, Shibuya", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the noise exposure level at Shibuya, in decibels? Rate your confidence."),
            ("ECR_1a", "A reader concludes that Shibuya’s noise exposure is 91 dB. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial pattern of noise exposure across the major intersections in central Tokyo? Rate your confidence."),
            ("ECR_1b", "A reader concludes that noise exposure is evenly distributed across all intersections with little distinction between commercial hubs and other locations. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any intersections that behave anomalously relative to the rest? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that there are no unusually noisy intersections and no location clearly exceeds the others. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "3G",
        "name": "Nitrate Concentration Lake",
        "type": "isoline map",
        "ground_truth": {
            "Q1": "5.91", "ECR_1a": "No",
            "Q2": "Low in the eastern side of the lake, and rise sharply to the eastern and southeastern sites", "ECR_1b": "No",
            "Q3": "Yes, Industrial Outlet", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the nitrate concentration at Industrial Outlet, in milligrams per litre? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the nitrate concentration at Industrial Outlet is 1.5mg/L. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial pattern of nitrate concentration across the lake network? Rate your confidence."),
            ("ECR_1b", "A reader concludes that nitrate concentrations decrease toward the eastern side of the lake network and remain uniformly low near the outlet. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any sites that behave anomalously relative to the broader field? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that there is no localized nitrate hotspot in the lake network. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "3H",
        "name": "Annual Precipitation Patagonia",
        "type": "isoline map",
        "ground_truth": {
            "Q1": "1530", "ECR_1a": "No",
            "Q2": "Highest in the western part and decline moving eastward", "ECR_1b": "No",
            "Q3": "Yes, 46°S 74°W", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the annual precipitation at 46°S 70°W, in millimetres? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the annual precipitation at 46°S 70°W is 600mm. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial pattern of precipitation across Patagonia? Rate your confidence."),
            ("ECR_1b", "A reader concludes that precipitation steadily increases from west to east across Patagonia. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any cells that behave anomalously relative to the broader field? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that a single isolated dry cell in western Patagonia breaks the overall pattern. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "3I",
        "name": "PM10 Industrial Corridor",
        "type": "isoline map",
        "ground_truth": {
            "Q1": "181", "ECR_1a": "No",
            "Q2": "Rise from north end to Power Station South and decrease to south end", "ECR_1b": "No",
            "Q3": "Yes, Power Station South", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the PM10 concentration at Power Station South, in micrograms per cubic metre? Rate your confidence."),
            ("ECR_1a", "A reader concludes that Power Station South has a PM10 concentration of 95μg/m3. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial pattern of PM10 concentration along the industrial corridor? Rate your confidence."),
            ("ECR_1b", "A reader concludes that PM10 steadily declines from north to south with no central pollution peak. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any sites that behave anomalously relative to the broader corridor pattern? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that there are no severe pollution hotspots along the industrial corridor and all sites fall within a similar range. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "3J",
        "name": "Nighttime Light Intensity Peninsula",
        "type": "isoline map",
        "ground_truth": {
            "Q1": "58.6", "ECR_1a": "No",
            "Q2": "Low at the edges and increase into a hotspot in the middle of the grid", "ECR_1b": "No",
            "Q3": "Yes, 37°N 129°E", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the nighttime light intensity at 37°N 129°E, in radiance units? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the nighttime light intensity at 37°N 129°E is 20 nW/cm2/sr. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial pattern of nighttime light intensity across the peninsula region? Rate your confidence."),
            ("ECR_1b", "A reader concludes that nighttime light intensity is highest around the western edge and declines toward the center. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any cells that behave anomalously relative to the broader field? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that the grid contains no concentrated urban light hotspot and all cells fall within a narrow radiance range. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },

    # ==========================================
    # SERIES 4: GLYPH MAPS
    # ==========================================
    {
        "id": "4A",
        "name": "North America Flight Data",
        "type": "glyph map",
        "ground_truth": {
            "Q1": "Newark", "ECR_1a": "No",
            "Q2": "Western coast airports (LAX, SFO, SEA, PDX, YVR) predominantly depart eastward, with bearings clustering between 62°–118°. Eastern coast airports (BOS, EWR, PHL, IAD, YUL) predominantly depart westward, with bearings clustering between 265°–268°. This creates a broadly mirrored pattern — western airports point inward toward the continent, eastern airports point inward toward the continent from the opposite side.", "ECR_1b": "No",
            "Q3": "Yes — several airports stand out. LAX (62°) and SFO (70°) depart notably more northeastward than their regional neighbours PHX (82°) and PDX (112°), suggesting a different dominant route network. Orlando (MCO) at 305° is a notable outlier among southeastern airports, departing predominantly northwestward while its neighbours ATL (280°), MIA (295°), and MSY (285°) all depart more westward. Denver (DEN) at 110° stands out among interior airports as departing eastward rather than toward either coast.", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "Which airport has the longest average flight duration? Rate your confidence."),
            ("ECR_1a", "A reader concludes that Atlanta (ATL) has the shortest average flight duration of any airport in the dataset. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the dominant departure bearing pattern for airports located on the western coast of North America compared to those on the eastern coast? Rate your confidence."),
            ("ECR_1b", "A reader concludes that western and eastern coast airports share a similar departure bearing. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any airports that stand out as anomalous in terms of departure bearing relative to other airports in their geographic region? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that Miami (MIA) has the same approximate departure bearing as Boston (BOS), as both are eastern seaboard airports with similar geographic orientations. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "4B",
        "name": "State Migration Flows",
        "type": "glyph map",
        "ground_truth": {
            "Q1": "82,481 to Texas", "ECR_1a": "No",
            "Q2": "Generally yes — the highest volumes cluster around large states (CA, NY, FL, TX), while smallest volumes belong to low-population states like Vermont, Wyoming, and Alaska", "ECR_1b": "No",
            "Q3": "The Kansas↔Missouri and Missouri↔Kansas mutual pairing is a notable structural outlier", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the migration volume recorded for California, and which state is listed as its top destination? Rate your confidence."),
            ("ECR_1a", "A reader concludes that California received the highest migration volume to any destination in this dataset. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "Do states with larger populations tend to have higher migration volumes than states with smaller populations, based on what is shown in this data? Rate your confidence."),
            ("ECR_1b", "A reader concludes that migration volume is evenly distributed across origin states with no clear pattern based on region. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Do any states have mutual pairings, where migrants move between the two states? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that every entry in this dataset eventually leads towards Florida. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "4C",
        "name": "Bay of Bengal Wind Map",
        "type": "glyph map",
        "ground_truth": {
            "Q1": "10.0 m/s (the single highest recorded speed in the dataset)", "ECR_1a": "No",
            "Q2": "Wind speed is lowest at the northern and southern peripheries of the domain and peaks strongly in the central region around 10°N, 87.5°E, creating a concentric bull's-eye pattern of increasing speed toward the centre. Wind direction is predominantly eastward (positive U components dominate throughout) with a northward V component that increases toward the centre, consistent with a cyclonic monsoon circulation pattern. At the periphery, winds are weaker and more uniformly eastward. At the centre, winds curve northeastward as the circulation tightens.", "ECR_1b": "No",
            "Q3": "Yes — the cell at 10°N, 87.5°E records 10.0 m/s, which is the single highest value in the entire dataset and stands out as the peak of the central circulation. It is notably higher than its immediate neighbours at 10°N, 85°E (9.5 m/s) and 10°N, 90°E (10.4 m/s — note this is from the raw U/V components; the speed field is smooth but tightly peaked). The northern edge of the domain (25°N) is a collective low-speed anomaly, with all cells recording uniformly low speeds of 3.9–4.3 m/s regardless of longitude, contrasting sharply with the high-speed central band.", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the wind speed at 10°N, 87.5°E? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the wind speed at 25°N, 90°E is higher than the wind speed at 10°N, 87.5°E. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial pattern of wind speed across the Bay of Bengal, and how does wind direction vary across the region? Rate your confidence."),
            ("ECR_1b", "A reader concludes that wind speed increases consistently from south to north, with the highest speeds recorded at the northernmost latitudes (25°N). Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Is there any location in the dataset that stands out as anomalous in terms of wind speed relative to its immediate neighbours? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that wind speeds are roughly uniform across all latitudes at 80°E longitude, with no significant variation from south to north along the western boundary of the domain. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "4D",
        "name": "Shipping Route Ports",
        "type": "glyph map",
        "ground_truth": {
            "Q1": "79.8", "ECR_1a": "No",
            "Q2": "The ports show substantial variation in both average route length and departure bearing. Most western Indian Ocean and South Asian ports have long routes with bearings clustered toward southwest-to-westward directions, while eastern ports such as Singapore and Fremantle exhibit distinct directional patterns and substantial route lengths.", "ECR_1b": "No",
            "Q3": "Yes, Singapore", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the annual cargo volume for Singapore, in million tonnes? Rate your confidence."),
            ("ECR_1a", "A reader concludes that Singapore handles 40 million tonnes annually. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall directional and magnitude pattern in the shipping route characteristics across the selected ports? Rate your confidence."),
            ("ECR_1b", "A reader concludes that all ports have nearly identical route lengths, cargo volumes, and departure directions. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any ports that behave anomalously compared to the rest? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that no port stands out in either cargo volume or route length. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "4E",
        "name": "Commuter Migration Flows",
        "type": "glyph map",
        "ground_truth": {
            "Q1": "92410 (~90000)", "ECR_1a": "Yes",
            "Q2": "Migration concentrate among large adjacent state or nearby-region corridors", "ECR_1b": "No",
            "Q3": "Yes, California to Nevada", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the migration volume from California to Nevada? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the migration volume from California to Nevada is 90,000. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall pattern in the largest commuter migration flows listed for these metropolitan origins? Rate your confidence."),
            ("ECR_1b", "A reader concludes that the dominant migration flows mainly connect distant, non-neighboring states with no geographic clustering. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any origin–destination pairs that behave anomalously compared to the rest? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that all origin–destination pairs in the dataset have nearly identical migration volumes. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "4F",
        "name": "Western Pacific Wind",
        "type": "glyph map",
        "ground_truth": {
            "Q1": "7.1", "ECR_1a": "No",
            "Q2": "Wind leaving the center, with increased intensity at the edges.", "ECR_1b": "No",
            "Q3": "Yes, 24°N 132°E", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the wind speed at 24°N 132°E, in metres per second? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the wind speed at 24°N 132°E is 3.0 m/s. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial and directional pattern of the wind field over the western Pacific? Rate your confidence."),
            ("ECR_1b", "A reader concludes that the wind field is uniform and flows in the same direction everywhere across the grid. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any regions that behave anomalously relative to the broader wind field? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that there is no concentrated wind core and no part of the grid stands out in speed or directional organization. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "4G",
        "name": "Surface Current Strait",
        "type": "glyph map",
        "ground_truth": {
            "Q1": "4.7m/s", "ECR_1a": "No",
            "Q2": "Aligned to the east, with intensity peaking in the middle and weakened at the edges of the grid", "ECR_1b": "No",
            "Q3": "Yes 40°N 35°E", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the surface current speed at 40°N 35°E, in metres per second? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the surface current speed at 40°N 35°E is 3.2 m/s. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial pattern of the surface current field through the strait? Rate your confidence."),
            ("ECR_1b", "A reader concludes that the strongest currents occur uniformly along the outer boundaries of the strait while the center remains weak. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any cells that behave anomalously compared to the surrounding current field? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that there is no central acceleration zone and no cell is notably stronger than the rest. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "4H",
        "name": "European Hub Airports",
        "type": "glyph map",
        "ground_truth": {
            "Q1": "57.8", "ECR_1a": "No",
            "Q2": "All point toward southeast", "ECR_1b": "No",
            "Q3": "Yes, Madrid", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the average annual passenger volume for Paris Charles de Gaulle (CDG), in millions? Rate your confidence."),
            ("ECR_1a", "A reader concludes that Paris Charles de Gaulle handles 303030 million passengers annually. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall pattern in operating characteristics across the European hubs? Rate your confidence."),
            ("ECR_1b", "A reader concludes that all hubs have identical operating characteristics and passenger volumes. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any hubs that behave anomalously relative to the rest? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that no airport stands out in traffic direction. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "4I",
        "name": "Interstate Relocation Flows",
        "type": "glyph map",
        "ground_truth": {
            "Q1": "84215", "ECR_1a": "No",
            "Q2": "Migration toward NSW, VIC, QLD", "ECR_1b": "No",
            "Q3": "Yes, NSW and QLD", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the migration volume from New South Wales to Queensland? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the migration volume from New South Wales to Queensland is 40,000. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall pattern in the largest interstate relocation flows across Australian states and territories? Rate your confidence."),
            ("ECR_1b", "A reader concludes that the largest interstate relocation flows are evenly distributed across all states with no concentration in the east. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any origin–destination pairs that behave anomalously compared to the rest? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that no relocation flow is substantially larger than the others and all volumes are similar. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    },
    {
        "id": "4J",
        "name": "Monsoon Low-Level Jet",
        "type": "glyph map",
        "ground_truth": {
            "Q1": "18.9", "ECR_1a": "No",
            "Q2": "Toward the east, with high intensity in the middle of the grid", "ECR_1b": "No",
            "Q3": "Yes 12°N 50°E", "ECR_1c": "No"
        },
        "questions": [
            ("Q1", "What is the wind speed at 12°N 50°E, in metres per second? Rate your confidence."),
            ("ECR_1a", "A reader concludes that the wind speed at 8°N 46°E is 14 m/s. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q2", "What is the overall spatial pattern of the monsoon low-level jet over the Somali coast? Rate your confidence."),
            ("ECR_1b", "A reader concludes that wind speeds are nearly uniform across the grid and show no focused jet core. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence."),
            ("Q3", "Are there any regions that behave anomalously relative to the broader field? If so, state which one(s). Rate your confidence."),
            ("ECR_1c", "A reader concludes that there is no central wind-speed maximum and no location stands out as part of a jet structure. Is this conclusion supported by the data? Answer Yes or No. Rate your confidence.")
        ]
    }
]