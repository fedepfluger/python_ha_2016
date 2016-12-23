Feature: Trabajo Practico 4 ej: 2 Behave

Scenario: Sum of 2 people
    Given The Person "p1" called "Federico" and is "30" years,
        and the Person "p2" called "Cristina" and is "29" years  
        When we add these 2 people
        Then we get a Group of 2 people Containing them
