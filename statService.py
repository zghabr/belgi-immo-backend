
def get_stats_data():
    return {
        "summary": {"avg_price": 345000, "transactions": 128000, "regions_tracked": 3},
        "top_expensive": {
            "total": [
                {"name": "Knokke-Heist", "price": "€845,000"},
                {"name": "Ixelles", "price": "€720,000"},
                {"name": "Uccle", "price": "€695,000"},
                {"name": "Sint-Martens-Latem", "price": "€680,000"},
                {"name": "Woluwe-Saint-Pierre", "price": "€650,000"},
            ],
            "per_m2": [
                {"name": "Ixelles", "price": "€4,850/m²"},
                {"name": "Saint-Gilles", "price": "€4,600/m²"},
                {"name": "Brussels City", "price": "€4,400/m²"},
                {"name": "Etterbeek", "price": "€4,350/m²"},
                {"name": "Knokke-Heist", "price": "€4,200/m²"},
            ],
        },
        "top_affordable": {
            "total": [
                {"name": "Hastière", "price": "€115,000"},
                {"name": "Colfontaine", "price": "€128,000"},
                {"name": "Quaregnon", "price": "€132,000"},
                {"name": "Viroinval", "price": "€135,000"},
                {"name": "Froidchapelle", "price": "€140,000"},
            ],
            "per_m2": [
                {"name": "Colfontaine", "price": "€1,050/m²"},
                {"name": "Quaregnon", "price": "€1,120/m²"},
                {"name": "Frameries", "price": "€1,180/m²"},
                {"name": "Dour", "price": "€1,220/m²"},
                {"name": "Charleroi", "price": "€1,250/m²"},
            ],
        },
        "regional_comparison": [
            {"name": "Brussels", "house": 485000, "apartment": 312000, "avgM2": 3200},
            {"name": "Flanders", "house": 340000, "apartment": 245000, "avgM2": 2600},
            {"name": "Wallonia", "house": 210000, "apartment": 185000, "avgM2": 1800},
        ],
        "scatter_data": [
            {"area": 80, "price": 250000, "region": "Flanders"},
            {"area": 120, "price": 380000, "region": "Flanders"},
            {"area": 150, "price": 450000, "region": "Flanders"},
            {"area": 200, "price": 580000, "region": "Flanders"},
            {"area": 60, "price": 280000, "region": "Brussels"},
            {"area": 90, "price": 420000, "region": "Brussels"},
            {"area": 130, "price": 550000, "region": "Brussels"},
            {"area": 180, "price": 720000, "region": "Brussels"},
            {"area": 100, "price": 180000, "region": "Wallonia"},
            {"area": 140, "price": 240000, "region": "Wallonia"},
            {"area": 190, "price": 310000, "region": "Wallonia"},
            {"area": 250, "price": 420000, "region": "Wallonia"},
        ],
        "market_distribution": {
            "House": [
                {"name": "Budget (<300k)", "value": 35, "color": "#E5E7EB"},
                {"name": "Mid-Range (300k-600k)", "value": 45, "color": "#9CA3AF"},
                {"name": "Premium (600k-1.2M)", "value": 15, "color": "#4B5563"},
                {"name": "Luxury (>1.2M)", "value": 5, "color": "#1F2937"},
            ],
            "Apartment": [
                {"name": "Budget (<300k)", "value": 55, "color": "#E5E7EB"},
                {"name": "Mid-Range (300k-600k)", "value": 35, "color": "#9CA3AF"},
                {"name": "Premium (600k-1.2M)", "value": 8, "color": "#4B5563"},
                {"name": "Luxury (>1.2M)", "value": 2, "color": "#1F2937"},
            ],
        },
        "currency": "EUR",
    }
