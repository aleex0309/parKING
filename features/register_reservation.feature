Feature: Register reservation
    In order to reserve a parking spot
    As a user
    I want to register a reservation in the corresponding parking spot with a vehicle together with its details

    Background: There is a registered user, parking spot and vehicle
        Given Exists a user "user" with password "password"
        And Exists vehicle registered by "user"
            | type  | plate number  |
            | Car   | 12345ABC      |
        And Exists parking spot
            | parking   | type  | free  |
            | UdL       | Car   | False |
    
    Scenario: Register reservation with complete information
        Given I login as "user" with password "password"
        When I register reservation at parking spot "UdL"
            | vehicle     | date                  |
            | 12345ABC    | 01/01/2000 - 12:00h   |
        Then I'm viewing the user dashboard with the recently created reservation listed
        And There are 1 reservation

    Scenario: Try to register a reservation but not logged in
        Given I'm not logged in
        When I register reservation at parking spot "UdL"
            | vehicle   | date                  |
            | 12345ABC  | 01/01/2000 - 12:00h   |
        Then I'm redirected to the login form
        And There are 0 reservation
