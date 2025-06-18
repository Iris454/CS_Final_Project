#CS30 Practical Exam Portion: Average Speed

class Mission:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

class SpaceProbe:
    def __init__(self, name):
        self.name = name
        self.times = {}

    def add_time(self, mission_name, time_min):
        self.times[mission_name] = time_min

    def average_speed(self, missions):
        total_distance = 0
        total_time = 0
        for m, t in self.times.items():
            if m in missions:
                total_distance += missions[m].distance
                total_time += t / 60 
        if total_time == 0:
            return 0
        return total_distance / total_time

class ReportGenerator:
    def __init__(self, probes, missions):
        self.probes = probes
        self.missions = missions

    def generate_report(self):
        lines = []
        for p in self.probes:
            speed = p.average_speed(self.missions)
            lines.append(f"{p.name}'s Avrage speed: {speed} km/h")
        with open("probe_perfromace.txt", "w") as f:
            f.write("\n".join(lines))

missions = {
    "Lunar Survey": Mission("Lunar Survey", 384000),
    "Mars Flyby": Mission("Mars Flyby", 225000000),
}

aurora = SpaceProbe("Aurora")
aurora.add_time("Lunar Survey", 720000)
aurora.add_time("Mars Flyby", 2800000)

voyager = SpaceProbe("Voyager")
voyager.add_time("Lunar Survey", 750000)
voyager.add_time("Mars Flyby", 2900000)

zenith = SpaceProbe("Zenith")
zenith.add_time("Lunar Survey", 735000)
zenith.add_time("Mars Flyby", 2850000)

probes = [aurora, voyager, zenith]

ReportGenerator(probes, missions).generate_report()
