# Created by Suganya.Jagadeesan at 13/02/2018

Feature: LogIn User
  In Order to LogIn as Student Admin user
  As a Product Owner
  I want the registered Email address and Password of the user

  Scenario: LogIn User Link
    Given Students Admin user is on Home Page
    When user clicks on LogIn Link
    Then the user should navigate to LogIn User page


  Scenario: Student Admin User LogIn and LogOff
    Given Students Admin user is on LogIn page
    When user provides Email,Password as mandatory details
    And clicks LogIn button
    Then user should navigate to Home page
    And user must have Hello,UserName! in navigation bar
    And user must have 'Log off' link to log off
