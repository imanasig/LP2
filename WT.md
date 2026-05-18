# 🎓 Web Technology — SQP Exam Preparation Guide
### Units 3, 4, 5 & 6 | SPPU Pattern | Oral Examination

---

## ⚠️ EXAMINER'S NOTE (Read This First)
> Based on SPPU past paper analysis, the following topics carry maximum marks and appear most frequently. Each Q&A below is framed exactly as an examiner would ask — and the answer is what you should say out loud.

---

# 📘 UNIT III — Java Servlets and XML

---

## Q1. What is a Servlet? Explain the Servlet Architecture with its working. *(Most Important)*

**Answer:**

A **Servlet** is a Java program that runs on the server side. It is used to generate dynamic web content in response to client requests.

**Architecture / Working:**
1. The client types a URL in the web browser and makes a request.
2. The web browser sends an HTTP request to the Web Server.
3. The Web Server finds the requested Servlet (managed by a **Servlet Container** like Tomcat).
4. The Servlet gathers relevant information, processes the request, and builds a web page.
5. The response (web page) is sent back to the client.

**Key Points:**
- Servlets run in the address space of the web server → very efficient.
- They are platform-independent (Java-based).
- They use **HttpServletRequest** to read client data and **HttpServletResponse** to write the response.
- Servlet container (e.g., Tomcat) manages the lifecycle.

**Advantages:** Efficient, platform-independent, support session tracking, generate dynamic content, support concurrent requests.

**Disadvantages:** Mixing Java and HTML makes it hard to write, requires Java runtime environment on server.

---

## Q2. Write a "Hello World" Servlet Program. *(SPPU May-19, Marks 5)*

**Answer:**

```java
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class FirstServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
    throws IOException, ServletException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<html>");
        out.println("<head><title>My First Servlet</title></head>");
        out.println("<body>");
        out.println("<h1>Hello World!</h1>");
        out.println("<h2>Welcome to Servlet Application</h2>");
        out.println("</body></html>");
    }
}
```

**Execution Steps:**
1. Compile: `javac FirstServlet.java`
2. Copy the `.class` file to: `C:\xampp\tomcat\webapps\examples\WEB-INF\classes`
3. Edit `web.xml` to add servlet mapping.
4. Start Tomcat.
5. Open browser: `http://localhost/examples/servlet/FirstServlet`

**Key packages used:**
- `java.io.*` — for I/O operations
- `javax.servlet.*` — Servlet interface
- `javax.servlet.http.*` — HttpServlet, HttpServletRequest, HttpServletResponse

---

## Q3. Explain the Servlet Life Cycle with a diagram. *(SPPU March-20, Marks 5)*

**Answer:**

The Servlet Life Cycle has **3 main methods:**

```
Client Request → [init()] → [service()] → [destroy()] → Servlet Unloaded
                    ↓             ↓               ↓
              (First time    (Every request)  (Shutdown)
               only)
```

**1. init() method:**
- Called only **once** when the servlet is loaded into memory for the first time.
- Used for initialization — reading config parameters, opening DB connections.
- Signature: `public void init(ServletConfig config) throws ServletException`

**2. service() method:**
- Called **for every request** from the client.
- Reads the HTTP request data and generates the response.
- For HTTP servlets, this calls `doGet()` or `doPost()` depending on the request type.
- Signature: `public void service(ServletRequest req, ServletResponse res)`

**3. destroy() method:**
- Called **once** when the servlet is being removed from memory (server shutdown).
- Used for cleanup — closing DB connections, saving state.
- Signature: `public void destroy()`

**Example Lifecycle Program:**
```java
public class LifeCycle extends GenericServlet {
    public void init(ServletConfig config) throws ServletException {
        System.out.println("init called");
    }
    public void service(ServletRequest request, ServletResponse response)
    throws ServletException, IOException {
        PrintWriter out = response.getWriter();
        out.println("Service method called");
    }
    public void destroy() {
        System.out.println("destroy called");
    }
}
```

---

## Q4. What are Sessions and Cookies in Servlets? Write a program. *(SPPU Dec-19, Marks 5)*

