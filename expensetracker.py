import flet as ft

def main(page: ft.Page):
    # Βασικές ρυθμίσεις
    page.title = "Expense Tracker "
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 450
    page.window.height = 650
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30

    # Μεταβλητή που κρατάει το συνολικό ποσό
    synolo = 0.0

    # --- Στοιχεία Οθόνης ---
    titlos = ft.Text("Track expenses  💸", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_400)
    
    # Εδώ θα εμφανίζεται το τεράστιο νούμερο του συνόλου
    keimeno_synolou = ft.Text("Sum: 0.00 €", size=34, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)

    # Πεδία εισαγωγής κειμένου
    onoma_exodou = ft.TextField(label="What did you buy? (e.g., Coffee)", expand=True) # Το expand=True το κάνει να πιάνει όλο τον ελεύθερο χώρο
    poso_exodou = ft.TextField(label="Price (€)", width=100)

    # Ένα αόρατο κουτί που θα γεμίζει με τα έξοδα δυναμικά
    # Έχει scroll=AUTO για να μπορούμε να σκρολάρουμε αν γίνουν πολλά
    lista_exodon = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO, expand=True)

    # Ένα κρυφό κόκκινο μήνυμα που θα εμφανίζεται μόνο αν ο χρήστης κάνει λάθος
    minima_lathous = ft.Text("", color=ft.Colors.RED_400, size=14)

    # --- Η Λογική ---
    def prosthiki_exodou(e):
        nonlocal synolo
        
        onoma = onoma_exodou.value
        poso_str = poso_exodou.value

        # Έλεγχος αν είναι άδεια τα πεδία
        if not onoma or not poso_str:
            minima_lathous.value = "Please fill in both fields!"
            page.update()
            return # Σταματάει τη συνάρτηση εδώ, δεν προχωράει παρακάτω

        # Έλεγχος αν έγραψε όντως αριθμό στο ποσό
        try:
            # Αντικαθιστούμε το κόμμα με τελεία
            poso = float(poso_str.replace(",", "."))
        except ValueError:
            minima_lathous.value = "The value must be a number (e.g., 2.50)!"
            page.update()
            return

        # Αν φτάσαμε εδώ, όλα είναι σωστά
        minima_lathous.value = ""
        
        # 1. Αυξάνουμε το συνολικό ποσό
        synolo += poso
        keimeno_synolou.value = f"Sum: {synolo:.2f} €" # Το .2f βάζει πάντα 2 δεκαδικά

        # 2. Φτιάχνουμε το "κουτάκι" για το νέο έξοδο
        nea_eggrafi = ft.Container(
            content=ft.Row(
                [
                    ft.Text(onoma, size=18, weight=ft.FontWeight.BOLD, expand=True),
                    ft.Text(f"{poso:.2f} €", size=18, color=ft.Colors.GREEN_300)
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            padding=15,
            bgcolor=ft.Colors.GREY_900,
            border_radius=10
        )

        # 3. Πετάμε το νέο έξοδο μέσα στη λίστα!
        lista_exodon.controls.append(nea_eggrafi)

        # 4. Αδειάζουμε τα πεδία για να γράψει το επόμενο κατευθείαν
        onoma_exodou.value = ""
        poso_exodou.value = ""

        # Ανανεώνουμε την οθόνη για να φανούν οι αλλαγές
        page.update()

    # Το κουμπί μας
    koumpi_prosthiki = ft.Button("Add", on_click=prosthiki_exodou, icon=ft.Icons.ADD)

    # Βάζουμε τα δύο πεδία στην ίδια σειρά
    grammi_eisagogis = ft.Row([onoma_exodou, poso_exodou])

    # Προσθήκη όλων στη σελίδα
    page.add(
        titlos,
        ft.Divider(height=10, color="transparent"),
        keimeno_synolou,
        ft.Divider(height=20, color="grey"),
        grammi_eisagogis,
        minima_lathous,
        koumpi_prosthiki,
        ft.Divider(height=20, color="transparent"),
        ft.Text("List of Expenses:", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_400),
        lista_exodon
    )

ft.run(main)