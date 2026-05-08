# Salesforce Apex Project - Feedback Form System

## Problem Statement
Creating an Application in SalesForce.com using Apex Programming Language.

---

# Aim

To develop a simple Feedback Form application using Salesforce Apex and Visualforce.

---

# Software Requirements

1. Internet Connection  
2. Web Browser  
3. Salesforce Developer Account  

---

# Introduction

The Feedback Form System is a simple Salesforce cloud application developed using Apex programming language and Visualforce pages.

It allows users to enter:
- Customer Name
- Email
- Feedback Message
- Rating

The application demonstrates:
- Apex Controller
- Visualforce User Interface
- Cloud-based Form Handling
- MVC Architecture

---

# What is Salesforce?

Salesforce is a cloud-based platform used for developing web applications.

In this project:

| Component | Purpose |
|---|---|
| Apex Class | Backend Logic |
| Visualforce Page | Frontend User Interface |
| Salesforce Cloud | Runs the application |

---

# Components Used

## 1. Apex Class (Controller)

The Apex class acts as the backend controller.

### Functions:
- Stores form data
- Handles button click actions
- Processes user input
- Displays result message

Example:
```java
public class FeedbackController
```

---

## 2. Visualforce Page

Visualforce is used to create the frontend user interface.

### Functions:
- Displays input form
- Accepts user data
- Calls Apex methods
- Shows output message

Example:
```html
<apex:page controller="FeedbackController">
```

---

# Working of the System

1. User enters feedback details.
2. Data is sent to Apex controller.
3. `submitFeedback()` method executes.
4. Success message is displayed.

---

# Step-by-Step Execution

## Step 1: Create Salesforce Account

Open:
https://developer.salesforce.com/signup

Create a free Salesforce Developer account and login.

---

## Step 2: Open Developer Console

After login:

1. Click Profile Icon (top-right corner)
2. Click **Developer Console**

---

## Step 3: Create Apex Class

In Developer Console:

```text
File → New → Apex Class
```

### File Name:
```text
FeedbackController
```

### Paste This Code:

```java
public class FeedbackController {

    public String customerName {get; set;}
    public String email {get; set;}
    public String feedback {get; set;}
    public Integer rating {get; set;}
    public String message {get; set;}

    public PageReference submitFeedback() {

        message = 'Feedback Submitted Successfully!';

        return null;
    }
}
```

### Then:
- Click Save
- Make sure no red error appears

---

# Understanding the Apex Code

## Properties

```java
public String customerName {get; set;}
```

Used to store customer name.

Similarly:
- `email` stores email
- `feedback` stores feedback message
- `rating` stores rating
- `message` stores success message

---

## Method

```java
public PageReference submitFeedback()
```

This method executes when Submit button is clicked.

It:
- Processes form data
- Displays success message

---

# Step 4: Create Visualforce Page

In Developer Console:

```text
File → New → Visualforce Page
```

### File Name:
```text
FeedbackPage
```

### Paste This Code:

```html
<apex:page controller="FeedbackController">

    <apex:form>

        <apex:pageBlock title="Customer Feedback Form">

            <apex:pageBlockSection columns="1">

                <apex:inputText 
                    label="Name"
                    value="{!customerName}" />

                <apex:inputText 
                    label="Email"
                    value="{!email}" />

                <apex:inputTextarea 
                    label="Feedback"
                    value="{!feedback}" />

                <apex:inputText 
                    label="Rating"
                    value="{!rating}" />

            </apex:pageBlockSection>

            <apex:pageBlockButtons>

                <apex:commandButton 
                    value="Submit"
                    action="{!submitFeedback}" />

            </apex:pageBlockButtons>

        </apex:pageBlock>

        <h3>{!message}</h3>

    </apex:form>

</apex:page>
```

### Then:
- Click Save
- Make sure no red error appears

---

# Understanding the Visualforce Code

## Controller Connection

```html
controller="FeedbackController"
```

This connects frontend page with Apex backend class.

---

## Input Fields

```html
<apex:inputText>
```

Used to take input from user.

---

## Submit Button

```html
<apex:commandButton>
```

Calls Apex method:

```html
action="{!submitFeedback}"
```

---

# Step 5: Run the Program

After saving:

1. Open Visualforce page
2. Click:
```text
Preview
```
OR

Open in browser using:

```text
https://yourInstance.apex/FeedbackPage
```

---

# Sample Test Case

## Input

| Field | Value |
|---|---|
| Name | Manasi |
| Email | manasi@gmail.com |
| Feedback | Excellent Service |
| Rating | 5 |

---

## Expected Output

```text
Feedback Submitted Successfully!
```

---

# Common Errors and Fixes

## 1. Unknown Controller Error

### Error:
```text
Unknown controller 'FeedbackController'
```

### Fix:
Make sure:
- Apex class name is `FeedbackController`
- Visualforce page controller name is same

---

## 2. Compile Error

### Reason:
- Missing semicolon
- Missing bracket

### Fix:
Check:
```java
;
{ }
```

---

## 3. Page Not Opening

### Fix:
- Save both files properly
- Refresh browser

---

# Advantages

- Easy to use
- Cloud-based application
- Beginner-friendly
- Fast form handling
- No software installation required

---

# Limitations

- Requires internet connection
- No database storage implemented
- Simple functionality only

---

# Conclusion

The Feedback Form System successfully demonstrates how Salesforce Apex and Visualforce can be used to develop a simple cloud-based application.

The project demonstrates:
- Frontend and backend integration
- Form handling
- Cloud application development using Salesforce

---

# Viva Questions

## Q1. What is Apex?
Apex is Salesforce’s programming language used for backend development.

---

## Q2. What is Visualforce?
Visualforce is a framework used to design user interfaces in Salesforce.

---

## Q3. What is Controller?
Controller handles communication between frontend and backend.

---

## Q4. What does submitFeedback() do?
It processes form submission and displays success message.

---

## Q5. What architecture is used?
MVC Architecture.

