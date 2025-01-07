class EmployeePage:
    def __init__(self, page):
        self.page = page
        self.name_input = page.locator('input[name="name"]')
        self.email_input = page.locator('input[name="email"]')
        self.address1_input = page.locator('input[name="address_line1"]')
        self.address2_input = page.locator('input[name="address_line2"]')
        self.city_input = page.locator('input[name="city"]')
        self.zip_code_input = page.locator('input[name="zip_code"]')
        self.hiring_date_input = page.locator('input[name="hiring_date"]')
        self.job_title_input = page.locator('input[name="job_title"]')
        self.add_button = page.locator("text='Add'")

    def navigate(self):
        self.page.goto("/add_employee")

    def fill_employee_form(self, name, email, address1, address2, city, zip_code, hiring_date, job_title):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.address1_input.fill(address1)
        self.address2_input.fill(address2)
        self.city_input.fill(city)
        self.zip_code_input.fill(zip_code)
        self.hiring_date_input.fill(hiring_date)
        self.job_title_input.fill(job_title)

    def submit(self):
        self.add_button.click()