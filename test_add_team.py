from models.team import TeamPage

def test_create_team(page):
    # in the test
    team_name = "my team"
    team_page = TeamPage(page)
    team_page.navigate_to_add_team()
    team_page.create_team(team_name)
    team_page.navigate_to_teams_list()
    assert team_page.is_team_visible(team_name)