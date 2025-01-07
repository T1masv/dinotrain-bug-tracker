import pytest

@pytest.fixture
def reset_team(page):
    # Make sure db is empty
    page.goto("/reset_db")
    proceed_button = page.locator("button:has-text('proceed')")
    proceed_button.click()
    page.close()
    
def test_delete_team(page):
    # Create an employee
    page.goto("/add_employee")
    name_input = page.locator('input[name="name"]')
    employee_name = "bob"
    name_input.fill(employee_name)
    email_input = page.locator('input[name="email"]')
    employee_email = "bob@gmail.com"
    email_input.fill(employee_email)
    address1_input = page.locator('input[name="address_line1"]')
    employee_address1 = "29 rue de Lorca"
    address1_input.fill(employee_address1)
    address2_input = page.locator('input[name="address_line2"]')
    employee_address2 = "Appt 2"
    address2_input.fill(employee_address2)
    city_input = page.locator('input[name="city"]')
    employee_city = "Saint-Ouen"
    city_input.fill(employee_city)
    zip_code_input = page.locator('input[name="zip_code"]')
    employee_zip_code = "93400"
    zip_code_input.fill(employee_zip_code)
    hiring_date_input = page.locator('input[name="hiring_date"]')
    employee_hiring_date = "2024-08-28"
    hiring_date_input.fill(employee_hiring_date)
    job_title_input = page.locator('input[name="job_title"]')
    employee_job_title = "dev"
    job_title_input.fill(employee_job_title)
    page.click("text='Add'")

    # Create a team 
    page.goto("/")
    page.goto("/add_team")
    name_input = page.locator('input[name="name"]')
    team_name = "my team"
    name_input.fill(team_name)
    page.click("text='Add'")

    # add employee to team
    page.goto("/")
    page.goto("/employees")
    # click on edit button for employe name 
    page.click(f"td:has-text('{employee_name}') + td button")
    # click on edit button same row

    
        
    # delete team
  
    # check team is delete
    assert not page.is_visible(f"td:has-text('{team_name}')")

    # check employee exist
    page.goto("/")
    page.goto("/employees")

    assert page.is_visible(f"td:has-text('{employee_name}')")
    #check name + email ?
