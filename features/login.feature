Feature: Login Feature

Scenario: Success Login
    Given Open Home Page
    And I Fill my credentials
    When I Click Login Button
    Then I should be logged in

Scenario: Failed Login With Wrong Email
    Given Open Home Page
    And I Fill my credentials with wrong email
    When I Click Login Button
    Then I should not be logged in
    And I should see the error message
