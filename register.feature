# Created by Suganya.Jagadeesan at 11/02/2018

Feature: Register New User
  In Order to Register a new Student Admin user
  As a Product Owner
  I want the Email address and Password of the user

 Scenario: Register User Link
    Given Students Admin user is on Home Page
    When user clicks on Register Link
    Then the user should navigate to Register User page


 Scenario: Mandatory Details for New Student Admin User Registration
    Given Students Admin user is on Register new user page
    When user provides Email,Password,ConfirmPassword as mandatory details
    And clicks Register button
    Then user detail must be added
    And user should navigate to Home page
    And Navigation bar must have Hello,UserName!


 Scenario: Password Mismatch in Students Admin User Registration
    Given Students Admin user is on Register new user page
    When user provides Email and mismatching Password and Confirm Password
    And clicks Register button
    Then error message must be displayed as 'Password and Confirm Password do not match'


 Scenario: User already exists in Student Admin User Registration
    Given Students Admin user is on Register new user page
    When user provides Email,Password,ConfirmPassword as mandatory details
    And clicks Register button
    Then user detail must not be added
    And error message must be displayed as 'Name user@mail.com is already taken.'
