Feature: Login Postulante

  Scenario: Login at /
    Given load path /
    When I click on Ingresa link
    When I put mario21ic@gmail.com and miclave1234
    When I clic on Ingresar buton
    When I wait 5 seconds
    Then I see the url 
