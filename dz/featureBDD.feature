Feature: Testing bot functionality

Scenario: Checking if current state is in the required state list
    Given required states are DEFAULT, current state is DEFAULT
    When checking for state
    Then current state being in required is True

Scenario: Checking if the plot file is created
    Given the plotted function is 'abs(x) if x < 0 else log(x)'
    When plotting and saving the file
    Then it is True that the file is there
