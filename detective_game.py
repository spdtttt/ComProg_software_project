from abc import ABC, abstractmethod
import random


# =========================================================
# CHARACTER
# =========================================================

class Character:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def introduce(self):
        return f"{self.name} - {self.role}"


class Victim(Character):
    def __init__(self, name, role):
        super().__init__(name, role)


class Suspect(Character):
    def __init__(self, name, role):
        super().__init__(name, role)

        # Encapsulation
        self.__statement = ""

    def set_statement(self, statement):
        self.__statement = statement

    def interrogate(self):
        print("\n================================")
        print(f"Interrogating: {self.name}")
        print(f"Occupation: {self.role}")
        print("================================")
        print(f'"{self.__statement}"')


class Detective(Character):
    def __init__(self, name):
        super().__init__(name, "Detective")
        self.evidence_inventory = []

    def collect_evidence(self, evidence):
        if evidence not in self.evidence_inventory:
            self.evidence_inventory.append(evidence)

    def show_evidence(self):
        print("\n========== EVIDENCE ==========")

        if len(self.evidence_inventory) == 0:
            print("You have not collected any evidence yet.")
            return

        for i, evidence in enumerate(self.evidence_inventory):
            print(f"\nEvidence #{i + 1}")
            evidence.examine()


# =========================================================
# EVIDENCE
# =========================================================

class Evidence(ABC):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @abstractmethod
    def examine(self):
        pass


class PhysicalEvidence(Evidence):
    def examine(self):
        print("[Physical Evidence]")
        print(f"Name: {self.name}")
        print(f"Detail: {self.description}")


class DigitalEvidence(Evidence):
    def examine(self):
        print("[Digital Evidence]")
        print(f"Name: {self.name}")
        print(f"Detail: {self.description}")


class TestimonyEvidence(Evidence):
    def examine(self):
        print("[Testimony]")
        print(f"Name: {self.name}")
        print(f"Detail: {self.description}")


# =========================================================
# LOCATION
# =========================================================

class Location:
    def __init__(self, name):
        self.name = name
        self.__evidence = []
        self.__investigated = False

    def add_evidence(self, evidence):
        self.__evidence.append(evidence)

    def is_investigated(self):
        return self.__investigated

    def investigate(self, detective):
        print("\n================================")
        print(f"Investigating: {self.name}")
        print("================================")

        if self.__investigated:
            print("You have already investigated this location.")
            return

        self.__investigated = True

        if len(self.__evidence) == 0:
            print("You searched the area...")
            print("Nothing suspicious was found.")
            return

        print(f"You found {len(self.__evidence)} piece(s) of evidence!")

        for evidence in self.__evidence:
            print()
            evidence.examine()

            detective.collect_evidence(evidence)

        print("\nEvidence added to your inventory.")


# =========================================================
# CASE
# =========================================================

class Case:
    def __init__(
        self,
        title,
        victim,
        suspects,
        locations,
        murderer,
        crime_time,
        motive,
        weapon,
        crime_location
    ):
        self.title = title
        self.victim = victim
        self.suspects = suspects
        self.locations = locations

        # Sensitive case information is encapsulated
        self.__murderer = murderer
        self.__crime_time = crime_time
        self.__motive = motive
        self.__weapon = weapon
        self.__crime_location = crime_location

    def show_case_information(self):
        print("\n========================================")
        print("             CASE FILE")
        print("========================================")

        print(f"Case: {self.title}")

        print("\nVictim:")
        print(f"{self.victim.name} - {self.victim.role}")

        print("\nKnown Suspects:")

        for i, suspect in enumerate(self.suspects):
            print(
                f"{i + 1}. "
                f"{suspect.name} "
                f"({suspect.role})"
            )

        print("\nPossible Locations:")

        for i, location in enumerate(self.locations):
            print(
                f"{i + 1}. "
                f"{location.name}"
            )

        print("\nYour objective:")
        print("Collect evidence, interrogate suspects,")
        print("and identify the murderer.")

    def show_suspects(self):
        print("\n========== SUSPECTS ==========")

        for i, suspect in enumerate(self.suspects):
            print(
                f"{i + 1}. "
                f"{suspect.name} "
                f"({suspect.role})"
            )

    def show_locations(self):
        print("\n========== LOCATIONS ==========")

        for i, location in enumerate(self.locations):

            status = ""

            if location.is_investigated():
                status = " [Investigated]"

            print(
                f"{i + 1}. "
                f"{location.name}"
                f"{status}"
            )

    def accuse(self, suspect):
        return suspect == self.__murderer

    def reveal_solution(self):
        print("\n========================================")
        print("            CASE SOLUTION")
        print("========================================")

        print(f"Murderer: {self.__murderer.name}")
        print(f"Role: {self.__murderer.role}")
        print(f"Crime Time: {self.__crime_time}")
        print(f"Crime Location: {self.__crime_location.name}")
        print(f"Weapon: {self.__weapon}")
        print(f"Motive: {self.__motive}")


