Feature:
    Calculating the roots of a biquadratic equation

Scenario: first equation
    Given coefficients 1, 0, 0
    When the roots get calculated
    Then they are [0]

Scenario: second equation
    Given coefficients 1, -1, 0
    When the roots get calculated
    Then they are [-1, 0, 1]

Scenario: third equation
    Given coefficients 2, 0, 1
    When the roots get calculated
    Then they are [ ]
    