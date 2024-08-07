import random

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
activities = ['Museum Visit', 'Hiking', 'Shopping', 'Dining Out', 'Concert']

def plan_trip():
    trip_plan = {city: random.choice(activities) for city in cities}
    return trip_plan

def display_plan(plan):
    print("Rencana Perjalanan:")
    for city, activity in plan.items():
        print(f"{city}: {activity}")
    print()

def main():
    print("Sistem Perencanaan Perjalanan")
    plan = plan_trip()
    display_plan(plan)

if __name__ == "__main__":
    main()
