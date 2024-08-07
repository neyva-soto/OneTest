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
      | username  |  password   |


     #verificar que existe el boton de login
  Scenario: Login successfully
    When The user is on the login page
    Then button will be displayed


  Scenario Outline: Login successfully
    Given The user is on the login page
    When the user enters the value "<User>" in the text-input for username
    And the user enters the value "<Password>" in the text-input for password
    And the user clicks login button
    Then the user should see the following text in the page "<Text>"

    Examples:
      | User    | Password   | Text      |
      | Admin   | admin123   | Dashboard |


    #verificar el inicio de sesion con datos vacios
  Scenario: Login successfully
    Given The user is on the login page
    When the user clicks login button
    Then User and password fields should be displayed are required


 #inicio de sesion con login vacio
  Scenario Outline: Login successfully
    Given The user is on the login page
    When the user enters the value "<Password>" in the text-input for password
    And the user clicks login button
    Then Then it will be shown that the username field is required

    Examples:
      | Password   | Text      |
      | admin123   | Dashboard |

 #inicio de sesion con password vacio
  Scenario Outline: Password sucessfully
    Given The user is on the login page
    When the user enters the value "<User>" in the text-input for username
    And the user clicks login button
    Then Then it will be shown that the password field is required

    Examples:
      | User  | Text      |
      | admin | Dashboard |


    #inicio de sesion con datos erroneos
  Scenario Outline: Login successfully
    Given The user is on the login page
    When the user enters the value "<User>" in the text-input for username
    And the user enters the value "<Password>" in the text-input for password
    And the user clicks login button
    Then will display a message <mensaje>

    Examples:
      | User  | Password | mensaje   |
      | super | super123 | Dashboard |

          #inicio de sesion con username erroneo
  Scenario Outline: Login successfully
    Given The user is on the login page
    When the user enters the value "<User>" in the text-input for username
    And the user enters the value "<Password>" in the text-input for password
    And the user clicks login button
    Then will display a message

    Examples:
      | User  | Password | mensaje   |
      | super | admin123 | Dashboard |


            #inicio de sesion con password erroneo
  Scenario Outline: Login successfully
    Given The user is on the login page
    When the user enters the value "<User>" in the text-input for username
    And the user enters the value "<Password>" in the text-input for password
    And the user clicks login button
    Then will display a message

    Examples:
      | User  | Password | mensaje   |
      | Admin | super123 | Dashboard |



       #verificar el enlace de olvidaste la contraseña
  Scenario : Forgot password
    Given The user is on the login page
    When the user clicks in forgotPassword
    Then the new password form will show up


    #Verificar el Formato de Credenciales Permitido
  Scenario Outline: Login successfully
    Given The user is on the login page
    When the user enters the value "<User>" in the text-input for username
    And the user enters the value "<Password>" in the text-input for password
    And the user clicks login button
    Then will display a message

    Examples:
      | User  | Password | Text      |
      | ADMIN | admin123 | Dashboard |
