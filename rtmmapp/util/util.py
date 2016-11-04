def validate_diameters(lip_outer_diameter, lip_inner_diameter, bottom_diameter):
    if lip_outer_diameter < lip_inner_diameter:
        return "Lip outer diameter not be less than lip inner diameter."

def get_help_text():
    return [
        "Cut black paths. Engrave or fast cut blue paths for positioning guides.",
        "Glue part #2 centrally onto part #1 using engraved/cut guide.",
        "Glue ring #3 centrally onto part #4 using engraved/cut guide",
        "Glue 3x mounting parts into slots in #4 on opposite side to ring."
    ]
    