# =========================================================
# CASE GENERATOR
# =========================================================

class CaseGenerator:

    SUSPECT_POOL = [
        ("Alice Wang", "Secretary"),
        ("Bob Banana", "Business Partner"),
        ("Charlie Chaplin", "Security Guard"),
        ("Nene Royal", "Daughter"),
        ("Cristiano Ronaldo", "Accountant"),
        ("Kanchai Kamnerdploy", "Lawyer"),
        ("George Russel", "Manager"),
        ("Max Verstappen", "Personal Assistant"),
    ]

    LOCATIONS = [
        "Office",
        "Lobby",
        "Parking Lot",
        "Security Room"
    ]

    CRIME_TIMES = [
        "21:30",
        "21:45",
        "22:00",
        "22:15",
        "22:30"
    ]

    MOTIVES = [
        "Money",
        "Revenge",
        "Jealousy",
        "Hidden Debt",
        "Business Conflict",
        "Inheritance",
        "Hungry"
    ]

    WEAPONS = [
        "Knife",
        "Poison",
        "Metal Pipe",
        "Heavy Statue",
        "Rope"
    ]

    CASE_TITLES = [
        "The Midnight Murder",
        "Death Behind Closed Doors",
        "The Silent Office",
        "Murder at Blackwood Company",
        "The Last Meeting"
    ]

    @staticmethod
    def generate():
        # -------------------------------------------------
        # Random number of suspects
        # -------------------------------------------------

        suspect_count = random.randint(4, 5)

        selected_people = random.sample(
            CaseGenerator.SUSPECT_POOL,
            suspect_count
        )

        suspects = []

        for name, role in selected_people:
            suspect = Suspect(name, role)
            suspects.append(suspect)

        # -------------------------------------------------
        # Create locations
        # -------------------------------------------------

        locations = []

        for location_name in CaseGenerator.LOCATIONS:
            locations.append(Location(location_name))

        # -------------------------------------------------
        # Random murderer
        # -------------------------------------------------

        murderer = random.choice(suspects)

        # -------------------------------------------------
        # Random crime information
        # -------------------------------------------------

        crime_time = random.choice(
            CaseGenerator.CRIME_TIMES
        )

        motive = random.choice(
            CaseGenerator.MOTIVES
        )

        weapon = random.choice(
            CaseGenerator.WEAPONS
        )

        crime_location = random.choice(
            locations
        )

        # -------------------------------------------------
        # Generate suspect statements
        # -------------------------------------------------

        CaseGenerator.generate_statements(
            suspects,
            murderer,
            locations,
            crime_location,
            crime_time
        )

        # -------------------------------------------------
        # Generate evidence
        # -------------------------------------------------

        CaseGenerator.generate_evidence(
            murderer,
            crime_time,
            weapon,
            crime_location,
            locations
        )

        # -------------------------------------------------
        # Victim
        # -------------------------------------------------

        victim = Victim(
            "Richard Black",
            "Company CEO"
        )

        title = random.choice(
            CaseGenerator.CASE_TITLES
        )

        # -------------------------------------------------
        # Return generated Case object
        # -------------------------------------------------

        return Case(
            title,
            victim,
            suspects,
            locations,
            murderer,
            crime_time,
            motive,
            weapon,
            crime_location
        )

    # =====================================================
    # GENERATE STATEMENTS
    # =====================================================

    @staticmethod
    def generate_statements(
        suspects,
        murderer,
        locations,
        crime_location,
        crime_time
    ):

        safe_locations = []

        for location in locations:
            if location != crime_location:
                safe_locations.append(location)

        for suspect in suspects:

            alibi_location = random.choice(
                safe_locations
            )

            if suspect == murderer:

                statement = (
                    f"I was at the {alibi_location.name} "
                    f"around {crime_time}. "
                    f"I never went near the "
                    f"{crime_location.name}."
                )

            else:

                statement = (
                    f"I was at the {alibi_location.name} "
                    f"around {crime_time}. "
                    f"I didn't see anything unusual."
                )

            suspect.set_statement(statement)

    # =====================================================
    # GENERATE EVIDENCE
    # =====================================================

    @staticmethod
    def generate_evidence(
        murderer,
        crime_time,
        weapon,
        crime_location,
        locations
    ):

        # -------------------------------------------------
        # Physical Evidence
        # -------------------------------------------------

        physical = PhysicalEvidence(
            f"{weapon} with fingerprints",

            (
                f"A {weapon.lower()} was discovered "
                f"at the crime scene. "
                f"Fingerprints matching "
                f"{murderer.name} were found on it."
            )
        )

        crime_location.add_evidence(
            physical
        )

        # -------------------------------------------------
        # Digital Evidence
        # -------------------------------------------------

        digital = DigitalEvidence(
            "Security Camera Footage",

            (
                f"CCTV footage shows "
                f"{murderer.name} entering "
                f"the {crime_location.name} "
                f"shortly before {crime_time}."
            )
        )

        security_room = None

        for location in locations:
            if location.name == "Security Room":
                security_room = location
                break

        security_room.add_evidence(
            digital
        )

        # -------------------------------------------------
        # Testimony
        # -------------------------------------------------

        testimony = TestimonyEvidence(
            "Witness Statement",

            (
                f"A witness remembers seeing "
                f"{murderer.name} leaving "
                f"the {crime_location.name} "
                f"around {crime_time}."
            )
        )

        lobby = None

        for location in locations:
            if location.name == "Lobby":
                lobby = location
                break

        lobby.add_evidence(
            testimony
        )


