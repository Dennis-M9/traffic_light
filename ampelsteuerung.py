import time

class ampel:
    # ID = the Identifikationnumber of the traffic light [str] #a1
    # Phases = Typ of Phases [dict] #{"green":-1, "yellow":1, "red":-1}
    # -1 = LED out | 1 = LED on
    def __init__(self, id, phase):
        self.id = id
        self.phase = phase

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.self = id

    def get_phase(self):
        return self.phase

    def set_phase(self, phase):
        self.phase = phase

    def show_phase(self):
        print("Ampel: %s" % self.id)
        for key in self.phase:
            print("%s: %d" % (key, self.phase[key]))
        print()

if __name__ == "__main__":
    a1 = ampel("a1", {"red":-1, "green":1})
    for ele in range(0,5):
        phase = a1.get_phase()
        phase["red"] = phase["red"]*-1
        phase["green"] = phase["green"]*-1
        a1.set_phase(phase)
        a1.show_phase()
        time.sleep(1)
