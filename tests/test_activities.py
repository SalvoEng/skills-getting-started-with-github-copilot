def test_get_activities_returns_seeded_data(client):
    response = client.get("/activities")

    assert response.status_code == 200

    activities = response.json()

    assert "Chess Club" in activities
    assert "Programming Class" in activities

    chess_club = activities["Chess Club"]
    assert chess_club["description"] == "Learn strategies and compete in chess tournaments"
    assert chess_club["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
    assert chess_club["max_participants"] == 12
    assert chess_club["participants"] == [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]


def test_get_activities_includes_expected_fields_for_each_activity(client):
    response = client.get("/activities")

    assert response.status_code == 200

    activities = response.json()

    for details in activities.values():
        assert set(details) == {
            "description",
            "schedule",
            "max_participants",
            "participants",
        }
        assert isinstance(details["participants"], list)