Feature: Register Vehicle
    In order to record the car I have,
    As a user
    I want to register a vehicle together with its type and plate number.

    Background: There is a registered user
        Given Exists a user "user" with password "password"
    
    Scenario: Register just vehicle type and plate number
        Given I login as user "user" with password "password"
        When I register vehicle
            | type  | plate number  |
            | Car   | 12345ABC      |
        Then I'm viewing the details page for vehicle by "user"
            | type  | plate number  |
            | Car   | 12345ABC      |
        And There are 1 vehicles
    
    Scenario: Try to register vehicle but not logged In
        Given I'm not logged In
        When I register vehicle
            | type  | plate number  |
            | Car   | 12345ABC      |
        Then I'm redirected to the login form
        And There are 0 vehicles