# =========================================================
# GAME
# =========================================================

class Game:
    def __init__(self):
        self.detective = Detective("Player")

        self.case = CaseGenerator.generate()

        self.game_over = False

    # =====================================================
    # MAIN GAME LOOP
    # =====================================================

    def start(self):
        print("\n========================================")
        print("          DETECTIVE GAME")
        print("========================================")

        self.case.show_case_information()

        while not self.game_over:

            self.show_menu()

            choice = input("\nChoose an action: ")

            if choice == "1":
                self.investigate()

            elif choice == "2":
                self.interrogate()

            elif choice == "3":
                self.detective.show_evidence()

            elif choice == "4":
                self.accuse()

            elif choice == "5":
                print("\nYou abandoned the investigation.")
                self.game_over = True

            else:
                print("\nInvalid choice.")

    # =====================================================
    # MENU
    # =====================================================

    def show_menu(self):
        print("\n========================================")
        print("                ACTIONS")
        print("========================================")

        print("1. Investigate Location")
        print("2. Interrogate Suspect")
        print("3. View Evidence Inventory")
        print("4. Accuse Suspect")
        print("5. Exit Game")

    # =====================================================
    # INVESTIGATION
    # =====================================================

    def investigate(self):
        self.case.show_locations()

        try:
            choice = int(
                input("\nChoose location: ")
            )

            if choice < 1 or choice > len(self.case.locations):
                print("Invalid location.")
                return

            location = self.case.locations[
                choice - 1
            ]

            location.investigate(
                self.detective
            )

        except ValueError:
            print("Please enter a number.")

    # =====================================================
    # INTERROGATION
    # =====================================================

    def interrogate(self):
        self.case.show_suspects()

        try:
            choice = int(
                input("\nChoose suspect: ")
            )

            if choice < 1 or choice > len(self.case.suspects):
                print("Invalid suspect.")
                return

            suspect = self.case.suspects[
                choice - 1
            ]

            suspect.interrogate()

        except ValueError:
            print("Please enter a number.")

    # =====================================================
    # ACCUSATION
    # =====================================================

    def accuse(self):
        print("\nWARNING:")
        print("You only have ONE chance to accuse someone.")
        print("A wrong accusation means GAME OVER.")

        confirm = input(
            "\nDo you want to continue? (y/n): "
        ).lower()

        if confirm != "y":
            return

        self.case.show_suspects()

        try:
            choice = int(
                input("\nWho is the murderer? ")
            )

            if choice < 1 or choice > len(self.case.suspects):
                print("Invalid suspect.")
                return

            suspect = self.case.suspects[
                choice - 1
            ]

            if self.case.accuse(suspect):

                print("\n========================================")
                print("                YOU WIN!")
                print("========================================")

                print(
                    f"\nCorrect! {suspect.name} "
                    f"is the murderer."
                )

            else:

                print("\n========================================")
                print("               YOU LOSE!")
                print("========================================")

                print(
                    f"\n{suspect.name} was innocent."
                )

            self.case.reveal_solution()

            self.game_over = True

        except ValueError:
            print("Please enter a number.")


# =========================================================
# RUN PROGRAM
# =========================================================

if __name__ == "__main__":
    game = Game()
    game.start()