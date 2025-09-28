def get_city_tier_benchmark(tier):
    benchmarks = {
        "Tier 1": {"healthy": 50, "moderate": 70},
        "Tier 2": {"healthy": 45, "moderate": 65},
        "Tier 3": {"healthy": 40, "moderate": 60}
    }
    return benchmarks.get(tier, benchmarks["Tier 2"])

