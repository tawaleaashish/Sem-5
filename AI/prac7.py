fact_base = {}
rule_base = []

def add_fact(fact_name, value):
    fact_base[fact_name] = value

def add_rule(conditions, action):
    rule_base.append((conditions, action))

def turn_on_lights():
    print("Turn on the lights\n")

def turn_off_lights():
    print("Turn off the lights\n")

def adjust_thermostat_for_heating():
    print("Adjust the thermostat for heating\n")

def adjust_thermostat_for_cooling():
    print("Adjust the thermostat for cooling\n")

def run_production_system():
    while True:
        triggered = False
        for conditions, action in rule_base:
            if all(eval(condition, fact_base) for condition in conditions):
                action()
                triggered = True
        if triggered:
            break


add_fact("time_of_day", "night")
add_fact("motion_detected", False)
add_fact("temperature", 16)

add_rule(["time_of_day == 'night'", "motion_detected"], turn_on_lights)
add_rule(["time_of_day == 'night'", "not motion_detected"], turn_off_lights)
add_rule(["temperature > 40"], adjust_thermostat_for_cooling)
add_rule(["temperature < 20"], adjust_thermostat_for_heating)

run_production_system()