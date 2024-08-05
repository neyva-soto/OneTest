Feature: Login - Successfully login

  User story:
  * As a user Login Page
  * I want to put username and password
  * in order login

  Acceptance criteria:
  * Login button should work and enter we page

  Scenario Outline: Campos successfully
    Given The user is on the login page
    Then I see input field in the page with id "<UserId>"
    And I see input field in the page with id "<PasswordId>"

    Examples:
      | UserId    | PasswordId  |
      |  username |  password   |


  Scenario Outline: ButtonLogin successfully
    Given The user is on the login page
    And the user clicks login button
    Then the user should see the following text in the page "<Text>"

    Examples:
      | User    | Password   | Text      |
      |         |            | Dashboard |

  Scenario Outline: Login successfully
    Given The user is on the login page
    When the user enters the value "<User>" in the text-input for username
    And the user enters the value "<Password>" in the text-input for password
    And the user clicks login button
    Then the user should see the following text in the page "<Text>"

    Examples:
      | User    | Password   | Text      |
      | Admin   | admin123   | Dashboard |

  Scenario Outline: Password successfully
    Given The user is on the login page
    When the user enters the value "<User>" in the text-input for username
    And the user enters the value "<Password>" in the text-input for password
    And the user clicks login button
    Then the user should see the following text in the page "<Text>"

    Examples:
      | User    | Password   | Text      |
      | Admin   | 12345   | Dashboard |

