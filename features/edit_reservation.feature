Feature: Edit Reservation
    In order to keep updated my previous registers about reservations
    As a user
    I want to edit a reservation register I created

    Background: There is a registered user and a reservation by them
        Given Exists a user "user" with password "password"
        And Exists reservation registered by "user"
            | vehicle   | date                  |
            | 12345ABC  | 01/01/2000 - 12:00h   |
    
    Scenario: Edit date of the reservation
        Given I login as user "user" with password "password"
        When I edit the date of the reservation of the vehicle "12345ABC"
            | date                  |
            | 01/01/2000 - 12:00h   |
        Then I'm viewing the user dashboard with the reservation date updated
            | vehicle   | date                  |
            | 12345ABC  | 01/01/2000 - 18:00h   |
        And There are 1 reservation
    
    Scenario: Cancel a reservation
        Given I login as user "user" with password "password"
        When I cancel the reservation for vehicle "12345ABC"
            | vehicle   | date                  |
            | 12345ABC  | 01/01/2000 - 12:00h   |
        Then I'm viewing the user dashboard with the reservation cancelled
        And There are 0 reservations