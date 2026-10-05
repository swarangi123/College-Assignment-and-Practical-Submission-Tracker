import tkinter as tk

from database.db import initialize_database


class SmartClassApp:

    def __init__(self, root):

        self.root = root

        self.root.title("SmartClass.ai")

        self.root.geometry("1200x700")
        self.root.minsize(1000, 600)

        self.current_user = None
        self.content_frame = None

        self.show_login()

    # ---------------- LOGIN ----------------

    def show_login(self):

        from ui.login import LoginPage

        LoginPage(
            self.root,
            self
        )

    def login_success(self, user):

        self.current_user = user

        self.show_dashboard()

    # ---------------- MAIN DASHBOARD ----------------

    def show_dashboard(self):

        # Clear the entire window
        for widget in self.root.winfo_children():
            widget.destroy()

        # ================= SIDEBAR =================

        sidebar = tk.Frame(
            self.root,
            bg="#17182b",
            width=230
        )

        sidebar.pack(
            side="left",
            fill="y"
        )

        sidebar.pack_propagate(False)

        # Logo
        tk.Label(
            sidebar,
            text="✦ SmartClass.ai",
            font=("Segoe UI", 17, "bold"),
            bg="#17182b",
            fg="white"
        ).pack(pady=(30, 5))

        # Show current role
        tk.Label(
            sidebar,
            text=self.current_user["role"],
            font=("Segoe UI", 9),
            bg="#17182b",
            fg="#a0aec0"
        ).pack(pady=(0, 25))

        # ================= CONTENT =================

        self.content_frame = tk.Frame(
            self.root,
            bg="#f5f6fa"
        )

        self.content_frame.pack(
            side="right",
            fill="both",
            expand=True
        )

        # ================= ROLE-BASED MENU =================

        if self.current_user["role"] == "Teacher":

            buttons = [
                ("⌂  Dashboard", "dashboard"),
                ("▣  Assignments", "assignments"),
                ("◈  Submissions", "submissions"),
                ("♟  Students", "students"),
                ("✦  AI Insights", "ai"),
                ("▤  Analytics", "analytics")
            ]

        else:

            buttons = [
                ("⌂  Dashboard", "dashboard"),
                ("▣  Assignments", "assignments"),
                ("◈  My Submissions", "submissions"),
                ("✦  AI Insights", "ai")
            ]

        # Create menu buttons
        for text, page in buttons:

            tk.Button(
                sidebar,
                text=text,
                command=lambda p=page: self.navigate(p),
                bg="#17182b",
                fg="white",
                activebackground="#6658f5",
                activeforeground="white",
                relief="flat",
                bd=0,
                anchor="w",
                font=("Segoe UI", 10, "bold"),
                cursor="hand2"
            ).pack(
                fill="x",
                padx=15,
                pady=3,
                ipady=10
            )

        # ================= LOGOUT =================

        tk.Button(
            sidebar,
            text="↪  Logout",
            command=self.logout,
            bg="#17182b",
            fg="#ffaaaa",
            activebackground="#332020",
            activeforeground="#ffaaaa",
            relief="flat",
            bd=0,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2"
        ).pack(
            side="bottom",
            fill="x",
            padx=15,
            pady=25,
            ipady=10
        )

        # Open dashboard first
        self.navigate("dashboard")

    # ---------------- NAVIGATION ----------------

    def navigate(self, page):

        if self.content_frame is None:
            return

        # Clear current page
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Dashboard
        if page == "dashboard":

            from ui.dashboard import DashboardPage

            DashboardPage(
                self.content_frame,
                self
            )

        # Assignments
        elif page == "assignments":

            from ui.assignments import AssignmentsPage

            AssignmentsPage(
                self.content_frame,
                self
            )

        # Students
        elif page == "students":

            # Students should NEVER access this page
            if self.current_user["role"] != "Teacher":
                return

            from ui.students import StudentsPage

            StudentsPage(
                self.content_frame,
                self
            )

        # Submissions
        elif page == "submissions":

            from ui.submissions import SubmissionsPage

            SubmissionsPage(
                self.content_frame,
                self
            )

        # AI
        elif page == "ai":

            from ui.ai_insights import AIInsightsPage

            AIInsightsPage(
                self.content_frame,
                self
            )

        # Analytics
        elif page == "analytics":

            # Students should NEVER access analytics
            if self.current_user["role"] != "Teacher":
                return

            from ui.analytics import AnalyticsPage

            AnalyticsPage(
                self.content_frame,
                self
            )

    # ---------------- LOGOUT ----------------

    def logout(self):

        self.current_user = None
        self.content_frame = None

        self.show_login()


# ================= START APPLICATION =================

if __name__ == "__main__":

    initialize_database()

    root = tk.Tk()

    app = SmartClassApp(root)

    root.mainloop()
