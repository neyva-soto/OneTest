Feature: Login - tes

 Scenario Outline: ButtonLogin successfully
    Given The user is on the login page
    Then the user clicks login button

    Examples:
      | User    | Password   | Text      |
      |         |            | Dashboard |