**Answer:**

### Sessions:
- A **session** tracks a user's interaction with the web application over multiple requests.
- HTTP is stateless, so sessions solve the problem of remembering user data between requests.
- Created using: `HttpSession session = request.getSession();`
- Data stored using: `session.setAttribute("name", value)`
- Data retrieved using: `session.getAttribute("name")`

### Cookies:
- Cookies are **small pieces of information** stored on the client's machine by the server.
- Used to remember user preferences, login status, etc.
- Can be dangerous if misused (privacy issues).

**Creating a Cookie:**
```java
Cookie cookie = new Cookie("user", "John");
response.addCookie(cookie);
```

**Reading Cookies:**
```java
Cookie[] cookies = request.getCookies();
for (Cookie c : cookies) {
    String name = c.getName();
    String value = c.getValue();
}
```

**Three session tracking techniques:**
1. Session ID (HttpSession)
2. Cookies
3. URL Rewriting

---

## Q5. Explain URL Rewriting for session management.

**Answer:**
- URL Rewriting is a session tracking technique where session information is embedded directly in the URL.
- Example: `http://example.com/page?sid=xf1234ad`
- The server recognizes the session ID from the URL and correlates the request with the previous session.
- Used when cookies are disabled on the client browser.
- The parameter is retrieved using: `String value = request.getParameter("paramName");`

---

## Q6. What is XML? Explain its features, advantages, and difference from HTML. *(SPPU Dec-18, 19, May-19)*

**Answer:**

**XML** stands for **eXtensible Markup Language**.
- XML is designed for **transporting and storing data**.
- HTML is designed for **displaying data**.
- XML tags are **not predefined** — the user creates their own tags.

**Features:**
- User can define their own tags.
- XML contains only data, no formatting information.
- Every XML document has a tree structure.
- Language-neutral and platform-independent.
- Can be validated using external tools (DTD or Schema).

**Difference between XML and HTML:**

| Feature | HTML | XML |
|---|---|---|
| Purpose | Display data | Store/transport data |
| Tags | Predefined | User-defined |
| Case | Case insensitive | Case sensitive |
| Type | Static | Dynamic |

**Advantages:** Human readable, language neutral, tree structure, OS independent.

**Limitations:** Verbose syntax, large file size, no array support, redundancy.

---

## Q7. What is DTD? Explain with an example. *(SPPU May-18, Marks 5)*

**Answer:**

**DTD** stands for **Document Type Definition**.
- DTD defines the building blocks (elements, attributes) of an XML document.
- It specifies rules for structuring data in an XML file.

