class TeamPage:
    def __init__(self, page):
        self.page = page
        self.name_input = page.locator('input[name="name"]')
        self.add_button = page.locator("text='Add'")
        self.proceed_button = page.locator("button:has-text('proceed')")

    #def reset_db(self):
        #self.page.goto("/reset_db")
        #self.proceed_button.click()

    def navigate_to_add_team(self):
        self.page.goto("/add_team")

    def create_team(self, team_name):
        self.name_input.fill(team_name)
        self.add_button.click()

    def navigate_to_teams_list(self):
        self.page.goto("/teams")

    def is_team_visible(self, team_name):
        return self.page.is_visible(f"td:has-text('{team_name}')")