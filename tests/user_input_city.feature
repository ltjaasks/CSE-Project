Feature: Giving city name as input

Scenario: User gives correct city name as input

    Given User enters the website
    When User types 'London' as city name
    When User clicks on the search button
    Then User should see the weather details of London

Scenario: User gives incorrect city name as input

    Given User enters the website
    When User types 'FakeCityName' as city name
    When User clicks on the search button
    Then User should see the error message 'Enter a valid city name'

Scenario: User gives empty city name as input

    Given User enters the website
    When User types '' as city name
    When User clicks on the search button
    Then User should see the error message 'Enter a valid city name'

Scenario: User gives a city name that is interpreted differently by APIs

    Given User enters the website
    When User types 'Kairo' as city name
    When User clicks on the search button
    Then User should see the note about the different interpretation of the city name by APIs