**Internal DTD Example:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE student [
  <!ELEMENT student (name, address, std, marks)>
  <!ELEMENT name (#PCDATA)>
  <!ELEMENT address (#PCDATA)>
  <!ELEMENT std (#PCDATA)>
  <!ELEMENT marks (#PCDATA)>
]>
<student>
  <name>Anand</name>
  <address>Pune</address>
  <std>Second</std>
  <marks>70 percent</marks>
</student>
```

**External DTD Example:**
```xml
<!-- student.dtd file -->
<!ELEMENT student (name, address, marks)>
<!ELEMENT name (#PCDATA)>

<!-- DTDDemo.xml -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE student SYSTEM "student.dtd">
<student>
  <name>Anand</name>
</student>
```

**Iterator characters in DTD:**
- `?` — zero or one occurrence
- `*` — zero or more occurrences
- `+` — one or more occurrences

---

## Q8. What is XML Schema? How is it better than DTD? *(SPPU May-18, Marks 5)*

**Answer:**

**XML Schema** (XSD) is an XML-based alternative to DTD for defining the structure of XML documents.

**Example Schema:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="Student_Name" type="xs:string"/>
  <xs:element name="My_Marks" type="xs:decimal"/>
  <xs:element name="Flag" type="xs:boolean"/>
</xs:schema>
```

**Schema Data Types:** String, Date (yyyy-mm-dd), Numeric (decimal, integer), Boolean.

**Schema is BETTER than DTD because:**
1. Schema is written in XML itself — no new language to learn.
2. Schema supports **data types** (DTD does not).
3. Schema is **namespace-aware** (DTD is not).
4. Schema supports more complex validations.
5. Schema is a W3C recommendation — widely supported.
6. Schema can handle large and complex operations.

---

## Q9. What is AJAX? Explain how it works with a diagram. *(SPPU Dec-18, 19, May-18, 19 — Very Important)*

**Answer:**

**AJAX** stands for **Asynchronous JavaScript And XML**.
- It is not a programming language but a technique for creating fast, dynamic web pages.
- AJAX allows the browser to send data to the server and receive a response **without reloading the entire page**.

**Working of AJAX:**
```
User Action → Browser creates XMLHttpRequest Object
           → Sends async HTTP request to Server
           → Server processes and sends response (XML/JSON/Text)
           → JavaScript updates part of the web page (DOM manipulation)
```

**Merits of AJAX:**
1. Faster response time → better performance.
2. Only updates part of the page → reduces bandwidth.
3. Used for form validation.
4. Fetches/stores database data without reloading the page.

**Demerits:**
1. Browser compatibility issues.
2. AJAX pages cannot be bookmarked.
3. Search engines cannot index AJAX-generated content.

---

## Q10. Explain XMLHttpRequest object with its properties and methods. *(SPPU May-18, 19)*

**Answer:**

The **XMLHttpRequest** object is the core of AJAX. It is used to exchange data with a server without reloading the page.

**Syntax:** `var req = new XMLHttpRequest();`

**Important Methods:**

| Method | Purpose |
|---|---|
| `open(method, URL, async)` | Opens a request (GET/POST, URL, true/false) |
| `send()` | Sends the request to server |
| `setRequestHeader()` | Adds label-value pair to header |

**Important Properties:**

| Property | Description |
|---|---|
| `readyState` | 0=not init, 1=connection established, 2=request received, 3=processing, **4=response ready** |
| `status` | **200**=OK, 403=Forbidden, 404=Not Found, 500=Server Error |
| `responseText` | Returns response as string |
| `onreadystatechange` | Event triggered when readyState changes |

**AJAX Script Example:**
```javascript
function MyFun() {
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        if (req.readyState == 4 && req.status == 200) {
            document.getElementById("myID").innerHTML = req.responseText;
        }
    };
    req.open("GET", "newdata.txt", true);
    req.send();
}
```

---

## Q11. What is XSLT? Explain its use for XML transformation. *(SPPU May-19, March-20, Marks 5)*

**Answer:**

**XSLT** = eXtensible Stylesheet Language Transformations.
- XSLT is used for **transforming and formatting XML documents**.
- XSL consists of three parts:
  1. **XSLT** — transforms XML documents
  2. **XPath** — navigates in XML documents
  3. **XSL-FO** — formats XML for display

**Key XSL elements:**
- `<xsl:template match="/">` — matches entire XML document
- `<xsl:value-of select="tag">` — extracts value of a tag
- `<xsl:for-each select="...">` — loops through elements
- `<xsl:sort>` — sorts elements
- `<xsl:if test="...">` — conditional display
- `<xsl:choose>` with `<xsl:when>` and `<xsl:otherwise>` — multiple conditions

**Difference between XML and XSLT:**

| XML | XSLT |
|---|---|
| Stores data | Transforms and formats data |
| User-defined tags | Special XSL tags |
| Does not perform transformations | Can convert XML to HTML or text |

---

# 📗 UNIT IV — JSP and Web Services

---

## Q12. What is JSP? Write advantages of JSP over Servlet. *(SPPU April-18, Marks 5)*

**Answer:**

**JSP** = Java Server Pages. It is an alternative to Servlets for building dynamic web pages. JSP is built on top of Servlet technology.

**Advantages of JSP over Servlet:**

| JSP | Servlet |
|---|---|
| Scripting language generating dynamic content | Java program compiled to generate dynamic content |
| Runs slower than Servlet | Runs faster than JSP |
| Acts as **View** in MVC | Acts as **Controller** in MVC |
| Can build **custom tags** | No custom tag facility |
| Can directly call **Java Beans** | No direct Java Bean call |
| Easier to code | Complex Java programs |

**JSP Life Cycle:**
1. Translation — JSP is converted to a Java Servlet
2. Compilation — Servlet is compiled to .class file
3. Class Loading
4. init() → service() → destroy()

---

## Q13. Explain the Basics of JSP — Directives, Scriptlets, Expressions, Declarations. *(SPPU April-18, May-18, 19, Dec-18, 19)*

**Answer:**

A JSP document contains 4 elements:

### 1. Directives
Control the overall processing of the JSP page.
```jsp
<%@ page language="java" contentType="text/html" %>
<%@ page import="java.util.*" %>
<%@ include file="calculate.jsp" %>
```
**Types:** page, include, taglib

### 2. Scriptlets
Java code embedded inside `<% %>` tags.
```jsp
<% 
   int i = 10;
   out.println("Value is: " + i);
%>
```

### 3. Expressions
Evaluated and converted to string, inserted into output. Uses `<%= %>`.
```jsp
Value of expression: <%= (10 * 20) %>
Today's Date: <%= new java.util.Date().toString() %>
```

### 4. Declarations
Declares variables or methods. Uses `<%! %>`.
```jsp
<%! String msg = "Hello"; %>
<% out.println(msg); %>
```

### JSP Comments:
```jsp
<!-- HTML comment (sent to browser) -->
<%-- JSP comment (not sent to browser) --%>
```

---

## Q14. List and explain JSP Implicit Objects. *(SPPU May-18, 19, Dec-18, Marks 5)*

**Answer:**

Implicit objects are **pre-defined variables** available in JSP without any declaration.

| Object | Class/Interface | Purpose |
|---|---|---|
| `request` | HttpServletRequest | Access client request data |
| `response` | HttpServletResponse | Formulate response to client |
| `out` | JspWriter | Write output to the page |
| `session` | HttpSession | Store session data |
| `application` | ServletContext | Share resources across the web app |
| `config` | ServletConfig | Pass initialization parameters |
| `pageContext` | PageContext | Access page attributes |
| `page` | Object | Reference to current JSP page |

**Most important:** `request`, `response`, `out`, `session`

---

## Q15. What are JavaBeans? How are they used in JSP? *(SPPU May-18, Marks 5)*

**Answer:**

**JavaBeans** are reusable software components. A Java Bean is a simple Java class with:
1. A public no-argument constructor.
2. Private properties (fields).
3. Public `getPropertyName()` (getter) and `setPropertyName()` (setter) methods.
4. Implements `Serializable` interface.

**JSP Bean Tags:**
```jsp
<!-- Create/find bean -->
<jsp:useBean id="empID" class="BeanProg.Employee" scope="session"/>

<!-- Set property value -->
<jsp:setProperty name="empID" property="empName" value="John"/>

<!-- Get property value -->
Employee Name: <jsp:getProperty name="empID" property="empName"/>
```

**Bean Scope:**
- `page` — only current page
- `request` — current request
- `session` — entire session
- `application` — entire application

---

## Q16. What is MVC? Explain its architecture for web applications. *(SPPU Dec-18, Marks 6)*

**Answer:**

**MVC** = Model-View-Controller. It is a design pattern for separating concerns in a web application.

```
Client Request → Controller (Servlet) → Model (Business Logic/JavaBean) → Database
                                            ↓
                              View (JSP) ← Response
```

**Three Components:**

1. **Model** — Business logic and data. Represented by JavaBeans or EJBs. Handles data manipulation, database access.

2. **View** — Presentation layer. Represented by JSP. Defines the look and feel of the web page (HTML, CSS).

3. **Controller** — Request processing. Represented by Servlet. Takes user input, passes it to the Model, and forwards to the appropriate View.

**Advantages of MVC:**
- Clear separation between business logic and presentation.
- Easy to change the UI without disturbing the business logic.
- Promotes code reuse and maintainability.
- Multiple views can be created for the same model.

---

## Q17. What are Web Services? Explain their components. *(SPPU May-18, 19, Dec-18 — Very Important)*

**Answer:**

**Definition:** Web Services are software systems that are accessed over the internet using standard web protocols, designed to support interoperable machine-to-machine communication.

**Examples:**
- Credit card validation system
- Weather forecast system
- Currency converter

**Basic Web Service Model:**
```
Service Provider → Publishes to UDDI Registry
Service Consumer → Searches Registry → Finds Service → Binds and Uses Service
```

**Components of Web Services:**

| Component | Full Form | Role |
|---|---|---|
| **XML** | eXtensible Markup Language | Data description at the lowest level |
| **SOAP** | Simple Object Access Protocol | XML-based messaging protocol over HTTP |
| **WSDL** | Web Service Description Language | Describes the web service in XML |
| **UDDI** | Universal Description, Discovery and Integration | Directory/registry of web services |

**Protocol Stack layers:** XML → SOAP → WSDL → UDDI

---

## Q18. What is WSDL? Explain its elements.

**Answer:**

**WSDL** = Web Service Description Language.
- WSDL is an **XML-based language** that describes a web service.
- It tells the client what operations the service provides, what parameters are needed, and how to access it.
- WSDL is a **W3C recommendation**.

**Elements of WSDL:**

| Element | Description |
|---|---|
| `types` | Data types used by the web service |
| `messages` | Messages exchanged by the web service |
| `portType` | Name of the operations (functions) |
| `binding` | Protocol used (typically SOAP) |

---

## Q19. What is SOAP? Explain its structure. *(SPPU — Important)*

**Answer:**

**SOAP** = Simple Object Access Protocol.
- SOAP is an **XML-based messaging protocol** used by web services for exchanging information over HTTP.
- It is platform-independent and language-independent.
- A W3C recommendation.

**SOAP is combination of HTTP + XML.**

**Structure of SOAP (4 Building Blocks):**

```
SOAP Envelope
├── Header (optional)
│   ├── mustUnderstand
│   ├── actor
│   └── encodingStyle
└── Body (required)
    └── Actual message / method call
    └── Fault (optional — error codes)
```

1. **Envelope** — Root element. Identifies the document as a SOAP message.
2. **Header** — Optional. Contains authentication, transaction info.
3. **Body** — Required. Contains the actual message/request.
4. **Fault** — Optional. Contains error information (faultcode, faultstring).

**SOAP Request Example (POST over HTTP):**
```xml
POST /mycreation HTTP/1.0
Content-Type: text/xml; charset=utf-8
<?xml version="1.0"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2001/12/soap-envelope">
  <SOAP-ENV:Body>
    <m:GetDetails xmlns:m="http://www.mywebsite.com">
      <m:Name>ABCD</m:Name>
    </m:GetDetails>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

---

## Q20. What is Struts? Explain Struts Architecture. *(SPPU Dec-18, May-18, 19)*

**Answer:**

**Struts** is an **open-source Java framework** for building web applications. It is based on MVC architecture. The latest version is Struts 2. Created by Craig McClanahan, donated to Apache.

**Features:**
1. Based on MVC architecture.
2. Action class is a POJO (Plain Old Java Object).
3. Supports AJAX technology.
4. Can integrate with Hibernate, Spring.
5. Provides tag support (UI tags, Data tags, Control tags).

**Struts Architecture:**
```
Client (Browser)
     ↓ GET/POST request
FilterDispatcher (Front Controller)
     ↓
ActionMapper
     ↓
Action (POJO — business logic + validation)
     ↓
Result (JSP — view)
     ↓
Client (Browser) ← Response
```

**Key Components:**
- **FilterDispatcher** — Intercepts all incoming requests.
- **Action** — Java class containing business logic.
- **Result** — JSP page that displays the response.
- **Interceptors** — Pre/post-processing of requests (like filters).
- **struts.xml** — Configuration file.

---

# 📙 UNIT V — Server Side Scripting Languages (PHP)

---

## Q21. What is PHP? Explain its features and syntax. *(Important)*

**Answer:**

**PHP** = PHP: Hypertext Preprocessor (recursive acronym).
- Developed in 1994 by Apache group.
- PHP is a **server-side scripting language** mainly used for form handling and database access.
- It is free, open-source, and platform-independent.
- Alternative to CGI, ASP.NET, JSP.
- Files have extensions: `.php`, `.php3`, `.phtml`

**General Syntax Characteristics:**
- PHP code is enclosed within `<?php` and `?>`
- Variable names begin with `$` sign: `$marks = 100;`
- Statements end with semicolon `;`
- Comments: `#`, `//`, `/* … */`
- PHP supports dynamic typing — no need to declare variable types.

**First PHP Program:**
```php
<html>
<body>
  <?php
    $i = 10;
    echo "<h3>Welcome to PHP</h3>";
    echo "The value is = $i";
  ?>
</body>
</html>
```

---

## Q22. Explain Arrays in PHP with examples. *(SPPU May-18, 19, Dec-18, Marks 6)*

**Answer:**

PHP supports three types of arrays:

### 1. Indexed Array
```php
<?php
$colors = array("Red", "Green", "Blue");
echo $colors[0]; // Red
echo count($colors); // 3
?>
```

### 2. Associative Array (Key-Value pairs)
```php
<?php
$student = array("name" => "Vidula", "marks" => 90, "grade" => "A");
echo $student["name"]; // Vidula
?>
```

### 3. Multidimensional Array
```php
<?php
$students = array(
  array("Vidula", 90, "A"),
  array("Manasi", 85, "B")
);
echo $students[0][0]; // Vidula
?>
```

**Useful Array Functions:**
- `count($arr)` — number of elements
- `sort($arr)` — sort ascending
- `rsort($arr)` — sort descending
- `array_push($arr, value)` — add element
- `array_pop($arr)` — remove last element

---

## Q23. Explain Session Tracking and Cookies in PHP. *(SPPU Dec-19, Marks 8 — Very Important)*

**Answer:**

### Cookies in PHP:
```php
<?php
// Setting a cookie
setcookie("user", "John", time() + 3600); // expires in 1 hour

// Reading a cookie
if (isset($_COOKIE["user"])) {
    echo "Welcome " . $_COOKIE["user"];
} else {
    echo "User not found";
}
?>
```

**Cookie Parameters:** `setcookie(name, value, expire, path, domain, secure)`

### Session Tracking in PHP:
- Sessions store user data on the **server** (unlike cookies which store on client).
- Each session has a unique **Session ID**.

```php
<?php
// Starting a session
session_start();

// Storing session data
$_SESSION["username"] = "Vidula";
$_SESSION["marks"] = 90;

// Accessing session data
echo "Welcome " . $_SESSION["username"];

// Destroying a session
session_destroy();
?>
```

**Difference between Sessions and Cookies:**

| Sessions | Cookies |
|---|---|
| Data stored on server | Data stored on client machine |
| More secure | Less secure |
| Lost when browser closes | Can persist for long time |
| Uses `$_SESSION` superglobal | Uses `$_COOKIE` superglobal |

---

## Q24. Explain MySQL with PHP — Steps to connect and perform CRUD. *(SPPU May-18, Dec-19 — Very Important)*

**Answer:**

### Step 1: Connecting to MySQL
```php
<?php
$conn = mysql_connect("localhost", "root", "password");
if (!$conn) {
    die('Connection Error: ' . mysql_error());
} else {
    echo "Connected successfully!";
}
?>
```

### Step 2: Selecting Database
```php
mysql_select_db("mydb", $conn);
```

### Step 3: Creating a Table
```php
$query = "CREATE TABLE mytable (
    id INT NOT NULL AUTO_INCREMENT, 
    PRIMARY KEY(id),
    name VARCHAR(30), 
    phone INT, 
    email VARCHAR(30)
)";
mysql_query($query, $conn);
```

### Step 4: Insert (CREATE)
```php
mysql_query("INSERT INTO mytable (name, phone) VALUES('Vidula', '9999999999')");
```

### Step 5: Select (READ)
```php
$result = mysql_query("SELECT * FROM mytable");
while ($row = mysql_fetch_array($result)) {
    echo $row['id'] . " " . $row['name'];
}
```

### Step 6: Update
```php
mysql_query("UPDATE mytable SET phone='8888888888' WHERE name='Vidula'");
```

### Step 7: Delete
```php
mysql_query("DELETE FROM mytable WHERE id=1");
```

### Step 8: Close Connection
```php
mysql_close($conn);
```

---

## Q25. Write a short note on Node.js. *(SPPU May-18, Marks 4)*

**Answer:**

**Node.js** is an open-source, cross-platform, server-side runtime environment built on **Chrome's V8 JavaScript engine**.

**Features:**
1. **Asynchronous and Event-driven** — All APIs are non-blocking. The server never waits for data to return.
2. **Very fast** — Built on V8 engine.
3. **Single-threaded** — Uses event looping, highly scalable.
4. **No buffering** — Data is output in chunks.

**Simple Node.js Server:**
```javascript
var http = require('http');
http.createServer(function(req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end("Welcome to Node.js!");
}).listen(8080);
```

**Uses:** Real-time applications (chat apps), REST APIs, streaming applications.

---

# 📕 UNIT VI — Ruby and Rails + EJB

---

## Q26. What is Ruby? Explain its features and scalar types. *(Important)*

**Answer:**

**Ruby** is a pure **object-oriented scripting language** designed by Yukihiro Matsumoto (Matz).
- Open source, freely available.
- Similar to Smalltalk, Python, Perl.
- Runs on Windows, Linux, Mac.
- Can connect to MySQL, DB2, Oracle.
- All data values in Ruby are objects.

**Scalar Types:**

```
Numeric
├── Integer
│   ├── Fixnum (≤ 32-bit)
│   └── Bignum (> 32-bit)
└── Float (double precision)

String (single-quoted or double-quoted)
```

**Ruby Program Example:**
```ruby
pi = 3.14
r = 15
puts "Value of pi = #{pi}"
puts "Area of circle = #{pi * r * r}"
```

**Key points:**
- No need to declare variables.
- Variables are typeless.
- If not assigned, value is `nil`.
- Constants start with capital letter.
- No `++` or `--` operators.
- Supports Math module (cos, sin, sqrt, etc.)

---

## Q27. Explain EJB — Introduction, Types, Benefits, Architecture. *(SPPU May-18, 19, Dec-18, Marks 8 — Very Important)*

**Answer:**

### Introduction:
**EJB** = Enterprise Java Beans.
- EJBs are server-side, distributed Java components that contain **business logic and business data**.
- They are part of the J2EE architecture.
- EJB components always reside in an **EJB container** (like GlassFish).

**Difference — Java Beans vs EJB:**

| Java Beans | EJB |
|---|---|
| Can be visible/invisible to user | Always invisible to user |
| Runs locally | Distributed, runs on server |
| Can be used as ActiveX | Cannot be used as ActiveX |
| Described with BeanInfo | Described with DeploymentDescriptor |

---

### Types of EJB:

**1. Entity Bean:**
- Represents **real-world data** (business concepts).
- Corresponds to records in the database.
- **Persistent** — survives server crashes.
- Two types:
  - **Bean Managed Persistent (BMP)** — Bean handles its own persistence.
  - **Container Managed Persistent (CMP)** — Container manages the persistence.

**2. Session Bean:**
- Represents **activities or processes** (e.g., compute net profit, process transaction).
- **Transient** — does not survive server crashes.
- Client-specific.
- Two types:
  - **Stateless Session Bean** — No state maintained between calls. Scalable.
  - **Stateful Session Bean** — Maintains state across calls for a specific client.

**3. Message-Driven Bean:**
- Activated when an **asynchronous message** arrives.
- No state maintained for specific client.
- Can process messages from multiple clients.
- Container calls `onMessage()` method when a message arrives.

---

### Benefits of EJB:
1. Used in Business-to-Business (B2B) e-commerce applications.
2. Suitable for large numbers of clients.
3. System-level services (transactions, security) are separate from business logic.
4. Portable across different EJB server vendors.
5. Client accesses EJB through container — provides component-location transparency.
6. Can be customized at deployment time via deployment descriptor.
7. Supports Enterprise Application Integration (EAI).

---

### Architecture:

```
Client Tier (Browser/App)
      ↓
Presentation Tier (JSP/Servlet)
      ↓
Business Tier (EJB Container)
  ├── Entity Beans
  ├── Session Beans
  └── Message-Driven Beans
      ↓
Data Tier (MySQL / Oracle Database)
```

**EJB Container Services:**
- Security
- Transactions
- Messaging
- Persistence
- Distributions
- Connectivity

**EJB Technology — 3 classes every EJB has:**
1. **Home Interface** — Factory for creating remote objects.
2. **Remote Object** — Used for client interaction.
3. **Bean Object** — Contains all business logic.

---

# 📝 QUICK REVISION — Top Definitions to Remember

| Term | One-Line Definition |
|---|---|
| Servlet | Java program running on server to generate dynamic web content |
| JSP | Server-side scripting alternative to Servlet, built on Servlet technology |
| XML | eXtensible Markup Language — stores and transports data using user-defined tags |
| DTD | Document Type Definition — defines rules for structuring XML data |
| Schema | XML-based alternative to DTD — supports data types and namespaces |
| AJAX | Asynchronous JavaScript and XML — updates web pages without full reload |
| XMLHttpRequest | Core AJAX API for exchanging data with server asynchronously |
| XSLT | eXtensible Stylesheet Language Transformations — transforms XML documents |
| Web Service | Software system accessible over internet for machine-to-machine communication |
| SOAP | Simple Object Access Protocol — XML-based messaging protocol over HTTP |
| WSDL | Web Service Description Language — XML file describing a web service |
| UDDI | Universal Directory for web service discovery |
| MVC | Model-View-Controller — design pattern separating business logic, view, and control |
| Struts | Open-source Java framework based on MVC for web applications |
| PHP | Server-side scripting language for form handling and database access |
| Session | Server-side mechanism to track user state across multiple requests |
| Cookie | Small data stored on client machine for tracking/preferences |
| EJB | Enterprise Java Beans — distributed, server-side Java components for business logic |
| Node.js | Server-side JavaScript runtime environment built on Chrome's V8 engine |
| Ruby | Pure object-oriented scripting language by Yukihiro Matsumoto |

---

# 🔥 PREDICTED ORAL QUESTIONS (High Probability)

1. **What is the servlet life cycle? Name the 3 methods.**
   *(Answer: init, service, destroy)*

2. **What is the difference between doGet and doPost?**
   *(GET — less secure, limited data, visible in URL; POST — secure, large data, not in URL)*

3. **What is the difference between JSP and Servlet?**
   *(JSP = View, Servlet = Controller in MVC; JSP has custom tags, Servlet doesn't)*

4. **What is AJAX? Why is it used?**
   *(Asynchronous JS+XML; updates page without reload, faster UX)*

5. **What is the readyState property values in AJAX?**
   *(0,1,2,3,4 — 4 means response is ready)*

6. **What is MVC?**
   *(Model=business logic, View=JSP, Controller=Servlet)*

7. **Difference between DTD and Schema?**
   *(Schema supports data types, is namespace-aware, is written in XML itself)*

8. **What is SOAP?**
   *(XML-based protocol for web service communication over HTTP)*

9. **What is WSDL?**
   *(XML file describing a web service — its operations, inputs, outputs)*

10. **What are the types of EJB?**
    *(Entity Bean, Session Bean {Stateful/Stateless}, Message-Driven Bean)*

11. **What is the difference between stateful and stateless session beans?**
    *(Stateful maintains client state; Stateless does not — more scalable)*

12. **What is session tracking in PHP? How many methods?**
    *(Session ID, Cookies, URL Rewriting)*

13. **What are JSP implicit objects? Name any 5.**
    *(request, response, out, session, application, config, pageContext, page)*

14. **What is Struts? What pattern does it use?**
    *(Open-source Java framework using MVC pattern)*

15. **What is Node.js?**
    *(Server-side JS runtime on V8 engine; asynchronous, event-driven)*

---

*Good luck, Vidula! You've got this! 🌟*
