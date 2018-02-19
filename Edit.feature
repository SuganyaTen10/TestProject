# Created by Suganya.Jagadeesan at 14/02/2018
Feature: Edit Student
  In Order to Edit a student detail
  As a Students Admin user
  I want FirstName, LastName, Academic Year


  Scenario: Edit Student link
    Given Students Admin user is on Student Account Page
    When user wants to edit a student
    Then there must be a link as "Edit"
    And clicking the link should navigate to Edit Students Page

  Scenario: Edit Student Details
    Given Students Admin user is on Edit Student Page
    When user wants to edit FirstName,LastName,Academic Year
    Then clicking Update button should update the Student detail
    And the user should navigate to Students page

  Scenario: Canceling in the process of Edit Student
    Given Students Admin user is again on Edit Student Page
    When user decides to cancel editing Student details
    Then clicking cancel button should cancel the edit
    And the user should navigate to Students page





