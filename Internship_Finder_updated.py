import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371 
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1-a))

# Every company from your list with a Penang presence
penang_db = [
    # --- BATU KAWAN / SEBERANG PERAI (Your Side) ---
    {"name": "Micron (BKIP)", "lat": 5.2335, "lon": 100.4308, "zone": "Batu Kawan"},
    {"name": "Western Digital (BKIP)", "lat": 5.2315, "lon": 100.4330, "zone": "Batu Kawan"},
    {"name": "HP Malaysia (BKIP)", "lat": 5.2279, "lon": 100.4473, "zone": "Batu Kawan"},
    {"name": "Aspen Group (Sales Gallery)", "lat": 5.2355, "lon": 100.4402, "zone": "Batu Kawan"},
    {"name": "Bosch (BKIP)", "lat": 5.2312, "lon": 100.4345, "zone": "Batu Kawan"},
    {"name": "UWC Berhad", "lat": 5.2750, "lon": 100.4340, "zone": "Batu Kawan"},
    {"name": "NationGate Solution", "lat": 5.2410, "lon": 100.4390, "zone": "Batu Kawan"},
    {"name": "JF Technology (JF-AMD)", "lat": 5.2385, "lon": 100.4420, "zone": "Batu Kawan"},
    {"name": "MKS Instruments", "lat": 5.2290, "lon": 100.4310, "zone": "Batu Kawan"},
    {"name": "Safetyware HQ", "lat": 5.3045, "lon": 100.4470, "zone": "Simpang Ampat"},
    {"name": "DKSH (Butterworth)", "lat": 5.3780, "lon": 100.3700, "zone": "Butterworth"},
    {"name": "Alliance Bank (BM)", "lat": 5.3470, "lon": 100.4570, "zone": "Bukit Mertajam"},

    # --- PENANG ISLAND (Requires Bridge Toll) ---
    {"name": "Intel (Bayan Lepas)", "lat": 5.2972, "lon": 100.2893, "zone": "Island"},
    {"name": "Jabil Circuit", "lat": 5.3000, "lon": 100.2800, "zone": "Island"},
    {"name": "Keysight Technologies", "lat": 5.2950, "lon": 100.2700, "zone": "Island"},
    {"name": "Plexus Riverside", "lat": 5.3015, "lon": 100.2750, "zone": "Island"},
    {"name": "Zebra Technologies", "lat": 5.2930, "lon": 100.2720, "zone": "Island"},
    {"name": "Celestica (Bayan Lepas)", "lat": 5.3020, "lon": 100.2810, "zone": "Island"},
    {"name": "PwC (Georgetown)", "lat": 5.4210, "lon": 100.3330, "zone": "Island"},
    {"name": "KPMG (Gurney)", "lat": 5.4360, "lon": 100.3110, "zone": "Island"},
    {"name": "EY (Tanjung Tokong)", "lat": 5.4510, "lon": 100.3070, "zone": "Island"},
    {"name": "BDO (Menara BHL)", "lat": 5.4265, "lon": 100.3235, "zone": "Island"},
    {"name": "Centific (Menara BHL)", "lat": 5.4266, "lon": 100.3236, "zone": "Island"},
    {"name": "JobStreet (SPICE)", "lat": 5.3280, "lon": 100.2790, "zone": "Island"},
    {"name": "EasyParcel HQ", "lat": 5.3318, "lon": 100.2925, "zone": "Island"},
    {"name": "Exabytes", "lat": 5.3320, "lon": 100.2930, "zone": "Island"},
    {"name": "Aloft Hotel", "lat": 5.3300, "lon": 100.2780, "zone": "Island"},
    {"name": "The Westin (Georgetown)", "lat": 5.4250, "lon": 100.3340, "zone": "Island"},
    {"name": "St. Giles (The Wembley)", "lat": 5.4130, "lon": 100.3300, "zone": "Island"},
    {"name": "Shangri-La Rasa Sayang", "lat": 5.4780, "lon": 100.2540, "zone": "Island"},
    {"name": "Golden Sands Resort", "lat": 5.4770, "lon": 100.2510, "zone": "Island"}
]

def main():
    print("\n" + "="*60)
    print("PENANG INTERNSHIP COMMUTE CALCULATOR")
    print("="*60)
    
    try:
        # Enter these when prompted, one by one.
        u_lat = float(input("1. Enter your Latitude (e.g. 5.24247): "))
        u_lon = float(input("2. Enter your Longitude (e.g. 100.43904): "))
    except ValueError:
        print("\n[!] Please enter only numeric values. Don't include commas.")
        return

    results = []
    for c in penang_db:
        dist = haversine(u_lat, u_lon, c['lat'], c['lon'])
        
        # Grab Fare Logic: RM5 base + RM1.40 per KM
        # Add RM5.74 if going to the Island (Bridge Toll)
        toll = 5.74 if c['zone'] == "Island" else 0
        fare = 5 + (dist * 1.40) + toll
        results.append((c['name'], dist, c['zone'], fare))

    results.sort(key=lambda x: x[1])
    
    print(f"\n{'Company Name':<25} | {'KM':<6} | {'Zone':<12} | {'Est. Fare'}")
    print("-" * 75)
    for name, d, zone, fare in results:
        # This part ensures the price is actually printed
        note = "✅ CHEAP" if d < 5 else "⚠️ PRICEY"
        print(f"{name:<25} | {d:>5.1f} | {zone:<12} | RM{fare:>6.2f} {note}")

if __name__ == "__main__":
    main()
