Feature: Edit vehicle
    In order to keep updated my previous registers about vehicles
    As a user
    I want to edit a vehicle register I created

    Background: There are registered users and a vehicle by one of them
        Given Exists a user "user1" with password "password"
        And Exists a user "user2" with password "password"
        And Exists a vehicle registered by "user1"
            | type  | plate number  |
            | Car   | 12345ABC      |

    Scenario: Edit type of an owned vehicle
        Given I login as user "user1" with password "password"
        When I edit the vehicle with plate number "12345ABC"
            | type  |
            | Car   |
        Then I'm viewing the details page for vehicle by "user1"
            | type      | plate number  |
            | Motorbike | 12345ABC      |
        And There are 1 vehicle
    
    Scenario: Edit plate number of an owned vehicle
        Given I login as user "user1" with password "password"
        When I edit the vehicle with plate number "12345ABC"
            | type  |
            | Car   |
        Then I'm viewing the details page for vehicle by "user1"
            | type  | plate number  |
            | Car   | 00000AAA      |
        And There are 1 vehicle