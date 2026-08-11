def view():
        info_dictionary=dict(
             welcome    = "╔══════════════════════════════════════╗",
        dashboard1 = "║    📘 GRADE TRACKER — {self.name:<10}║",
        dashboard2 = "╠══════════════════════════════════════╣",
        dashboard3 = "║   1. ➕  Add Homework                ║",
        dashboard4 = "║   2. ➕  Add Exam                    ║",
        dashboard5 = "║   3. 📋  List Assignments            ║",
        dashboard6 = "║   4. 🔍  Filter Assignments          ║",
        dashboard7 = "║   5. 📊  Show Summary                ║",
        dashboard8 = "║   0. 🚪  Exit                        ║",
        dashboard9 = "╚══════════════════════════════════════╝"
        )
        for i in info_dictionary.values():
            print(i)
view()