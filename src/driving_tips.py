def generate_tips(
    speed,
    terrain,
    braking,
    acceleration,
    energy
):

    tips = []


    # Energy consumption analysis
    if energy > 25:
        tips.append(
            "High energy usage detected. Try driving more efficiently."
        )

    elif energy > 15:
        tips.append(
            "Moderate energy consumption. Some improvements are possible."
        )

    else:
        tips.append(
            "Excellent energy efficiency. Keep driving smoothly."
        )


    # Speed analysis
    if speed > 80:
        tips.append(
            "Reduce speed to around 50-70 km/h to improve battery range."
        )

    elif speed < 20:
        tips.append(
            "Very low speed may reduce traffic efficiency."
        )


    # Braking analysis
    if braking >= 4:
        tips.append(
            "Frequent braking detected. Maintain a safe distance and drive smoothly."
        )

    elif braking <= 2:
        tips.append(
            "Good braking habits detected."
        )


    # Acceleration analysis
    if acceleration >= 4:
        tips.append(
            "Aggressive acceleration consumes more battery. Accelerate gradually."
        )

    else:
        tips.append(
            "Acceleration pattern is efficient."
        )


    # Terrain analysis
    if terrain == 1:
        tips.append(
            "Uphill driving requires more energy. Maintain steady speed."
        )

    elif terrain == 2:
        tips.append(
            "Downhill detected. Use regenerative braking when possible."
        )

    else:
        tips.append(
            "Flat terrain provides optimal driving conditions."
        )


    return tips