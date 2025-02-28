import pytest
from models.employee import EmployeePage
from models.team import TeamPage

@pytest.fixture
def reset_team(page):
    page.goto("/reset_db")
    proceed_button = page.locator("button:has-text('proceed')")
    proceed_button.click()
    page.close()
    
def test_delete_team(page):
    employee_name = "bob"
    employee_email = "bob@gmail.com"
    employee_address1 = "29 rue de Lorca"
    employee_address2 = "Appt 2"
    employee_city = "Saint-Ouen"
    employee_zip_code = "93400"
    employee_hiring_date = "2024-08-28"
    employee_job_title = "dev"
    team_name = "my team"
    
    employee_page = EmployeePage(page)
    employee_page.navigate()
    employee_page.fill_employee_form(employee_name, employee_email, employee_address1, employee_address2, employee_city, employee_zip_code, employee_hiring_date, employee_job_title)
    employee_page.submit()
    
    team_page = TeamPage(page)
    team_page.navigate()
    team_page.create_team(team_name)
    
    team_page.delete_team(team_name)
    
    assert not page.is_visible(f"td:has-text('{team_name}')")
    
    page.goto("/employees")
    assert page.is_visible(f"td:has-text('{employee_name}')")
    assert page.is_visible(f"td:has-text('{employee_email}')")